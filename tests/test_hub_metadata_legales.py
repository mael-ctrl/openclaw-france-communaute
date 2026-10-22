"""SEO des pages légales : identité canonique et aperçus sans ancienne offre."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
ORIGIN = "https://openclaw-france.fr"
PAGES = ("mentions-legales", "politique-de-confidentialite")


class HeadMetadata(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.in_head = False
        self.canonicals = []
        self.meta = {}
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "head":
            self.in_head = True
        if not self.in_head:
            return
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonicals.append(attrs.get("href"))
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            self.meta.setdefault(key, []).append(attrs.get("content"))

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False


class HubMetadataLegalesTest(unittest.TestCase):
    def test_toutes_les_pages_du_sitemap_ont_une_canonical_unique(self):
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        for node in ET.parse(SITE / "sitemap.xml").findall("s:url/s:loc", ns):
            url = node.text
            with self.subTest(url=url):
                page = SITE / url.removeprefix(ORIGIN).strip("/") / "index.html"
                self.assertEqual(HeadMetadata(page.read_text()).canonicals, [url])

    def test_descriptions_legales_sans_promesse_commerciale_perimee(self):
        for slug in PAGES:
            with self.subTest(page=slug):
                meta = HeadMetadata((SITE / slug / "index.html").read_text()).meta
                descriptions = [meta[key] for key in ("description", "og:description", "twitter:description")]
                self.assertEqual(len(descriptions[0]), 1)
                self.assertTrue(descriptions[0][0])
                self.assertEqual(descriptions, [descriptions[0]] * 3)
                self.assertIn("OpenClaw France", descriptions[0][0])
                for stale in ("24h", "Pack Tout-Inclus", "Installation PRO"):
                    self.assertNotIn(stale, descriptions[0][0])

    def test_identite_et_images_de_partage_absolues(self):
        for slug in PAGES:
            with self.subTest(page=slug):
                meta = HeadMetadata((SITE / slug / "index.html").read_text()).meta
                self.assertEqual(meta.get("og:url"), [ORIGIN + "/" + slug + "/"])
                self.assertEqual(meta.get("og:image"), [ORIGIN + "/static/og-image.png"])
                self.assertEqual(meta.get("twitter:image"), meta["og:image"])
                self.assertEqual(meta.get("twitter:card"), ["summary_large_image"])
                self.assertTrue((SITE / "static/og-image.png").is_file())


if __name__ == "__main__":
    unittest.main()
