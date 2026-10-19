"""Le catalogue conservé complète le fil de 400 sans inventer l'historique."""
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import construction
import config
from test_pagination_actus import LiensActus, breves_test


class ArchivesConserveesTest(unittest.TestCase):
    def construire_fixture(self, breves, racine):
        source = racine / "breves.json"
        source.write_text(json.dumps(breves), encoding="utf-8")
        sortie = racine / "site"
        with ExitStack() as pile:
            for nom, valeur in (("FICHIER_BREVES", source), ("DOSSIER_SORTIE", sortie),
                                ("DOSSIER_ARTICLES", racine / "articles")):
                pile.enter_context(patch.object(config, nom, valeur))
            # Hors contrat : annexes ; vrais rendus, couvertures et sitemap.
            pile.enter_context(patch("annexes.construire_annexes", return_value=({}, {})))
            construction.construire()
        return sortie

    def test_toutes_les_sources_conservees_sont_construites_sans_elargir_le_fil(self):
        with tempfile.TemporaryDirectory() as dossier:
            breves = breves_test(401)
            # Deux chemins peuvent avoir le même ID : ne pas les fusionner.
            breves[0]["id"] = breves[-1]["id"] = "meme-identifiant"
            sortie = self.construire_fixture(breves, Path(dossier))
            self.assertTrue((sortie / "breves/breve-400/index.html").is_file(),
                            "La brève conservée hors fil doit être reconstruite")
            self.assertFalse((sortie / "actus/page/5").exists())
            urls = {n.text for n in ET.parse(sortie / "sitemap.xml").findall(
                ".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
            self.assertEqual({u for u in urls if "/breves/" in u},
                             {config.URL_SITE + f"/breves/breve-{i}/" for i in range(401)})

    def test_catalogue_pagine_relie_toutes_les_sources_avec_ses_canoniques(self):
        with tempfile.TemporaryDirectory() as dossier:
            sortie = self.construire_fixture(breves_test(401), Path(dossier))
            chemins = ["/archives-breves/"] + [f"/archives-breves/page-{i}/" for i in range(2, 6)]
            self.assertTrue((sortie / "archives-breves/index.html").is_file())
            groupes = []
            for numero, chemin in enumerate(chemins, 1):
                document = (sortie / chemin.lstrip("/") / "index.html").read_text()
                liens = LiensActus(document)
                self.assertEqual(liens.canoniques, [config.URL_SITE + chemin])
                self.assertIn("pas un historique exhaustif", document)
                self.assertIn("Rechercher sur cette page", document)
                self.assertEqual([a["href"] for a in liens.liens if a.get("rel") == "prev"],
                                 [chemins[numero - 2]] if numero > 1 else [])
                self.assertEqual([a["href"] for a in liens.liens if a.get("rel") == "next"],
                                 [chemins[numero]] if numero < 5 else [])
                groupe = {a["href"] for a in liens.liens if a["href"].startswith("/breves/")}
                self.assertEqual(groupe, {f"/breves/breve-{i}/" for i in range((numero-1)*100, min(numero*100,401))})
                groupes.append(groupe)
            self.assertEqual(sum(map(len, groupes)), len(set.union(*groupes)))
            self.assertIn('href="/archives-breves/"', (sortie / "actus/index.html").read_text())
            self.assertIn(config.URL_SITE + "/archives-breves/", (sortie / "llms.txt").read_text())
            xml = ET.parse(sortie / "sitemap.xml")
            ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
            urls = {e.findtext("s:loc", namespaces=ns): e for e in xml.findall("s:url", ns)}
            self.assertTrue({config.URL_SITE + c for c in chemins} <= urls.keys())
            self.assertIsNone(urls[config.URL_SITE + "/breves/breve-400/"].find("s:lastmod", ns))


    def test_limites_du_catalogue_vide_court_et_pages_incompletes(self):
        for nombre in (0, 1, 100, 101, 201, 400, 401):
            with self.subTest(nombre=nombre):
                groupes = []
                pages = max(1, (nombre + 99) // 100)
                for numero in range(1, pages + 1):
                    document = construction.page_actus(breves_test(nombre), numero, archives=True)
                    liens = LiensActus(document)
                    groupes.append({a["href"] for a in liens.liens if a["href"].startswith("/breves/")})
                    self.assertEqual(any(a.get("rel") == "next" for a in liens.liens), numero < pages)
                    self.assertEqual(any(a.get("rel") == "prev" for a in liens.liens), numero > 1)
                self.assertEqual(len(set.union(*groupes)), nombre)
                self.assertEqual(sum(map(len, groupes)), nombre)

    def test_collision_hors_fil_refusee_avant_ecriture_html(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            breves = breves_test(401)
            breves[-1]["slug"] = breves[0]["slug"]
            with self.assertRaisesRegex(ValueError, "dupliquée"):
                self.construire_fixture(breves, racine)
            self.assertEqual(list((racine / "site").rglob("*.html")), [])

    def test_traversee_hors_fil_refusee_avant_ecriture_html(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            breves = breves_test(401)
            breves[-1]["slug"] = "../hors-site"
            with self.assertRaises(ValueError):
                self.construire_fixture(breves, racine)
            self.assertEqual(list((racine / "site").rglob("*.html")), [])

    def test_budget_cloud_borne_couvre_le_premier_envoi_des_archives(self):
        import re
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/maj.yml").read_text()
        minutes = int(re.search(r"timeout-minutes:\s*(\d+)", workflow).group(1))
        # Le premier envoi réel a été annulé à 25 min, au milieu des brèves.
        self.assertGreaterEqual(minutes, 40)
        self.assertLessEqual(minutes, 45, "Garder un garde-fou de durée explicite")


if __name__ == "__main__":
    unittest.main()
