#!/usr/bin/env bash
# =============================================================================
#  Kit OpenClaw France — scripts/sauvegarde.sh                  (version 1.0)
# -----------------------------------------------------------------------------
#  Rôle : sauvegarder l'état complet d'OpenClaw (état, configuration,
#  identifiants, agents, espaces de travail) avec la commande OFFICIELLE
#  « openclaw backup create », puis supprimer les sauvegardes trop
#  anciennes selon la rétention choisie.
#
#  Pourquoi c'est important : une sauvegarde permet de tout restaurer après
#  une erreur de manipulation, une mise à jour ratée ou un serveur perdu.
#  La documentation officielle insiste : ne recopiez JAMAIS les fichiers
#  .sqlite à chaud — utilisez « openclaw backup » (c'est ce que fait ce script).
#
#  Utilisation manuelle :
#      bash scripts/sauvegarde.sh
#
#  Automatisation — ajoutez cette ligne avec « crontab -e » (tous les jours
#  à 3h30 du matin) :
#      30 3 * * * /chemin/vers/kit-openclaw/scripts/sauvegarde.sh >> /chemin/vers/kit-openclaw/sauvegardes/journal.log 2>&1
#
#  Doc officielle : https://docs.openclaw.ai/install/backups
#  Support communauté : https://communaute-ia.fr
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# Variables — tout se règle ici, en haut du fichier.
# -----------------------------------------------------------------------------
RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"   # dossier du kit
MODE="${MODE:-auto}"                     # auto | classique | docker
DOSSIER_BACKUPS="${DOSSIER_BACKUPS:-}"   # vide = dossier automatique selon la méthode
RETENTION_JOURS="${RETENTION_JOURS:-14}" # nombre de jours de sauvegardes conservées

# Si OpenClaw ou Node sont installés hors des chemins standards, ajoutez leur
# dossier ci-dessous : cron ne reprend PAS votre environnement de connexion.
PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:$PATH"
export PATH

# -----------------------------------------------------------------------------
# Petites fonctions d'affichage
# -----------------------------------------------------------------------------
info()   { printf 'ℹ️  %s\n' "$*"; }
ok()     { printf '✅ %s\n' "$*"; }
avis()   { printf '⚠️  %s\n' "$*"; }
erreur() { printf '❌ %s\n' "$*" >&2; }

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
# Sauvegarde (méthode officielle dans les deux cas)
# -----------------------------------------------------------------------------
sauvegarder() {
  case "$MODE" in
    classique)
      if [ -z "$DOSSIER_BACKUPS" ]; then
        DOSSIER_BACKUPS="$HOME/Backups/openclaw"
      fi
      mkdir -p "$DOSSIER_BACKUPS"
      info "Sauvegarde en cours → $DOSSIER_BACKUPS"
      openclaw backup create --output "$DOSSIER_BACKUPS" --verify
      ;;
    docker)
      if [ -n "$DOSSIER_BACKUPS" ] && [ "$DOSSIER_BACKUPS" != "$RACINE/sauvegardes" ]; then
        avis "En mode Docker, le dossier de destination est fixé par docker-compose.yml"
        avis "(./sauvegardes). Pour le changer, modifiez le montage"
        avis "« ./sauvegardes:/home/node/sauvegardes » puis relancez ce script."
      fi
      DOSSIER_BACKUPS="$RACINE/sauvegardes"
      mkdir -p "$DOSSIER_BACKUPS"
      info "Sauvegarde en cours (conteneur openclaw-cli) → ./sauvegardes"
      ( cd "$RACINE" && docker compose run -T --rm openclaw-cli \
          backup create --output /home/node/sauvegardes --verify )
      ;;
  esac
}

# -----------------------------------------------------------------------------
# Purge des sauvegardes plus vieilles que la rétention choisie
# -----------------------------------------------------------------------------
purger() {
  if [ ! -d "$DOSSIER_BACKUPS" ]; then
    return 0
  fi
  info "Purge des sauvegardes de plus de $RETENTION_JOURS jours…"
  trouvees="$(find "$DOSSIER_BACKUPS" -maxdepth 1 -type f \
    -name '*openclaw-backup.tar.gz' -mtime +"$RETENTION_JOURS" 2>/dev/null || true)"
  if [ -z "$trouvees" ]; then
    ok "Rien à purger."
  else
    printf '%s\n' "$trouvees" | while IFS= read -r fichier; do
      rm -f -- "$fichier"
      info "Supprimée : $(basename "$fichier")"
    done
  fi
}

# -----------------------------------------------------------------------------
# Exécution
# -----------------------------------------------------------------------------
detecter_mode
info "Méthode détectée : $MODE"

sauvegarder
purger

echo
ok "Sauvegarde terminée."
if [ -d "$DOSSIER_BACKUPS" ]; then
  info "Dossier : $DOSSIER_BACKUPS"
  info "Dernières sauvegardes :"
  ls -lht "$DOSSIER_BACKUPS" 2>/dev/null | grep 'openclaw-backup' | head -n 3 || true
fi
cat <<'RAPPEL'

Rappels utiles :
  • Les sauvegardes contiennent des secrets (jetons, identifiants) → conservez-les en lieu sûr.
  • Copiez régulièrement ce dossier ailleurs (disque externe, stockage cloud privé).
  • Restauration : voir la section « Sauvegardes » du GUIDE.md.

RAPPEL
