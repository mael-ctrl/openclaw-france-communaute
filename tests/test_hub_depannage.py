"""Aide Hermes publique : liens, diagnostic prudent et absence de scripts."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
SOURCE = "https://hermes-agent.nousresearch.com/docs/getting-started/installation#troubleshooting"


class Elements(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.tags = []
        self.text = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)


class HubDepannageTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "hermes/index.html").read_text(encoding="utf-8")
        match = re.search(r"<section id=\"depannage\"[^>]*>(.*?)</section>", self.html, re.S)
        self.assertIsNotNone(match, "Section de dépannage manquante")
        self.block = match.group(1)
        self.doc = Elements(self.block)

    def test_aide_accessible_depuis_le_hero_et_sans_javascript(self):
        hero = self.html.split("</section>", 1)[0]
        self.assertIn("href=\"#depannage\"", hero)
        self.assertIn("aria-labelledby=\"titre-depannage\"", self.html)
        self.assertIn(("h2", {"id": "titre-depannage"}), self.doc.tags)
        self.assertEqual(sum(tag == "details" for tag, _ in self.doc.tags), 3)
        self.assertEqual(sum(tag == "summary" for tag, _ in self.doc.tags), 3)
        self.assertFalse(any(tag in ("script", "form", "iframe") for tag, _ in self.doc.tags))

    def test_diagnostics_precis_et_secrets_proteges(self):
        for command in ("hermes: command not found", "source ~/.zshrc", "source ~/.bashrc",
                        "hermes model", "hermes doctor"):
            self.assertIn(command, self.block)
        text = " ".join(self.doc.text)
        for notice in ("nouveau terminal", "macOS ou Linux", "Masque", "clés API", "jetons", "données personnelles",
                       "Ne supprime pas", "~/.hermes", "terminal personnel"):
            self.assertIn(notice, text)
        self.assertNotIn("rm -rf", self.block)
        self.assertNotIn("sudo", self.block)

    def test_source_officielle_et_contact_reel(self):
        links = [attrs.get("href") for tag, attrs in self.doc.tags if tag == "a"]
        self.assertIn(SOURCE, links)
        self.assertIn("mailto:support@openclaw-france.fr", links)
        self.assertIn("06/10/2026", self.block)
        self.assertIn("aide indépendante", self.block)


if __name__ == "__main__":
    unittest.main()
