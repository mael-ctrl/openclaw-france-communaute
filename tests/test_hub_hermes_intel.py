"""P10 — ne pas reconduire un avertissement périmé sur le kit."""
from pathlib import Path
import os
import re
import unittest

ROOT = Path(os.environ.get('P10_TREE', Path(__file__).resolve().parents[1]))


class HtmlIntel(unittest.TestCase):
    def test_renvoi_guide_readme_sans_diagnostic_perime(self):
        html = (ROOT / 'sites/openclaw-france/hermes/index.html').read_text()
        block = re.search(r'<section id="prerequis"[^>]*>(.*?)</section>', html, re.S).group(1)
        self.assertNotIn('conservent le', block)
        self.assertNotIn('Leur mention de bundles Intel', block)
        self.assertIn('prérequis du guide', block)
        self.assertIn('README', block)
        self.assertIn('documentation officielle actuelle prévaut', block)
        self.assertIn('Desktop Intel : aucun bundle actuel.', block)


if __name__ == '__main__':
    unittest.main()
