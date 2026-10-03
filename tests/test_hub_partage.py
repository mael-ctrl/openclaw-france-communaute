"""Contrat des aperçus sociaux du hub gratuit — stdlib seule."""
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
import struct
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
PAGES = {"index.html": "/", "openclaw/index.html": "/openclaw/",
         "hermes/index.html": "/hermes/", "gratuit/index.html": "/gratuit/"}
IMAGE = "https://openclaw-france.fr/static/og-image.png"


class Metadata(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.meta = defaultdict(list)
        self.canonical = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            self.meta[attrs.get("property") or attrs.get("name")].append(attrs.get("content"))
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))


class HubPartageTest(unittest.TestCase):
    def test_chaque_page_a_une_identite_et_une_carte_completes(self):
        for path, route in PAGES.items():
            with self.subTest(page=route):
                doc = Metadata((SITE / path).read_text())
                meta = doc.meta
                url = "https://openclaw-france.fr" + route
                self.assertEqual(doc.canonical, [url])
                self.assertEqual(meta["og:url"], [url])
                self.assertEqual(meta["og:image"], [IMAGE])
                self.assertEqual(meta["og:image:type"], ["image/png"])
                self.assertEqual(meta["og:image:width"], ["1200"])
                self.assertEqual(meta["og:image:height"], ["630"])
                self.assertEqual(meta["og:site_name"], ["OpenClaw France"])
                self.assertEqual(meta["og:locale"], ["fr_FR"])
                self.assertEqual(meta["twitter:card"], ["summary_large_image"])
                for key in ("title", "description", "image", "image:alt"):
                    self.assertEqual(len(meta["og:" + key]), 1, key)
                    self.assertTrue(meta["og:" + key][0], key)
                    self.assertEqual(meta["twitter:" + key], meta["og:" + key], key)
                for key, values in meta.items():
                    self.assertEqual(len(values), 1, key)

    def test_image_png_presente_aux_dimensions_declarees(self):
        data = (SITE / "static/og-image.png").read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(struct.unpack(">II", data[16:24]), (1200, 630))
        self.assertLess(len(data), 2_000_000)


if __name__ == "__main__":
    unittest.main()
