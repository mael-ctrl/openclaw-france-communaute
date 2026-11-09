"""Retour explicite vers le formulaire, sans dépendre de l'historique."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import construction

RETOUR = '<p class="petit-texte"><a href="/#la-breve">Retour au formulaire de La Brève</a></p>'


class RetourNewsletterTest(unittest.TestCase):
    def test_confidentialite_offre_un_retour_natif_au_formulaire(self):
        page = annexes.page_transparence([], [], {}, [])
        self.assertEqual(page.count(RETOUR), 1, "Retour explicite absent ou dupliqué")
        self.assertLess(page.index('id="breve"'), page.index(RETOUR))
        self.assertLess(page.index(RETOUR), page.index('id="mesure-audience"'))
        self.assertNotIn('<form', page)
        home = construction.page_accueil([], [], {}, [])
        self.assertEqual(home.count('class="breve-form"'), 1)
        self.assertEqual(home.count('id="la-breve"'), 1)


if __name__ == "__main__":
    unittest.main()
