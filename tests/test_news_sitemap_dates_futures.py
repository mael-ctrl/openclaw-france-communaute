"""Fixtures SYNTHÉTIQUES : garde temporelle News, aucune preuve de publication."""
import copy
import sys
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import construction
from test_news_sitemap import NS

NOW = datetime(2026, 11, 11, 23, 53, 2, 369830, tzinfo=timezone.utc)

class Frozen(datetime):
    calls = 0
    @classmethod
    def now(cls, tz=None):
        cls.calls += 1
        return NOW.astimezone(tz)


def entry(slug, **dates):
    return {'slug':slug, 'titre':'SYNTHÉTIQUE & <IA> 🦀 '+slug, **dates}


def render(articles, breves):
    Frozen.calls = 0
    with patch.object(construction, 'datetime', Frozen):
        xml = construction.news_sitemap_xml(articles, breves)
    return ET.fromstring(xml)


def paths(root):
    return [e.findtext('s:loc', namespaces=NS).removeprefix(construction.config.URL_SITE)
            for e in root.findall('s:url', NS)]


class NewsSitemapDatesFuturesTest(unittest.TestCase):
    def test_exclut_le_lendemain_sur_horloge_figee(self):
        # Le 12/11 00:00Z était futur au relevé du 11/11 23:53Z,
        # pas nécessairement à l'heure d'exécution réelle de cette recette.
        future = '2026-11-12T00:00:00+00:00'
        articles = [entry('a-futur', date=future)]
        breves = [entry('b-source-future', date_source=future),
                  entry('b-redac-future', date_redac=future)]
        self.assertEqual(paths(render(articles, breves)), [])

    def test_frontieres_inclusives_a_la_microseconde(self):
        cases = [
            (NOW - timedelta(hours=48, microseconds=1), False),
            (NOW - timedelta(hours=48), True),
            (NOW - timedelta(hours=48) + timedelta(microseconds=1), True),
            (NOW - timedelta(microseconds=1), True), (NOW, True),
            (NOW + timedelta(microseconds=1), False),
        ]
        for instant, admitted in cases:
            for field in ('date', 'date_source', 'date_redac'):
                with self.subTest(instant=instant, field=field):
                    row = entry('frontiere', **{field: instant.isoformat()})
                    args = ([row], []) if field == 'date' else ([], [row])
                    root = render(*args)
                    self.assertEqual(bool(paths(root)), admitted)
                    if admitted:
                        self.assertEqual(root.findtext('s:url/news:news/news:publication_date', namespaces=NS),
                                         instant.isoformat())
                    self.assertEqual(Frozen.calls, 1)

    def test_offsets_positifs_negatifs_et_z_comme_instants(self):
        for offset in (timezone(timedelta(hours=5, minutes=30)),
                       timezone(timedelta(hours=-3)), timezone.utc):
            for delta, admitted in ((timedelta(), True), (timedelta(microseconds=1), False),
                                    (-timedelta(hours=48), True),
                                    (-timedelta(hours=48, microseconds=1), False)):
                instant = (NOW + delta).astimezone(offset)
                for text in (instant.isoformat(), instant.isoformat().replace('+00:00', 'Z')):
                    with self.subTest(text=text):
                        root = render([entry('offset', date=text)], [entry('offset-b', date_source=text)])
                        self.assertEqual(len(paths(root)), 2 if admitted else 0)
                        if admitted:
                            emitted = root.findall('s:url/news:news/news:publication_date', NS)
                            self.assertEqual([e.text for e in emitted], [instant.isoformat()] * 2)

    def test_naive_et_jour_seul_conservent_la_convention_utc(self):
        # Convention héritée, pas une validation du fuseau de l'émetteur.
        cases = [(NOW.replace(tzinfo=None).isoformat(), True),
                 ((NOW + timedelta(microseconds=1)).replace(tzinfo=None).isoformat(), False),
                 ('2026-11-11', True), ('2026-11-12', False)]
        for text, admitted in cases:
            for field in ('date', 'date_source', 'date_redac'):
                with self.subTest(text=text, field=field):
                    row = entry('naive', **{field:text})
                    args = ([row], []) if field == 'date' else ([], [row])
                    root = render(*args)
                    self.assertEqual(bool(paths(root)), admitted)
                    if admitted:
                        emitted = root.findtext('s:url/news:news/news:publication_date', namespaces=NS)
                        self.assertEqual(emitted, datetime.fromisoformat(text).replace(tzinfo=timezone.utc).isoformat())

    def test_absente_ou_malformee_ne_devient_pas_maintenant(self):
        for value in (None, '', 'inconnue', '2026-02-30T00:00:00Z',
                      '2026-11-11T23:00:00+25:00', 42, {}, 'date <&>'):
            for field in ('date', 'date_source', 'date_redac'):
                with self.subTest(value=value, field=field):
                    row = entry('invalide', **{field:value})
                    args = ([row], []) if field == 'date' else ([], [row])
                    self.assertEqual(paths(render(*args)), [])

    def test_priorite_source_et_repli_inchanges_sans_redater(self):
        now = NOW.isoformat()
        breves = [entry('source-future', date_source='2026-11-12', date_redac=now),
                  entry('source-malformee', date_source='inconnue', date_redac=now),
                  entry('source-ancienne', date_source='2026-10-01', date_redac=now),
                  entry('source-valide', date_source=now, date_redac='2026-11-12'),
                  entry('source-vide', date_source='', date_redac=now),
                  entry('source-nulle', date_source=None, date_redac=now),
                  entry('sans-source', date_redac=now)]
        original = copy.deepcopy(breves)
        self.assertEqual(paths(render([], breves)), ['/breves/'+s+'/' for s in
                         ('source-valide','source-vide','source-nulle','sans-source')])
        self.assertEqual(breves, original)

    def test_tri_instant_stable_titres_et_non_mutation(self):
        instant = NOW - timedelta(hours=1)
        articles = [entry('a-ancien', date=(NOW-timedelta(hours=2)).isoformat()),
                    entry('a1', date=instant.isoformat()),
                    entry('a2', date=instant.astimezone(timezone(timedelta(hours=2))).isoformat())]
        breves = [entry('b1', date_source=instant.astimezone(timezone(timedelta(hours=-3))).isoformat())]
        original = copy.deepcopy((articles, breves))
        root = render(articles, breves)
        self.assertEqual(paths(root), ['/articles/a1/', '/articles/a2/', '/breves/b1/', '/articles/a-ancien/'])
        self.assertEqual(root.findtext('s:url/news:news/news:title', namespaces=NS), articles[1]['titre'])
        self.assertEqual((articles, breves), original)

    def test_plafond_400_breves_avant_filtrage_sans_remplissage(self):
        breves = [entry('futur', date_redac='2026-11-12')] + [
            entry('b-'+str(i), date_redac=NOW.isoformat()) for i in range(400)]
        root = render([], breves)
        self.assertEqual(paths(root), ['/breves/b-'+str(i)+'/' for i in range(399)])

    def test_plafond_1000_apres_filtrage_et_egalites_stables(self):
        articles = [entry('futur', date='2026-11-12')] + [
            entry('a-'+str(i), date=NOW.isoformat()) for i in range(1001)]
        original = copy.deepcopy(articles)
        root = render(articles, [entry('b', date_redac=NOW.isoformat())])
        self.assertEqual(paths(root), ['/articles/a-'+str(i)+'/' for i in range(1000)])
        self.assertEqual(articles, original)

    def test_vide_et_horloge_lue_une_seule_fois(self):
        self.assertEqual(paths(render([], [])), [])
        self.assertEqual(Frozen.calls, 1)


if __name__ == '__main__':
    unittest.main()
