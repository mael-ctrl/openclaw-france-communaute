#!/usr/bin/env bash
# =============================================================================
#  Kit OpenClaw France — scripts/mise-a-jour.sh                 (version 1.0)
# -----------------------------------------------------------------------------
#  Rôle : mettre à jour OpenClaw proprement, dans cet ordre :
#      1. sauvegarde de sécurité (recommandée par la doc officielle avant
#         toute mise à jour importante) ;
#      2. mise à jour via la méthode officielle ;
#      3. vérifications (version, diagnostic, passerelle).
#
#  Utilisation :
#      bash scripts/mise-a-jour.sh          # avec confirmation
#      bash scripts/mise-a-jour.sh --oui    # sans confirmation (automatisation)
#
#  La sauvegarde préalable se désactive avec : FAIRE_SAUVEGARDE=0
#
#  Doc officielle : https://docs.openclaw.ai/install/updating
#  Support communauté : https://communaute-ia.fr
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Variables — tout se règle ici, en haut du fichier.
# -----------------------------------------------------------------------------
RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"   # dossier du kit
MODE="${MODE:-auto}"                          # auto | classique | docker
FAIRE_SAUVEGARDE="${FAIRE_SAUVEGARDE:-1}"     # 1 = sauvegarder avant de mettre à jour
CONFIRMATION=1                                # 0 = ne rien demander (option --oui)

# Si OpenClaw ou Node sont installés hors des chemins standards, ajoutez leur
# dossier ci-dessous (utile quand le script tourne depuis cron).
PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:$PATH"
export PATH

# -----------------------------------------------------------------------------
# Petites fonctions d'affichage
# -----------------------------------------------------------------------------
info()   { printf 'ℹ️  %s\n' "$*"; }
ok()     { printf '✅ %s\n' "$*"; }
avis()   { printf '⚠️  %s\n' "$*"; }
erreur() { printf '❌ %s\n' "$*" >&2; }

afficher_aide() {
  cat <<'AIDE'
Kit OpenClaw France — scripts/mise-a-jour.sh

Met à jour OpenClaw en sécurité : sauvegarde → mise à jour → vérifications.

Utilisation :
  bash scripts/mise-a-jour.sh          avec confirmation (recommandé)
  bash scripts/mise-a-jour.sh --oui    sans confirmation (automatisation)

Réglages (en haut du script) :
  FAIRE_SAUVEGARDE=0   désactiver la sauvegarde automatique préalable
  MODE=classique|docker   forcer la méthode d'installation détectée

Doc officielle : https://docs.openclaw.ai/install/updating
AIDE
}

# -----------------------------------------------------------------------------
# Lecture des options
# -----------------------------------------------------------------------------
while [ $# -gt 0 ]; do
  case "$1" in
    --oui|-o) CONFIRMATION=0 ;;
    --aide|-h|--help) afficher_aide; exit 0 ;;
    *) erreur "Option inconnue : $1"; afficher_aide; exit 1 ;;
  esac
  shift
done

# -----------------------------------------------------------------------------
# Détection de la méthode d'installation
# -----------------------------------------------------------------------------
detecter_mode() {
  case "$MODE" in
    classique|docker) return 0 ;;
    auto)
      if command -v openclaw >/dev/null 2>&1; then
        MODE="classique"
      elif [ -f "$RACINE/docker-compose.yml" ] && command -v docker >/dev/null 2>&1; then
        MODE="docker"
      else
        erreur "Aucune installation détectée (ni commande « openclaw », ni Docker)."
        erreur "Lisez le GUIDE.md du kit pour d'abord installer OpenClaw."
        exit 1
      fi
      ;;
    *)
      erreur "Valeur MODE inconnue : $MODE (attendu : auto, classique ou docker)"
      exit 1
      ;;
  esac
}

# -----------------------------------------------------------------------------
# Exécution
# -----------------------------------------------------------------------------
detecter_mode
info "Méthode détectée : $MODE"

if [ "$CONFIRMATION" -eq 1 ]; then
  printf 'Mettre à jour OpenClaw maintenant ? [o/N] '
  if ! read -r reponse; then
    reponse="n"
  fi
  case "$reponse" in
    o|O|oui|OUI|y|Y) ;;
    *) info "Mise à jour annulée."; exit 0 ;;
  esac
fi

# --- 1. Sauvegarde de sécurité -------------------------------------------------
if [ "$FAIRE_SAUVEGARDE" -eq 1 ] && [ -f "$RACINE/scripts/sauvegarde.sh" ]; then
  info "Sauvegarde de sécurité avant mise à jour…"
  bash "$RACINE/scripts/sauvegarde.sh"
  ok "Sauvegarde effectuée."
else
  avis "Pas de sauvegarde automatique (désactivée ou script absent)."
  avis "Rappel : la doc officielle recommande une sauvegarde avant toute mise à jour."
fi

# --- 2. Mise à jour ------------------------------------------------------------
case "$MODE" in
  classique)
    info "Mise à jour via la commande officielle « openclaw update »…"
    openclaw update --yes
    ;;
  docker)
    info "Mise à jour des images Docker officielles…"
    ( cd "$RACINE" && \
      docker compose pull openclaw-gateway openclaw-cli && \
      docker compose up -d openclaw-gateway )
    ;;
esac
ok "Mise à jour terminée."

# --- 3. Vérifications ----------------------------------------------------------
echo
info "Vérifications :"
case "$MODE" in
  classique)
    openclaw --version || true
    openclaw doctor || avis "« openclaw doctor » a relevé des points à vérifier ci-dessus."
    openclaw gateway status || avis "Statut de la passerelle indisponible — voir « Dépannage » dans GUIDE.md."
    ;;
  docker)
    ( cd "$RACINE" && docker compose ps ) || true
    PORT_TEST="${OPENCLAW_GATEWAY_PORT:-}"
    if [ -z "$PORT_TEST" ] && [ -f "$RACINE/.env" ]; then
      PORT_TEST="$(grep -E '^OPENCLAW_GATEWAY_PORT=' "$RACINE/.env" | head -n 1 | cut -d= -f2 | tr -d ' ' || true)"
    fi
    PORT_TEST="${PORT_TEST:-18789}"
    info "Test de santé sur http://127.0.0.1:${PORT_TEST}/healthz (jusqu'à 60 s)…"
    sante=0
    i=1
    while [ "$i" -le 12 ]; do
      if curl -fsS "http://127.0.0.1:${PORT_TEST}/healthz" >/dev/null 2>&1; then
        sante=1
        break
      fi
      sleep 5
      i=$((i + 1))
    done
    if [ "$sante" -eq 1 ]; then
      ok "La passerelle répond. 🎉"
    else
      avis "Pas de réponse après 60 s. Affichez les journaux :"
      avis "   cd $RACINE && docker compose logs -f openclaw-gateway"
    fi
    ;;
esac

cat <<'SUITE'

──────────────────────────────────────────────────────────────
  C'est fini.
  Si quelque chose ne répond pas : GUIDE.md, section « Dépannage ».
  Docs officielles : https://docs.openclaw.ai/install/updating
  Support communauté : https://communaute-ia.fr
──────────────────────────────────────────────────────────────
SUITE
