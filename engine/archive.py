# -*- coding: utf-8 -*-
"""Archivage quotidien (Wayback Machine) — preuve horodatée et indépendante.

Une fois par jour, la page d'accueil est confiée à web.archive.org : on obtient
un témoin externe daté de l'état du site, utile pour le dossier de record.
Silencieux et sans échec bloquant : tout problème est journalisé, jamais fatal.
"""
import urllib.error
import urllib.request

import config
import journal
import reseau


def _aujourd_hui():
    import time
    return time.strftime("%Y-%m-%d", time.gmtime())


def archiver_si_necessaire():
    """Sauvegarde https://communaute.openclaw-france.fr/ sur Wayback (max 3 tentatives/jour)."""
    stats = journal.charger_stats()
    if stats.get("derniere_archive") == _aujourd_hui():
        return ""
    tent = stats.get("archive_tentatives") or {}
    if tent.get("jour") != _aujourd_hui():
        tent = {"jour": _aujourd_hui(), "n": 0}
    if tent.get("n", 0) >= 3:
        return ""
    tent["n"] = tent.get("n", 0) + 1
    stats["archive_tentatives"] = tent
    journal.sauver_stats(stats)
    url = f"https://web.archive.org/save/{config.URL_SITE}/"
    code = None
    try:
        req = urllib.request.Request(url, headers={"User-Agent": config.HTTP_UA})
        with urllib.request.urlopen(req, timeout=50, context=reseau.contexte()) as r:
            code = r.status
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        journal.erreur(f"archivage wayback : {e}")
        return "échec (voir journal)"
    if code and 200 <= code < 400:
        stats["derniere_archive"] = _aujourd_hui()
        journal.sauver_stats(stats)
        journal.ajouter("archivage", wayback=code)
        return f"wayback HTTP {code}"
    journal.ajouter("archivage", wayback=code, tentative=tent["n"])
    return f"wayback HTTP {code} (tentative {tent['n']}/3)"
