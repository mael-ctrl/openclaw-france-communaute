#!/usr/bin/env bash
# =============================================================================
# Kit Hermes Agent (OpenClaw France) — installateur macOS / Linux / WSL2
# -----------------------------------------------------------------------------
# Ce script ne fait qu'une chose : vérifier vos prérequis, puis lancer
# l'INSTALLATEUR OFFICIEL de Hermes Agent (Nous Research), tel que documenté sur
#   https://hermes-agent.nousresearch.com/docs/getting-started/installation
#
# La méthode officielle est :
#   curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
# Ici, nous le téléchargeons d'abord dans un dossier temporaire (pour pouvoir
# transmettre proprement des options), puis nous l'exécutons tel quel.
#
# IMPORTANT : aucun secret (clé API, jeton) n'est demandé ni stocké par ce
# script. Les clés API se configureront ensuite avec « hermes setup » ou
# « hermes model », jamais dans ce fichier.
#
# Usage :
#   bash scripts/install.sh                  # installation standard (interactive)
#   bash scripts/install.sh --skip-browser   # exemple d'option transmise
#   bash scripts/install.sh --help
#
# Options documentées de l'installateur officiel, que vous pouvez transmettre :
#   --skip-browser        ne pas installer les outils navigateur
#   --skip-computer-use   ne pas installer le pilote « computer use »
#   --non-interactive     sauter les étapes qui demandent une saisie
#   --verbose             afficher tous les détails de chaque étape
#   --include-desktop     construire aussi l'app desktop depuis les sources
#
# Pour désinstaller / mettre à jour plus tard : « hermes update », puis
# « hermes uninstall --dry-run » — voir le GUIDE.md inclus dans ce kit.
# =============================================================================

set -euo pipefail

readonly OFFICIAL_INSTALL_URL="https://hermes-agent.nousresearch.com/install.sh"
readonly DOCS_URL="https://hermes-agent.nousresearch.com/docs/getting-started/installation"

# --- Affichage (français, sobre) ---------------------------------------------
if [ -t 1 ]; then
  C_BLEU=$'\033[1;34m'; C_VERT=$'\033[1;32m'; C_JAUNE=$'\033[1;33m'; C_ROUGE=$'\033[1;31m'; C_FIN=$'\033[0m'
else
  C_BLEU=""; C_VERT=""; C_JAUNE=""; C_ROUGE=""; C_FIN=""
fi
info() { printf '%s▸%s %s\n' "$C_BLEU" "$C_FIN" "$*"; }
ok()   { printf '%s✓%s %s\n' "$C_VERT" "$C_FIN" "$*"; }
warn() { printf '%s!%s %s\n' "$C_JAUNE" "$C_FIN" "$*"; }
fail() { printf '%s✗%s %s\n' "$C_ROUGE" "$C_FIN" "$*" >&2; }

usage() {
  cat <<'EOT'
Kit Hermes Agent — installateur (macOS / Linux / WSL2)

Usage :
  bash scripts/install.sh [options]

Déroulé :
  1. vérifie que votre système et vos prérequis sont bons
     (Git, curl, tar et un utilitaire SHA-256 — requis par la doc officielle) ;
  2. télécharge l'installateur officiel de Nous Research depuis
     https://hermes-agent.nousresearch.com/install.sh ;
  3. l'exécute. Toutes les options que vous ajoutez lui sont transmises
     telles quelles (ex. : --skip-browser, --skip-computer-use,
     --non-interactive, --verbose, --include-desktop).

Ce script ne demande et ne stocke aucun secret. Les clés API se configurent
après l'installation, avec « hermes setup » ou « hermes model ».

Documentation officielle :
  https://hermes-agent.nousresearch.com/docs/getting-started/installation

Support communautaire francophone : https://communaute-ia.fr
EOT
}

# Aide demandée ? On répond avant toute vérification.
case "${1:-}" in
  -h|--help) usage; exit 0 ;;
esac

echo
info "Kit Hermes Agent — vérification de votre machine…"

# --- 1. Sécurité de base : pas de root ----------------------------------------
if [ "$(id -u)" -eq 0 ]; then
  fail "Ne lancez pas ce script en root ou avec sudo."
  info "D'après la FAQ officielle, l'installateur s'installe dans ~/.local/bin et ne doit pas être exécuté avec sudo."
  info "Relancez-le avec votre compte utilisateur normal."
  exit 1
fi

# --- 2. Système supporté ------------------------------------------------------
systeme="$(uname -s)"
machine="$(uname -m)"

case "$systeme" in
  Darwin)
    if [ "$machine" = "arm64" ]; then
      ok "macOS détecté (Apple Silicon) — plateforme Tier 1 de la doc officielle."
    else
      warn "macOS Intel détecté ($machine)."
      info "L'installeur graphique Hermes-Setup.dmg est réservé aux Mac Apple Silicon ; sur Intel, la doc officielle prévoit le bundle darwin-x64 ou l'installation CLI (celle-ci, justement)."
    fi
    ;;
  Linux)
    if grep -qi "microsoft" /proc/version 2>/dev/null; then
      ok "Linux sous WSL2 détecté (Windows) — plateforme Tier 1 de la doc officielle."
    else
      ok "Linux détecté ($machine)."
      info "La doc officielle recommande un système avec glibc, systemd et l'arborescence standard (testé sur Ubuntu récent)."
    fi
    ;;
  *)
    fail "Système non pris en charge par ce script : $systeme"
    info "La doc officielle couvre macOS, Linux, WSL2 et Windows. Voir : $DOCS_URL"
    exit 1
    ;;
esac

# --- 3. Prérequis (doc officielle : Git, curl, tar, utilitaires SHA-256) -------
manquants=()
for outil in curl git tar; do
  if ! command -v "$outil" >/dev/null 2>&1; then
    manquants+=("$outil")
  fi
done
if ! command -v shasum >/dev/null 2>&1 && ! command -v sha256sum >/dev/null 2>&1; then
  manquants+=("shasum ou sha256sum")
fi

if [ "${#manquants[@]}" -gt 0 ]; then
  fail "Prérequis manquants : ${manquants[*]}"
  info "La doc officielle demande : Git, curl, tar et un utilitaire SHA-256."
  info "Installez-les avec le gestionnaire de paquets de votre distribution (apt, dnf, pacman selon le cas), puis relancez ce script."
  info "Sur macOS, ces outils viennent avec les outils de développement Apple (la fenêtre d'installation proposée par macOS quand un outil manque)."
  exit 1
fi
ok "Prérequis en place : curl, git, tar et un utilitaire SHA-256."

# --- 4. Terminal interactif ? --------------------------------------------------
if [ ! -t 0 ]; then
  warn "L'entrée standard n'est pas un terminal interactif."
  info "L'installateur officiel lance normalement un assistant de configuration à la fin. Pour en profiter, préférez lancer ce script directement dans votre terminal."
fi

# --- 5. Téléchargement de l'installateur officiel ------------------------------
tmp_dir="$(mktemp -d)"
trap 'rm -rf "$tmp_dir"' EXIT

info "Téléchargement de l'installateur officiel : $OFFICIAL_INSTALL_URL"
if ! curl -fsSL "$OFFICIAL_INSTALL_URL" -o "$tmp_dir/install-officiel.sh"; then
  fail "Le téléchargement a échoué. Vérifiez votre connexion internet, puis réessayez."
  exit 1
fi
if ! head -n 1 "$tmp_dir/install-officiel.sh" | grep -qE '^#!'; then
  fail "Le fichier téléchargé ne ressemble pas à un script shell — arrêt par prudence."
  info "Réessayez plus tard ou installez manuellement : voir $DOCS_URL"
  exit 1
fi
ok "Installateur officiel téléchargé et vérifié (en-tête de script valide)."

# --- 6. Lancement de l'installateur officiel -----------------------------------
echo
info "Lancement de l'installateur officiel de Hermes Agent (Nous Research)…"
info "C'est lui qui fait tout le travail : sources, dépendances, lanceur, configuration initiale."
echo

if ! bash "$tmp_dir/install-officiel.sh" "$@"; then
  fail "L'installateur officiel s'est arrêté sur une erreur."
  info "Son journal détaillé se trouve dans logs/install.log, sous le dossier de données Hermes (~/.hermes)."
  info "En cas de doute : $DOCS_URL"
  exit 1
fi

# --- 7. Et maintenant ? ---------------------------------------------------------
echo
ok "Installation terminée par l'installateur officiel."
echo
info "Prochaines étapes :"
cat <<'EOT'
  1) Rechargez votre shell :
       source ~/.zshrc     (macOS / zsh — le cas par défaut)
       source ~/.bashrc    (bash)
     …ou ouvrez simplement un nouveau terminal.

  2) Vérifiez que tout est sain :
       hermes doctor

  3) Branchez un fournisseur de modèle (votre clé API), au choix :
       hermes setup        (assistant complet)
       hermes model        (choix du fournisseur et du modèle)

  4) Lancez votre première session :
       hermes

  Guides : GUIDE.md et demarrage.md, inclus dans ce kit.
  Documentation officielle : https://hermes-agent.nousresearch.com/docs
  Support communautaire : https://communaute-ia.fr
EOT
echo
ok "Bonne route avec Hermes Agent !"
