"""CSS commune intégrée au HTML, pure Python et sans réseau."""
from functools import lru_cache
import re

import config
from vendor.rcssmin import _make_cssmin

_minifier = _make_cssmin(python_only=True)


@lru_cache(maxsize=4)
def _compacter(texte):
    compacte = _minifier(texte, keep_bang_comments=True)
    # Contrat volontairement conservateur pour la CSS maison sans ressource.
    # Ne jamais changer silencieusement la base des URL en déplaçant la feuille.
    if not compacte.strip() or re.search(r'</style|url\s*\(|@import|@charset', compacte, re.I):
        raise ValueError('CSS commune non intégrable : vide, fermeture HTML ou ressource externe')
    return compacte


def balise_css():
    """Relit la source : une modification invalide le cache même à mtime égal."""
    texte = (config.DOSSIER_ASSETS / 'style.css').read_text(encoding='utf-8')
    return '<style id="style-commun">' + _compacter(texte) + '</style>'
