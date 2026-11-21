"""Contrat P10 documentaire, écrit avant le correctif. Aucun installateur exécuté."""
from pathlib import Path
import os
import re
import unittest

ROOT = Path(os.environ.get('P10_TREE', Path(__file__).resolve().parents[1]))
SITE = ROOT / 'sites/openclaw-france'


class MarkdownIntel(unittest.TestCase):
    def test_guide_et_readme_distinguent_desktop_et_cli(self):
        for name in ('GUIDE.md', 'README.md'):
            text = (SITE / 'dl/kit-hermes' / name).read_text()
            with self.subTest(name=name):
                self.assertIn('Desktop Intel : aucun bundle actuel', text)
                self.assertIn('flux macOS', text)
                self.assertIn('Apple Silicon', text)
                self.assertIn('CLI', text)
                self.assertIn('compatibilité non garantie', text)
                self.assertIn('divergent', text)
                self.assertIn('2026-11-21', text)
                self.assertNotIn('bundles Intel conditionnels', text)
                self.assertNotIn('`darwin-x64` construits seulement', text)
                self.assertIn('pas une installation testée', text)
                self.assertIn('platform-support#build-targets-and-support-priority', text)

    def test_methode_dmg_bornee_apple_silicon(self):
        text = (SITE / 'dl/kit-hermes/GUIDE.md').read_text()
        section = text.split('### Méthode A', 1)[1].split('### Méthode B', 1)[0]
        self.assertIn('macOS Apple Silicon', section)
        self.assertIn('Mac Intel', section)
        self.assertIn('ne prouve pas', section)


if __name__ == '__main__':
    unittest.main()
