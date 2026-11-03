"""Contrats de navigation native ; aucune génération éditoriale ni transport."""
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import construction


def article(corps):
    return {'slug': 'essai', 'titre': 'Article de test', 'chapo': 'Introduction.',
            'html': corps, 'date': '2026-11-02T07:00:00+00:00', 'sources': [], 'tags': []}


def rendre(corps):
    return construction.page_article(article(corps), [])


def bloc(document):
    m = re.search(r'<details class="sommaire-article">.*?</details>\n', document, re.S)
    return m.group() if m else ''


class Elements(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def cibles(document):
    return [unquote(a['href'][1:]) for t, a in Elements(bloc(document)).tags if t == 'a']


class SommaireArticlesTest(unittest.TestCase):
    def test_ancres_lisibles_accents_doublons_et_ids_reserves(self):
        corps = ('<h2>Été &amp; café</h2><h2>Été &amp; café</h2><h2>🦀</h2>'
                 '<h2 id="section-ete-cafe">Ancienne ancre</h2>'
                 '<p id="section-ete-cafe-2">Réservation après les titres</p>'
                 '<h2>contenu</h2><h2 id="a&amp;b&quot;%#é">Spécial &lt; &amp; &quot;</h2>')
        doc = rendre(corps)
        self.assertEqual(cibles(doc), ['section-ete-cafe-3', 'section-ete-cafe-4',
                         'section-section', 'section-ete-cafe', 'section-contenu', 'a&b"%#é'])
        self.assertIn('<h2 id="a&amp;b&quot;%#é">', doc)
        self.assertIn('Spécial &lt; &amp; &quot;', bloc(doc))
        self.assertIn('href="#a%26b%22%25%23%C3%A9"', bloc(doc))
        ids = [a['id'] for t, a in Elements(doc).tags if 'id' in a]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(doc, rendre(corps))

    def test_html_hors_sous_ensemble_ou_malforme_reste_intact(self):
        from sommaire import enrichir_article
        bons = '<h2>A</h2><h2>B</h2><h2>C</h2>'
        invalides = ['<h2/>faux', '<h2>X', '<p><h2>X</h2></p>', '<h2><p>X</p></h2>',
                     '<h2><em>X</h2></em>', '<h2 id="x" id="y">X</h2>',
                     '<h2 id="x" rubbish>Y</h2>', '<h2 id="x"/ >Y</h2>',
                     '<script>"<h2>Faux</h2>"</script>', '<textarea/><h2>Faux</h2>',
                     '<title><h2>Faux</h2></title>', '<template><h2>Faux</h2></template>',
                     '<svg><h2>Faux</h2></svg>', '<details><h2>Caché</h2></details>',
                     '<h2 hidden>Caché</h2>', '<h2 style="display:none">Caché</h2>',
                     '<h2 aria-hidden="true">Caché</h2>', '<!doctype html>', '<?xml x?>',
                     '<h2>A</h2 x>', '<p><a href="/a"><a href="/b">B</a></a></p>',
                     '<p>Non fermé', '\x00', '<h2 id=noncite>Limite documentée</h2>', '<!-- ouvert',
                     '<h2\u00a0id="fantome">Faux titre navigateur</h2>', '<h2>X</h2\u00a0>']
        for invalide in invalides:
            with self.subTest(invalide=invalide):
                corps = bons + invalide
                origine = '<div class="corps-article">\n' + corps + '</div>'
                self.assertEqual(enrichir_article(origine, corps), origine)

    def test_ids_existants_ambigus_exclus_sans_reparation(self):
        corps = ('<h2 id="contenu">Collision gabarit</h2><h2 id="double">D1</h2>'
                 '<p id="double">D2</p><h2 id="">Vide</h2><h2 id="a b">Espace</h2>'
                 '<h2 id="a&#10;b">Saut</h2><h2>A</h2><h2>B</h2><h2>C</h2>')
        doc = rendre(corps)
        self.assertEqual(cibles(doc), ['section-a', 'section-b', 'section-c'])
        self.assertIn('<h2 id="contenu">Collision gabarit</h2>', doc)
        self.assertEqual(doc.count('id="double"'), 2)  # dette préexistante, non réparée

    def test_seuil_apres_exclusion_titres_vides_ou_invalides(self):
        for corps in ('', ' \n', '<p>Texte</p>', '<h2>A</h2><h2>B</h2>',
                      '<h2>A</h2><h2>B</h2><h3>C</h3>',
                      '<h2>A</h2><h2>B</h2><h2>&nbsp;<em> </em></h2>',
                      '<h2>A</h2><h2>B</h2><h2>\u200b</h2>',
                      '<h2>A</h2><h2>B</h2><h2 id="contenu">Collision</h2>'):
            with self.subTest(corps=corps):
                self.assertFalse(bloc(rendre(corps)))
                self.assertIn(corps, rendre(corps))
                self.assertNotIn('id="section-', rendre(corps))

    def test_fragment_absent_ou_repete_et_double_enrichissement(self):
        from sommaire import enrichir_article
        corps = '<h2>A</h2><h2>B</h2><h2>C</h2>'
        for doc in ('autre', ('<div class="corps-article">\n' + corps) * 2):
            self.assertEqual(enrichir_article(doc, corps), doc)
        doc = rendre(corps)
        self.assertEqual(enrichir_article(doc, corps), doc)
        for vide in (None, '', 0):
            self.assertEqual(enrichir_article('document', vide), 'document')

    def test_octets_preserves_inline_majuscules_et_separateurs_unicode(self):
        corps = ('<p>Amont\u2028préservé\rencore</p>\n<H2 TITLE="titre" >Été <em>cité</em>'
                 '<br/> &lt; &amp; &gt;</H2>\r\n<h2>Deux</h2>\n<h2>Trois</h2>')
        doc = rendre(corps)
        self.assertEqual(cibles(doc), ['section-ete-cite', 'section-deux', 'section-trois'])
        nouveau = doc.split('<div class="corps-article">\n', 1)[1].split('\n      </div>', 1)[0]
        self.assertEqual(re.sub(r' id="section-[a-z0-9-]+"', '', nouveau), corps)
        self.assertIn('Été cité &lt; &amp; &gt;', bloc(doc))

    def test_reservation_des_ancres_nommees_hors_corps(self):
        from sommaire import enrichir_article
        corps = '<h2>A</h2><h2>B</h2><h2>C</h2>'
        doc = '<a name="section-a"></a><div class="corps-article">\n' + corps + '</div>'
        self.assertEqual(cibles(enrichir_article(doc, corps)), ['section-a-2', 'section-b', 'section-c'])

    def test_styles_locaux_focus_et_retour_a_la_ligne(self):
        css = (Path(__file__).resolve().parents[1] / 'assets/style.css').read_text()
        for attendu in ('.sommaire-article {', '.sommaire-article summary:focus-visible',
                        '.sommaire-article a:focus-visible', '.sommaire-article a {'):
            self.assertIn(attendu, css)
        regle = re.search(r'\.sommaire-article a \{([^}]+)\}', css).group(1)
        self.assertIn('overflow-wrap: anywhere', regle)
        self.assertIn('min-height: 44px', regle)

    def test_trois_h2_existants_sommaire_natif_ferme(self):
        corps = '<h2 id="un">Un</h2><p>Texte.</p><h2 id="deux">Deux</h2><h2 id="trois">Trois</h2>'
        document = rendre(corps)
        self.assertTrue(bloc(document), 'Sommaire absent pour trois sections réelles')
        self.assertEqual(cibles(document), ['un', 'deux', 'trois'])
        self.assertIn('<summary>Dans cet article — 3 sections</summary>', bloc(document))
        self.assertIn('<nav aria-label="Sommaire de cet article">', bloc(document))
        self.assertNotIn('open', dict(Elements(bloc(document)).tags[0][1]))
        self.assertIn(corps, document)
        self.assertNotRegex(bloc(document), r'<script|onclick|javascript:')


if __name__ == '__main__':
    unittest.main()
