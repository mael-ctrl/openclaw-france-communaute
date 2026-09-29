# -*- coding: utf-8 -*-
"""Diffusion sociale — Bluesky (AT Protocol), 100 % stdlib.

Le Crabe publie ici les brèves et articles récents. Identifiants :
- soit BLUESKY_IDENTIFIER + BLUESKY_MOT_DE_PASSE (variables d'environnement,
  utilisées par GitHub Actions),
- soit le Trousseau macOS (services « bluesky-communaute-app », en local).
Le mot de passe d'application n'apparaît jamais dans les logs.
"""
import json
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone

import config
import journal
import reseau

API = config.BLUESKY_PDS.rstrip("/") + "/xrpc"
SERVICE_TROUSSEAU = "bluesky-communaute-app"
COMPTE_TROUSSEAU = "crabe"


def _trousseau(service, compte):
    if sys.platform != "darwin":
        return ""
    r = subprocess.run(
        ["security", "find-generic-password", "-s", service, "-a", compte, "-w"],
        capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def _identifiant():
    return config.BLUESKY_IDENTIFIER or config.BLUESKY_HANDLE


def _mot_de_passe():
    if config.BLUESKY_MOT_DE_PASSE:
        return config.BLUESKY_MOT_DE_PASSE
    return _trousseau(SERVICE_TROUSSEAU, COMPTE_TROUSSEAU)


def disponible():
    """Vrai si un mot de passe d'application est disponible (env ou Trousseau)."""
    return bool(_mot_de_passe())


def _poste(chemin, corps, jeton=None, essais=2):
    donnees = json.dumps(corps).encode("utf-8")
    entetes = {"Content-Type": "application/json"}
    if jeton:
        entetes["Authorization"] = "Bearer " + jeton
    derniere = None
    for tentative in range(essais + 1):
        try:
            req = urllib.request.Request(API + chemin, data=donnees,
                                         headers=entetes, method="POST")
            with urllib.request.urlopen(req, timeout=45,
                                        context=reseau.contexte()) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            derniere = e
            if tentative < essais:
                time.sleep(2 * (tentative + 1))
    raise derniere


def _ts(valeur):
    if not valeur:
        return 0.0
    try:
        return datetime.fromisoformat(str(valeur).replace("Z", "+00:00")).timestamp()
    except ValueError:
        return 0.0


def _composer(lien, titre, resume):
    """Post ≤ 300 signes (limite Bluesky), avec lien et mots-clés."""
    queue = f"\n\n🔗 {lien}\n#IA #OpenClaw"
    tete = f"🦀 {titre}"
    place = 300 - len(tete) - len(queue)
    corps = ""
    if place >= 60 and resume:
        corps = "\n\n" + resume
        if len(corps) > place:
            corps = corps[:place].rsplit(" ", 1)[0] + "…"
    return tete + corps + queue


def _candidats():
    """Brèves (≤ 36 h, importance ≥ 2) et articles pas encore diffusés, récents d'abord."""
    elements = []
    if config.FICHIER_BREVES.exists():
        try:
            breves = json.loads(config.FICHIER_BREVES.read_text(encoding="utf-8"))
        except ValueError:
            breves = []
        for b in breves:
            if b.get("importance", 2) < 2:
                continue
            ts = _ts(b.get("date_source")) or _ts(b.get("date_redac"))
            if ts and ts < time.time() - 36 * 3600:
                continue
            elements.append(("br-" + str(b.get("id") or b.get("slug")), ts,
                             f"{config.URL_SITE}/breves/{b['slug']}/",
                             b["titre"], b.get("resume", "")))
    if config.DOSSIER_ARTICLES.exists():
        for f in sorted(config.DOSSIER_ARTICLES.glob("*.json")):
            try:
                a = json.loads(f.read_text(encoding="utf-8"))
            except ValueError:
                continue
            elements.append(("ar-" + f.stem, _ts(a.get("date")),
                             f"{config.URL_SITE}/articles/{f.stem}/",
                             a["titre"], a.get("chapo", "")))
    elements.sort(key=lambda e: e[1], reverse=True)
    return elements


def diffuser(max_publications=None):
    """Publie sur Bluesky les éléments pas encore diffusés. Renvoie le nombre de posts."""
    if not disponible():
        return 0
    if max_publications is None:
        max_publications = config.MAX_PUBLICATIONS_PAR_RUN

    etat = {}
    if config.FICHIER_SOCIAL_ETAT.exists():
        try:
            etat = json.loads(config.FICHIER_SOCIAL_ETAT.read_text(encoding="utf-8"))
        except ValueError:
            etat = {}
    publies = etat.setdefault("publies", {})

    session = _poste("/com.atproto.server.createSession",
                     {"identifier": _identifiant(), "password": _mot_de_passe()})
    jeton, did = session["accessJwt"], session["did"]

    envois = 0
    for cle, _moment, lien, titre, resume in _candidats():
        if cle in publies:
            continue
        if envois >= max_publications:
            break
        texte = _composer(lien, titre, resume)
        d = _poste("/com.atproto.repo.createRecord",
                   {"repo": did,
                    "collection": "app.bsky.feed.post",
                    "record": {
                        "$type": "app.bsky.feed.post",
                        "text": texte,
                        "langs": ["fr"],
                        "createdAt": datetime.now(timezone.utc).isoformat(
                            timespec="seconds").replace("+00:00", "Z"),
                    }},
                   jeton)
        publies[cle] = {"uri": d.get("uri"),
                        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
        envois += 1
        print(f"   🦋 Bluesky : {titre[:64]}")
        time.sleep(2)
    if envois:
        config.FICHIER_SOCIAL_ETAT.write_text(
            json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
        journal.ajouter("diffusion", reseau="bluesky", publications=envois)
    return envois
