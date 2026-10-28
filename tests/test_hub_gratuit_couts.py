"""La page de gratuité distingue les fichiers offerts des coûts d’usage."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
COUTS = "/guides/demarrer-openclaw-hermes/#couts"

class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags, self.text = [], []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, text):
        self.text.append(text)

    def texte(self):
        return " ".join(" ".join(self.text).split())

class GratuitCoutsTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "gratuit/index.html").read_text(encoding="utf-8")

    def test_limite_de_gratuite_visible_dans_introduction(self):
        hero = re.search(r"<section class=\"heros\"[^>]*>(.*?)</section>", self.html, re.S)
        self.assertIsNotNone(hero)
        doc = Document(hero.group(1))
        for repere in ("La gratuité concerne nos kits et guides.", "modèle IA", "hébergement", "peuvent être payants", "ne sont pas inclus"):
            self.assertIn(repere, doc.texte())
        self.assertEqual(sum(a.get("id") == "couts-usage" for _, a in Document(self.html).tags), 1)
        self.assertLess(self.html.index("id=\"couts-usage\""), self.html.index("📦 Kit OpenClaw gratuit"))

    def test_lien_budget_direct_et_ancre_existante(self):
        hero = re.search(r"<section class=\"heros\"[^>]*>(.*?)</section>", self.html, re.S).group(1)
        self.assertIn(COUTS, [a.get("href") for tag, a in Document(hero).tags if tag == "a"])
        guide = Document((SITE / "guides/demarrer-openclaw-hermes/index.html").read_text())
        self.assertEqual(sum(a.get("id") == "couts" for _, a in guide.tags), 1)

if __name__ == "__main__":
    unittest.main()
