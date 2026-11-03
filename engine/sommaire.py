"""Sommaire natif des seuls articles : transformation locale du rendu."""
from html import escape
from html.parser import HTMLParser
from urllib.parse import quote
from collections import Counter
import re
import unicodedata


class _Ids(HTMLParser):
    def __init__(self, document):
        super().__init__(convert_charrefs=True)
        self.ids = Counter()
        self.feed(document)

    def handle_starttag(self, tag, attrs):
        self.ids.update(v for k, v in attrs if k == 'id' or (tag == 'a' and k == 'name'))


class _Titres(HTMLParser):
    """Lecteur d'un sous-ensemble fermé, pas un parseur/validateur HTML5.

    Au moindre balisage hors contrat, ne pas enrichir le fragment.
    L'original n'est jamais sérialisé ni corrigé par HTMLParser.
    """
    INLINE = {'a', 'abbr', 'b', 'br', 'code', 'em', 'i', 'mark', 's',
              'small', 'span', 'strong', 'sub', 'sup'}
    BLOCS = {'h2', 'h3', 'p', 'ul', 'ol', 'blockquote'}
    OUVERTURE = re.compile(r'''<[a-zA-Z][a-zA-Z0-9]*(?:\s+[a-zA-Z][a-zA-Z0-9-]*\s*=\s*(?:"[^"<>]*"|'[^'<>]*'))*\s*/?>''')

    def __init__(self, corps):
        super().__init__(convert_charrefs=True)
        self.corps = corps
        self.titres = []
        self.courant = None
        self.pile = []
        self.invalide = bool(re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]', corps))
        # HTMLParser compte seulement LF, pas CR/U+2028 comme splitlines().
        self.lignes = [0] + [m.end() for m in re.finditer('\n', corps)]

    def position(self):
        ligne, col = self.getpos()
        return self.lignes[ligne - 1] + col

    def handle_starttag(self, tag, attrs):
        parent = self.pile[-1] if self.pile else None
        permis = (self.BLOCS if parent is None else
                  {'li'} if parent in {'ul', 'ol'} else
                  self.BLOCS - {'h2', 'h3'} if parent == 'blockquote' else
                  self.INLINE | {'p', 'ul', 'ol'} if parent == 'li' else self.INLINE)
        noms = [k for k, v in attrs]
        attributs = {'id', 'class', 'title', 'lang', 'dir'} | ({'href', 'rel'} if tag == 'a' else set())
        brut = self.get_starttag_text()
        if (tag not in permis or not self.OUVERTURE.fullmatch(brut)
                or len(noms) != len(set(noms)) or not set(noms) <= attributs
                or (tag == 'a' and 'a' in self.pile)):
            self.invalide = True
        if tag == 'h2':
            self.courant = [dict(attrs).get('id'), [], self.position() + len(brut) - 1]
        if tag == 'br':
            if self.courant is not None:
                self.courant[1].append(' ')
        else:
            self.pile.append(tag)

    def handle_startendtag(self, tag, attrs):
        if tag != 'br':
            self.invalide = True
        else:
            self.handle_starttag(tag, attrs)

    def handle_data(self, data):
        if ((not self.pile or self.pile[-1] in {'ul', 'ol', 'blockquote'}) and data.strip()
                or self.corps[self.position():].startswith('<')):
            self.invalide = True
        if self.courant is not None:
            self.courant[1].append(data)

    def handle_endtag(self, tag):
        if (not self.pile or self.pile[-1] != tag
                or not re.match(r'</' + re.escape(tag) + r'\s*>', self.corps[self.position():], re.I | re.ASCII)):
            self.invalide = True
            return
        self.pile.pop()
        if tag == 'h2' and self.courant is not None:
            ident, texte, position = self.courant
            titre = ' '.join(''.join(texte).split())
            if any(not c.isspace() and not unicodedata.category(c).startswith('C') for c in titre):
                self.titres.append((ident, titre, position))
            self.courant = None

    def handle_comment(self, data):
        self.invalide = True

    def handle_decl(self, decl):
        self.invalide = True

    def handle_pi(self, data):
        self.invalide = True

    def unknown_decl(self, data):
        self.invalide = True


def enrichir_article(document, corps):
    if not isinstance(corps, str) or not corps:
        return document
    origine = '<div class="corps-article">\n' + corps
    if document.count(origine) != 1 or '<details class="sommaire-article">' in document:
        return document
    parseur = _Titres(corps)
    try:
        parseur.feed(corps)
        parseur.close()
    except (ValueError, AssertionError):
        return document
    if parseur.invalide or parseur.pile or len(parseur.titres) < 3:
        return document
    frequences = _Ids(document).ids
    valides = [(i, t, p) for i, t, p in parseur.titres
               if i is None or (i and frequences[i] == 1
                   and not any(c.isspace() or unicodedata.category(c).startswith('C') for c in i))]
    if len(valides) < 3:
        return document
    reserves = set(frequences)
    titres = []
    ajouts = []
    for ident, titre, position in valides:
        if ident is None:
            ascii_titre = unicodedata.normalize('NFKD', titre).encode('ascii', 'ignore').decode().lower()
            radical = 'section-' + (re.sub(r'[^a-z0-9]+', '-', ascii_titre).strip('-')[:64].rstrip('-') or 'section')
            ident, suffixe = radical, 2
            while ident in reserves:
                ident = f'{radical}-{suffixe}'
                suffixe += 1
            reserves.add(ident)
            ajouts.append((position, f' id="{ident}"'))
        titres.append((ident, titre))
    transforme = corps
    for position, ajout in reversed(ajouts):
        transforme = transforme[:position] + ajout + transforme[position:]
    liens = ''.join(f'<li><a href="#{escape(quote(i, safe=""), quote=True)}">{escape(t)}</a></li>'
                    for i, t in titres)
    bloc = ('<details class="sommaire-article">'
            f'<summary>Dans cet article — {len(titres)} sections</summary>'
            '<nav aria-label="Sommaire de cet article"><ol>' + liens + '</ol></nav></details>\n')
    return document.replace(origine, bloc + '<div class="corps-article">\n' + transforme, 1)
