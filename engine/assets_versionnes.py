"""URL immuables des seuls CSS/JS locaux chargés par les gabarits.

Les originaux restent copiés pour les anciennes pages. Aucun alias serveur :
une empreinte désigne les octets exacts, jamais la dernière version du fichier.
"""
import hashlib
import os


import config
import couvertures

NOMS = ("app.js", "pack-copie.js", "b2b-demo.css")
# Date technique fixe des fichiers immuables ; aucune date éditoriale changée.
MTIME = 946684800


def _asset(nom):
    if nom not in NOMS:
        raise ValueError(f"Asset hors liste autorisée : {nom!r}")
    source = couvertures.verifier_chemin(config.DOSSIER_ASSETS / nom)
    data = source.read_bytes()
    empreinte = hashlib.sha256(data).hexdigest()
    return f"/assets/versionnes/{source.stem}.{empreinte}{source.suffix}", data


def url(nom):
    return _asset(nom)[0]


def copier(sortie):
    for nom in NOMS:
        chemin, data = _asset(nom)
        cible = couvertures.verifier_chemin(sortie / chemin.lstrip("/"))
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_bytes(data)
        os.utime(cible, (MTIME, MTIME))
