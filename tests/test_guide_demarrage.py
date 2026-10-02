"""Contrat du parcours débutant du hub gratuit — aucune API ni mutation."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import unittest
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
ROUTE = "/guides/demarrer-openclaw-hermes/"
GUIDE = SITE / ROUTE.strip("/") / "index.html"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.textes = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.textes.append(data)

    def liens(self):
        return [a["href"] for t, a in self.tags if t == "a" and "href" in a]


class GuideDemarrageTest(unittest.TestCase):
    def test_le_guide_est_decouvrable_depuis_le_hub_et_le_sitemap(self):
        for page in ("index.html", "openclaw/index.html", "hermes/index.html", "gratuit/index.html"):
            document = Document((SITE / page).read_text(encoding="utf-8"))
            self.assertIn(ROUTE, document.liens(), page)
        racine = ET.parse(SITE / "sitemap.xml").getroot()
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        self.assertIn("https://openclaw-france.fr" + ROUTE,
                      [e.text for e in racine.findall("s:url/s:loc", ns)])
        self.assertIn("https://openclaw-france.fr" + ROUTE,
                      (SITE / "llms.txt").read_text(encoding="utf-8"))

    def test_les_donnees_structurees_decrivent_le_guide_sans_fausse_preuve(self):
        html = GUIDE.read_text(encoding="utf-8")
        schemas = [json.loads(s) for s in re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S)]
        self.assertEqual({s["@type"] for s in schemas}, {"Article", "BreadcrumbList"})
        article = next(s for s in schemas if s["@type"] == "Article")
        self.assertEqual(article["mainEntityOfPage"], "https://openclaw-france.fr" + ROUTE)
        self.assertEqual(article["datePublished"], "2026-10-02")
        self.assertIn("Le Crabe", article["author"]["name"])
        self.assertNotIn("aggregateRating", article)
        self.assertNotIn("review", article)

    def test_le_guide_a_une_identite_seo_sur_son_propre_domaine(self):
        document = Document(GUIDE.read_text(encoding="utf-8"))
        canonical = [a.get("href") for t, a in document.tags
                     if t == "link" and a.get("rel") == "canonical"]
        self.assertEqual(canonical, ["https://openclaw-france.fr" + ROUTE])
        meta = {a.get("property") or a.get("name"): a.get("content")
                for t, a in document.tags if t == "meta"}
        self.assertEqual(meta.get("og:url"), canonical[0])
        self.assertEqual(meta.get("og:type"), "article")
        self.assertTrue(meta.get("description"))
        self.assertEqual(meta.get("twitter:image"), meta.get("og:image"))
        self.assertTrue(meta.get("og:image", "").startswith("https://openclaw-france.fr/"))
        self.assertTrue(meta.get("og:image:alt"))
        self.assertNotIn("noindex", meta.get("robots", ""))

    def test_le_guide_mene_aux_deux_kits_sans_compte(self):
        self.assertTrue(GUIDE.is_file(), "Le guide de choix/démarrage est absent")
        document = Document(GUIDE.read_text(encoding="utf-8"))
        for lien in ("/openclaw/", "/hermes/", "/dl/kit-openclaw.zip?v=2",
                     "/dl/kit-hermes.zip?v=2", "/gratuit/"):
            self.assertIn(lien, document.liens())
        self.assertEqual(sum(t == "h1" for t, _ in document.tags), 1)
        self.assertFalse(any(t in ("form", "iframe") for t, _ in document.tags))
        for tag, attrs in document.tags:
            if tag == "script":
                self.assertEqual(attrs.get("type"), "application/ld+json")
        texte = " ".join(document.textes).lower()
        self.assertIn("coûts du modèle", texte)
        self.assertIn("guide indépendant", texte)
        self.assertNotIn("openclawfrance.fr", texte)


if __name__ == "__main__":
    unittest.main()
