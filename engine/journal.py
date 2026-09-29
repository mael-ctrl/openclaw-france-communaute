# -*- coding: utf-8 -*-
"""Petit carnet de bord — journal.jsonl + stats.json.

Tout ce que fait le robot est consigné : c'est la matière première de la
page /transparence. Aucun effacement : le journal s'allonge, c'est voulu.
"""
import json
import time
from datetime import datetime, timezone

import config

MAX_JOURNAL = 2000  # on garde large ; le site n'en affiche qu'une tranche


def _maintenant():
    return datetime.now(timezone.utc)


def _iso(dt):
    return dt.isoformat(timespec="seconds")


def charger_stats():
    if config.FICHIER_STATS.exists():
        try:
            return json.loads(config.FICHIER_STATS.read_text(encoding="utf-8"))
        except ValueError:
            pass
    return {
        "runs": 0, "items_collectes": 0, "breves_publiees": 0, "articles_publies": 0,
        "tokens_entree": 0, "tokens_sortie": 0,
        "premier_run": None, "dernier_run": None, "solde": None,
        "dernieres_erreurs": [],
    }


def sauver_stats(stats):
    config.DOSSIER_DATA.mkdir(parents=True, exist_ok=True)
    config.FICHIER_STATS.write_text(
        json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")


def ajouter(evenement, **details):
    """Ajoute une entrée au journal (une ligne JSON)."""
    config.DOSSIER_DATA.mkdir(parents=True, exist_ok=True)
    entree = {"ts": _iso(_maintenant()), "evenement": evenement, "details": details}
    with open(config.FICHIER_JOURNAL, "a", encoding="utf-8") as f:
        f.write(json.dumps(entree, ensure_ascii=False) + "\n")
    return entree


def lire_journal(dernieres=None):
    if not config.FICHIER_JOURNAL.exists():
        return []
    lignes = []
    with open(config.FICHIER_JOURNAL, encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                lignes.append(json.loads(ligne))
            except ValueError:
                continue
    if dernieres:
        return lignes[-dernieres:]
    return lignes


def erreur(message):
    """Consigne une erreur (visible sur /transparence, jamais silencieuse)."""
    ajouter("erreur", message=str(message)[:500])
    stats = charger_stats()
    ring = stats.get("dernieres_erreurs") or []
    ring.append({"ts": _iso(_maintenant()), "message": str(message)[:300]})
    stats["dernieres_erreurs"] = ring[-5:]
    sauver_stats(stats)


def crediter(tokens):
    """Cumule des tokens consommés."""
    stats = charger_stats()
    stats["tokens_entree"] = stats.get("tokens_entree", 0) + int(tokens.get("entree", 0))
    stats["tokens_sortie"] = stats.get("tokens_sortie", 0) + int(tokens.get("sortie", 0))
    sauver_stats(stats)


def horodatage_pour_humains(iso):
    """« 29 sept. 2026, 23 h 04 » — sans dépendance locale."""
    try:
        dt = datetime.fromisoformat(iso)
    except ValueError:
        return iso
    mois = ["janv.", "févr.", "mars", "avr.", "mai", "juin",
            "juil.", "août", "sept.", "oct.", "nov.", "déc."]
    return f"{dt.day} {mois[dt.month - 1]} {dt.year}, {dt.hour:02d} h {dt.minute:02d}"


def depense_du_mois(stats, quand=None):
    """Dépense estimée du mois courant (USD), d'après l'historique du solde.

    Première mesure du mois − dernière mesure : c'est le garde-fou qui protège
    le plafond mensuel (30 €). Si l'historique est vide, on renvoie 0.
    """
    hist = stats.get("historique_solde") or []
    if not hist or not hist[-1]:
        return 0.0
    quand = quand or _maintenant()
    prefixe = quand.strftime("%Y-%m")
    du_mois = [h for h in hist if str(h[0]).startswith(prefixe) and h[1] is not None]
    if not du_mois:
        return 0.0
    try:
        return max(0.0, round(float(du_mois[0][1]) - float(hist[-1][1]), 4))
    except (TypeError, ValueError):
        return 0.0
