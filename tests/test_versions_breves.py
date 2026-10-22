"""Une URL peut conserver plusieurs rédactions, sans écrasement arbitraire."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET

import test_archives_conservees
from test_pagination_actus import breves_test
import construction
import config


class VersionsBrevesTest(unittest.TestCase):
    def versions(self):
        ancienne, autre = breves_test(2)
        ancienne.update(id="identite-complete", source="Source", lien_source="https://example.org/info",
                        date_source=None, date_redac="2026-10-22T09:50:10+00:00",
                        resume="VERSION ANCIENNE CONSERVEE")
        recente = copy.deepcopy(ancienne)
        recente.update(date_redac="2026-10-22T10:21:40+00:00", resume="VERSION RECENTE RETENUE")
        return ancienne, recente, autre

    def test_build_une_url_derniere_redaction_sans_modifier_les_sources(self):
        ancienne, recente, autre = self.versions()
        for versions in ([recente, autre, ancienne], [ancienne, autre, recente]):
            with self.subTest(ordre=[b['resume'] for b in versions]), tempfile.TemporaryDirectory() as tmp:
                racine = Path(tmp)
                sortie = test_archives_conservees.ArchivesConserveesTest().construire_fixture(versions, racine)
                self.assertEqual(json.loads((racine / 'breves.json').read_text()), versions)
                document = (sortie / f"breves/{recente['slug']}/index.html").read_text()
                self.assertIn(recente['resume'], document)
                self.assertNotIn(ancienne['resume'], document)
                cible = config.URL_SITE + f"/breves/{recente['slug']}/"
                sitemap = ET.parse(sortie / 'sitemap.xml')
                urls = [n.text for n in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
                self.assertEqual(urls.count(cible), 1)
                rss = ET.parse(sortie / 'feed.xml')
                self.assertEqual([n.text for n in rss.findall('.//item/link')].count(cible), 1)
                for page in ('actus/index.html', 'archives-breves/index.html'):
                    texte = (sortie / page).read_text()
                    self.assertIn(recente['resume'], texte)
                    self.assertNotIn(ancienne['resume'], texte)


    def test_ambiguite_meme_ancienne_date_non_masquee_par_une_version_recente(self):
        from itertools import permutations
        ancienne, recente, _ = self.versions()
        divergente = dict(ancienne, resume="AUTRE TEXTE A LA MEME DATE")
        for versions in permutations((ancienne, divergente, recente)):
            with self.subTest(ordre=[b['resume'] for b in versions]):
                with self.assertRaisesRegex(ValueError, 'dupliquée'):
                    construction.breves_pour_publication(versions)

    def test_identite_ou_chronologie_ambigue_refusee_avant_html(self):
        ancienne, recente, _ = self.versions()
        mutations = [
            ('id', 'autre-identite'), ('id', ''), ('source', 'Autre source'),
            ('lien_source', 'https://example.org/autre'), ('lien_source', None),
            ('date_redac', ancienne['date_redac']), ('date_redac', None),
            ('date_redac', 'invalide'), ('date_redac', '2026-10-22T11:00:00'),
            ('slug', '../sortie'),
        ]
        for cle, valeur in mutations:
            with self.subTest(cle=cle, valeur=valeur), tempfile.TemporaryDirectory() as tmp:
                racine = Path(tmp)
                with self.assertRaises(ValueError):
                    test_archives_conservees.ArchivesConserveesTest().construire_fixture(
                        [ancienne, dict(recente, **{cle: valeur})], racine)
                self.assertEqual(list((racine / 'site').rglob('*.html')), [])

    def test_offsets_compares_comme_instants_pas_comme_chaines(self):
        ancienne, recente, _ = self.versions()
        ancienne['date_redac'] = '2026-10-22T12:00:00+02:00'
        self.assertEqual(construction.breves_pour_publication([ancienne, recente]), [recente])
        ancienne['date_redac'] = '2026-10-22T12:21:40+02:00'
        with self.assertRaisesRegex(ValueError, 'dupliquée'):
            construction.breves_pour_publication([ancienne, recente])

    def test_identiques_compactes_mais_slugs_distincts_preserves_sans_mutation(self):
        ancienne, _, autre = self.versions()
        autre.update(id=ancienne['id'], source=ancienne['source'], lien_source=ancienne['lien_source'])
        entrees = [ancienne, autre, copy.deepcopy(ancienne)]
        avant = copy.deepcopy(entrees)
        self.assertEqual(construction.breves_pour_publication(entrees), [ancienne, autre])
        self.assertEqual(entrees, avant)
        self.assertEqual(construction.breves_pour_publication([]), [])


if __name__ == '__main__':
    unittest.main()
