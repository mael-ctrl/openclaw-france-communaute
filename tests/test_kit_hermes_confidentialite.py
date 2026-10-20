"""Confidentialité du kit Hermes : stockage local sans promesse de confinement."""
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
DOCS = "https://hermes-agent.nousresearch.com/docs/"
TITLE = "### Confidentialité : modèle local ne veut pas dire hors ligne"


class KitHermesConfidentialiteTest(unittest.TestCase):
    def setUp(self):
        self.guide = (SITE / "dl/kit-hermes/GUIDE.md").read_text(encoding="utf-8")
        self.text = " ".join(self.guide.split())

    def test_resume_sans_promesse_de_confinement(self):
        resume = self.text.split("**Votre vie privée**", 1)[1].split("**Combien", 1)[0]
        for phrase in ("outils", "contexte", "ne rend pas", "hors ligne"):
            self.assertIn(phrase, resume)
        for promise in ("rien ne sort du tout", "tout reste chez vous", "Seuls les appels au fournisseur"):
            self.assertNotIn(promise, self.text)

    def test_distingue_stockage_modele_et_services_connectes(self):
        self.assertIn(TITLE, self.text)
        section = self.text.split(TITLE, 1)[1].split("## 5.", 1)[0]
        for phrase in ("~/.hermes/", "contexte", "fichiers", "outils", "fournisseur",
                       "recherche web", "MCP", "messagerie", "mémoire", "modèles auxiliaires",
                       "fournisseurs de secours", "hermes model", "hermes tools"):
            self.assertIn(phrase, section)

    def test_precautions_et_sources_datees_sans_audit_invente(self):
        self.assertIn(TITLE, self.text)
        section = self.text.split(TITLE, 1)[1].split("## 5.", 1)[0]
        for phrase in ("sans secrets", "sauvegardes", "terminal", "contrôle réseau indépendant",
                       "pas un audit réseau", "2026-10-20"):
            self.assertIn(phrase, section)
        for path in ("reference/faq#is-my-data-sent-anywhere", "user-guide/features/tools#using-toolsets",
                     "user-guide/configuration#auxiliary-models", "integrations/providers#optional-api-keys",
                     "integrations/providers#fallback-providers"):
            self.assertIn(DOCS + path, section)


if __name__ == "__main__":
    unittest.main()
