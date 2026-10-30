"""Signalement éditorial natif : aucun envoi ni donnée de navigation."""
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class Liens(HTMLParser):
    def __init__(self, document):
        super().__init__(convert_charrefs=True)
        self.liens = []
        self.canoniques = []
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self.liens.append(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canoniques.append(attrs["href"])


def documents(titre):
    commun = {"titre": titre, "tags": ["IA"], "slug": "essai-ia"}
    breve = dict(commun, resume="Résumé sourcé.", source="Source",
                 lien_source="https://example.org/?lecteur=NON#prive",
                 date_redac="2026-10-30T06:00:00+00:00")
    article = dict(commun, chapo="Analyse sourcée.", html="<p>Texte.</p>",
                   date="2026-10-30T06:00:00+00:00", sources=[])
    return [construction.page_breve(breve, []), construction.page_article(article, [])]


class SignalerErreurTest(unittest.TestCase):
    def test_aucune_query_ni_fragment_ni_donnee_lecteur_dans_le_brouillon(self):
        canonique = 'https://communaute-ia.fr/articles/caf%C3%A9-%26-%22-test/'
        bloc = construction.bloc_signaler_erreur(
            'Épreuve & "citation" <b> + % ?', canonique + '?email=lecteur%40example.org&utm_source=NON#prive')
        liens = Liens(bloc).liens
        self.assertEqual(len(liens), 1)
        mail = urlsplit(liens[0]['href'])
        champs = parse_qs(mail.query)
        self.assertEqual(set(champs), {'subject', 'body'})
        self.assertEqual(champs['body'], ['Page concernée : ' + canonique + '\r\n\r\nErreur relevée :\r\n'])
        self.assertEqual(champs['subject'], ['Signaler une erreur — Épreuve & "citation" <b> + % ?'])
        self.assertNotIn('example.org', bloc)
        for interdit in ('<script', '<form', '<input', 'onclick', 'target=', '<b>', 'sous 24', 'réponse garantie'):
            self.assertNotIn(interdit, bloc)

    def test_bloc_autonome_et_cta_existants_inchanges(self):
        suivi = construction.bloc_suivre()
        attentes = [config.URL_SITE + '/feed.xml', config.URL_SITE + '/feed-articles.xml',
                    'https://bsky.app/profile/' + config.BLUESKY_HANDLE, '/podcast/', '/#la-breve']
        self.assertEqual([a['href'] for a in Liens(suivi).liens], attentes)
        self.assertNotIn('signaler-erreur', suivi)
        for document in documents('Titre simple'):
            self.assertEqual(document.count(suivi), 1)
            blocs = re.findall(r'<aside class="a-cote" aria-labelledby="signaler-erreur">.*?</aside>', document, re.S)
            self.assertEqual(len(blocs), 1)
            self.assertIn(suivi, document.replace(blocs[0], ''))
            self.assertNotIn('collecte', blocs[0])
            self.assertIn('Vous choisissez les précisions à ajouter et l’envoi.', blocs[0])

    def test_caracteres_speciaux_ne_creent_pas_de_champs_mail(self):
        for titre in ('A & B', '"Guillemets" <script>alert(1)</script>', 'cafés 🦀 + 100%',
                      'Sujet?body=faux&bcc=tiers@example.org#fragment', "L’apostrophe et l'autre"):
            with self.subTest(titre=titre):
                bloc = construction.bloc_signaler_erreur(titre, 'https://communaute-ia.fr/breves/test/')
                lien = Liens(bloc).liens[0]
                self.assertEqual(set(lien), {'href'})
                champs = parse_qs(urlsplit(lien['href']).query)
                self.assertEqual(set(champs), {'subject', 'body'})
                self.assertEqual(champs['subject'], ['Signaler une erreur — ' + titre])
                self.assertNotIn('<script>', bloc)

    def test_deux_gabarits_mailto_decode_et_echappe(self):
        titre = 'IA & <modèle> "cité" : 50% + café / #? = 🦀'
        for document in documents(titre):
            with self.subTest(gabarit=Liens(document).canoniques):
                liens = Liens(document)
                mails = [a for a in liens.liens if a.get("href", "").startswith("mailto:")]
                self.assertEqual(len(mails), 1, "Un seul signalement natif par page éditoriale")
                mail = urlsplit(mails[0]["href"])
                self.assertEqual(mail.path, "crabe@blockos.fr")
                self.assertEqual(mail.fragment, "")
                self.assertEqual(parse_qs(mail.query), {
                    "subject": ["Signaler une erreur — " + titre],
                    "body": ["Page concernée : " + liens.canoniques[0] + "\r\n\r\nErreur relevée :\r\n"],
                })
                raw_href = re.search(r'href="(mailto:[^"]+)"', document).group(1)
                self.assertIn("&amp;body=", raw_href)
                self.assertNotIn("<modèle>", raw_href)
                self.assertNotIn("lecteur=", mails[0]["href"])
                self.assertEqual(set(mails[0]), {"href"})
                self.assertIn('>Signaler une erreur par email</a>', document)
                self.assertIn("Ce média est rédigé par IA.", document)
                self.assertEqual(document.count('id="signaler-erreur"'), 1)
                self.assertLess(document.index('</article>'), document.index('id="signaler-erreur"'))
                self.assertLess(document.index('id="signaler-erreur"'), document.index('aria-labelledby="suivre-le-crabe"'))


if __name__ == "__main__":
    unittest.main()
