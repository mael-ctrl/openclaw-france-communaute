# -*- coding: utf-8 -*-
"""Créer le compte Bluesky du Crabe (à exécuter une seule fois, en local).

Usage :
    BSKY_MOT_DE_PASSE='…' BSKY_EMAIL='support@openclaw-france.fr' \
        python3 outils/creer_compte_bluesky.py

Le mot de passe du compte est fourni par l'environnement et rangé ensuite
dans le Trousseau macOS, comme le mot de passe d'application généré par
Bluesky (celui que le robot utilise au quotidien). Aucun secret n'est affiché.
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "..", "engine"))
import reseau  # noqa: E402

PDS = os.environ.get("BSKY_PDS", "https://atproto.openclaw-france.fr")
API = PDS.rstrip("/") + "/xrpc"
HANDLE_PERSO = os.environ.get("BSKY_HANDLE_PERSO", "communaute.openclaw-france.fr")
HANDLES_ESSAI = ["crabe.openclaw-france.fr"]


def _poste(chemin, corps, jeton=None):
    donnees = json.dumps(corps).encode("utf-8")
    entetes = {"Content-Type": "application/json"}
    if jeton:
        entetes["Authorization"] = "Bearer " + jeton
    req = urllib.request.Request(API + chemin, data=donnees, headers=entetes, method="POST")
    with urllib.request.urlopen(req, timeout=60, context=reseau.contexte()) as r:
        brut = r.read().decode("utf-8")
        return json.loads(brut) if brut.strip() else {}


def main():
    mot_de_passe = os.environ.get("BSKY_MOT_DE_PASSE", "")
    email = os.environ.get("BSKY_EMAIL", "")
    if not mot_de_passe or not email:
        return "BSKY_MOT_DE_PASSE et BSKY_EMAIL sont requis."

    session = None
    for handle in HANDLES_ESSAI:
        try:
            session = _poste("/com.atproto.server.createAccount",
                             {"handle": handle, "email": email, "password": mot_de_passe})
            print(f"✅ Compte créé : {handle}")
            break
        except Exception as e:  # noqa: BLE001
            print(f"… {handle} indisponible ({str(e)[:90]})")
    if not session:
        return "Échec : aucun handle d'essai disponible."

    did, jeton = session["did"], session["accessJwt"]
    print(f"   did : {did}")

    app = _poste("/com.atproto.server.createAppPassword", {"name": "crabe-bot"}, jeton)
    print("   mot de passe d'application créé")

    _poste("/com.atproto.repo.putRecord",
           {"repo": did,
            "collection": "app.bsky.actor.profile",
            "rkey": "self",
            "record": {
                "$type": "app.bsky.actor.profile",
                "displayName": "Le Crabe 🦀 — La Communauté",
                "description": ("L'actu de l'IA en français, écrite et publiée à 100 % par une IA. "
                                "OpenClaw · Hermes · Claude · OpenAI · Mistral. "
                                "communaute.openclaw-france.fr"),
            }},
           jeton)
    print("   profil renseigné")

    handle_actuel = session["handle"]
    if HANDLE_PERSO and HANDLE_PERSO != handle_actuel:
        for _essai in range(6):
            try:
                _poste("/com.atproto.identity.updateHandle", {"handle": HANDLE_PERSO}, jeton)
                print(f"✅ Handle personnalisé actif : {HANDLE_PERSO}")
                handle_actuel = HANDLE_PERSO
                break
            except Exception as e:  # noqa: BLE001
                print(f"… DNS pas encore propagé ({str(e)[:70]}) — nouvelle tentative dans 10 s")
                time.sleep(10)

    if sys.platform == "darwin":
        for service, compte, valeur in (
                ("bluesky-communaute", handle_actuel, mot_de_passe),
                ("bluesky-communaute-app", "crabe", app["password"])):
            subprocess.run(["security", "add-generic-password", "-U",
                            "-s", service, "-a", compte, "-w", valeur], check=False)
        print("🔐 Secrets rangés dans le Trousseau macOS (compte + mot de passe d'application)")

    print(f"FINAL handle={handle_actuel} did={did}")
    return None


if __name__ == "__main__":
    probleme = main()
    if probleme:
        print("❌ " + probleme)
        sys.exit(1)
