"""Le démarrage distingue modèle local, coûts et confinement réseau."""
from pathlib import Path
import os
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
DOCS = "https://hermes-agent.nousresearch.com/docs/"


class KitHermesDemarrageLocalTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / "kit-hermes/demarrage.md").read_text()
        self.section = " ".join(self.raw.split("### 10.", 1)[1].split("## Et après", 1)[0].split())

    def test_couts_locaux_sans_promesse_absolue(self):
        for phrase in ("kit", "gratuits", "facturation API de ce modèle", "matériel", "électricité", "hébergement", "outils externes", "Ollama Cloud"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        for promise in ("100 % en local (gratuit)", "sans coût", "Tout reste chez vous", "sans dépenser"):
            self.assertNotIn(promise, self.raw)

    def test_hors_ligne_conditionnel_et_verifiable(self):
        for phrase in ("ne garantit pas le hors-ligne", "modèles auxiliaires", "fournisseurs de secours", "hermes tools", "terminal", "contrôle réseau indépendant", "sans secrets", "pas un audit réseau"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        self.assertIn("GUIDE.md", self.section)

    def test_parcours_local_et_sources_datees(self):
        for phrase in ("https://docs.ollama.com/quickstart", "hermes model", "Custom endpoint", "http://localhost:11434/v1", "appel", "outils", "64 000", "contexte", "2026-11-23"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        for path in ("reference/faq#can-i-use-it-offline--with-local-models", "user-guide/configuration#auxiliary-models", "integrations/providers#fallback-providers"):
            self.assertIn(DOCS + path, self.section)
        self.assertNotIn("curl -fsSL https://ollama.com/install.sh | sh", self.section)

    def test_archive_livre_la_meme_notice(self):
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            data = archive.read("demarrage.md")
            self.assertEqual(data, (DL / "kit-hermes/demarrage.md").read_bytes())
            self.assertIn("ne garantit pas le hors-ligne", data.decode())


if __name__ == "__main__":
    unittest.main()
