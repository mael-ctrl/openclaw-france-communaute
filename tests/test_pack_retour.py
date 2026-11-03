"""Le retour statique du Pack n'est pas une vérification de paiement."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes


class RetourPackTests(unittest.TestCase):
    def test_retour_ne_confirme_pas_un_paiement_non_verifie(self):
        rendu = annexes.page_pack_merci()
        self.assertNotIn("Ton paiement est passé", rendu)
        self.assertNotIn("le pack est à toi", rendu)
        self.assertIn("elle ne vérifie pas le statut d’un paiement", rendu)
        self.assertIn("Sa seule ouverture ne vaut donc pas confirmation d’achat", rendu)


    def test_doute_paiement_oriente_vers_aide_avant_reessai(self):
        rendu = annexes.page_pack_merci()
        aide = '<a href="mailto:crabe@blockos.fr">crabe@blockos.fr</a>'
        self.assertIn(aide, rendu)
        self.assertIn("avant de réessayer", rendu)
        self.assertIn("Ne transmets pas de données bancaires", rendu)
        self.assertLess(rendu.index(aide), rendu.index('<h2>Télécharge ton pack</h2>'))
        self.assertIn('href="/dl/pack-du-crabe-100-prompts.md" download', rendu)
        self.assertIn('href="/dl/pack-du-crabe-100-prompts.json" download', rendu)
        self.assertNotIn("buy.stripe.com", rendu)


if __name__ == "__main__":
    unittest.main()
