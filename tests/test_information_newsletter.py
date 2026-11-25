"""Information newsletter bornée aux réglages et à l'aperçu contrôlés."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes


class InformationNewsletterTest(unittest.TestCase):
    def test_le_suivi_est_decrit_par_un_constat_date_et_borne(self):
        html = annexes.page_transparence([], [], {}, [])
        bloc = html.split('id="breve"', 1)[1].split('id="mesure-audience"', 1)[0]
        for texte in (
            'id="mesure-breve"', '17 novembre 2026',
            'mesures d’ouvertures et de clics', 'paramètres UTM',
            'étaient désactivés', 'aperçu reçu', 'lien technique du prestataire',
            'pas sur tous les traitements internes', 'ni sur une campagne',
            'pas une validation juridique',
        ):
            self.assertIn(texte, bloc)
        self.assertNotIn('statistiques de la newsletter se limitent', bloc)
        self.assertNotIn('désactivables sur demande', bloc)
        for interdit in ('aucun suivi', 'zéro suivi', 'conforme au RGPD'):
            self.assertNotIn(interdit, bloc)
        for preserve in (
            'Double opt-in', 'Désinscription',
            'https://buttondown.com/legal/privacy', 'société américaine',
            'crabe@blockos.fr', 'href="/#la-breve"',
        ):
            self.assertIn(preserve, bloc)
        self.assertNotIn('<form', bloc)
        self.assertNotIn('<script', bloc)


if __name__ == '__main__':
    unittest.main()
