"""Formulaire d'inscription à La Brève (Buttondown) : présent, sans secret, sans JS."""
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class BreveFormTest(unittest.TestCase):
    def test_le_formulaire_utilise_l_endpoint_public_buttondown(self):
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
            self.assertIn('action="https://buttondown.com/api/emails/embed-subscribe/la-breve-du-crabe"', accueil)
            self.assertIn('method="post"', accueil)
            self.assertIn('name="email"', accueil)
            self.assertIn('name="embed" value="1"', accueil)
            self.assertIn('class="breve-piege"', accueil)  # honeypot
            # Aucun secret dans le HTML public
            for interdit in ("api_key", "Authorization", "95cc8fe9"):
                self.assertNotIn(interdit, accueil)
            # La page RGPD liée existe avec son ancre
            transparence = (sortie / "transparence" / "index.html").read_text(encoding="utf-8")
            self.assertIn('id="breve"', transparence)
            self.assertIn("La Brève &amp; vos données", transparence)
            self.assertIn("Buttondown", transparence)


if __name__ == "__main__":
    unittest.main()
