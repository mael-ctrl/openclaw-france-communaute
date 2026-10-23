"""Mesure d'audience GoatCounter (sans cookie) présente sur le site public."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class GoatCounterTest(unittest.TestCase):
    def test_le_script_de_mesure_est_pose(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            articles = racine / "articles"
            articles.mkdir()
            breves = racine / "breves.json"
            breves.write_text("[]", encoding="utf-8")
            sortie = racine / "site"
            with patch.object(config, "DOSSIER_ARTICLES", articles), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            accueil = (sortie / "index.html").read_text(encoding="utf-8")
            self.assertIn('data-goatcounter="https://communaute-ia.goatcounter.com/count"', accueil)
            self.assertIn("gc.zgo.at/count.js", accueil)
            # Transparence : la mesure d'audience est déclarée
            transparence = (sortie / "transparence" / "index.html").read_text(encoding="utf-8")
            self.assertIn("GoatCounter", transparence)


if __name__ == "__main__":
    unittest.main()
