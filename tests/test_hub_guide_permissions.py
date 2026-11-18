"""Le mode minimal Hermes n’est pas présenté comme une barrière de lecture seule."""
from html.parser import HTMLParser
from pathlib import Path
import json
import re
import unittest
import xml.etree.ElementTree as ET

SITE = Path(__file__).resolve().parents[1] / "sites/openclaw-france"
ROUTE = "guides/demarrer-openclaw-hermes/index.html"

class Text(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.parts = []
        self.feed(html)
    def handle_data(self, data):
        self.parts.append(data)

class GuidePermissionsTest(unittest.TestCase):
    def test_mode_minimal_distinct_de_lecture_seule(self):
        html = (SITE / ROUTE).read_text()
        section = re.search(r'<section id="verifier".*?</section>', html, re.S).group()
        note = re.search(r'<p id="outils-hermes">.*?</p>', section, re.S)
        self.assertIsNotNone(note, "La vérification des accès omet le mode minimal Hermes")
        self.assertEqual(html.count('id="outils-hermes"'), 1)
        text = "".join(Text(note.group()).parts)
        for expected in ("Blank Slate", "hermes setup", "opérations sur fichiers", "terminal", "ne garantit pas la lecture seule", "hermes tools", "environnement isolé sans secrets"):
            self.assertIn(expected, text)
        self.assertIn("ne remplace pas les permissions techniques", section)

    def test_reference_officielle_sur_le_mode_minimal(self):
        html = (SITE / ROUTE).read_text()
        note = re.search(r'<p id="outils-hermes">.*?</p>', html, re.S)
        self.assertIsNotNone(note)
        self.assertIn('href="#source-3"', note.group())
        source = re.search(r'<li id="source-3">.*?</li>', html, re.S).group()
        self.assertIn("https://hermes-agent.nousresearch.com/docs/getting-started/quickstart", source)
        self.assertIn("Aucun délai de réponse ni support individuel n’est garanti.", html)

    def test_dates_publication_revision_et_sources_distinctes(self):
        html = (SITE / ROUTE).read_text()
        schemas = [json.loads(s) for s in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)]
        article = next(s for s in schemas if s["@type"] == "Article")
        self.assertEqual(article["datePublished"], "2026-10-02")
        self.assertRegex(html, r'mis à jour le <time datetime="' + article["dateModified"])
        sources = re.search(r'<section id="sources".*?</section>', html, re.S).group()
        self.assertRegex(sources, r'Consultées le <time datetime="[0-9]{4}-[0-9]{2}-[0-9]{2}">')
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = ET.parse(SITE / "sitemap.xml").getroot()
        entry = next(u for u in urls if u.find("s:loc", ns).text == article["mainEntityOfPage"])
        self.assertEqual(entry.find("s:lastmod", ns).text, article["dateModified"])

if __name__ == "__main__":
    unittest.main()
