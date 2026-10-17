"""Contrat des épisodes effectivement indexés, sans date de publication déduite."""
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'engine'))
import config
import construction


class PodcastCourantTest(unittest.TestCase):
    def test_deux_episodes_indexes_et_pilote_dans_le_build(self):
        index = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())
        self.assertTrue({'breve-2026-10-15', 'breve-2026-10-16'} <= {e['id'] for e in index})
        with tempfile.TemporaryDirectory() as temp:
            out = Path(temp)
            with patch.object(config, 'DOSSIER_SORTIE', out):
                construction.construire()
            self.assertTrue((out / 'podcast/feed.xml').is_file(), 'RSS des épisodes indexés absent')
            flux = ET.parse(out / 'podcast/feed.xml')
            items = flux.findall('channel/item')
            self.assertEqual(len(items), len(index) + 1)
            guids = [item.findtext('guid') for item in items]
            prefix = 'urn:communaute-ia:podcast:la-breve-du-crabe:'
            expected = [prefix + e['id'] for e in sorted(index, key=lambda e: (e['date'], e['id']), reverse=True)]
            self.assertEqual(guids, expected + [prefix + 'pilote'])
            self.assertEqual(len(set(guids)), len(guids))
            self.assertIsNone(flux.find('channel/lastBuildDate'))
            page = (out / 'podcast/index.html').read_text()
            self.assertEqual(page.count('<audio '), len(items))
            for original in index:
                item = items[guids.index(prefix + original['id'])]
                self.assertEqual(item.findtext('title'), original['titre'])
                self.assertEqual(item.findtext('{http://www.itunes.com/dtds/podcast-1.0.dtd}duration'), str(round(original['durée'])))
                self.assertEqual(item.find('enclosure').attrib, {
                    'url': config.URL_SITE + '/' + original['fichier'],
                    'length': str((ROOT / original['fichier']).stat().st_size),
                    'type': 'audio/mpeg'})
                self.assertEqual((ROOT / original['fichier']).read_bytes(), (out / original['fichier']).read_bytes())
                self.assertIn('datetime="' + original['date'] + '"', page)
                self.assertIn(format(original['durée'], '.3f').replace('.', ',') + ' s', page)
            for item in items:
                self.assertEqual(item.find('guid').get('isPermaLink'), 'false')
                self.assertIsNone(item.find('pubDate'), 'Le jour éditorial ne prouve pas la publication')
            self.assertEqual(items[guids.index(prefix + 'pilote')].findtext('{http://www.itunes.com/dtds/podcast-1.0.dtd}episodeType'), 'trailer')


if __name__ == '__main__':
    unittest.main()
