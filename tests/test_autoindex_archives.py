"""Le build protège les répertoires d'archives, sans les indexer au sitemap."""
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class AutoindexArchivesTest(unittest.TestCase):
    def test_build_protege_les_deux_repertoires_sans_toucher_la_racine(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            source = racine / "breves.json"
            source.write_text("[]", encoding="utf-8")
            sortie = racine / "site"
            sortie.mkdir()
            # Une configuration d'hébergement préexistante doit rester intacte.
            htaccess = sortie / ".htaccess"
            htaccess.write_text("# configuration existante\n", encoding="utf-8")
            with patch.object(config, "FICHIER_BREVES", source), \
                    patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            for repertoire in ("breves", "actus/page"):
                cible = sortie / repertoire / ".htaccess"
                self.assertTrue(cible.is_file(), f"Listing non désactivé : {repertoire}")
                self.assertIn("Options -Indexes", cible.read_text(encoding="utf-8").splitlines())
            # Seul le répertoire parent redirige : aucune ancienne brève capturée.
            regles = (sortie / "breves/.htaccess").read_text().splitlines()
            redirects = [ligne.split() for ligne in regles if ligne.startswith("RedirectMatch ")]
            self.assertEqual(len(redirects), 1, "Le parent /breves/ doit rejoindre le fil HTML")
            directive, statut, motif, cible = redirects[0]
            self.assertEqual((directive, statut, cible),
                             ("RedirectMatch", "301", config.URL_SITE + "/actus/"))
            for url in ("/breves", "/breves/"):
                self.assertIsNotNone(re.search(motif, url))
            for url in ("/breves/ancienne-breve/", "/breves/ancienne-breve/index.html",
                        "/breves/inconnue/", "/breves-long/", "/actus/", "/dl/pack.zip"):
                self.assertIsNone(re.search(motif, url), url)
            self.assertEqual((sortie / "actus/page/.htaccess").read_text(), "Options -Indexes\n")
            self.assertEqual(htaccess.read_text(), "# configuration existante\n")
            self.assertNotIn(".htaccess", (sortie / "sitemap.xml").read_text())
            self.assertTrue((sortie / "actus/index.html").is_file())


if __name__ == "__main__":
    unittest.main()
