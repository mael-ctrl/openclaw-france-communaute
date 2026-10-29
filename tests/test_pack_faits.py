"""La copie commerciale reste factuelle ; pas une qualification juridique."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import annexes


class PackFaitsTest(unittest.TestCase):
    def test_la_page_ne_nie_pas_la_mesure_audience_existante(self):
        page = annexes.page_pack()
        corps = page.split('<section class="section section-lecture">', 1)[1].rsplit('</section>', 1)[0]
        self.assertNotIn('sans traqueur', corps)
        self.assertIn('Une mesure d’audience GoatCounter est présente sur le site', corps)
        self.assertIn('<a href="/transparence/">Transparence</a>', corps)
        for promesse in ('conforme au RGPD', 'exempté de consentement', 'aucune donnée personnelle'):
            self.assertNotIn(promesse, corps)

    def test_origine_ia_sans_faux_temoignage_usage(self):
        page = annexes.page_pack()
        self.assertNotIn('qui les utilise vraiment', page)
        self.assertIn('rédigés par une IA, à adapter à ton besoin et à vérifier', page)
        self.assertIn('100 prompts professionnels en français', page)


if __name__ == '__main__':
    unittest.main()
