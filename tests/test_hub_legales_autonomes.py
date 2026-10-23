"""Les pages légales se lisent sans ressources de présentation tierces."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import urljoin, urlsplit

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
ORIGIN = "https://openclaw-france.fr"
PAGES = ("mentions-legales", "politique-de-confidentialite")


class Resources(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.urls = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "img", "iframe", "source", "video", "audio", "embed"):
            self.urls.extend(attrs[key] for key in ("src", "poster") if attrs.get(key))
        if tag == "link" and set(attrs.get("rel", "").split()) & {
            "stylesheet", "preload", "modulepreload", "prefetch", "preconnect", "dns-prefetch", "icon"
        }:
            self.urls.append(attrs.get("href", ""))


class HubLegalesAutonomesTest(unittest.TestCase):
    def test_ressources_html_sur_notre_origine_uniquement(self):
        for slug in PAGES:
            with self.subTest(page=slug):
                html = (SITE / slug / "index.html").read_text()
                for url in Resources(html).urls:
                    resolved = urlsplit(urljoin(ORIGIN + "/", url))
                    self.assertEqual((resolved.scheme, resolved.netloc), ("https", "openclaw-france.fr"), url)
                    self.assertTrue((SITE / resolved.path.lstrip("/")).is_file(), url)

    def test_styles_sans_import_reseau_et_police_systeme(self):
        for slug in PAGES:
            with self.subTest(page=slug):
                html = (SITE / slug / "index.html").read_text()
                css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
                self.assertTrue(css)
                self.assertNotRegex(css, r"(?i)@import|url\(\s*[\"\']?(?:https?:)?//")
                self.assertIn("font-family: system-ui, -apple-system, BlinkMacSystemFont", css)
                self.assertNotIn("cdn.tailwindcss.com", html)
                self.assertNotIn("fonts.googleapis.com", html)
                self.assertNotIn("cdnjs.cloudflare.com", html)


if __name__ == "__main__":
    unittest.main()
