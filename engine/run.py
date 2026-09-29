# -*- coding: utf-8 -*-
"""Orchestrateur — une commande pour tout faire.

Usage :
    python engine/run.py --tout                # collecte + rédaction + build + déploiement
    python engine/run.py --essai               # mode test : 2 brèves max, pas de déploiement
    python engine/run.py --sans-deploiement    # tout sauf l'envoi FTP
    python engine/run.py --sans-redaction      # collecte + build + déploiement seulement
"""
import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import collecte          # noqa: E402
import config            # noqa: E402
import construction      # noqa: E402
import deepseek          # noqa: E402
import deploiement       # noqa: E402
import journal           # noqa: E402
import redaction         # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="Pipeline du site La Communauté 🦀")
    ap.add_argument("--tout", action="store_true", help="tout faire (défaut)")
    ap.add_argument("--essai", action="store_true", help="mode test (réduit, sans FTP)")
    ap.add_argument("--sans-deploiement", action="store_true")
    ap.add_argument("--sans-redaction", action="store_true")
    args = ap.parse_args()

    if args.essai:
        config.MAX_BREVES_PAR_RUN = min(config.MAX_BREVES_PAR_RUN, 2)
        config.MAX_ITEMS_PAR_RUN = min(config.MAX_ITEMS_PAR_RUN, 14)
        config.MAX_ARTICLES_PAR_RUN = min(config.MAX_ARTICLES_PAR_RUN, 1)

    debut = time.time()
    print(f"🦀 Run du {time.strftime('%d/%m/%Y %H:%M')} — début"
          + (" (mode essai)" if args.essai else ""))

    stats = journal.charger_stats()
    resume = {"neufs": 0, "breves": 0, "articles": 0, "fichiers": 0}

    # 1) Collecte
    try:
        items, rapport_flux = collecte.collecter()
        resume["neufs"] = len(items)
        journal.ajouter("collecte", neufs=len(items))
    except Exception as e:
        journal.erreur(f"collecte : {e}")
        items, rapport_flux = [], []

    # 2) Rédaction
    if not args.sans_redaction and config.DEEPSEEK_CLE and items:
        try:
            breves = redaction.rediger_breves(items)
            resume["breves"] = len(breves)
        except Exception as e:
            journal.erreur(f"rédaction brèves : {e}")
        try:
            articles = redaction.rediger_articles_si_besoin(items)
            resume["articles"] = len(articles)
        except Exception as e:
            journal.erreur(f"rédaction articles : {e}")
    elif not config.DEEPSEEK_CLE:
        journal.erreur("DEEPSEEK_API_KEY absente — rédaction sautée")

    # 3) Stats du run courant, AVANT le build (le site publie les chiffres à jour)
    stats = journal.charger_stats()
    solde_avant = (stats.get("solde") or {}).get("total")
    d_solde = deepseek.solde() if config.DEEPSEEK_CLE else {"erreur": "clé absente"}
    stats["runs"] = stats.get("runs", 0) + 1
    stats["items_collectes"] = stats.get("items_collectes", 0) + resume["neufs"]
    stats["breves_publiees"] = stats.get("breves_publiees", 0) + resume["breves"]
    stats["articles_publies"] = stats.get("articles_publies", 0) + resume["articles"]
    stats["premier_run"] = stats.get("premier_run") or time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())
    stats["dernier_run"] = time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime())
    if solde_avant and d_solde.get("total"):
        stats.setdefault("solde_initial", solde_avant)
    if d_solde.get("total") and stats.get("solde_initial"):
        try:
            consomme = float(stats["solde_initial"]) - float(d_solde["total"])
            stats["depense_usd"] = round(consomme, 2)
        except (TypeError, ValueError):
            pass
    stats["solde"] = d_solde
    journal.sauver_stats(stats)

    # 4) Construction du site
    try:
        resume["fichiers"] = construction.construire()
        journal.ajouter("construction", fichiers=resume["fichiers"])
    except Exception as e:
        journal.erreur(f"construction : {e}")
        raise

    # 5) Déploiement
    if not args.essai and not args.sans_deploiement:
        try:
            envois, octets = deploiement.deployer()
            journal.ajouter("deploiement", fichiers=envois, octets=octets)
            resume["envois"] = envois
        except Exception as e:
            journal.erreur(f"déploiement : {e}")
            print(f"   ⚠️  déploiement impossible : {e}")

    # 6) Bilan
    journal.ajouter("bilan", duree_s=round(time.time() - debut, 1), **resume)

    print(f"🦀 Terminé en {time.time() - debut:.0f} s — "
          f"{resume['neufs']} neuf(s), {resume['breves']} brève(s), "
          f"{resume['articles']} article(s), {resume.get('envois', 0)} fichier(s) envoyé(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
