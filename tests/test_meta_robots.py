"""Prérequis Discover : max-image-preview:large partout, 404 en noindex."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import construction


class MetaRobotsTest(unittest.TestCase):
    def test_max_image_preview_sur_les_pages(self):
        html = construction.page("T", "D", "<p>x</p>", "/")
        self.assertIn('<meta name="robots" content="index,follow,max-image-preview:large">', html)

    def test_la_404_ne_demande_pas_l_indexation(self):
        html = annexes.page_404()
        self.assertIn('<meta name="robots" content="noindex,follow">', html)
        self.assertNotIn("max-image-preview", html)


if __name__ == "__main__":
    unittest.main()
