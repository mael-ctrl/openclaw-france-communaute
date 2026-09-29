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

import archive           # noqa: E402
import collecte          # noqa: E402
import config            # noqa: E402
import construction      # noqa: E402
import deepseek          # noqa: E402
import deploiement       # noqa: E402
import indexnow          # noqa: E402
import journal           # noqa: E402
import redaction         # noqa: E402
import social            # noqa: E402


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

    # 2) Solde + garde-fou budget mensuel (mis à jour AVANT toute dépense)
    d_solde = deepseek.solde() if config.DEEPSEEK_CLE else {"erreur": "clé absente"}
    stats = journal.charger_stats()
    hist = stats.setdefault("historique_solde", [])
    if d_solde.get("total") is not None:
        hist.append([time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime()), d_solde["total"]])
        del hist[:-500]
    depense_mois = journal.depense_du_mois(stats)
    budget_usd = config.BUDGET_MENSUEL_EUR * config.TAUX_EUR_USD
    mode_budget = "normal"
    if depense_mois >= budget_usd:
        mode_budget = "budget_atteint"
    elif depense_mois >= budget_usd * 0.75:
        mode_budget = "economie"
    stats["mode_budget"] = mode_budget
    stats["depense_mois_usd"] = round(depense_mois, 2)
    journal.sauver_stats(stats)
    if mode_budget == "budget_atteint":
        print(f"   💸 Budget mensuel atteint ({depense_mois:.2f} $ / {budget_usd:.2f} $) — rédaction en pause")
        journal.ajouter("budget", mode=mode_budget, depense_usd=round(depense_mois, 2),
                        plafond_eur=config.BUDGET_MENSUEL_EUR)
    elif mode_budget == "economie":
        config.MAX_BREVES_PAR_RUN = min(config.MAX_BREVES_PAR_RUN, 2)
        config.MAX_ARTICLES_PAR_RUN = 0
        print("   🪙 Mode économie (75 % du budget atteint) — cadence réduite")
        journal.ajouter("budget", mode=mode_budget, depense_usd=round(depense_mois, 2),
                        plafond_eur=config.BUDGET_MENSUEL_EUR)

    # 3) Rédaction
    if not args.sans_redaction and config.DEEPSEEK_CLE and items and mode_budget != "budget_atteint":
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

    # 4) Stats du run courant, AVANT le build (le site publie les chiffres à jour)
    stats = journal.charger_stats()
    solde_avant = (stats.get("solde") or {}).get("total")
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

    # 5) Construction du site
    try:
        resume["fichiers"] = construction.construire()
        journal.ajouter("construction", fichiers=resume["fichiers"])
    except Exception as e:
        journal.erreur(f"construction : {e}")
        raise

    try:
        indexnow.ecrire_cle()
    except Exception as e:
        journal.erreur(f"indexnow (clé) : {e}")

    # 6) Déploiement
    if not args.essai and not args.sans_deploiement:
        try:
            envois, octets = deploiement.deployer()
            journal.ajouter("deploiement", fichiers=envois, octets=octets)
            resume["envois"] = envois
        except Exception as e:
            journal.erreur(f"déploiement : {e}")
            print(f"   ⚠️  déploiement impossible : {e}")

    # 7) Signal d'indexation (IndexNow : Bing/Yandex, sans compte)
    if not args.essai and not args.sans_deploiement:
        try:
            code = indexnow.signaler()
            journal.ajouter("indexation", indexnow=code)
            print(f"   🧭 IndexNow : {code}")
        except Exception as e:
            journal.erreur(f"indexation : {e}")

    # 8) Archivage quotidien (Wayback Machine) — preuve horodatée indépendante
    if not args.essai and not args.sans_deploiement:
        try:
            resultat_archive = archive.archiver_si_necessaire()
            if resultat_archive:
                print(f"   🗄️  Archive : {resultat_archive}")
        except Exception as e:
            journal.erreur(f"archivage : {e}")

    # 9) Diffusion sociale — le Crabe parle au monde (Bluesky)
    if not args.essai and social.disponible():
        try:
            resume["publications"] = social.diffuser()
        except Exception as e:
            journal.erreur(f"diffusion sociale : {e}")

    # 8) Bilan
    journal.ajouter("bilan", duree_s=round(time.time() - debut, 1), **resume)

    print(f"🦀 Terminé en {time.time() - debut:.0f} s — "
          f"{resume['neufs']} neuf(s), {resume['breves']} brève(s), "
          f"{resume['articles']} article(s), {resume.get('envois', 0)} fichier(s) envoyé(s), "
          f"{resume.get('publications', 0)} publication(s) Bluesky")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
