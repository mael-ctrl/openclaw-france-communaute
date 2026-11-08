"""Le retour à la ligne de navigation couvre aussi les tablettes."""
from pathlib import Path
import re
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"

class HubNavigationTabletteTest(unittest.TestCase):
    def test_entete_adaptable_jusqua_1000px(self):
        css = (SITE / "static/style.css").read_text()
        self.assertIn("@media (max-width:1000px){", css)
        tablette = css.split("@media (max-width:1000px){", 1)[1].split("@media", 1)[0]
        self.assertRegex(tablette, r"\.entete\s*\{[^}]*position:static")
        self.assertRegex(tablette, r"\.entete \.wrap\s*\{[^}]*height:auto")
        self.assertRegex(tablette, r"\.entete \.wrap\s*\{[^}]*flex-wrap:wrap")
        self.assertRegex(tablette, r"\.nav\s*\{[^}]*flex-basis:100%")
        self.assertRegex(tablette, r"\.nav\s*\{[^}]*flex-wrap:wrap")
        self.assertRegex(tablette, r"\.nav a\s*\{[^}]*min-height:44px")

    def test_mise_en_page_du_contenu_reste_au_seuil_mobile(self):
        css = (SITE / "static/style.css").read_text()
        self.assertIn("@media (max-width:1000px){", css)
        tablette = css.split("@media (max-width:1000px){", 1)[1].split("@media", 1)[0]
        self.assertNotIn(".pied{", tablette)
        self.assertNotIn(".heros{", tablette)
        mobile = css.split("@media (max-width:760px){", 1)[1]
        self.assertIn(".pied{grid-template-columns:1fr 1fr}", mobile)
        self.assertIn(".heros{padding-top:48px}", mobile)

if __name__ == "__main__":
    unittest.main()
