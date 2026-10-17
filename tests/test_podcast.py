"""Contrat du pilote : tests hors réseau, sans production audio."""
import importlib.util
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE / 'engine'))


def module_podcast():
    spec = importlib.util.find_spec('podcast')
    if spec is None:
        raise AssertionError('Le module podcast manque : le flux pilote reste à construire')
    return __import__('podcast')


def episode():
    return {
        'titre': 'La Brève du Crabe — Pilote',
        'description': 'Pilote audio, texte produit par IA et voix synthétique.',
        'guid': 'urn:communaute-ia:podcast:la-breve-du-crabe:pilote',
        'fichier': 'la-breve-du-crabe-pilote.mp3',
        'octets': 366768,
        'mime': 'audio/mpeg',
        'duree_secondes': 61.128,
        'publie_le': None,
    }


class PodcastTest(unittest.TestCase):
    def test_flux_pilote_enclosure_et_guid_stable_sans_date_inventee(self):
        podcast = module_podcast()
        xml = podcast.flux_xml(episode(), 'https://communaute-ia.fr')
        racine = ET.fromstring(xml)
        self.assertEqual(racine.attrib, {'version': '2.0'})
        canal = racine.find('channel')
        self.assertEqual(canal.findtext('language'), 'fr-FR')
        self.assertEqual(canal.findtext('link'), 'https://communaute-ia.fr/podcast/')
        self.assertEqual(len(canal.findall('item')), 1)
        item = canal.find('item')
        self.assertEqual(item.findtext('title'), episode()['titre'])
        self.assertEqual(item.find('enclosure').attrib, {
            'url': 'https://communaute-ia.fr/assets/podcast/la-breve-du-crabe-pilote.mp3',
            'length': '366768', 'type': 'audio/mpeg'})
        self.assertEqual(item.findtext('guid'), episode()['guid'])
        self.assertEqual(item.find('guid').get('isPermaLink'), 'false')
        self.assertIsNone(item.find('pubDate'))
        self.assertIsNone(canal.find('lastBuildDate'))
        ns = {'i': 'http://www.itunes.com/dtds/podcast-1.0.dtd', 'a': 'http://www.w3.org/2005/Atom'}
        self.assertEqual(item.findtext('i:episodeType', namespaces=ns), 'trailer')
        self.assertEqual(item.findtext('i:duration', namespaces=ns), '61')
        self.assertIsNone(item.find('i:episode', ns))
        self.assertEqual(canal.find('a:link', ns).attrib, {
            'href': 'https://communaute-ia.fr/podcast/feed.xml',
            'rel': 'self', 'type': 'application/rss+xml'})
        self.assertEqual(xml, podcast.flux_xml(episode(), 'https://communaute-ia.fr'))
        modifie = {**episode(), 'titre': 'Titre corrigé', 'fichier': 'pilote-renomme.mp3'}
        autre = ET.fromstring(podcast.flux_xml(modifie, 'https://exemple.fr'))
        self.assertEqual(autre.findtext('channel/item/guid'), episode()['guid'])

    def test_date_documentee_normalisee_utc_et_texte_xml_echappe(self):
        podcast = module_podcast()
        titre = 'La Brève & <Crabe> "pilote"'
        desc = 'Texte & voix <IA>, pas de CDATA ]]>.'
        p = {**episode(), 'titre': titre, 'description': desc,
             'publie_le': '2026-10-14T23:30:00-03:00'}
        xml = podcast.flux_xml(p, 'https://communaute-ia.fr')
        item = ET.fromstring(xml).find('channel/item')
        self.assertEqual(item.findtext('pubDate'), 'Thu, 15 Oct 2026 02:30:00 GMT')
        self.assertEqual(item.findtext('title'), titre)
        self.assertEqual(item.findtext('description'), desc)
        self.assertIn('&amp;', xml)
        self.assertIn('&lt;Crabe&gt;', xml)
        for valeur in ('2026-10-14', '2026-10-14T12:30:00', '', 'inconnue', '2026-13-40T00:00:00Z'):
            with self.subTest(valeur=valeur), self.assertRaises(ValueError):
                podcast.flux_xml({**episode(), 'publie_le': valeur}, 'https://communaute-ia.fr')

    def test_page_ecoute_native_sans_js_et_divulgations(self):
        from html.parser import HTMLParser

        class Document(HTMLParser):
            def __init__(self, texte):
                super().__init__()
                self.tags = []
                self.texte = []
                self.feed(texte)

            def handle_starttag(self, tag, attrs):
                self.tags.append((tag, dict(attrs)))

            def handle_data(self, data):
                self.texte.append(data)

        podcast = module_podcast()
        self.assertTrue(hasattr(podcast, 'page_ecoute'), 'La page HTML native manque')
        pilote = {**episode(), 'titre': 'Pilote & <script>alert(1)</script>'}
        html = podcast.page_ecoute(pilote, 'https://communaute-ia.fr')
        doc = Document(html)
        self.assertFalse(any(t in ('script', 'iframe') for t, _ in doc.tags))
        audio = [a for t, a in doc.tags if t == 'audio']
        self.assertEqual(len(audio), 1)
        self.assertIn('controls', audio[0])
        self.assertNotIn('autoplay', audio[0])
        self.assertEqual(audio[0]['preload'], 'none')
        source = next(a for t, a in doc.tags if t == 'source')
        self.assertEqual(source['type'], 'audio/mpeg')
        lien = next(a for t, a in doc.tags if t == 'a' and 'download' in a)
        self.assertEqual(lien['href'], source['src'])
        self.assertEqual(source['src'], 'https://communaute-ia.fr/assets/podcast/la-breve-du-crabe-pilote.mp3')
        self.assertTrue(any(t == 'a' and a.get('href') == '/podcast/feed.xml' for t, a in doc.tags))
        self.assertTrue(any(t == 'link' and a.get('rel') == 'alternate' and
                            a.get('href') == '/podcast/feed.xml' for t, a in doc.tags))
        texte = ''.join(doc.texte)
        for fragment in (pilote['titre'], 'voix synthétique', 'produit par IA',
                         'pas un épisode éditorial', 'Aucune cadence',
                         '61,128 s', '366 768 octets', 'première publication non documentée',
                         'engagement', 'pas une preuve de versement'):
            self.assertIn(fragment, texte)
        self.assertNotIn('<time', html)
        datee = podcast.page_ecoute({**episode(), 'publie_le': '2026-10-14T23:30:00-03:00'},
                                   'https://communaute-ia.fr')
        self.assertIn('datetime="2026-10-15T02:30:00+00:00"', datee)
        self.assertIn('15/10/2026 à 02:30 UTC', datee)

    def test_metadonnees_adossees_aux_octets_reels_et_rejet_des_ecarts(self):
        import hashlib
        import json
        import tempfile

        podcast = module_podcast()
        self.assertTrue(hasattr(podcast, 'charger_pilote'), 'La validation du MP3 manque')
        donnees = (RACINE / 'assets/podcast/la-breve-du-crabe-pilote.mp3').read_bytes()
        meta = {**episode(), 'sha256': hashlib.sha256(donnees).hexdigest()}
        with tempfile.TemporaryDirectory() as dossier:
            assets = Path(dossier)
            cible = assets / 'podcast'
            cible.mkdir()
            fichier = cible / meta['fichier']
            fichier.write_bytes(donnees)
            manifeste = cible / 'pilote.json'
            manifeste.write_text(json.dumps(meta), encoding='utf-8')
            self.assertEqual(podcast.charger_pilote(assets), meta)
            for cle, valeur in [('octets', len(donnees) + 1), ('sha256', '0' * 64),
                                ('mime', 'text/html'), ('duree_secondes', -1),
                                ('duree_secondes', float('nan')), ('guid', ''),
                                ('fichier', '../ailleurs.mp3'), ('fichier', '/ailleurs.mp3'),
                                ('fichier', 'https://exemple.fr/pilote.mp3')]:
                with self.subTest(cle=cle, valeur=valeur):
                    manifeste.write_text(json.dumps({**meta, cle: valeur}), encoding='utf-8')
                    with self.assertRaises(ValueError):
                        podcast.charger_pilote(assets)
            manifeste.write_text(json.dumps(meta), encoding='utf-8')
            fichier.unlink()
            with self.assertRaises(FileNotFoundError):
                podcast.charger_pilote(assets)

    def test_rejet_url_non_https_et_donnees_non_serialisables(self):
        podcast = module_podcast()
        for fonction in (podcast.flux_xml, podcast.page_ecoute):
            for url in ('http://communaute-ia.fr', 'javascript:alert(1)', '//communaute-ia.fr',
                        'https://user:secret@exemple.fr', 'https://exemple.fr?x=1',
                        'https://exemple.fr/chemin', 'https://exemple.fr/#fragment'):
                with self.subTest(fonction=fonction.__name__, url=url), self.assertRaises(ValueError):
                    fonction(episode(), url)
            for cle, valeur in (('titre', 'Titre\x00non XML'), ('description', 'Texte\x01'),
                                ('fichier', '../ailleurs.mp3'), ('octets', 1.5),
                                ('octets', True), ('octets', 0), ('duree_secondes', float('inf')),
                                ('mime', 'text/html'), ('guid', '')):
                with self.subTest(fonction=fonction.__name__, cle=cle), self.assertRaises(ValueError):
                    fonction({**episode(), cle: valeur}, 'https://communaute-ia.fr')

    def test_build_statque_integre_page_flux_et_liens_sans_recycler_date(self):
        import hashlib
        import tempfile
        from unittest.mock import patch
        import config
        import construction

        with tempfile.TemporaryDirectory() as dossier:
            sortie = Path(dossier)
            with patch.object(config, 'DOSSIER_SORTIE', sortie):
                construction.construire()
            page = sortie / 'podcast/index.html'
            flux = sortie / 'podcast/feed.xml'
            self.assertTrue(page.is_file(), 'Le moteur doit construire la page podcast')
            self.assertTrue(flux.is_file(), 'Le moteur doit construire le flux podcast')
            self.assertNotIn('<script', page.read_text(encoding='utf-8'))
            item = next(i for i in ET.parse(flux).findall('channel/item')
                        if i.findtext('guid') == episode()['guid'])
            self.assertIsNone(item.find('pubDate'))
            self.assertEqual(item.findtext('guid'), episode()['guid'])
            audio = sortie / 'assets/podcast/la-breve-du-crabe-pilote.mp3'
            self.assertEqual(len(audio.read_bytes()), int(item.find('enclosure').get('length')))
            self.assertEqual(hashlib.sha256(audio.read_bytes()).hexdigest(),
                             '7f40ff240698c28ce4c7172bda9d7fa63a9b7be597929f324f9a4fb2e4cecea6')
            self.assertIn('href="/podcast/"', (sortie / 'index.html').read_text(encoding='utf-8'))
            ns = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            sitemap = ET.parse(sortie / 'sitemap.xml')
            pages = [n for n in sitemap.findall('s:url', ns)
                     if n.findtext('s:loc', namespaces=ns) == config.URL_SITE + '/podcast/']
            self.assertEqual(len(pages), 1)
            self.assertIsNone(pages[0].find('s:lastmod', ns))
            self.assertNotIn('/podcast/', (sortie / 'news-sitemap.xml').read_text(encoding='utf-8'))
            for nom in ('feed.xml', 'feed-articles.xml'):
                ancien = ET.parse(sortie / nom)
                self.assertNotIn(episode()['guid'], [x.text for x in ancien.findall('channel/item/guid')])
                self.assertTrue(all(x.get('isPermaLink') == 'true'
                                    for x in ancien.findall('channel/item/guid')))


if __name__ == '__main__':
    unittest.main()
