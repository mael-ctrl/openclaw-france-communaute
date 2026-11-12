"""Commandes OpenClaw de dépannage lisibles et copiables sur mobile."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
COMMANDES = [
    "openclaw gateway status",
    "openclaw logs --follow",
    "docker compose ps --all",
    "docker compose logs --tail 50 openclaw-gateway",
    "ssh -N -L 18789:127.0.0.1:18789 utilisateur@votre-serveur",
    "docker compose run --rm openclaw-cli dashboard --no-open",
]
REFERENCES = ["docker-compose.yml", "127.0.0.1", "utilisateur@votre-serveur",
              "http://127.0.0.1:18789", "OPENCLAW_GATEWAY_PORT", ".env"]

class Codes(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.codes = []
        self.current = None
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        if tag == "code":
            self.current = {"attrs": dict(attrs), "text": ""}
            self.codes.append(self.current)
    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data
    def handle_endtag(self, tag):
        if tag == "code":
            self.current = None

class HubCommandesDepannageTest(unittest.TestCase):
    def setUp(self):
        self.html = (SITE / "openclaw/index.html").read_text()
        self.section = re.search(r'<section id="depannage"[^>]*>.*?</section>',
                                 self.html, re.S).group()
        self.codes = Codes(self.section).codes

    def test_six_commandes_distinctes_reutilisent_le_style_mobile(self):
        blocks = [c for c in self.codes if "commande" in c["attrs"].get("class", "").split()]
        self.assertEqual([c["text"] for c in blocks], COMMANDES)
        self.assertIn("/static/style.css?v=20261111-commandes", self.html)
        self.assertRegex((SITE / "static/style.css").read_text(), r"code\.commande\s*\{")

    def test_texte_exact_et_references_non_executables_en_ligne(self):
        for text in COMMANDES + REFERENCES:
            with self.subTest(text=text):
                matches = [c for c in self.codes if c["text"] == text]
                self.assertEqual(len(matches), 1)
                if text in REFERENCES:
                    self.assertNotIn("commande", matches[0]["attrs"].get("class", "").split())
        self.assertNotRegex(self.section, "[\u00ad\u200b]")

    def test_contexte_securite_et_accordeons_sans_script_conserves(self):
        self.assertEqual(self.section.count('<details class="faq"'), 3)
        self.assertIn('href="#depannage"', self.html.split("</section>", 1)[0])
        for context in ["Installation classique", "Avec Docker", "sur le serveur",
                        "depuis ton ordinateur", "Ctrl+C", "Ne supprime pas",
                        "Ne publie pas", "Ne désactive pas", "Masque les clés API"]:
            self.assertIn(context, self.section)
        self.assertNotRegex(self.section, r"<(script|button|form|iframe)\b")

if __name__ == "__main__":
    unittest.main()
