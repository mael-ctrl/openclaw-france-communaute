"""Fiche d'évaluation manuelle : téléchargement natif et contenu traçable."""
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

FICHIER = "comparer-reponses-ia.md"
TITRE = "Comparer deux IA sur vos propres cas"


class Liens(HTMLParser):
    def __init__(self, document):
        super().__init__()
        self.liens = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.liens.append(dict(attrs))


class FicheComparaisonTest(unittest.TestCase):
    def test_fiche_decouvrable_gratuite_et_livree_sans_transformation(self):
        document = annexes.page_skills()
        liens = [lien for lien in Liens(document).liens
                 if lien.get("href") == "/fichiers/" + FICHIER]
        self.assertEqual(len(liens), 1, "La nouvelle fiche doit être accessible depuis /skills/")
        self.assertIn("download", liens[0])
        self.assertNotIn("onclick", liens[0])
        self.assertIn(TITRE, document)
        self.assertIn("sans inscription", document)
        fiche = config.DOSSIER_FICHIERS / FICHIER
        self.assertTrue(fiche.is_file())
        texte = fiche.read_text(encoding="utf-8")
        for attendu in ("méthode proposée aux lecteurs", "pas un classement universel",
                        "données fictives", "NON TESTÉ", "critères avant",
                        "réponses brutes", "sans preuve", "## Sources"):
            self.assertIn(attendu, texte)
        self.assertIn(config.URL_SITE + "/fichiers/" + FICHIER, construction.llms_txt())
        with tempfile.TemporaryDirectory() as dossier:
            sortie = Path(dossier)
            with patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            self.assertEqual((sortie / "fichiers" / FICHIER).read_bytes(), fiche.read_bytes())
            self.assertIn("/fichiers/" + FICHIER, (sortie / "skills/index.html").read_text())
            self.assertIn(config.URL_SITE + "/fichiers/" + FICHIER,
                          (sortie / "llms.txt").read_text())


if __name__ == "__main__":
    unittest.main()
