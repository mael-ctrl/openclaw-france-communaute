"""Préparer hors réseau l'ajout XML au .htaccess distant sauvegardé.

Le constructeur ne gère pas la racine Apache : les redirections de domaine
restent préservées. Ce module n'effectue aucun transfert et ne charge aucun secret.
"""

import hashlib

DEBUT = b"# BEGIN CRABE COMPRESSION XML v1\n"
FIN = b"# END CRABE COMPRESSION XML v1\n"
BLOC = (DEBUT
        + b'<FilesMatch "\\.(xml|opml)$">\n'
        + b"<IfModule mod_deflate.c>\n"
        + b"  <IfModule mod_filter.c>\n"
        + b"    AddOutputFilterByType DEFLATE application/xml text/xml application/rss+xml application/atom+xml text/x-opml\n"
        + b"  </IfModule>\n"
        + b"</IfModule>\n"
        + b"</FilesMatch>\n"
        + FIN)


def preparer(original: bytes, sha256_attendu: str) -> bytes:
    """Retourner une configuration candidate, sans écrire la base."""
    if hashlib.sha256(original).hexdigest() != sha256_attendu:
        raise ValueError("La base ne correspond pas à son SHA256 attendu")
    marqueur = b"CRABE COMPRESSION XML"
    if marqueur in original:
        if original.count(marqueur) == 2 and original.count(BLOC) == 1:
            return original
        raise ValueError("Bloc XML existant différent, incomplet ou dupliqué")
    return original + b"\n" + BLOC


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base", type=Path)
    parser.add_argument("sortie", type=Path)
    parser.add_argument("--sha256", required=True)
    args = parser.parse_args()
    candidate = preparer(args.base.read_bytes(), args.sha256)
    with args.sortie.open("xb") as fichier:
        fichier.write(candidate)
    print(hashlib.sha256(candidate).hexdigest())

