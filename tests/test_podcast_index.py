"""Index réel : identité, dates éditoriales, fichiers locaux, coexistence B2B."""
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'engine'))
import podcast


class PodcastIndexTest(unittest.TestCase):
    def index_temp(self, root, entries):
        import shutil
        # L’index réel peut déclarer un script : copier ses dépendances de contenu.
        shutil.copytree(ROOT / 'contenus/podcast', root / 'contenus/podcast', dirs_exist_ok=True)
        if not (root / 'assets/podcast').exists():
            shutil.copytree(ROOT / 'assets/podcast', root / 'assets/podcast')
        (root / 'contenus/podcast/episodes.json').write_text(json.dumps(entries), encoding='utf-8')

    def test_index_refuse_identites_chemins_et_dates_ambigus(self):
        original = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())[0]
        cases = [
            ('id', 'pilote'), ('id', '../episode'), ('id', ' espace'), ('id', ''),
            ('fichier', '../assets/podcast/breve-2026-10-15.mp3'),
            ('fichier', 'assets/podcast/../podcast/breve-2026-10-15.mp3'),
            ('fichier', 'https://evil.test/breve.mp3'),
            ('fichier', '/assets/podcast/breve-2026-10-15.mp3'),
            ('fichier', 'assets/podcast/breve%2f2026.mp3'),
            ('fichier', 'assets/podcast/la-breve-du-crabe-pilote.mp3'),
            ('date', '2026-02-30'), ('date', '20261015'), ('date', '2026-10-15T00:00:00Z'),
            ('durée', True), ('durée', 0), ('durée', float('nan')), ('durée', '127.584'),
            ('titre', 'Texte\x00'), ('titre', ''), ('publie_le', '2026-10-15'),
        ]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for key, value in cases:
                with self.subTest(key=key, value=value):
                    self.index_temp(root, [{**original, key: value}])
                    with self.assertRaises(ValueError):
                        podcast.charger_episodes(root)
            for entries in ([original, original], [original, {**original, 'id': 'autre'}], {}, [None], [{}]):
                with self.subTest(entries=entries):
                    self.index_temp(root, entries)
                    with self.assertRaises(ValueError):
                        podcast.charger_episodes(root)
            self.index_temp(root, [{**original, 'fichier': 'assets/podcast/lien.mp3'}])
            (root / 'assets/podcast/lien.mp3').symlink_to(ROOT / original['fichier'])
            with self.assertRaises(ValueError):
                podcast.charger_episodes(root)
            self.index_temp(root, [{**original, 'fichier': 'assets/podcast/absent.mp3'}])
            with self.assertRaises(FileNotFoundError):
                podcast.charger_episodes(root)

    def test_origine_et_types_invalides_refuses_explicitement(self):
        for url in ('https://example.test\\evil', 'https://exa<mple.test',
                    'https://example.test:99999', 'https://-exemple.test', 'https://example.test"'):
            with self.subTest(url=url), self.assertRaises(ValueError):
                podcast.origine_https(url)
        original = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())[0]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for key, value in [('fichier', []), ('fichier', None), ('date', None), ('id', 7), ('publie_le', True)]:
                with self.subTest(key=key, value=value):
                    self.index_temp(root, [{**original, key: value}])
                    with self.assertRaises(ValueError):
                        podcast.charger_episodes(root)

    def test_tri_identite_stable_echappement_et_index_vide(self):
        original = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())[0]
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.index_temp(root, [])
            self.assertEqual(len(podcast.charger_episodes(root)), 1)
            self.index_temp(root, [original])
            before = podcast.charger_episodes(root)[0]['guid']
            modified = {**original, 'titre': 'IA & <script>"actualité"</script>', 'date': '2026-10-14',
                        'fichier': 'assets/podcast/renomme.mp3', 'publie_le': '2026-10-15T23:30:00-03:00'}
            (root / modified['fichier']).write_bytes((root / original['fichier']).read_bytes())
            self.index_temp(root, [modified, {**original, 'id': 'autre'}])
            episodes = podcast.charger_episodes(root)
            self.assertEqual([e.get('id') for e in episodes], ['autre', original['id'], None])
            self.assertEqual(episodes[1]['guid'], before)
            xml = podcast.flux_xml(episodes, 'https://autre.test')
            item = ET.fromstring(xml).findall('channel/item')[1]
            self.assertEqual(item.findtext('title'), modified['titre'])
            self.assertEqual(item.findtext('pubDate'), 'Fri, 16 Oct 2026 02:30:00 GMT')
            self.assertIn('&lt;script&gt;', xml)
            self.assertEqual(episodes[1]['duree_secondes'], original['durée'])

    def test_build_multi_episode_et_b2b_sans_javascript(self):
        from html.parser import HTMLParser
        from unittest.mock import patch
        import config
        import construction
        import annexes

        class Document(HTMLParser):
            def __init__(self, text):
                super().__init__()
                self.tags = []
                self.text = []
                self.feed(text)
            def handle_starttag(self, tag, attrs):
                self.tags.append((tag, dict(attrs)))
            def handle_data(self, text):
                self.text.append(text)

        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            with patch.object(config, 'DOSSIER_SORTIE', out):
                construction.construire()
            items = ET.parse(out / 'podcast/feed.xml').findall('channel/item')
            episodes = podcast.charger_episodes(ROOT)
            self.assertEqual(len(items), len(episodes), 'Le vrai épisode manque au build')
            doc = Document((out / 'podcast/index.html').read_text())
            audios = [a for t, a in doc.tags if t == 'audio']
            self.assertEqual(len(audios), len(episodes))
            self.assertFalse(any(t in ('script', 'iframe') for t, _ in doc.tags))
            ids = [a['id'] for t, a in doc.tags if 'id' in a]
            self.assertEqual(len(set(ids)), len(ids))
            for audio in audios:
                self.assertIn('controls', audio)
                self.assertNotIn('autoplay', audio)
                self.assertEqual(audio['preload'], 'none')
                self.assertIn(audio['aria-labelledby'], ids)
            downloads = [a['href'] for t, a in doc.tags if t == 'a' and 'download' in a]
            sources = [a['src'] for t, a in doc.tags if t == 'source']
            self.assertEqual(downloads, sources)
            for item in items:
                enclosure = item.find('enclosure')
                self.assertIn(enclosure.get('url'), sources)
                rel = enclosure.get('url').removeprefix(config.URL_SITE + '/')
                self.assertEqual((out / rel).read_bytes(), (ROOT / rel).read_bytes())
                self.assertEqual((out / rel).stat().st_size, int(enclosure.get('length')))
                self.assertIsNone(item.find('pubDate'))
            text = ''.join(doc.text)
            for fragment in ('127,584 s', '61,128 s', 'voix synthétique', 'produit par IA',
                             '15/10/2026', 'Date éditoriale', 'première publication non documentée'):
                self.assertIn(fragment, text)
            self.assertEqual((out / 'b2b/index.html').read_text(), annexes.page_b2b())
            for name in ('echantillon-veille.html', 'echantillon-veille.md', 'questionnaire-qualification.md'):
                rel = 'b2b/echantillon-veille/' + ('index.html' if name.endswith('.html') else name)
                self.assertEqual((out / rel).read_text(), annexes._fichier_demo_b2b(name))
            sitemap = (out / 'sitemap.xml').read_text()
            self.assertIn('/podcast/', sitemap)
            self.assertIn('/b2b/echantillon-veille/', sitemap)
            self.assertNotIn('/podcast/feed.xml', sitemap)
            self.assertNotIn('questionnaire-qualification.md', sitemap)
            self.assertNotIn('/podcast/', (out / 'news-sitemap.xml').read_text())

    def test_index_reel_dans_flux_sans_timestamp_invente(self):
        self.assertTrue(hasattr(podcast, 'charger_episodes'), 'Chargeur de l’index réel manquant')
        episodes = podcast.charger_episodes(ROOT)
        index = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())
        self.assertEqual(len(episodes), len(index) + 1)
        flux = ET.fromstring(podcast.flux_xml(episodes, 'https://communaute-ia.fr'))
        items = flux.findall('channel/item')
        self.assertEqual(len(items), len(episodes))
        guids = [i.findtext('guid') for i in items]
        self.assertEqual(len(set(guids)), len(guids))
        for original in index:
            guid = 'urn:communaute-ia:podcast:la-breve-du-crabe:' + original['id']
            item = next(i for i in items if i.findtext('guid') == guid)
            self.assertEqual(item.findtext('title'), original['titre'])
            self.assertEqual(item.find('guid').get('isPermaLink'), 'false')
            self.assertIsNone(item.find('pubDate'))
            self.assertEqual(item.find('enclosure').attrib, {
                'url': 'https://communaute-ia.fr/' + original['fichier'],
                'length': str((ROOT / original['fichier']).stat().st_size),
                'type': 'audio/mpeg'})
            self.assertEqual(item.findtext('{%s}episodeType' % podcast.ITUNES), 'full')
            self.assertEqual(item.findtext('{%s}duration' % podcast.ITUNES), str(round(original['durée'])))
        self.assertEqual(items[-1].findtext('guid'), 'urn:communaute-ia:podcast:la-breve-du-crabe:pilote')
        self.assertIsNone(items[-1].find('pubDate'))
        self.assertEqual(items[-1].findtext('{%s}episodeType' % podcast.ITUNES), 'trailer')
        self.assertIsNone(flux.find('channel/lastBuildDate'))


if __name__ == '__main__':
    unittest.main()
