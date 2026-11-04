"""Le prix du fichier ne promet pas un assistant ni des crédits inclus."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import annexes


class PackUsageTest(unittest.TestCase):
    def test_outil_ia_et_couts_separes_du_pack(self):
        page = annexes.page_pack()
        self.assertNotIn('Aucune dépendance, aucun abonnement', page)
        self.assertIn('Aucun abonnement au Pack', page)
        self.assertIn('Le Pack contient des fichiers de texte, pas un logiciel ni un accès à une IA.', page)
        self.assertIn('Les éventuels frais de cet outil ou de son API ne sont pas inclus dans les 14 €.', page)
        self.assertLess(page.index('Les éventuels frais'), page.index('id="prix-pack"'))
        self.assertEqual(page.count('href="https://buy.stripe.com/9B628s2cE6IL09P8421ck0n"'), 1)
        self.assertIn('Acheter le pack — 14 €', page)


    def test_mode_emploi_natif_sans_promesse_import_universel(self):
        import re
        from unittest.mock import patch
        page = annexes.page_pack()
        blocs = re.findall(r'<details class="pack-mode-emploi">(.*?)</details>', page, re.S)
        self.assertEqual(len(blocs), 1)
        bloc = blocs[0]
        self.assertIn('<summary>Comment utiliser les fichiers du Pack ?</summary>', bloc)
        self.assertEqual(bloc.count('<li>'), 3)
        for texte in ('éditeur de texte', 'entre crochets', 'informations non sensibles',
                      'Vérifie les faits', 'Pas d’import universel ni d’automatisation prête à lancer'):
            self.assertIn(texte, bloc)
        for interdit in ('/dl/', '<script', '<form', '<iframe', 'buy.stripe.com'):
            self.assertNotIn(interdit, bloc)
        self.assertLess(page.index('class="pack-mode-emploi"'), page.index('id="extraits-pack"'))
        self.assertNotIn('<details class="pack-mode-emploi" open', page)
        with patch.object(annexes, 'extraits_pack', return_value=''):
            self.assertIn('class="pack-mode-emploi"', annexes.page_pack())


if __name__ == '__main__':
    unittest.main()
