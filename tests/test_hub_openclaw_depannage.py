"""Dépannage OpenClaw : distinguer natif/Docker et préserver les accès privés."""
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

    def handle_data(self, data):
        self.text.append(data)


class OpenClawDepannageTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "openclaw/index.html").read_text(encoding="utf-8")
        match = re.search(r'<section id="depannage"[^>]*>(.*?)</section>', self.html, re.S)
        self.assertIsNotNone(match, "Section de dépannage OpenClaw manquante")
        self.block = match.group(1)
        self.doc = Elements(self.block)

    def test_decouvrable_et_accessible_sans_javascript(self):
        self.assertIn('href="#depannage"', self.html.split("</section>", 1)[0])
        self.assertIn('aria-labelledby="titre-depannage"', self.html)
        self.assertIn(("h2", {"id": "titre-depannage"}), self.doc.tags)
        self.assertEqual(sum(t == "details" for t, _ in self.doc.tags), 3)
        self.assertEqual(sum(t == "summary" for t, _ in self.doc.tags), 3)
        self.assertFalse(any(t in ("script", "form", "iframe") for t, _ in self.doc.tags))

    def test_diagnostics_distinguent_natif_docker_et_serveur(self):
        for command in ("openclaw gateway status", "openclaw logs --follow",
                        "docker compose ps --all",
                        "docker compose logs --tail 50 openclaw-gateway",
                        "ssh -N -L 18789:127.0.0.1:18789 utilisateur@votre-serveur",
                        "docker compose run --rm openclaw-cli dashboard --no-open"):
            self.assertIn(command, self.block)
        text = " ".join(" ".join(self.doc.text).split())
        for notice in ("Installation classique", "Avec Docker", "dossier du kit",
                       "sur le serveur", "depuis ton ordinateur", "OPENCLAW_GATEWAY_PORT",
                       "127.0.0.1", "Ne publie pas", "Ne désactive pas",
                       "Masque les clés API", "jetons", "données personnelles",
                       "ne joins pas", ".env", "Ne supprime pas"):
            self.assertIn(notice, text)
        for dangerous in ("rm -rf", "chmod 777", "--fix", "devices approve", "down -v"):
            self.assertNotIn(dangerous, self.block)
        compose = (SITE / "dl/kit-openclaw/docker-compose.yml").read_text()
        self.assertIn("  openclaw-gateway:", compose)
        self.assertIn("  openclaw-cli:", compose)

    def test_sources_officielles_datees_et_aide_francaise(self):
        links = [a.get("href") for t, a in self.doc.tags if t == "a"]
        for link in ("https://docs.openclaw.ai/help/troubleshooting",
                     "https://docs.openclaw.ai/gateway/remote",
                     "https://docs.openclaw.ai/install/docker/sandbox-and-troubleshooting",
                     "https://docs.docker.com/reference/cli/docker/compose/ps/",
                     "https://docs.docker.com/reference/cli/docker/compose/logs/",
                     "/dl/kit-openclaw/GUIDE.md", "mailto:support@openclaw-france.fr"):
            self.assertIn(link, links)
        self.assertIn("07/10/2026", self.block)
        self.assertIn("aide indépendante", self.block)


if __name__ == "__main__":
    unittest.main()
