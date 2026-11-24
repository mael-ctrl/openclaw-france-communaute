"""Le premier essai du kit est limité, sans promettre un confinement."""
from pathlib import Path
import os
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
DOCS = "https://hermes-agent.nousresearch.com/docs/"


class KitHermesPremierEssaiTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / "kit-hermes/demarrage.md").read_text()
        self.first = " ".join(self.raw.split("## Premiers pas", 1)[1].split("## 10 usages", 1)[0].replace("\n   > ", " ").split())

    def test_preparation_avant_la_session(self):
        before = self.first.split("**Lancez votre première session**", 1)[0]
        for phrase in ("Avant de lancer Hermes", "environnement isolé sans secrets", "copie de test", "hermes tools", "permissions techniques", "terminal", "GUIDE.md"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, before)
        self.assertIn("ne confine pas", before)
        self.assertIn("ne remplace pas", before)
        self.assertIn("ne configure ni ne certifie", before)

    def test_premiere_demande_bornee_et_limites_explicites(self):
        for phrase in ("Lis uniquement", "essai.txt", "3 points", "Ne modifie aucun fichier", "ne lance aucun script", "ne contacte aucun service externe", "consigne de travail", "pas une barrière technique", "modèle distant", "sorties d’outils"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.first)
        self.assertNotIn("Résume ce dossier en 5 points", self.raw)
        self.assertNotIn("Hermes lit votre machine comme vous", self.raw)
        self.assertIn("copie de travail", self.raw.split("### 1.", 1)[1].split("### 2.", 1)[0])

    def test_diagnostic_et_sources_sans_garantie(self):
        self.assertIn("pas un audit de sécurité", self.first)
        self.assertNotIn("Tout doit être vert", self.first)
        self.assertIn("2026-11-24", self.first)
        for path in ("user-guide/features/tools#using-toolsets", "user-guide/security#file-write-safety", "user-guide/security#terminal-backend-security-comparison"):
            self.assertIn(DOCS + path, self.first)

    def test_archive_livre_le_meme_premier_essai(self):
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(archive.read("demarrage.md"), self.raw.encode())
            self.assertIn("Lis uniquement", archive.read("demarrage.md").decode())


if __name__ == "__main__":
    unittest.main()
