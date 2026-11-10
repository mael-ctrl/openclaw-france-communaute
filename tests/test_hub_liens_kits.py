"""Les liens des cartes annoncent le guide ou le ZIP et le kit concerné."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"

class CardLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.in_card = False
        self.current = None
        self.links = []
        self.feed(html)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and "carte" in attrs.get("class", "").split():
            self.in_card = True
        if tag == "a" and self.in_card:
            self.current = {"attrs": attrs, "text": ""}
            self.links.append(self.current)
    def handle_data(self, data):
        if self.current is not None:
            self.current["text"] += data
    def handle_endtag(self, tag):
        if tag == "a":
            self.current = None
        if tag == "article":
            self.in_card = False

class HubKitLinkTest(unittest.TestCase):
    def setUp(self):
        self.links = CardLinks((SITE / "index.html").read_text()).links

    def test_chaque_guide_nomme_son_kit_dans_le_texte_visible(self):
        for slug, name in (("openclaw", "OpenClaw"), ("hermes", "Hermes Agent")):
            with self.subTest(kit=slug):
                matches = [l for l in self.links if l["attrs"].get("href") == f"/{slug}/"]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["text"].strip(), f"Guide {name}")

    def test_chaque_archive_annonce_zip_et_kit(self):
        for slug, name in (("openclaw", "OpenClaw"), ("hermes", "Hermes Agent")):
            with self.subTest(kit=slug):
                matches = [l for l in self.links if l["attrs"].get("href") == f"/dl/kit-{slug}.zip?v=2"]
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["text"].strip(), f"⬇ ZIP {name}")

    def test_libelles_distincts_et_liens_natifs(self):
        self.assertEqual(len(self.links), 4)
        self.assertEqual(len({l["text"].strip() for l in self.links}), 4)
        for link in self.links:
            self.assertNotIn("aria-label", link["attrs"])
            self.assertNotIn("onclick", link["attrs"])
            self.assertNotIn("tabindex", link["attrs"])

if __name__ == "__main__":
    unittest.main()
