"""Contrats CSS ciblés ; complétés par reflow_qa.cjs, pas une certification."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]

class ReflowContenuTest(unittest.TestCase):
    def setUp(self):
        self.css = (ROOT/'assets/style.css').read_text(encoding='utf-8')
        marker = '/* ---------------- Reflow du contenu ---------------- */'
        self.assertIn(marker, self.css, 'La stratégie de reflow de contenu manque')
        self.rules = self.css.split(marker, 1)[1].split('/* ---------------- Responsive', 1)[0]

    def test_mots_et_liens_longs_restent_dans_contenu(self):
        self.assertIn('main, .pied { overflow-wrap: anywhere; }', self.rules)

    def test_colonne_minimale_ne_depasse_pas_conteneur(self):
        self.assertIn('minmax(min(285px, 100%), 1fr)', self.rules)

    def test_titres_actions_et_champs_peuvent_revenir_ligne(self):
        self.assertIn('.section-tete { flex-wrap: wrap; }', self.rules)
        self.assertIn('.bouton { min-width: 0; max-width: 100%; }', self.rules)
        self.assertIn('.breve-champs input { min-width: 0; max-width: 100%; }', self.rules)
        self.assertIn('.lire { white-space: normal; }', self.rules)

    def test_aucun_masquage_ni_navigation_modifiee(self):
        self.assertNotRegex(self.rules, r'overflow(?:-x|-y)?\s*:|display\s*:|visibility\s*:|font-size\s*:|height\s*:|clip|text-overflow|\.entete|\.nav|\.marque')
        self.assertEqual(len(re.findall(r'\{', self.rules)), 6)

if __name__ == '__main__':
    unittest.main()
