"""Contrat progressif du gabarit partagé fil/archives, sans build complet."""
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import construction


class Elements(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.elements = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        self.elements.append((tag, dict(attrs)))


class FiltresActusTest(unittest.TestCase):
    def test_statut_poli_vide_present_avant_interaction(self):
        for archives in (False, True):
            document = construction.page_actus([], archives=archives)
            statuts = [a for _, a in Elements(document).elements if a.get('id') == 'resultats-actus']
            self.assertEqual(len(statuts), 1)
            self.assertEqual(statuts[0].get('role'), 'status')
            self.assertEqual(statuts[0].get('aria-live'), 'polite')
            self.assertEqual(statuts[0].get('aria-atomic'), 'true')
            self.assertRegex(document, r'<p[^>]*id="resultats-actus"[^>]*></p>')

    def test_outils_inoperants_masques_et_boutons_natifs_non_selectionnes(self):
        breves = [{'slug': 'essai', 'titre': 'Essai', 'resume': 'Résumé', 'source': 'Source', 'lien_source': 'https://example.org/', 'tags': ['IA']}]
        for archives in (False, True):
            with self.subTest(archives=archives):
                document = construction.page_actus(breves, archives=archives)
                elements = Elements(document).elements
                outils = [a for _, a in elements if a.get('id') == 'outils-actus']
                self.assertEqual(len(outils), 1, 'Conteneur progressif absent')
                self.assertIn('hidden', outils[0])
                boutons = [(t, a) for t, a in elements if 'filtre' in a.get('class', '').split()]
                self.assertEqual(len(boutons), 2)
                for tag, attrs in boutons:
                    self.assertEqual(tag, 'button')
                    self.assertEqual(attrs.get('type'), 'button')
                    self.assertEqual(attrs.get('aria-pressed'), 'false')
                    self.assertNotIn('actif', attrs['class'].split())
                self.assertTrue(any(t == 'label' and a.get('for') == 'recherche' for t, a in elements))
                self.assertIn('Rechercher sur cette page', document)
                self.assertIn('/breves/essai/', document)
        css = (Path(__file__).resolve().parents[1] / 'assets/style.css').read_text()
        self.assertRegex(css, r'\.barre-outils\[hidden\]\s*\{\s*display:\s*none;?\s*\}')


if __name__ == '__main__':
    unittest.main()
