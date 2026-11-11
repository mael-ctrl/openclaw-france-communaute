"""Les commandes SHA-256 restent lisibles et copiables sur petit écran."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"

class CodeBlocks(HTMLParser):
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

def commands(kit):
    return [f"shasum -a 256 kit-{kit}.zip", f"sha256sum kit-{kit}.zip",
            f"Get-FileHash -Algorithm SHA256 kit-{kit}.zip"]

class HubIntegrityCommandTest(unittest.TestCase):
    def test_trois_commandes_identifiees_par_page(self):
        for kit in ("openclaw", "hermes"):
            html = (SITE / kit / "index.html").read_text()
            blocks = [c for c in CodeBlocks(html).codes
                      if "commande" in c["attrs"].get("class", "").split()]
            self.assertEqual([c["text"] for c in blocks], commands(kit))
            self.assertIn("/static/style.css?v=20261111-commandes", html)

    def test_commandes_exactes_sans_caractere_ajoute(self):
        for kit in ("openclaw", "hermes"):
            codes = CodeBlocks((SITE / kit / "index.html").read_text()).codes
            for command in commands(kit):
                self.assertEqual(sum(c["text"] == command for c in codes), 1)

    def test_css_retour_ligne_sans_troncature_ni_cesure(self):
        css = (SITE / "static/style.css").read_text()
        match = re.search(r"code\.commande\s*\{([^}]+)\}", css)
        self.assertIsNotNone(match)
        rules = dict(re.findall(r"([a-z-]+)\s*:\s*([^;]+)", match.group(1)))
        for key, value in {"display": "block", "max-width": "100%",
                           "white-space": "pre-wrap", "overflow-wrap": "anywhere",
                           "word-break": "normal", "hyphens": "none"}.items():
            self.assertEqual(rules.get(key), value)
        self.assertNotIn("overflow", rules)
        self.assertNotIn("text-overflow", rules)
        self.assertNotIn("user-select", rules)

if __name__ == "__main__":
    unittest.main()
