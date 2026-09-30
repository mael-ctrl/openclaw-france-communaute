# -*- coding: utf-8 -*-
"""Preuves horodatées — dossier de record (Guinness World Records, §3.2).

Deux artefacts produits à chaque passage du pipeline :

1. ``data/publications.jsonl`` — le registre des publications : une ligne par
   brève et par article, avec l'empreinte SHA-256 du contenu publié (titre +
   corps). Régénéré de façon déterministe depuis ``data/breves.json`` et
   ``data/articles/`` ; réécrit uniquement s'il change (pas de diff inutile).

2. ``data/preuves/manifeste-AAAA-MM-JJ.json`` — le sceau quotidien : les
   empreintes SHA-256 des fichiers d'état (journal, stats, registre) au moment
   du sceau, plus la référence au manifeste de la veille. Chaque manifeste
   scelle le précédent : c'est une chaîne d'archives continue, ancrée dans
   l'historique Git public.

Chaînage du journal : depuis le 2026-10-01, chaque nouvelle ligne du journal
porte un champ ``sha256`` (auto-empreinte — voir ``journal.ajouter``). Les
lignes antérieures restent couvertes par le sceau global des manifestes.

Ce module n'échoue jamais en silence : toute erreur remonte à l'appelant
(``run.py`` la journalise et continue).
"""
import hashlib
import json
import time
from datetime import datetime, timezone

import config
import journal

DOSSIER_PREUVES = config.DOSSIER_DATA / "preuves"
FICHIER_PUBLICATIONS = config.DOSSIER_DATA / "publications.jsonl"


# --- Empreintes -------------------------------------------------------------

def _sha256_fichier(chemin):
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(65536), b""):
            h.update(bloc)
    return h.hexdigest()


def _sha256_texte(texte):
    return hashlib.sha256(texte.encode("utf-8")).hexdigest()


def canonique(objet):
    """Sérialisation stable : clés triées, séparateurs compacts."""
    return json.dumps(objet, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _jours_exploitation(stats):
    premiere = stats.get("premier_run") or ""
    try:
        t0 = datetime.fromisoformat(premiere)
    except ValueError:
        return None
    if t0.tzinfo is None:
        t0 = t0.replace(tzinfo=timezone.utc)
    return (datetime.now(timezone.utc).date() - t0.date()).days + 1


# --- 1. Registre des publications -------------------------------------------

def _ligne_breve(b):
    corps = {"titre": b.get("titre", ""), "resume": b.get("resume", "")}
    return {
        "id": b.get("id") or b.get("slug", ""),
        "type": "breve",
        "date": (b.get("date_redac") or b.get("date_source") or ""),
        "titre": b.get("titre", ""),
        "url": f"{config.URL_SITE}/breves/{b['slug']}/",
        "sources": [s for s in [b.get("lien_source")] if s],
        "sha256": _sha256_texte(canonique(corps)),
    }


def _ligne_article(a):
    corps = {"titre": a.get("titre", ""), "chapo": a.get("chapo", ""), "html": a.get("html", "")}
    return {
        "id": a.get("pivot") or a.get("slug", ""),
        "type": "article",
        "date": a.get("date", ""),
        "titre": a.get("titre", ""),
        "url": f"{config.URL_SITE}/articles/{a['slug']}/",
        "sources": [s.get("url") for s in (a.get("sources") or []) if isinstance(s, dict) and s.get("url")],
        "sha256": _sha256_texte(canonique(corps)),
    }


def construire_registre():
    """Regénère ``data/publications.jsonl`` (déterministe, trié date puis id)."""
    lignes = []

    if config.FICHIER_BREVES.exists():
        try:
            breves = json.loads(config.FICHIER_BREVES.read_text(encoding="utf-8")) or []
        except ValueError:
            breves = []
        for b in breves:
            if isinstance(b, dict) and b.get("slug"):
                lignes.append(_ligne_breve(b))

    if config.DOSSIER_ARTICLES.exists():
        for p in sorted(config.DOSSIER_ARTICLES.glob("*.json")):
            try:
                a = json.loads(p.read_text(encoding="utf-8"))
            except ValueError:
                continue
            if isinstance(a, dict) and a.get("slug"):
                lignes.append(_ligne_article(a))

    lignes.sort(key=lambda x: (x["date"], x["id"]))
    contenu = "".join(
        json.dumps(l, ensure_ascii=False, separators=(",", ":")) + "\n" for l in lignes)

    ancien = FICHIER_PUBLICATIONS.read_text(encoding="utf-8") if FICHIER_PUBLICATIONS.exists() else ""
    change = contenu != ancien
    if change:
        config.DOSSIER_DATA.mkdir(parents=True, exist_ok=True)
        FICHIER_PUBLICATIONS.write_text(contenu, encoding="utf-8")

    compteurs = {
        "breves": sum(1 for l in lignes if l["type"] == "breve"),
        "articles": sum(1 for l in lignes if l["type"] == "article"),
        "total": len(lignes),
    }
    return {"compteurs": compteurs, "change": change, "total": len(lignes)}


# --- 2. Sceau quotidien -----------------------------------------------------

def _manifeste_precedent():
    candidats = sorted(DOSSIER_PREUVES.glob("manifeste-*.json")) if DOSSIER_PREUVES.exists() else []
    if not candidats:
        return None
    dernier = candidats[-1]
    return {"fichier": dernier.name, "sha256": _sha256_fichier(dernier)}


def sceller_jour(compteurs):
    """Écrit le manifeste du jour (une seule fois par jour). Renvoie un résumé ou None."""
    DOSSIER_PREUVES.mkdir(parents=True, exist_ok=True)
    jour = time.strftime("%Y-%m-%d", time.gmtime())
    cible = DOSSIER_PREUVES / f"manifeste-{jour}.json"
    if cible.exists():
        return None

    stats = journal.charger_stats()
    manifeste = {
        "jour": jour,
        "genere_le": time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()),
        "site": config.URL_SITE,
        "depot": config.DEPOT_GITHUB,
        "depuis": stats.get("premier_run"),
        "jours_exploitation": _jours_exploitation(stats),
        "runs": stats.get("runs"),
        "publications": compteurs,
        "sha256": {},
        "manifeste_precedent": _manifeste_precedent(),
        "note_chainage": (
            "Les manifestes quotidiens forment une chaîne : chaque manifeste scelle le précédent. "
            "Depuis le 2026-10-01, chaque nouvelle ligne du journal porte un champ sha256 "
            "(auto-empreinte) ; l'entrée annonçant un sceau est elle-même couverte par le sceau "
            "suivant. Les lignes du journal antérieures au 2026-10-01 sont couvertes par les "
            "empreintes globales des manifestes."
        ),
    }
    for nom, chemin in (("journal.jsonl", config.FICHIER_JOURNAL),
                        ("stats.json", config.FICHIER_STATS),
                        ("publications.jsonl", FICHIER_PUBLICATIONS)):
        if chemin.exists():
            manifeste["sha256"][nom] = _sha256_fichier(chemin)

    cible.write_text(json.dumps(manifeste, ensure_ascii=False, indent=1), encoding="utf-8")
    journal.ajouter("preuves", manifeste=cible.name, publications=compteurs["total"])
    return (f"sceau {cible.name} — {compteurs['total']} publications "
            f"(brèves {compteurs['breves']}, articles {compteurs['articles']})")


# --- Point d'entrée du pipeline ---------------------------------------------

def apres_run():
    """Registre + sceau du jour. Renvoie une phrase de bilan (jamais vide)."""
    info = construire_registre()
    sceau = sceller_jour(info["compteurs"])
    if sceau:
        return sceau
    etat = "mis à jour" if info["change"] else "inchangé"
    return f"registre {info['total']} publications ({etat})"


def main():
    print(f"🧾 {apres_run()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
