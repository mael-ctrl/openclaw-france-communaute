#!/usr/bin/env python3
"""Composer local de La Brève du Crabe. Bibliothèque standard uniquement."""
import argparse
import html
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path
from datetime import date, datetime, timedelta, timezone
from urllib.parse import urldefrag, urlsplit, unquote, parse_qsl

SITE = "https://communaute-ia.fr"
MAX_BYTES = 8 * 1024 * 1024
PLACEHOLDERS = re.compile(
    r"\b(?:TODO|TBD|FIXME|PLACEHOLDER|Lorem ipsum)\b|"
    r"(?:^|\[)\s*(?:à|a)\s+(?:remplacer|compléter|renseigner)|"
    r"\[(?:secteur|public cible|objectif|canaux|nombre)\]|\{\{|\}\}|\$\{", re.I
)
REQUIRED = {'id', 'slug', 'titre', 'resume', 'source', 'lien_source', 'date_redac', 'date_source'}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("clé JSON dupliquée")
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError("constante non JSON refusée : " + value)


def load_input(path):
    if not path.is_file():
        raise ValueError("un fichier local ordinaire est requis")
    with path.open('rb') as source:
        raw = source.read(MAX_BYTES + 1)
    if len(raw) > MAX_BYTES:
        raise ValueError("JSON au-delà de la limite de 8 Mio")
    data = json.loads(raw.decode('utf-8'), object_pairs_hook=unique_object, parse_constant=reject_constant)
    return data, hashlib.sha256(raw).hexdigest()


def escape_text(value):
    text = html.escape(' '.join(value.split()), quote=False)
    return re.sub(r'([\\`*_{}\[\]()#+!|])', r'\\\1', text)


def validate_url(url):
    # Analyse syntaxique seule : aucune requête, résolution DNS ou réécriture.
    if any(c.isspace() or ord(c) < 32 or c in '<>"\\`' for c in url):
        raise ValueError("URL contenant des caractères interdits")
    if re.search(r'%(?![0-9a-fA-F]{2})', url) or any(ord(c) < 32 for c in unquote(url)):
        raise ValueError("encodage URL invalide")
    parts = urlsplit(url)
    host = parts.hostname or ''
    if parts.scheme != 'https' or parts.username is not None or parts.password is not None:
        raise ValueError("URL HTTPS publique sans identifiants requise")
    if parts.port not in (None, 443) or not re.fullmatch(
        r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}', host
    ):
        raise ValueError("nom de domaine public requis, ports non standards et IP refusés")
    blocked = ('localhost', 'local', 'internal', 'invalid', 'test', 'example', 'lan',
               'home', 'example.com', 'example.org', 'example.net')
    if any(host == item or host.endswith('.' + item) for item in blocked):
        raise ValueError("domaine réservé ou privé refusé")
    for key, _ in parse_qsl(parts.query, keep_blank_values=True):
        if key.casefold().startswith('utm_') or key.casefold() in {
            'gclid', 'dclid', 'fbclid', 'msclkid', 'mc_cid', 'mc_eid'
        }:
            raise ValueError("URL de suivi refusée ; fournir une source directe validée")


def parse_timestamp(value):
    if not isinstance(value, str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,6})?(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)", value
    ):
        raise ValueError("horodatage ISO avec fuseau obligatoire")
    return datetime.fromisoformat(value).astimezone(timezone.utc)


def validate(rows):
    if not isinstance(rows, list) or not rows:
        raise ValueError("liste de brèves non vide attendue")
    for index, row in enumerate(rows):
        prefix = f"entrée {index + 1} : "
        if not isinstance(row, dict) or not REQUIRED <= row.keys():
            raise ValueError(prefix + "objet incomplet")
        if row.keys() - REQUIRED - {'importance', 'tags', 'gen'}:
            raise ValueError(prefix + "champ inconnu (pas de données de contacts)")
        if 'importance' in row and (type(row['importance']) is not int or not 1 <= row['importance'] <= 5):
            raise ValueError(prefix + "importance entière entre 1 et 5 attendue")
        if 'tags' in row and (not isinstance(row['tags'], list) or
                              any(not isinstance(tag, str) for tag in row['tags'])):
            raise ValueError(prefix + "tags doit être une liste de textes")
        if 'gen' in row and not isinstance(row['gen'], dict):
            raise ValueError(prefix + "gen doit être un objet")
        for key in REQUIRED - {'date_source'}:
            value = row[key]
            if not isinstance(value, str) or not value.strip():
                raise ValueError(prefix + f"{key} doit être un texte non vide")
            if len(value) > 10000 or any(
                unicodedata.category(c).startswith('C') and c not in '\n\t\r' for c in value
            ):
                raise ValueError(prefix + f"{key} trop long ou avec caractères de contrôle")
            if PLACEHOLDERS.search(value):
                raise ValueError(prefix + f"placeholder dans {key}")
        if not re.fullmatch(r'[0-9a-f]{16}', row['id']):
            raise ValueError(prefix + "id invalide")
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,199}', row['slug']):
            raise ValueError(prefix + "slug invalide")
        validate_url(row['lien_source'])
        parse_timestamp(row['date_redac'])
        if row['date_source'] is not None:
            parse_timestamp(row['date_source'])


def select(rows, issue_date, limit=5, days=7, only_ids=None):
    validate(rows)
    slugs = [r['slug'] for r in rows[:400]]
    if len(slugs) != len(set(slugs)):
        raise ValueError("Page éditoriale dupliquée dans les 400 pages construites")
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', issue_date):
        raise ValueError("date explicite requise au format YYYY-MM-DD")
    if type(limit) is not int or not 1 <= limit <= 10 or type(days) is not int or not 1 <= days <= 31:
        raise ValueError("limite attendue : 1–10 brèves et 1–31 jours")
    end = datetime.combine(date.fromisoformat(issue_date) + timedelta(days=1),
                           datetime.min.time(), tzinfo=timezone.utc)
    start = end - timedelta(days=days)
    candidates = [r for r in rows[:400]
                  if start <= parse_timestamp(r['date_source'] or r['date_redac']) < end
                  and parse_timestamp(r['date_redac']) < end]
    if only_ids is not None:
        if (not only_ids or any(not re.fullmatch(r'[0-9a-f]{16}', i) for i in only_ids)
                or len(set(only_ids)) != len(only_ids) or len(only_ids) > limit):
            raise ValueError("IDs explicites uniques et valides requis, sans dépasser --limit")
        candidates = [r for r in candidates if r['id'] in only_ids]
        if any(sum(r['id'] == i for r in candidates) != 1 for i in only_ids):
            raise ValueError("ID absent, ambigu, hors fenêtre ou hors des 400 pages construites")
    candidates.sort(key=lambda r: (-parse_timestamp(r['date_redac']).timestamp(),
                                   r['slug'], json.dumps(r, sort_keys=True, ensure_ascii=False)))
    seen = set()
    selected = []
    for row in candidates:
        keys = {('id', row['id']), ('slug', row['slug']),
                ('title', ' '.join(row['titre'].casefold().split())),
                ('url', urldefrag(row['lien_source']).url),
                ('source', ' '.join(row['source'].casefold().split()))}
        if seen.intersection(keys):
            continue
        seen.update(keys)
        selected.append(row)
        if len(selected) == limit:
            break
    if only_ids is not None and {r['id'] for r in selected} != set(only_ids):
        raise ValueError("sélection explicite incompatible avec la déduplication")
    if not selected:
        raise ValueError("aucune brève admissible dans la fenêtre ; aucun brouillon produit")
    return selected


def compose(rows, issue_date, sha, limit=5, days=7, *, input_sha256, only_ids=None):
    if not re.fullmatch(r'[0-9a-f]{40}', sha):
        raise ValueError("SHA Git complet de 40 caractères hexadécimaux minuscules requis")
    rows = select(rows, issue_date, limit, days, only_ids)
    lines = [
        f"# La Brève du Crabe 🦀 — édition du {issue_date}", "",
        "> BROUILLON LOCAL — NON ENVOYÉ", "",
        f"Date d'édition : {issue_date} (UTC).",
        f"Commit source déclaré : `{sha}`.", "",
        f"SHA-256 du JSON local (octets) : `{input_sha256}`.",
        f"Sélection : {len(rows)} brève(s), plafond {limit}, fenêtre de {days} jour(s) calendaires UTC.", "",
        "Ce brouillon est préparé par une intelligence artificielle à partir des JSON du média.",
        "Aucun envoi ni inscription n'est effectué.", "",
    ]
    if only_ids is not None:
        lines += ["Sélection éditoriale explicite (IDs) : " + ", ".join(sorted(only_ids)) + ".", ""]
    for index, row in enumerate(rows, 1):
        lines.extend([
            f"## {index}. {escape_text(row['titre'])}", "",
            "**Reprise sourcée — non vérifiée indépendamment.**", "",
            f"D'après {escape_text(row['source'])}, dans le résumé du moteur :", "",
            '> ' + escape_text(row["resume"]), "",
            f"- Lire la brève : <{SITE}/breves/{row['slug']}/>",
            f"- Source exacte : {escape_text(row['source'])} — <{row['lien_source']}>",
            f"- Date de rédaction moteur : {row['date_redac']}",
            f"- Date source déclarée : {row['date_source'] or 'non renseignée dans le JSON'}", "",
        ])
    lines.extend([
        "---", "",
        "Les résumés ci-dessus sont repris du moteur, sans nouvelle génération ni vérification factuelle automatique. "
        "Une citation et un lien accessible ne prouvent pas une annonce. Les versions de test, fuites et performances "
        "rapportées restent à confirmer avant toute republication comme faits établis.", "",
        "Engagement du projet : consacrer 100 % des bénéfices (pas du chiffre d'affaires) à des associations "
        "françaises loi 1901. Cette phrase ne constate aucun don réalisé.", "",
        "Aucun chiffre d'audience ni bilan financier n'est ajouté. Aucun formulaire, abonnement, lien de "
        "désinscription factice ou pixel de suivi n'est inclus. Les conditions d'un éventuel lancement restent à valider.", "",
    ])
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="JSON local data/breves.json")
    parser.add_argument("--date", required=True, help="Date explicite de l'édition")
    parser.add_argument("--sha", required=True, help="Commit source complet")
    parser.add_argument("--limit", type=int, default=5, help="Nombre maximum de brèves (1–10)")
    parser.add_argument("--days", type=int, default=7, help="Fenêtre calendaire UTC (1–31 jours)")
    parser.add_argument("--output", type=Path, help="Nouveau fichier Markdown, jamais écrasé ; sinon stdout")
    parser.add_argument("--expect-sha256", help="Empreinte attendue des octets du JSON")
    parser.add_argument("--only-id", action="append", help="ID relu à retenir, répétable ; aucun contournement des bornes")
    args = parser.parse_args()
    try:
        rows, digest = load_input(args.input)
        if args.expect_sha256 is not None and args.expect_sha256 != digest:
            raise ValueError("empreinte du JSON différente de --expect-sha256")

        result = compose(rows, args.date, args.sha, args.limit, args.days,
                         input_sha256=digest, only_ids=args.only_id)
        if args.output:
            with args.output.open('x', encoding='utf-8', newline='\n') as output:
                output.write(result)
    except (ValueError, OSError, OverflowError, RecursionError) as error:
        print(f"Erreur : {error}", file=sys.stderr)
        return 2
    if not args.output:
        print(result, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
