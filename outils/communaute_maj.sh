#!/bin/bash
# 🦀 Mise à jour locale du site La Communauté (appelé par le cron Hermes).
# Récupère l'état distant, exécute le pipeline, republie l'état dans le dépôt.
# Dépôt de travail = CLONE dédié hors Bureau (~/.hermes/workspaces/communaute) : les
# contextes de scripts (process démon) ne peuvent PAS lire les fichiers du Bureau
# (deadlock FileProvider → lectures vides / « not a git repository », vécu 30/09→03/10).
# Ne pas repointer vers ~/Desktop sans re-tester depuis un run cron réel.
set -uo pipefail

# PATH minimal garanti pour les contextes cron/launchd (gh, git, python)
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"
REPO="$HOME/.hermes/workspaces/communaute"
cd "$REPO" || { echo "dépôt introuvable: $REPO"; exit 1; }

# Canaris de lisibilité : sans eux, tout « passe » silencieusement (lectures vides)
git rev-parse --verify HEAD >/dev/null 2>&1 || { echo "⚠ dépôt illisible depuis ce contexte (git)"; exit 1; }
[ -s engine/run.py ] || { echo "⚠ lecture vide de engine/run.py — abandon"; exit 1; }

# Préflight du 28 réemployé, aussi relu après synchronisation.
preflight() {
for operation in rebase-merge rebase-apply MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD sequencer; do
  chemin=$(git rev-parse --git-path "$operation") || exit "$?"
  if [ -e "$chemin" ]; then
    echo "[i] préflight refusé : opération Git en cours ($operation)" >&2
    exit 65
  fi
done
non_fusionne=$(git ls-files --unmerged) || exit "$?"
if [ -n "$non_fusionne" ]; then
  echo "[i] préflight refusé : index non fusionné" >&2
  exit 65
fi

etat=$(GIT_OPTIONAL_LOCKS=0 git status --porcelain --untracked-files=all) || exit "$?"
if [ -n "$etat" ]; then
  echo "[i] préflight refusé : dépôt sale avant pull (index, worktree ou fichiers non suivis)" >&2
  exit 65
fi

branche=$(git symbolic-ref --quiet HEAD) || { rc=$?; [ "$rc" -ne 1 ] && exit "$rc"; echo "[i] HEAD détaché refusé" >&2; exit 65; }
[ "$branche" = refs/heads/main ] || { echo "[i] branche autre que main refusée" >&2; exit 65; }
suivi_remote=$(git config --get-all branch.main.remote) || exit "$?"
suivi_ref=$(git config --get-all branch.main.merge) || exit "$?"
if [ "$suivi_remote" != origin ] || [ "$suivi_ref" != refs/heads/main ]; then
  echo "[i] suivi autre que origin/main refusé" >&2
  exit 65
fi
}
preflight

# Refuser tout commit local non contenu dans la pointe distante récupérée.
git fetch --no-tags -q origin refs/heads/main || exit "$?"
distant=$(git rev-parse --verify "FETCH_HEAD^{commit}") || exit "$?"
git merge-base --is-ancestor HEAD "$distant"
rc=$?
if [ "$rc" -eq 1 ]; then
  echo "[i] synchronisation refusée : avance locale ou divergence" >&2
  exit 65
elif [ "$rc" -ne 0 ]; then
  exit "$rc"
fi

PY="/usr/local/bin/python3"
[ -x "$PY" ] || PY="$(command -v python3 || true)"
[ -n "$PY" ] || { echo "python3 introuvable"; exit 1; }
# Récupérer uniquement par avance rapide, sans réparation automatique.
pull=$(git pull --ff-only --no-rebase --no-autostash --no-tags -q origin refs/heads/main 2>&1) || { rc=$?; echo "[i] pull impossible : $(echo "$pull" | tail -1)"; exit "$rc"; }
# Observation supplémentaire : refus si origin/main a changé depuis le fetch.
annonce=$(git ls-remote --exit-code origin refs/heads/main) || exit "$?"
if [ "$annonce" != "$distant"$'\trefs/heads/main' ]; then
  echo "[i] synchronisation refusée : pointe distante modifiée" >&2
  exit 65
fi
local_head=$(git rev-parse --verify HEAD) || exit "$?"
[ "$local_head" = "$distant" ] || { echo "[i] HEAD différent de la pointe récupérée" >&2; exit 65; }
preflight
# Pas un verrou : un écrivain peut encore agir après ces observations.
DEEPSEEK_API_KEY=$({ grep -E '^DEEPSEEK_API_KEY=' "$HOME/.hermes/.env" | head -1 | cut -d= -f2- | tr -d '"' | sed "s/'//g"; } 2>/dev/null) || { rc=$?; echo "[i] lecture de clé impossible" >&2; exit "$rc"; }
[ -n "$DEEPSEEK_API_KEY" ] || { echo "[i] clé vide refusée" >&2; exit 65; }
export DEEPSEEK_API_KEY

echo "🦀 Run local $(date '+%Y-%m-%d %H:%M')"
"$PY" engine/run.py 2>&1 | tail -25 || exit "$?"

# Republier l'état (journal, brèves, stats) — c'est notre transparence publique
git add data || exit "$?"
git diff --quiet --cached
rc=$?
if [ "$rc" -eq 1 ]; then
  git commit -q -m "MAJ locale — $(date '+%Y-%m-%d %H:%M %Z')" || { rc=$?; echo "[i] commit impossible"; exit "$rc"; }
  # Aucun second pull : ne pas fusionner le commit produit avec du nouveau code.
  git fetch --no-tags -q origin refs/heads/main || exit "$?"
  avant_push=$(git rev-parse --verify "FETCH_HEAD^{commit}") || exit "$?"
  [ "$avant_push" = "$distant" ] || { echo "[i] republication refusée : remote modifié; commit local conservé" >&2; exit 65; }
  sortie=$(git push -q origin HEAD:refs/heads/main 2>&1)
  rc=$?
  if [ $rc -ne 0 ]; then
    echo "[i] republication impossible (rc=$rc) : $(echo "$sortie" | tail -1) — commit local conservé, inspection requise"
    exit "$rc"
  fi
elif [ "$rc" -ne 0 ]; then
  exit "$rc"
fi
