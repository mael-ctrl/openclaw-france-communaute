# -*- coding: utf-8 -*-
"""Signal d'indexation IndexNow (Bing, Yandex, Seznam…) — sans compte.

On dépose un fichier de clé à la racine du site, puis on notifie chaque
déploiement avec la liste des URL récentes. Coût : zéro. Effet : les
moteurs qui soutiennent IndexNow viennent voir les nouveautés tout de suite.
"""
import json
import urllib.error
import urllib.request

import config
import reseau

POINT_ENTREE = "https://api.indexnow.org/indexnow"


def ecrire_cle():
    """Dépose <clé>.txt à la racine du site généré (doit être déployé)."""
    config.DOSSIER_SORTIE.mkdir(parents=True, exist_ok=True)
    fichier = config.DOSSIER_SORTIE / f"{config.INDEXNOW_CLE}.txt"
    fichier.write_text(config.INDEXNOW_CLE, encoding="utf-8")
    return fichier


def _urls_recentes(limite=60):
    base = config.URL_SITE
    urls = [f"{base}/", f"{base}/actus/", f"{base}/articles/",
            f"{base}/manifeste/", f"{base}/transparence/", f"{base}/skills/"]
    if config.FICHIER_BREVES.exists():
        try:
            breves = json.loads(config.FICHIER_BREVES.read_text(encoding="utf-8"))
            for b in breves[-35:]:
                urls.append(f"{base}/breves/{b['slug']}/")
        except ValueError:
            pass
    if config.DOSSIER_ARTICLES.exists():
        for f in sorted(config.DOSSIER_ARTICLES.glob("*.json"))[-10:]:
            urls.append(f"{base}/articles/{f.stem}/")
    return urls[:limite]


def signaler():
    """Notifie IndexNow. Renvoie le code HTTP (200/202 = accepté)."""
    hote = config.URL_SITE.split("//", 1)[1].split("/", 1)[0]
    corps = {"host": hote, "key": config.INDEXNOW_CLE, "urlList": _urls_recentes()}
    donnees = json.dumps(corps).encode("utf-8")
    req = urllib.request.Request(
        POINT_ENTREE, data=donnees,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=30, context=reseau.contexte()) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
