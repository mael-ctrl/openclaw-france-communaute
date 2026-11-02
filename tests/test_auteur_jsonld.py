"""L'auteur organisation renvoie à la présentation transparente du média IA."""
import copy
import json
from pathlib import Path
import re
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'engine'))
import config
import construction


def objets_jsonld(contenu):
    return [json.loads(x) for x in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', contenu, re.S)]


class AuteurJsonldTest(unittest.TestCase):
    def test_les_deux_gabarits_identifient_l_organisation_et_sa_page(self):
        breve = {'slug': 'source', 'titre': 'Une brève', 'resume': 'Résumé.',
                 'source': 'Source', 'lien_source': 'https://example.org/source',
                 'date_redac': '2026-10-30T12:00:00Z', 'tags': ['agents']}
        article = {'slug': 'analyse', 'titre': 'Analyse', 'chapo': 'Chapeau.',
                   'html': '<p>Texte.</p>', 'date': '2026-10-30T13:00:00Z',
                   'sources': [{'nom': 'Source', 'url': 'https://example.org/source'}]}
        avant = copy.deepcopy((breve, article))
        for page in (construction.page_breve(breve, [breve]),
                     construction.page_article(article, [article])):
            with self.subTest(page=page[:100]):
                donnees = next(x for x in objets_jsonld(page) if x.get('@type') == 'NewsArticle')
                self.assertEqual(donnees['author'], {
                    '@id': config.URL_SITE + '/#organisation',
                    '@type': 'Organization', 'name': config.NOM_SITE,
                    'url': config.URL_SITE + '/transparence/',
                })
                self.assertEqual(donnees['publisher'], {'@id': config.URL_SITE + '/#organisation'})
                self.assertIn('href="/transparence/"', page)
                self.assertNotIn('datePublished', donnees)
                self.assertNotIn('dateModified', donnees)
        self.assertEqual((breve, article), avant)


    def test_configuration_et_echappement_sans_persona_invente(self):
        nom = 'Média "test" </script> & 🦀'
        with patch.object(config, 'URL_SITE', 'https://example.org'), patch.object(config, 'NOM_SITE', nom):
            rendu = construction.jsonld_item('NewsArticle', 'https://example.org/article/',
                'Titre', 'Résumé', None, None, 'Articles', [])
        self.assertEqual(rendu.count('</script>'), 1)
        auteur = objets_jsonld(rendu)[0]['author']
        self.assertEqual(auteur, {'@id': 'https://example.org/#organisation',
            '@type': 'Organization', 'name': nom, 'url': 'https://example.org/transparence/'})

    def test_graphe_du_site_et_pages_non_editoriales_inchanges(self):
        graphe = objets_jsonld(construction.jsonld_site())[0]['@graph']
        organisation = next(x for x in graphe if x['@type'] == 'Organization')
        self.assertEqual(organisation['@id'], config.URL_SITE + '/#organisation')
        self.assertEqual(organisation['name'], config.NOM_SITE)
        self.assertEqual(organisation['url'], config.URL_SITE + '/')
        self.assertIn('100 %', organisation['description'])
        page = construction.page('Index', 'Description', '<p>Index.</p>', '/articles/')
        self.assertFalse(any('author' in x for x in objets_jsonld(page)))

    def test_autres_champs_et_dates_explicites_conserves(self):
        source = {'nom': 'Source & recherche', 'url': 'https://example.org/?a=1&b=2'}
        image = {'path': '/assets/couverture.jpg', 'width': 1200, 'height': 630, 'caption': 'Illustration.'}
        contenu = construction.jsonld_item('NewsArticle', 'https://example.org/article/',
            'Titre complet', 'Description complète', '2026-10-01T10:00:00Z',
            '2026-10-02T10:00:00Z', 'Articles', ['agents'], [source], image)
        donnees = objets_jsonld(contenu)[0]
        donnees.pop('author')
        self.assertEqual(donnees, {
            '@context': 'https://schema.org', '@type': 'NewsArticle',
            '@id': 'https://example.org/article/#article',
            'mainEntityOfPage': 'https://example.org/article/',
            'headline': 'Titre complet', 'description': 'Description complète',
            'inLanguage': 'fr-FR', 'isAccessibleForFree': True,
            'articleSection': 'Articles', 'keywords': 'agents',
            'publisher': {'@id': config.URL_SITE + '/#organisation'},
            'datePublished': '2026-10-01T10:00:00Z', 'dateModified': '2026-10-02T10:00:00Z',
            'citation': [{'@type': 'CreativeWork', 'url': source['url'], 'name': source['nom']}],
            'image': {'@type': 'ImageObject', 'url': config.URL_SITE + image['path'],
                      'width': 1200, 'height': 630, 'caption': 'Illustration.'},
        })


if __name__ == '__main__':
    unittest.main()
