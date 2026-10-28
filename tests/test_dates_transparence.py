"""Gardes CSS locaux ; la géométrie est vérifiée séparément dans Chromium."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class DatesTransparenceTest(unittest.TestCase):
    def test_dates_erreurs_autorisent_retour_ligne(self):
        css = (ROOT / 'assets/style.css').read_text()
        rule = re.search(r'\.erreurs-liste\s+\.j-ts\s*\{([^}]*)\}', css)
        self.assertIsNotNone(rule, 'les dates hors tableau héritent encore du nowrap du journal')
        self.assertRegex(rule.group(1), r'white-space\s*:\s*normal\s*;')

    def test_dates_tableau_restent_non_secables(self):
        css = (ROOT / 'assets/style.css').read_text()
        rule = re.search(r'^\.j-ts\s*\{([^}]*)\}', css, re.M)
        self.assertIsNotNone(rule)
        self.assertRegex(rule.group(1), r'white-space\s*:\s*nowrap\s*;')

    def test_pas_de_masquage_des_erreurs(self):
        css = (ROOT / 'assets/style.css').read_text()
        rules = re.findall(r'\.erreurs-liste[^{}]*\{([^}]*)\}', css)
        self.assertTrue(rules)
        self.assertNotRegex(' '.join(rules), r'overflow(?:-x)?\s*:\s*(?:hidden|clip)|text-overflow\s*:\s*ellipsis|display\s*:\s*none')

if __name__ == '__main__':
    unittest.main()
