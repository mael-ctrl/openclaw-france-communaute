"""Le kit ne confond pas Blank Slate et une protection en lecture seule."""
from pathlib import Path
import os
import unittest
import zipfile

DL = Path(os.environ.get("KIT_HERMES_DL", Path(__file__).resolve().parents[1] / "sites/openclaw-france/dl"))
SOURCE = "https://hermes-agent.nousresearch.com/docs/getting-started/quickstart#2-choose-a-provider"


class KitHermesPermissionsTest(unittest.TestCase):
    def test_guide_explique_les_acces_avant_la_premiere_session(self):
        text = (DL / "kit-hermes/GUIDE.md").read_text()
        setup = text.split("## 4. Étape 2", 1)[1].split("## 5.", 1)[0]
        for phrase in ("Blank Slate", "opérations sur fichiers", "terminal",
                       "ne garantit pas la lecture seule", "hermes tools",
                       "environnement isolé sans secrets", "permissions techniques"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, setup)
        self.assertNotIn("tout le reste\ndésactivé", setup)
        self.assertIn("désactiver les outils de fichiers", setup)
        self.assertIn("2026-11-22", setup)
        self.assertIn(SOURCE, setup)

    def test_readme_avertit_avant_de_lancer_la_session(self):
        text = (DL / "kit-hermes/README.md").read_text()
        setup = text.split("## Démarrage rapide", 1)[1].split("## Ce que", 1)[0]
        before_chat = setup.split("4. **Lancez", 1)[0]
        for phrase in ("Blank Slate", "opérations sur fichiers", "terminal",
                       "ne garantit pas la lecture seule", "hermes tools",
                       "environnement isolé sans secrets", "GUIDE.md"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, before_chat)
        self.assertIn(SOURCE, before_chat)

    def test_zip_livre_les_deux_avertissements_exacts(self):
        with zipfile.ZipFile(DL / "kit-hermes.zip") as archive:
            self.assertIsNone(archive.testzip())
            for name in ("GUIDE.md", "README.md"):
                with self.subTest(name=name):
                    data = archive.read(name)
                    self.assertEqual(data, (DL / "kit-hermes" / name).read_bytes())
                    self.assertIn("ne garantit pas la lecture seule", data.decode())


if __name__ == "__main__":
    unittest.main()
