"""Contrat CSS de la seule grille mobile, sans exécuter les kits (IA)."""
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / 'sites' / 'openclaw-france'

class HubGrilleResiduelleTest(unittest.TestCase):
    def test_colonne_reductible_dans_le_seuil_mobile_existant(self):
        css = (SITE / 'static/style.css').read_text()
        mobile = css.split('@media (max-width:760px){', 1)[1]
        self.assertRegex(mobile, r'\.grille-2\s*\{\s*grid-template-columns:minmax\(0,1fr\)\s*\}')

    def test_regle_desktop_et_seuil_tablette_conserves(self):
        css = (SITE / 'static/style.css').read_text()
        self.assertIn('.grille-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:22px}', css)
        tablette = css.split('@media (max-width:1000px){', 1)[1].split('@media', 1)[0]
        self.assertNotIn('.grille-2', tablette)

    def test_pas_de_masquage_global_pour_dissimuler_le_debordement(self):
        css = (SITE / 'static/style.css').read_text()
        self.assertNotRegex(css, r'overflow(?:-x)?\s*:\s*(?:hidden|clip)')

if __name__ == '__main__':
    unittest.main()
