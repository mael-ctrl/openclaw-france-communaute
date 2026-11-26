"""Le kit sépare configuration, autorisation et essai de messagerie."""
from pathlib import Path
import os
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
DOCS = "https://hermes-agent.nousresearch.com/docs/"


class KitHermesMessagerieTest(unittest.TestCase):
    def setUp(self):
        self.raw = (DL / "kit-hermes/demarrage.md").read_text()
        self.section = " ".join(self.raw.split("### 9.", 1)[1].split("### 10.", 1)[0].replace("\n> ", " ").split())

    def test_preparer_bot_prive_et_proteger_identifiants(self):
        for phrase in ("bot de test", "profil actif", "BotFather", "Developer Portal", "Message Content Intent", "jeton", "jamais dans une conversation", "identifiant numérique", "pas celui du salon", "TELEGRAM_ALLOWED_USERS", "DISCORD_ALLOWED_USERS", "appairage", "identité"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)

    def test_distinguer_configuration_et_execution(self):
        for phrase in ("hermes gateway setup", "modifie la configuration", "ne prouve pas", "hermes gateway status", "hermes gateway run", "au premier plan", "pas un second gateway", "hermes gateway start", "service déjà installé"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        self.assertNotIn("# vérifier que ça tourne", self.section)

    def test_autorisation_et_essai_sans_garantie(self):
        for phrase in ("GATEWAY_ALLOW_ALL_USERS=true", "DISCORD_ALLOW_ALL_USERS=true", "pas un confinement", "hermes tools", "terminal", "message privé", "Réponds uniquement", "aucun fichier", "aucun outil", "réponse effective", "modèle distant", "budget", "sans secrets"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.section)
        self.assertIn("permissions techniques", self.section)

    def test_sources_datees_et_archive_identique(self):
        self.assertIn("2026-11-26", self.section)
        self.assertIn("aucun bot configuré", self.section)
        for path in ("user-guide/messaging/telegram#step-5-configure-hermes", "user-guide/messaging/discord#step-8-configure-hermes-agent", "user-guide/security#user-authorization-gateway", "reference/cli-commands#hermes-gateway"):
            self.assertIn(DOCS + path, self.section)
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(archive.read("demarrage.md"), self.raw.encode())


if __name__ == "__main__":
    unittest.main()
