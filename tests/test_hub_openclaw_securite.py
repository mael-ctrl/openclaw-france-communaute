"""Promesses de la page OpenClaw alignées sur les scripts réellement fournis."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"


class Document(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.tags, self.text = [], []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def handle_data(self, data):
        self.text.append(data)

    def texte(self):
        return " ".join(" ".join(self.text).split())


class OpenClawSecuriteTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "openclaw/index.html").read_text(encoding="utf-8")

    def section(self):
        match = re.search(r"<section id=\"securite-sauvegardes\"[^>]*>(.*?)</section>", self.html, re.S)
        self.assertIsNotNone(match, "Section sécurité et sauvegardes absente")
        return Document(match.group(1))

    def test_limites_accessibles_avant_telechargement_sans_garantie_absolue(self):
        hero = re.search(r"<section class=\"heros\">(.*?)</section>", self.html, re.S).group(1)
        avant = Document(hero.split("<div class=\"actions\">", 1)[0])
        self.assertIn("#securite-sauvegardes", [a.get("href") for t, a in avant.tags if t == "a"])
        tags = Document(self.html).tags
        sections = [a for t, a in tags if a.get("id") == "securite-sauvegardes"]
        self.assertEqual(len(sections), 1)
        self.assertEqual(sections[0]["aria-labelledby"], "titre-securite-sauvegardes")
        self.assertEqual(sum(a.get("id") == "titre-securite-sauvegardes" for t, a in tags), 1)
        for promesse in ("Sécurisé par défaut", "tous les ennuis", "HTTPS automatique", "sauvegarde automatique dès", "sauvegardes automatiques."):
            self.assertNotIn(promesse, self.html)

    def test_securite_distingue_installateur_configuration_et_verification(self):
        doc = self.section()
        for repere in ("install.sh", "installateur officiel", "pare-feu", "SSH", "HTTPS", "ne configure pas", "127.0.0.1", "authentification", "openclaw security audit", "pas une garantie"):
            self.assertIn(repere, doc.texte())
        links = [a.get("href") for t, a in doc.tags if t == "a"]
        for url in ("/dl/kit-openclaw/scripts/install.sh", "/dl/kit-openclaw/securite.md", "https://docs.openclaw.ai/gateway/security"):
            self.assertIn(url, links)
        for url in links:
            if url and url.startswith("/dl/"):
                self.assertTrue((SITE / url.lstrip("/")).is_file(), url)

    def test_sauvegarde_planification_secrets_et_restauration_distincts(self):
        doc = self.section()
        for repere in ("sauvegarde.sh", "ne programme pas", "cron", "~/Backups/openclaw", "sauvegardes/", "RETENTION_JOURS", "14", "--verify", "restauration", "secrets", "autre support", "ne chiffre pas", "ne copie pas"):
            self.assertIn(repere, doc.texte())
        links = [a.get("href") for t, a in doc.tags if t == "a"]
        self.assertIn("/dl/kit-openclaw/scripts/sauvegarde.sh", links)
        self.assertIn("https://docs.openclaw.ai/install/backups", links)
        script = (SITE / "dl/kit-openclaw/scripts/sauvegarde.sh").read_text()
        for repere in ("$HOME/Backups/openclaw", "$RACINE/sauvegardes", "${RETENTION_JOURS:-14}", "--verify"):
            self.assertIn(repere, script)


if __name__ == "__main__":
    unittest.main()
