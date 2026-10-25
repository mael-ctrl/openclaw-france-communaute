"""Accès natif au formulaire existant, sans inscription automatique."""
import sys
import unittest

from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import construction


class LectureNewsletterTest(unittest.TestCase):
    def test_l_invitation_pointe_vers_la_section_du_formulaire_existant(self):
        bloc = construction.bloc_suivre()
        self.assertIn('<a class="bouton fantome" href="/#la-breve">La newsletter gratuite</a>', bloc)
        accueil = construction.page_accueil([], [], {}, [])
        self.assertIn('<section class="section" id="la-breve" aria-labelledby="breve-titre">', accueil)
        self.assertEqual(accueil.count('id="la-breve"'), 1)
        self.assertLess(accueil.index('id="la-breve"'), accueil.index('class="breve-form"'))

    def test_le_lien_ne_soumet_rien_et_ne_duplique_pas_le_formulaire(self):
        bloc = construction.bloc_suivre()
        for interdit in ("<form", "<input", "<script", "<iframe", "onclick", "buttondown.com"):
            self.assertNotIn(interdit, bloc)
        accueil = construction.page_accueil([], [], {}, [])
        self.assertEqual(accueil.count('class="breve-form"'), 1)
        self.assertIn('method="post"', accueil)
        self.assertIn('type="email" required', accueil)
        self.assertIn('double opt-in', accueil)
        self.assertIn('href="/transparence/#breve"', accueil)


if __name__ == "__main__":
    unittest.main()
