"""Prérequis Hermes : parcours accessible et compatibilité sans promesse."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
DOCS = "https://hermes-agent.nousresearch.com/docs/getting-started/"


class Elements(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.text = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, text):
        self.text.append(text)


class HubPrerequisTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "hermes/index.html").read_text(encoding="utf-8")
        match = re.search(r'<section id="prerequis"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(match, "Prérequis absents de la page Hermes")
        self.block = match.group(1)
        self.doc = Elements(self.block)
        self.text = " ".join(" ".join(self.doc.text).split())

    def test_acces_avant_telechargement_et_section_nommee(self):
        hero = self.html.split('<section class="heros">', 1)[1].split("</section>", 1)[0]
        self.assertLess(hero.index('href="#prerequis"'), hero.index('class="actions"'))
        self.assertIn('aria-labelledby="titre-prerequis"', self.html)
        self.assertIn(("h2", {"id": "titre-prerequis"}), self.doc.tags)
        ids = [attrs["id"] for _, attrs in Elements(self.html).tags if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertFalse(any(tag in ("script", "form", "iframe") for tag, _ in self.doc.tags))

    def test_prerequis_et_limites_explicites(self):
        for word in ("Apple Silicon", "Linux", "WSL2", "x86_64", "arm64", "Git", "curl", "tar", "SHA-256", "PowerShell", "Bash"):
            self.assertIn(word, self.text)
        for phrase in ("Mac Intel", "divergent", "compatibilité non garantie", "kit", "plus anciennes", "bibliothèques système", "pas une installation testée"):
            self.assertIn(phrase, self.text)
        self.assertNotIn("curl -fsSL", self.block)

    def test_sources_datees_et_guide_consultable(self):
        links = [attrs.get("href") for tag, attrs in self.doc.tags if tag == "a"]
        for url in (DOCS + "installation#prerequisites", DOCS + "platform-support", DOCS + "installation#windows-native", "/dl/kit-hermes/GUIDE.md"):
            self.assertIn(url, links)
        self.assertIn('datetime="2026-10-12"', self.block)
        self.assertIn("indépendante", self.text)


if __name__ == "__main__":
    unittest.main()
