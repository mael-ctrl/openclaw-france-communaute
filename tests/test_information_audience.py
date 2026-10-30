"""Information technique datée, sans validation juridique ni suivi nouveau."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import annexes

class InformationAudienceTest(unittest.TestCase):
    def test_le_traitement_transitoire_ip_ua_est_explique_et_source(self):
        html = annexes.page_transparence([], [], {}, [])
        self.assertNotIn('sans identifiant personnel', html)
        self.assertIn('id="mesure-audience"', html)
        self.assertIn('https://www.goatcounter.com/help/privacy', html)
        for texte in ('adresse IP', 'User-Agent', 'huit heures', 'selon sa documentation'):
            self.assertIn(texte, html)
        self.assertIn('ne désigne pas la conservation des statistiques', html)
        for promesse in ('conforme au RGPD', 'exempté de consentement', 'aucune donnée personnelle'):
            self.assertNotIn(promesse, html)

    def test_reglages_dates_sans_confusion_sur_la_conservation(self):
        html = annexes.page_transparence([], [], {}, [])
        for texte in ('30 octobre 2026', 'sans suppression automatique', 'pages vues individuelles',
                      'référents et paramètres de campagne', 'navigateur et système', 'taille d’écran',
                      'pays et certaines régions', 'durée finie', 'n’est pas activé',
                      'mailto:crabe@blockos.fr', 'pas une validation juridique'):
            self.assertIn(texte, html)
        self.assertIn('ne prouve pas la durée effective des sauvegardes', html)

if __name__ == '__main__':
    unittest.main()
