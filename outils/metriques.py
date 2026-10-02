#!/usr/bin/env python3
"""Métriques trafic & audience — La Communauté 🦀

Télécharge les logs journaliers du hosting OVH (logs.ovh.net, compte « userLogs »
stocké au Trousseau macOS sous « ovh-communo-logs »), calcule des agrégats par
jour (humains/robots, visiteurs uniques par site, top pages, statuts HTTP, bande
servie, référents externes) et met à jour data/trafic.json.

Aucune IP n'est conservée : uniquement des compteurs agrégés (publiables).

Usage :
  python3 outils/metriques.py            # complète les jours manquants (8 derniers jours)
  python3 outils/metriques.py --jours 3  # limite la fenêtre de rattrapage
  python3 outils/metriques.py --json     # sortie JSON compacte (cron / scripts)
"""
import argparse
import base64
import collections
import datetime as dt
import gzip
import json
import re
import ssl
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "data" / "trafic.json"
CACHE = Path.home() / ".hermes" / "cache" / "trafic-logs"
BASE_LOGS = "https://logs.cluster131.hosting.ovh.net/communo.cluster131.hosting.ovh.net"
NOM_FICHIER = "communo.cluster131.hosting.ovh.net-{j:02d}-{m:02d}-{a}.log.gz"

BOTS = re.compile(
    r"bot|spider|crawl|slurp|facebookexternalhit|preview|python-requests|okhttp|"
    r"curl|wget|monitor|uptime|pingdom|node-fetch|Go-http|headless|axios|libwww", re.I)
BOT_NOMS = [
    ("Googlebot", re.compile(r"googlebot", re.I)),
    ("Bingbot", re.compile(r"bingbot", re.I)),
    ("AhrefsBot", re.compile(r"ahrefs", re.I)),
    ("Applebot", re.compile(r"applebot", re.I)),
    ("YandexBot", re.compile(r"yandex", re.I)),
    ("SemrushBot", re.compile(r"semrush", re.I)),
    ("PetalBot", re.compile(r"petal", re.I)),
    ("Bytespider", re.compile(r"bytespider", re.I)),
]
LIGNE = re.compile(r'^(\S+) (\S+) \S+ \[([^\]]+)\] "(\S+) (\S+)[^"]*" (\d{3}) (\S+)(?: "([^"]*)" "([^"]*)")?')
HOTES_INTERNES = re.compile(r"communaute-ia\.(fr|com)|openclaw-france\.fr", re.I)


def _ctx():
    c = ssl.create_default_context()
    try:
        c.load_verify_locations("/etc/ssl/cert.pem")
    except Exception:
        pass
    return c


def mot_de_passe():
    r = subprocess.run(
        ["security", "find-generic-password", "-s", "ovh-communo-logs", "-a", "communo-logs", "-w"],
        capture_output=True, text=True)
    return r.stdout.strip()


def telecharger(jour, mot):
    CACHE.mkdir(parents=True, exist_ok=True)
    nom = NOM_FICHIER.format(j=jour.day, m=jour.month, a=jour.year)
    local = CACHE / nom
    if local.exists():
        return local
    url = f"{BASE_LOGS}/logs/logs-{jour.month:02d}-{jour.year}/{nom}"
    auth = base64.b64encode(f"communo-logs:{mot}".encode()).decode()
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    try:
        with urllib.request.urlopen(req, timeout=60, context=_ctx()) as r:
            local.write_bytes(r.read())
        return local
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def analyser(chemin):
    humains = 0
    robots = 0
    sans_ua = 0
    requetes = 0
    bande = 0
    uniqs = collections.defaultdict(set)
    pages = collections.Counter()
    statuts = collections.Counter()
    robots_top = collections.Counter()
    refs = collections.Counter()
    for ligne in gzip.open(chemin, "rt", errors="ignore"):
        m = LIGNE.match(ligne)
        if not m:
            continue
        ip, vhost, _ts, _meth, url, statut, taille, ref, ua = m.groups()
        requetes += 1
        statuts[statut] += 1
        if ua and BOTS.search(ua):
            robots += 1
            robots_top[next((n for n, rx in BOT_NOMS if rx.search(ua)), "autre")] += 1
        else:
            humains += 1
            uniqs[vhost].add(ip)
            pages[url] += 1
            if not ua or ua == "-":
                sans_ua += 1
            try:
                bande += int(taille)
            except Exception:
                pass
        if ref and ref != "-" and not HOTES_INTERNES.search(ref):
            refs[ref] += 1
    tous = set().union(*uniqs.values()) if uniqs else set()
    return {
        "requetes": requetes,
        "humains": humains,
        "robots": robots,
        "sans_ua": sans_ua,
        "uniques": len(tous),
        "uniques_par_site": {k: len(v) for k, v in sorted(uniqs.items(), key=lambda x: -len(x[1]))},
        "pages_top": [[p, c] for p, c in pages.most_common(10)],
        "statuts": dict(statuts.most_common(8)),
        "robots_top": dict(robots_top.most_common(8)),
        "refs_ext": [[r[:90], c] for r, c in refs.most_common(8)],
        "bande_mo": round(bande / 1048576, 1),
    }


def bluesky():
    try:
        req = urllib.request.Request(
            "https://public.api.bsky.app/xrpc/app.bsky.actor.getProfile?actor=communaute-ia.fr")
        with urllib.request.urlopen(req, timeout=30, context=_ctx()) as r:
            d = json.loads(r.read().decode())
        return {"followers": d.get("followersCount"), "posts": d.get("postsCount")}
    except Exception:
        return {}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jours", type=int, default=8, help="fenêtre de rattrapage en jours")
    ap.add_argument("--json", action="store_true", help="sortie JSON compacte")
    args = ap.parse_args()

    data = json.loads(SORTIE.read_text(encoding="utf-8")) if SORTIE.exists() else {}
    data.setdefault("jours", {})
    mot = mot_de_passe()
    if not mot:
        print("ERREUR : Trousseau « ovh-communo-logs » introuvable (compte communo-logs).")
        return 2

    nouveaux = []
    for delta in range(1, args.jours + 1):
        jour = dt.date.today() - dt.timedelta(days=delta)
        cle = jour.isoformat()
        if cle in data["jours"]:
            continue
        chemin = telecharger(jour, mot)
        if chemin is None:
            continue
        data["jours"][cle] = analyser(chemin)
        nouveaux.append(cle)

    horodatage = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    data["audience"] = {"bluesky": bluesky(), "maj": horodatage}
    data["maj"] = horodatage
    data["jours"] = dict(sorted(data["jours"].items()))
    SORTIE.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    if args.json:
        dernier = sorted(data["jours"])[-1] if data["jours"] else None
        print(json.dumps({"nouveaux": nouveaux, "dernier": dernier,
                          "audience": data["audience"]["bluesky"]}, ensure_ascii=False))
    else:
        print("Nouveaux jours :", ", ".join(nouveaux) if nouveaux else "aucun")
        for j, d in data["jours"].items():
            print(f"  {j} : {d['uniques']} visiteurs uniques | {d['humains']} req. humaines | "
                  f"{d['robots']} robots | {d['bande_mo']} Mo")
        aud = data["audience"].get("bluesky") or {}
        if aud:
            print(f"  Bluesky : {aud.get('followers')} abonné(s), {aud.get('posts')} posts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
