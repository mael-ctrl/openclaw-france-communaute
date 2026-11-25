"""Le kit distingue préparation, exécution planifiée et livraison."""
from pathlib import Path
import os
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
DOCS = "https://hermes-agent.nousresearch.com/docs/"


class KitHermesPlanificationTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / "kit-hermes/demarrage.md").read_text()
        self.section = " ".join(self.raw.split("### 8.", 1)[1].split("### 9.", 1)[0].replace("\n> ", " ").split())

    def test_preparer_sans_creer_et_borner_essai(self):
        for phrase in ("sans créer ni modifier de tâche", "essai ponctuel", "sans secrets", "chemin absolu", "Europe/Paris", "budget", "permissions techniques", "accord explicite"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        self.assertNotIn("fais-moi la synthèse de ma journée et envoie-la-moi", self.section)

    def test_prerequis_et_livraison_separes(self):
        for phrase in ("gateway", "profil actif", "hermes cron status", "hermes cron list", "hermes cron runs", "deliver=local", "modèle distant", "réponse finale", "doublon", "réception effective"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        self.assertIn("ne prouve pas", self.section)

    def test_arret_et_sources_documentaires(self):
        for phrase in ("hermes cron pause", "hermes cron cancel", "ne stoppe pas", "ne désactive pas", "actions déjà effectuées", "2026-11-25", "aucune tâche créée"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        for path in ("user-guide/features/cron#how-it-works", "user-guide/features/cron#delivery-options", "user-guide/features/cron#lifecycle-actions", "reference/cli-commands#hermes-cron"):
            self.assertIn(DOCS + path, self.section)

    def test_archive_contient_la_meme_notice(self):
        self.assertIn("sans créer ni modifier de tâche", self.section)
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(archive.read("demarrage.md"), self.raw.encode())


if __name__ == "__main__":
    unittest.main()
