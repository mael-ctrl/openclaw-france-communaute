"""Le garde anti-symlink doit accepter le dossier temporaire macOS (lui-même symlinké)."""
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import couvertures


class VerifierCheminTmpTest(unittest.TestCase):
    def test_accepte_le_dossier_temporaire_meme_symlinke(self):
        with tempfile.TemporaryDirectory() as dossier:
            cible = couvertures.verifier_chemin(Path(dossier) / "site")
            self.assertTrue(str(cible).endswith("site"))

    def test_refuse_un_vrai_lien_symbolique(self):
        with tempfile.TemporaryDirectory() as dossier:
            base = Path(dossier).resolve()
            reel = base / "site"
            reel.mkdir()
            lien = base / "evil"
            os.symlink(reel, lien)
            with self.assertRaises(ValueError):
                couvertures.verifier_chemin(lien / "sub")


if __name__ == "__main__":
    unittest.main()
