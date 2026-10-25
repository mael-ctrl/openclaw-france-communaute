"""Contrats CSS du correctif navigation ; géométrie éprouvée séparément en Chromium.

Ces tests stdlib protègent la stratégie de reflow, pas une conformité WCAG globale.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def bloc(css, debut):
    """Lire un bloc CSS connu avec accolades imbriquées, sans parseur tiers."""
    start = css.index(debut) + len(debut)
    opening = css.index("{", start)
    depth = 1
    for end in range(opening + 1, len(css)):
        depth += (css[end] == "{") - (css[end] == "}")
        if depth == 0:
            return css[opening + 1:end]
    raise AssertionError("Bloc CSS non terminé")


def declarations(css, selector):
    body = bloc(css, selector)
    return dict((key.strip(), value.strip()) for key, value in
                (part.split(":", 1) for part in body.split(";") if ":" in part))


class NavigationMobileTest(unittest.TestCase):
    def test_navigation_reflow_sans_rognage_ni_reordonnancement(self):
        css = (ROOT / "assets/style.css").read_text(encoding="utf-8")
        mobile = bloc(css, "@media (max-width: 900px) ")
        nav = declarations(mobile, ".nav ")
        self.assertEqual(nav.get("flex"), "0 0 100%", "La nav doit occuper sa propre ligne sans rétrécissement")
        self.assertEqual(nav.get("min-width"), "0")
        self.assertNotIn("order", nav, "Conserver l'ordre visuel du DOM et de Tab")
        self.assertFalse(any(key.startswith("overflow") for key in nav), "Ne pas rogner/faire défiler la nav")
        self.assertEqual(declarations(css, ".nav ").get("flex-wrap"), "wrap")
        self.assertEqual(declarations(css, ".nav a ").get("overflow-wrap"), "anywhere")
        self.assertEqual(declarations(css, ".marque-txt ").get("min-width"), "0")
        self.assertEqual(declarations(css, ".marque-txt ").get("overflow-wrap"), "anywhere")
        self.assertEqual(declarations(css, ".marque ").get("max-width"), "100%")
        self.assertEqual(declarations(css, ".entete-actions ").get("flex-wrap"), "wrap")
        header = declarations(css, ".entete-interne ")
        self.assertNotIn("height", header, "La hauteur doit suivre le contenu")
        self.assertEqual(header.get("min-height"), "66px")
        small = bloc(css, "@media (max-width: 900px), (max-height: 600px)")
        self.assertEqual(declarations(small, ".entete ").get("position"), "static")
        desktop = bloc(css, "@media (min-width: 901px) and (min-height: 601px)")
        self.assertEqual(declarations(desktop, "html ").get("scroll-padding-top"), "8rem")
        self.assertEqual(declarations(css, ".entete ").get("position"), "sticky")


if __name__ == "__main__":
    unittest.main()
