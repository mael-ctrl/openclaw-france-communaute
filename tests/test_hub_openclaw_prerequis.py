"""Prérequis OpenClaw : distinguer le kit Bash, Windows et Docker."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"


class Elements(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags = []
        self.text = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, text):
        self.text.append(text)


class OpenClawPrerequisTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "openclaw/index.html").read_text(encoding="utf-8")
        match = re.search(r'<section id="prerequis"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(match, "Prérequis absents de la page OpenClaw")
        self.block = match.group(1)
        self.doc = Elements(self.block)
        self.text = " ".join(" ".join(self.doc.text).split())

    def test_acces_avant_telechargement_et_section_accessible(self):
        hero = self.html.split('<section class="heros">', 1)[1].split("</section>", 1)[0]
        self.assertLess(hero.index('href="#prerequis"'), hero.index('class="actions"'))
        self.assertIn('aria-labelledby="titre-prerequis"', self.html)
        self.assertIn(("h2", {"id": "titre-prerequis"}), self.doc.tags)
        ids = [attrs["id"] for _, attrs in Elements(self.html).tags if "id" in attrs]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(sum(tag == "details" for tag, _ in self.doc.tags), 3)
        self.assertFalse(any(tag in ("script", "form", "iframe") for tag, _ in self.doc.tags))

    def test_bash_windows_node_docker_et_limites(self):
        for word in ("macOS", "Linux", "Bash", "curl", "PowerShell", "WSL2", "Node.js",
                     "24.16", "26.1", "node -v", "Docker Compose v2", "docker compose version",
                     "6 Go", "construction", "préconstruite", "mémoire", "disque", "SSH"):
            self.assertIn(word, self.text)
        for phrase in ("pas dans PowerShell", "pas une garantie", "pas une installation testée",
                       "prérequis du guide", "modèle IA", "hébergement"):
            self.assertIn(phrase, self.text)
        self.assertNotIn("curl -fsSL", self.block)
        compose = (SITE / "dl/kit-openclaw/docker-compose.yml").read_text()
        self.assertIn("ghcr.io/openclaw/openclaw:latest", compose)
        script = (SITE / "dl/kit-openclaw/scripts/install.sh").read_text()
        self.assertIn("Linux|Darwin", script)

    def test_sources_datees_guide_et_faq_coherente(self):
        links = [attrs.get("href") for tag, attrs in self.doc.tags if tag == "a"]
        for url in ("https://docs.openclaw.ai/install", "https://docs.openclaw.ai/install/docker",
                    "https://docs.openclaw.ai/platforms/windows", "/dl/kit-openclaw/GUIDE.md",
                    "/guides/demarrer-openclaw-hermes/#couts"):
            self.assertIn(url, links)
        self.assertIn('datetime="2026-10-15"', self.block)
        self.assertIn("indépendante", self.text)
        faq = self.html.split("Il me faut quoi pour commencer ?</summary>", 1)[1].split("</details>", 1)[0]
        self.assertIn('href="#prerequis"', faq)
        self.assertNotIn("n’importe lequel", faq)
        self.assertNotIn("n'importe lequel", faq)


if __name__ == "__main__":
    unittest.main()
