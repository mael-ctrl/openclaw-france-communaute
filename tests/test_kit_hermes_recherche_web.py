"""Contrat documentaire du premier essai de recherche web dans le kit Hermes."""
from pathlib import Path
import os
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
DOCS = "https://hermes-agent.nousresearch.com/docs/"

class KitHermesRechercheWebTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / "kit-hermes/demarrage.md").read_text()
        self.section = " ".join(self.raw.split("### 5.", 1)[1].split("### 6.", 1)[0].replace("\n> ", " ").replace("**", "").split())

    def test_outils_et_budget_non_garantis(self):
        for phrase in ("hermes tools", "profil actif", "web_search", "web_extract", "fournisseur", "budget", "ne garantit pas", "requêtes", "sans secrets"):
            with self.subTest(phrase=phrase): self.assertIn(phrase, self.section)

    def test_consigne_bornee_et_sources_verifiables(self):
        for phrase in ("Remplacez", "[sujet]", "[date de début]", "[date de fin]", "trois sources", "sources primaires", "URL", "date de publication", "date de consultation", "date inconnue", "CONFIRMÉ", "À VALIDER", "CONTRADICTOIRE", "extrait de moteur", "Ouvrez"):
            with self.subTest(phrase=phrase): self.assertIn(phrase, self.section)

    def test_pas_de_contournement_ni_confiance_aveugle(self):
        for phrase in ("connexion", "paywall", "CAPTCHA", "Ne contourne", "ne publie rien", "instructions", "données", "permissions techniques", "ne lance aucun script"):
            with self.subTest(phrase=phrase): self.assertIn(phrase, self.section)

    def test_sources_datees_et_archive_exacte(self):
        self.assertIn("2026-11-27", self.section)
        for path in ("user-guide/features/tools#available-tools", "user-guide/features/tools#using-toolsets", "user-guide/security#website-access-policy"):
            self.assertIn(DOCS + path, self.section)
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(archive.read("demarrage.md"), self.raw.encode())

if __name__ == "__main__":
    unittest.main()
