#!/usr/bin/env bash
# =============================================================================
#  Kit OpenClaw France — scripts/install.sh                    (version 1.0)
# -----------------------------------------------------------------------------
#  Rôle : installer OpenClaw sur une machine Linux ou macOS en suivant la
#  méthode OFFICIELLE du projet (https://docs.openclaw.ai/install).
#
#  Ce script ne réinvente rien : il vérifie vos pré-requis, télécharge
#  l'installateur officiel (https://openclaw.ai/install.sh) puis le lance
#  pour vous. L'installateur officiel installe Node.js si nécessaire,
#  installe OpenClaw et démarre l'assistant de configuration.
#
#  Utilisation :
#      bash scripts/install.sh                    # installation + assistant
#      bash scripts/install.sh --sans-onboarding  # installation seule
#      bash scripts/install.sh --aide             # afficher l'aide
#
#  Sécurité :
#    - aucun secret n'est demandé ni enregistré par ce script ;
#    - seules des commandes officielles sont exécutées.
#
#  Support communauté : https://communaute-ia.fr
#  Guide en français  : voir GUIDE.md, dans le dossier du kit.
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Variables — tout se règle ici, en haut du fichier.
# -----------------------------------------------------------------------------
URL_INSTALLATEUR="https://openclaw.ai/install.sh"   # installateur officiel
SANS_ONBOARDING=0                                   # 1 = passer --no-onboard
FICHIER_TEMP=""                                     # rempli automatiquement

# -----------------------------------------------------------------------------
# Petites fonctions d'affichage
# -----------------------------------------------------------------------------
info()   { printf 'ℹ️  %s\n' "$*"; }
ok()     { printf '✅ %s\n' "$*"; }
avis()   { printf '⚠️  %s\n' "$*"; }
erreur() { printf '❌ %s\n' "$*" >&2; }

afficher_aide() {
  cat <<'AIDE'
Kit OpenClaw France — scripts/install.sh

Installe OpenClaw (méthode officielle) sur Linux ou macOS.

Utilisation :
  bash scripts/install.sh                     installation + assistant de démarrage
  bash scripts/install.sh --sans-onboarding   installation seule (sans assistant)
  bash scripts/install.sh --aide              afficher cette aide

Après l'installation :
  openclaw onboard --install-daemon    (si l'assistant ne s'est pas lancé)
  openclaw gateway status              vérifier que la passerelle tourne
  openclaw dashboard                   ouvrir le tableau de bord

Docs officielles   : https://docs.openclaw.ai
Support communauté : https://communaute-ia.fr
AIDE
}

nettoyage() {
  if [ -n "$FICHIER_TEMP" ]; then
    rm -f "$FICHIER_TEMP"
  fi
}
trap nettoyage EXIT

# -----------------------------------------------------------------------------
# Lecture des options
# -----------------------------------------------------------------------------
while [ $# -gt 0 ]; do
  case "$1" in
    --sans-onboarding) SANS_ONBOARDING=1 ;;
    --aide|-h|--help)  afficher_aide; exit 0 ;;
    *) erreur "Option inconnue : $1"; afficher_aide; exit 1 ;;
  esac
  shift
done

# -----------------------------------------------------------------------------
# 1. Vérifications des pré-requis
# -----------------------------------------------------------------------------
info "Vérification de votre système…"

case "$(uname -s)" in
  Linux|Darwin) ok "Système détecté : $(uname -s)" ;;
  *)
    erreur "Système non pris en charge par ce script : $(uname -s)."
    erreur "Voir la page officielle : https://docs.openclaw.ai/install"
    exit 1
    ;;
esac

if ! command -v curl >/dev/null 2>&1; then
  erreur "L'outil « curl » est requis mais introuvable."
  info  "Sur Debian/Ubuntu : sudo apt update && sudo apt install -y curl"
  info  "Sur macOS : curl est normalement déjà installé."
  exit 1
fi
ok "Outil « curl » disponible"

if [ "$(id -u)" -eq 0 ]; then
  avis "Vous êtes connecté en root. C'est fréquent sur un VPS neuf."
  avis "Pour une sécurité maximale, un compte utilisateur dédié est conseillé (voir securite.md)."
fi

# Node.js : OpenClaw exige Node 24.16+ (ou 26.1+). S'il est absent ou trop
# ancien, aucune inquiétude : l'installateur officiel s'en occupe lui-même.
if command -v node >/dev/null 2>&1; then
  VERSION_NODE="$(node -v 2>/dev/null || echo 'inconnue')"
  info "Node.js détecté : $VERSION_NODE (mis à jour automatiquement si nécessaire)"
else
  info "Node.js absent : l'installateur officiel l'installera automatiquement."
fi

# Sans terminal interactif (cron, automatisation), on évite l'assistant.
if [ ! -t 0 ] && [ "$SANS_ONBOARDING" -eq 0 ]; then
  avis "Pas de terminal interactif détecté → l'assistant de démarrage est désactivé."
  SANS_ONBOARDING=1
fi

# -----------------------------------------------------------------------------
# 2. Téléchargement de l'installateur officiel
# -----------------------------------------------------------------------------
info "Téléchargement de l'installateur officiel OpenClaw…"
FICHIER_TEMP="$(mktemp "${TMPDIR:-/tmp}/openclaw-install.XXXXXX")"
curl -fsSL --proto '=https' --tlsv1.2 -o "$FICHIER_TEMP" "$URL_INSTALLATEUR"
ok "Installateur téléchargé depuis $URL_INSTALLATEUR"

# -----------------------------------------------------------------------------
# 3. Lancement de l'installateur officiel
# -----------------------------------------------------------------------------
if [ "$SANS_ONBOARDING" -eq 1 ]; then
  info "Lancement de l'installateur (sans assistant)…"
  bash "$FICHIER_TEMP" --no-onboard
else
  info "Lancement de l'installateur (l'assistant de démarrage va s'ouvrir)…"
  bash "$FICHIER_TEMP"
fi
ok "Installateur terminé."

# -----------------------------------------------------------------------------
# 4. Vérification de l'installation
# -----------------------------------------------------------------------------
if command -v openclaw >/dev/null 2>&1; then
  ok "OpenClaw est installé (version : $(openclaw --version 2>/dev/null || echo '?'))"
  info "Contrôle de santé :"
  openclaw doctor || avis "« openclaw doctor » a relevé des points à corriger — lisez les indications ci-dessus."
else
  avis "La commande « openclaw » n'est pas encore disponible dans ce terminal."
  avis "Ouvrez un nouveau terminal (ou tapez « source ~/.bashrc » / « source ~/.zshrc »),"
  avis "puis vérifiez avec : openclaw --version"
fi

# -----------------------------------------------------------------------------
# 5. Prochaines étapes
# -----------------------------------------------------------------------------
cat <<'SUITE'

──────────────────────────────────────────────────────────────
  Prochaines étapes
──────────────────────────────────────────────────────────────
  openclaw onboard --install-daemon    assistant + service en arrière-plan
  openclaw gateway status              vérifier que la passerelle tourne
  openclaw dashboard                   ouvrir le tableau de bord
  openclaw security audit              premier bilan de sécurité

  Guide complet (français) : GUIDE.md du kit
  Checklist sécurité       : securite.md du kit
  Docs officielles         : https://docs.openclaw.ai
  Support communauté       : https://communaute-ia.fr
──────────────────────────────────────────────────────────────
SUITE

ok "Terminé. 🦀"
