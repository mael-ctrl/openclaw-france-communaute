"""Une fiche gratuite accessible depuis /skills/, livrée sans transformation."""
import sys
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))

import annexes
import config
import construction

FICHIER = "verifier-actualite-ia.md"


class Liens(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.liens = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.liens.append(dict(attrs))


class FicheVerificationTest(unittest.TestCase):
    def test_fiche_gratuite_decouvrable_et_livree_octet_pour_octet(self):
        document = annexes.page_skills()
        liens = [a for a in Liens(document).liens
                 if a.get("href") == "/fichiers/" + FICHIER]
        self.assertEqual(len(liens), 1, "La fiche doit être proposée dans /skills/")
        self.assertIn("download", liens[0])
        self.assertNotIn("onclick", liens[0])
        self.assertIn("Vérifier une actualité IA avant de la partager", document)
        self.assertIn("sans inscription", document)
        self.assertNotIn("réellement utilisés par la machine", document)
        source = config.DOSSIER_FICHIERS / FICHIER
        self.assertTrue(source.is_file())
        texte = source.read_text(encoding="utf-8")
        for garde_fou in ("CONFIRMÉ", "À VALIDER", "CONTRADICTOIRE",
                          "source inaccessible", "pas une garantie", "sans accès web"):
            self.assertIn(garde_fou, texte)
        self.assertIn(config.URL_SITE + "/fichiers/" + FICHIER, construction.llms_txt())
        with tempfile.TemporaryDirectory() as dossier:
            sortie = Path(dossier)
            with patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            self.assertEqual((sortie / "fichiers" / FICHIER).read_bytes(), source.read_bytes())
            self.assertIn('/fichiers/' + FICHIER, (sortie / "skills/index.html").read_text())
            self.assertIn(config.URL_SITE + '/fichiers/' + FICHIER,
                          (sortie / "llms.txt").read_text())


if __name__ == "__main__":
    unittest.main()
