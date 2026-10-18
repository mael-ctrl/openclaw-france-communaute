"""Les scripts éditoriaux existants sont lisibles sans audio ni JavaScript."""
import json
import shutil
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'engine'))
import podcast


class TexteScript(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.textes = []
        self.actif = False
        self.tags = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        if dict(attrs).get('class') == 'podcast-script':
            self.actif = True
            self.textes.append('')

    def handle_endtag(self, tag):
        if tag == 'div':
            self.actif = False

    def handle_data(self, data):
        if self.actif:
            self.textes[-1] += data


class ScriptPodcastTest(unittest.TestCase):
    def preparer(self, root, script='contenus/podcast/2026-10-15/script.txt'):
        shutil.copytree(ROOT / 'assets/podcast', root / 'assets/podcast')
        entree = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())[0]
        entree = {**entree, 'script': script}
        dossier = root / 'contenus/podcast'
        dossier.mkdir(parents=True)
        (dossier / 'episodes.json').write_text(json.dumps([entree]), encoding='utf-8')
        return entree

    def test_script_explicitement_lie_lisible_echappe_et_flux_inchange(self):
        texte = 'Première ligne & <script>alert("x")</script>.\n\nDeuxième paragraphe.\n'
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            entree = self.preparer(root)
            fichier = root / entree['script']
            fichier.parent.mkdir()
            fichier.write_text(texte, encoding='utf-8')
            episodes = podcast.charger_episodes(root)
            html = podcast.page_ecoute(episodes, 'https://communaute-ia.fr')
            doc = TexteScript(html)
            self.assertEqual(doc.textes, [texte])
            self.assertIn('<summary>Lire le texte de l’épisode</summary>', html)
            self.assertIn('Script éditorial', html)
            self.assertIn('pas une transcription synchronisée', html)
            self.assertNotIn('script', doc.tags)
            self.assertIn('details', doc.tags)
            avant = [{k: v for k, v in e.items() if k != 'texte'} for e in episodes]
            self.assertEqual(podcast.flux_xml(episodes, 'https://communaute-ia.fr'),
                             podcast.flux_xml(avant, 'https://communaute-ia.fr'))

    def test_script_refuse_chemin_hors_perimetre_symlink_et_vide(self):
        for chemin in ('contenus/podcast/episodes.json',
                       'contenus/podcast/2026-10-15/../episodes.json',
                       str(ROOT / 'contenus/podcast/2026-10-15/script.txt'),
                       'https://exemple.test/script.txt', None, []):
            with self.subTest(chemin=chemin), tempfile.TemporaryDirectory() as temp:
                root = Path(temp).resolve()
                self.preparer(root, chemin)
                with self.assertRaises(ValueError):
                    podcast.charger_episodes(root)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            entree = self.preparer(root)
            fichier = root / entree['script']
            fichier.parent.mkdir()
            fichier.symlink_to(ROOT / entree['script'])
            with self.assertRaises(ValueError):
                podcast.charger_episodes(root)
            fichier.unlink()
            fichier.write_text(' \n', encoding='utf-8')
            with self.assertRaises(ValueError):
                podcast.charger_episodes(root)
            fichier.unlink()
            with self.assertRaises(FileNotFoundError):
                podcast.charger_episodes(root)

    def test_absence_de_declaration_n_invente_aucun_texte(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            entree = self.preparer(root)
            del entree['script']
            (root / 'contenus/podcast/episodes.json').write_text(json.dumps([entree]))
            episodes = podcast.charger_episodes(root)
            self.assertTrue(all('texte' not in e for e in episodes))
            self.assertNotIn('<details>', podcast.page_ecoute(episodes, 'https://communaute-ia.fr'))

    def test_build_lie_les_trois_scripts_existants_sans_les_recrire(self):
        from unittest.mock import patch
        import config
        import construction
        index = json.loads((ROOT / 'contenus/podcast/episodes.json').read_text())
        attendus = {'breve-2026-10-15', 'breve-2026-10-16', 'breve-2026-10-17'}
        declares = {e['id'] for e in index if 'script' in e}
        self.assertTrue(attendus <= declares, 'Les trois scripts existants doivent être explicitement liés')
        with tempfile.TemporaryDirectory() as temp:
            sortie = Path(temp)
            with patch.object(config, 'DOSSIER_SORTIE', sortie):
                construction.construire()
            doc = TexteScript((sortie / 'podcast/index.html').read_text())
            tries = sorted(index, key=lambda e: (e['date'], e['id']), reverse=True)
            self.assertEqual(doc.textes, [(ROOT / e['script']).read_text() for e in tries if 'script' in e])
            self.assertNotIn('script', doc.tags)
            for e in index:
                self.assertEqual((sortie / e['fichier']).read_bytes(), (ROOT / e['fichier']).read_bytes())


if __name__ == '__main__':
    unittest.main()
