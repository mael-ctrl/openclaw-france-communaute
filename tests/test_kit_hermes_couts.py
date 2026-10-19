"""Budget du kit Hermes : coût local et garde-fous sans promesse universelle."""
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
SOURCE = "https://hermes-agent.nousresearch.com/docs/getting-started/quickstart#2-choose-a-provider"


class KitHermesCoutsTest(unittest.TestCase):
    def setUp(self):
        self.guide = (SITE / "dl/kit-hermes/GUIDE.md").read_text(encoding="utf-8")
        self.text = " ".join(self.guide.split())

    def test_resume_distingue_kit_api_outils_et_hebergement(self):
        resume = self.text.split("**Combien ça coûte ?**", 1)[1].split("## 2.", 1)[0]
        for word in ("kit", "gratuits", "API", "abonnement", "outils", "hébergement", "matériel", "électricité"):
            self.assertIn(word, resume)
        for promise in ("100 % gratuits", "100 % gratuite", "sans dépenser un centime"):
            self.assertNotIn(promise, self.text)

    def test_limite_conditionnelle_et_premier_essai_court(self):
        budget = self.text.split("### Modèle et budget avant le premier essai", 1)[1].split("> **Où", 1)[0]
        for word in ("plafond", "si le fournisseur le permet", "abonnement", "tarifs", "essai court", "facturation", "/usage"):
            self.assertIn(word, budget)
        self.assertIn("ne remplace pas", budget)
        self.assertIn(SOURCE, budget)
        self.assertIn("2026-10-19", budget)

    def test_modele_local_ressources_et_non_garantie(self):
        title = "### Un modèle local : sans facturation API du modèle"
        self.assertIn(title, self.text)
        section = self.text.split(title, 1)[1].split("## 5.", 1)[0]
        for word in ("matériel", "électricité", "outils externes", "hébergement", "quantification", "contexte", "64 000", "aucun minimum RAM universel"):
            self.assertIn(word, section)
        self.assertNotIn("Comptez 8 Go", section)
        self.assertIn("http://localhost:11434/v1", section)
        self.assertIn("hermes model", section)
        self.assertIn("https://hermes-agent.nousresearch.com/docs/integrations/providers#ollama--local-models-zero-config", section)


if __name__ == "__main__":
    unittest.main()
