"""Navigation mobile native, sans masquer les accès aux kits."""
from pathlib import Path
import re
import unittest

SITE=Path(__file__).resolve().parents[1]/"sites"/"openclaw-france"
ROUTES=("index.html","openclaw/index.html","hermes/index.html","gratuit/index.html",
        "temoignages/index.html","cgv/index.html","guides/demarrer-openclaw-hermes/index.html")

class HubNavigationMobileTest(unittest.TestCase):
    def setUp(self):
        self.css=(SITE/"static/style.css").read_text()
        self.mobile=self.css.split("@media (max-width:760px){",1)[1]

    def test_navigation_mobile_visible_et_retour_a_la_ligne(self):
        self.assertNotRegex(self.mobile,r"\.nav\s*\{[^}]*display\s*:\s*none")
        nav=re.search(r"\.nav\s*\{([^}]*)\}",self.mobile).group(1)
        self.assertIn("display:flex",nav)
        self.assertIn("flex-wrap:wrap",nav)
        self.assertIn("margin-left:0",nav)

    def test_entete_mobile_ne_masque_pas_les_ancres_et_cibles_tactiles(self):
        self.assertRegex(self.mobile,r"\.entete\s*\{[^}]*position:static")
        self.assertRegex(self.mobile,r"\.entete \.wrap\s*\{[^}]*height:auto")
        self.assertRegex(self.mobile,r"\.nav a\s*\{[^}]*min-height:44px")

    def test_style_versionne_et_liens_des_deux_kits_conserves(self):
        for route in ROUTES:
            with self.subTest(route=route):
                html=(SITE/route).read_text()
                self.assertTrue("href=\"/static/style.css?v=20261107-nav\"" in html, "Stylesheet cache version missing")
                nav=re.search(r"<nav class=\"nav\"[^>]*>(.*?)</nav>",html,re.S).group(1)
                self.assertIn("href=\"/openclaw/\"",nav)
                self.assertIn("href=\"/hermes/\"",nav)

if __name__=="__main__": unittest.main()
