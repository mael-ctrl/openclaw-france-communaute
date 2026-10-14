"""Sitemap Google News : fraîcheur 48 h, protocole news, déclaré dans robots.txt."""
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction

NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9",
      "news": "http://www.google.com/schemas/sitemap-news/0.9"}


def iso(heures=0):
    return (datetime.now(timezone.utc) - timedelta(hours=heures)).isoformat()


class NewsSitemapTest(unittest.TestCase):
    def test_fraicheur_48h_et_protocole_news(self):
        articles = [
            {"slug": "frais", "titre": "Article frais & vif", "date": iso(1)},
            {"slug": "vieux", "titre": "Article ancien", "date": iso(24 * 10)},
        ]
        breves = [
            {"slug": "breve-fraiche", "titre": "Brève fraîche", "date_source": iso(2)},
            {"slug": "breve-vieille", "titre": "Brève ancienne", "date_redac": iso(24 * 5)},
        ]
        racine = ET.fromstring(construction.news_sitemap_xml(articles, breves))
        urls = racine.findall("s:url", NS)
        titres = [u.find("news:news/news:title", NS).text for u in urls]
        self.assertEqual(titres, ["Article frais & vif", "Brève fraîche"])
        lieux = [u.findtext("s:loc", namespaces=NS) for u in urls]
        self.assertIn(config.URL_SITE + "/articles/frais/", lieux)
        self.assertIn(config.URL_SITE + "/breves/breve-fraiche/", lieux)
        langue = racine.find("s:url/news:news/news:publication/news:language", NS)
        self.assertEqual(langue.text, "fr")
        dates = [u.findtext("news:news/news:publication_date", namespaces=NS) for u in urls]
        self.assertEqual(dates, sorted(dates, reverse=True))

    def test_build_l_ecrit_et_le_declare_dans_robots(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            articles = racine / "articles"
            articles.mkdir()
            (articles / "1.json").write_text(json.dumps({
                "slug": "dernier", "titre": "Dernier", "chapo": "c", "html": "<p>x</p>",
                "date": iso(1), "sources": [], "tags": []}), encoding="utf-8")
            breves = racine / "breves.json"
            breves.write_text(json.dumps([{
                "slug": "b1", "titre": "B1", "resume": "r", "source": "S",
                "lien_source": "https://example.org/", "date_redac": iso(0.5)}]), encoding="utf-8")
            sortie = racine / "site"
            with patch.object(config, "DOSSIER_ARTICLES", articles), \
                    patch.object(config, "FICHIER_BREVES", breves), \
                    patch.object(config, "DOSSIER_SORTIE", sortie):
                construction.construire()
            fichier = sortie / "news-sitemap.xml"
            self.assertTrue(fichier.is_file(), "Le build doit produire news-sitemap.xml")
            racine_xml = ET.parse(fichier).getroot()
            self.assertTrue(racine_xml.tag.endswith("urlset"))
            robots = (sortie / "robots.txt").read_text(encoding="utf-8")
            self.assertIn(f"Sitemap: {config.URL_SITE}/news-sitemap.xml", robots)

    def test_sans_contenu_recent_le_fichier_reste_valide(self):
        racine = ET.fromstring(construction.news_sitemap_xml([], []))
        self.assertEqual(racine.findall("s:url", NS), [])


if __name__ == "__main__":
    unittest.main()
