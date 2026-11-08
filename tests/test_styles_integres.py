"""CSS commune compacte dans le HTML, sans réécriture éditoriale."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'engine'))
import construction


class StylesIntegresTest(unittest.TestCase):
    def test_page_integre_css_commune_compacte_sans_requete_style(self):
        contenu = '<pre>  lignes\n   conservées &amp; texte</pre>'
        page = construction.page('Test', 'Description', contenu, '/test/')
        blocs = re.findall(r'<style id="style-commun">(.*?)</style>', page, re.S)
        self.assertEqual(len(blocs), 1, 'La CSS commune doit être intégrée une fois')
        self.assertLess(len(blocs[0].encode()), (ROOT / 'assets/style.css').stat().st_size)
        self.assertIn(':root{', blocs[0])
        self.assertNotIn('href="/assets/style.css"', page)
        self.assertIn(contenu, page)
        self.assertLess(page.index('<style id="style-commun">'), page.index('</head>'))

    def test_podcast_partage_css_sans_ajouter_de_script(self):
        import podcast
        page = podcast.page_ecoute([], 'https://communaute-ia.fr')
        self.assertEqual(page.count('<style id="style-commun">'), 1)
        self.assertNotIn('href="/assets/style.css"', page)
        self.assertNotIn('<script', page)
        self.assertIn('audio {display:block', page)

    def test_refuse_css_non_transportable_au_lieu_de_casser_le_html(self):
        import styles
        from unittest.mock import patch
        from tempfile import TemporaryDirectory
        for texte in ('', '/* commentaire seul */', 'a::after{content:"</STYLE><p>"}',
                      'a{background:url(image.png)}', '@import "autre.css";',
                      '@charset "utf-8"; a{color:red}'):
            with self.subTest(texte=texte), TemporaryDirectory() as tmp:
                dossier = Path(tmp)
                (dossier / 'style.css').write_text(texte)
                with patch.object(styles.config, 'DOSSIER_ASSETS', dossier):
                    with self.assertRaises(ValueError):
                        styles.balise_css()


    def test_cache_par_contenu_pas_par_chemin_ou_date(self):
        import styles
        from unittest.mock import patch
        from tempfile import TemporaryDirectory
        import os
        with TemporaryDirectory() as tmp:
            dossier = Path(tmp)
            fichier = dossier / 'style.css'
            fichier.write_text('a { color: red; }')
            with patch.object(styles.config, 'DOSSIER_ASSETS', dossier):
                premier = styles.balise_css()
                self.assertEqual(premier, styles.balise_css())
                temps = fichier.stat().st_mtime_ns
                fichier.write_text('a { color: tan; }')
                os.utime(fichier, ns=(temps, temps))
                self.assertNotEqual(premier, styles.balise_css())
                self.assertIn('color:tan', styles.balise_css())

    def test_css_absente_echoue_sans_repli_silencieux(self):
        import styles
        from unittest.mock import patch
        from tempfile import TemporaryDirectory
        with TemporaryDirectory() as tmp, patch.object(styles.config, 'DOSSIER_ASSETS', Path(tmp)):
            with self.assertRaises(FileNotFoundError):
                styles.balise_css()

    def test_calc_chaines_unicode_impression_et_licence_conserves(self):
        import styles
        texte = '''/*! licence */ :root { --largeur: 10px; }
        a::after { content: "été  /* non commentaire */ & <"; }
        @media print { a { width: calc(100% - var(--largeur)); } }
        a:is(:hover, :focus-visible) { color: red; }'''
        compacte = styles._compacter(texte)
        self.assertIn('/*! licence */', compacte)
        self.assertIn('"été  /* non commentaire */ & <"', compacte)
        self.assertIn('calc(100% - var(--largeur))', compacte)
        self.assertIn('@media print{', compacte)
        self.assertIn('a:is(:hover,:focus-visible)', compacte)
        self.assertEqual(compacte, styles._compacter(compacte))


if __name__ == '__main__':
    unittest.main()
