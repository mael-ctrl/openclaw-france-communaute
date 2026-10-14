"""Un abonnement aux analyses seules, sans modifier le flux général."""
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class FluxArticlesTest(unittest.TestCase):
    def test_les_lecteurs_rss_decouvrent_les_deux_flux_depuis_le_html(self):
        class Flux(HTMLParser):
            def __init__(self):
                super().__init__()
                self.liens = []

            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == "link" and attrs.get("rel") == "alternate" and attrs.get("type") == "application/rss+xml":
                    self.liens.append(attrs)

        parser = Flux()
        parser.feed(construction.page("Test", "Description", "<p>Test</p>", "/"))
        self.assertEqual([lien["href"] for lien in parser.liens], ["/feed.xml", "/feed-articles.xml"])
        self.assertEqual(parser.liens[1]["title"], config.NOM_SITE + " — RSS articles uniquement")

    def test_flux_vide_valide_et_titre_echappe(self):
        titre = 'Analyses & IA <français> "🦀"'
        canal = ET.fromstring(construction.feed_xml([], [], titre_flux=titre)).find("channel")
        self.assertEqual(canal.findtext("title"), titre)
        self.assertEqual(canal.findall("item"), [])

    def test_build_produit_un_flux_des_20_articles_recents_sans_breve(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            articles = racine / "articles"
            articles.mkdir()
            for i in range(1, 26):
                article = {
                    "slug": f"analyse-{i}", "titre": f"Analyse {i} & IA",
                    "chapo": "Résumé <sourcé> & lisible.", "html": "<p>Analyse.</p>",
                    "date": f"2026-09-{i:02d}T12:00:00+00:00", "sources": [], "tags": [],
                }
                (articles / f"{i}.json").write_text(json.dumps(article), encoding="utf-8")
            breves = racine / "breves.json"
            breves.write_text(json.dumps([{
                "slug": "une-breve", "titre": "Une brève", "resume": "Résumé.",
                "source": "Source", "lien_source": "https://example.org/",
                "date_redac": "2026-09-26T12:00:00+00:00", "tags": [],
            }]), encoding="utf-8")
            sortie = racine / "site"
            with patch.object(config, "DOSSIER_ARTICLES", articles), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            cible = sortie / "feed-articles.xml"
            self.assertTrue(cible.is_file(), "Le build doit produire le flux des analyses seules")
            canal = ET.parse(cible).find("channel")
            self.assertEqual(canal.findtext("title"), config.NOM_SITE + " — Articles de fond")
            items = canal.findall("item")
            attendus = [f"{config.URL_SITE}/articles/analyse-{i}/" for i in range(25, 5, -1)]
            self.assertEqual([item.findtext("link") for item in items], attendus)
            self.assertEqual([item.findtext("guid") for item in items], attendus)
            self.assertEqual(items[0].findtext("title"), "Analyse 25 & IA")
            self.assertEqual(items[0].findtext("description"), "Résumé <sourcé> & lisible.")
            for item in items:
                self.assertEqual(item.find("guid").get("isPermaLink"), "true")
                chemin = item.findtext("link").removeprefix(config.URL_SITE).lstrip("/")
                self.assertTrue((sortie / chemin / "index.html").is_file())
            general = ET.parse(sortie / "feed.xml").find("channel")
            self.assertEqual(general.findtext("title"), config.NOM_SITE)
            self.assertIn(config.URL_SITE + "/breves/une-breve/",
                          [item.findtext("link") for item in general.findall("item")])


if __name__ == "__main__":
    unittest.main()
