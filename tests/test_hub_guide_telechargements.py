"""Le guide mène aux bons ZIP et aux contrôles avant/après téléchargement."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites/openclaw-france"
ROUTE = "guides/demarrer-openclaw-hermes/index.html"

class Links(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.links = []
        self.current = None
        self.ids = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a":
            self.current = {"attrs": attrs, "text": ""}
            self.links.append(self.current)
    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data
    def handle_endtag(self, tag):
        if tag == "a":
            self.current = None

class GuideTelechargementsTest(unittest.TestCase):
    def setUp(self):
        html = (SITE / ROUTE).read_text()
        section = re.search(r'<section id="choisir".*?</section>', html, re.S).group()
        self.cards = re.findall(r"<article\b.*?</article>", section, re.S)
        self.assertEqual(len(self.cards), 2)

    def test_zip_annonces_par_format_et_agent_sans_changer_les_url(self):
        for card, slug, name in zip(self.cards, ("openclaw", "hermes"), ("OpenClaw", "Hermes Agent")):
            with self.subTest(kit=slug):
                links = Links(card).links
                zipped = [l for l in links if l["attrs"].get("href") == f"/dl/kit-{slug}.zip?v=2"]
                self.assertEqual(len(zipped), 1)
                self.assertEqual(zipped[0]["text"], f"ZIP {name} gratuit")
                self.assertIn("download", zipped[0]["attrs"])
                for attr in ("aria-label", "onclick", "tabindex"):
                    self.assertNotIn(attr, zipped[0]["attrs"])

    def test_prerequis_avant_zip_et_integrite_apres_dans_chaque_carte(self):
        for card, slug, name in zip(self.cards, ("openclaw", "hermes"), ("OpenClaw", "Hermes Agent")):
            with self.subTest(kit=slug):
                links = Links(card).links
                hrefs = [l["attrs"].get("href") for l in links]
                before, archive, after = f"/{slug}/#prerequis", f"/dl/kit-{slug}.zip?v=2", f"/{slug}/#verifier-zip"
                self.assertIn(before, hrefs)
                self.assertIn(after, hrefs)
                self.assertLess(hrefs.index(before), hrefs.index(archive))
                self.assertLess(hrefs.index(archive), hrefs.index(after))
                self.assertEqual(links[hrefs.index(before)]["text"], f"prérequis {name}")
                self.assertEqual(links[hrefs.index(after)]["text"], f"vérifier le ZIP {name}")

    def test_cibles_prerequis_et_verification_existantes_et_uniques(self):
        for slug in ("openclaw", "hermes"):
            ids = Links((SITE / slug / "index.html").read_text()).ids
            for anchor in ("prerequis", "verifier-zip"):
                with self.subTest(kit=slug, anchor=anchor):
                    self.assertEqual(ids.count(anchor), 1)

if __name__ == "__main__":
    unittest.main()
