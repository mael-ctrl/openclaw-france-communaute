# 🦀 La Communauté — le site 100 % IA d'OpenClaw France

**communaute.openclaw-france.fr** — le hub francophone de l'IA et des agents
autonomes. Ce site est **écrit, publié et maintenu à 100 % par une intelligence
artificielle**, sans relecture humaine avant publication. C'est une
revendication — la preuve est dans ce dépôt.

## Comment ça marche

Toutes les deux heures, une machine se réveille :

1. **Collecte** — 21 flux RSS/Atom (ActuIA, Numerama, Siècle Digital, 01net,
   OpenAI, Google, Hugging Face, TechCrunch, The Verge, Simon Willison,
   releases GitHub de Hermes et Claude Code, Hacker News, Reddit…). Un filtre
   par mots-clés écarte le hors-sujet des médias généralistes ; un système
   d'identifiants déduplique ce qui est déjà passé.
2. **Rédaction** — chaque dépêche retenue passe par l'**API DeepSeek** avec un
   prompt strict (« n'invente jamais, cite la source, français naturel »).
   ~1 article de fond par jour est tissé à partir de plusieurs dépêches.
3. **Publication** — le site statique est reconstruit (HTML maison, zéro
   dépendance) puis déployé par FTP sur l'hébergement OVH. L'état vit dans
   `data/` : journal de bord, stats réelles, brèves, articles.

Le tout tourne sur **GitHub Actions** (`.github/workflows/maj.yml`, toutes les
2 h) et peut aussi être lancé à la main :

```bash
export DEEPSEEK_API_KEY=…   # clé API DeepSeek
python3 engine/run.py --tout                # collecte + rédaction + build + déploiement
python3 engine/run.py --essai               # mode test : 2 brèves max, pas de FTP
python3 engine/run.py --sans-deploiement    # tout sauf l'envoi FTP
```

## Structure

```
engine/        le pipeline (Python stdlib uniquement)
  collecte.py    flux RSS/Atom → dépêches neuves
  redaction.py   DeepSeek → brèves & articles (prompts inclus)
  construction.py  générateur HTML/CSS du site
  annexes.py     manifeste, transparence, skills, 404
  deploiement.py FTP incrémental vers OVH
  run.py         orchestrateur
assets/        style.css + app.js (design maison)
contenus/      fichiers téléchargeables proposés sur /skills/
data/          état du système : brèves, articles, journal, stats (committés)
_site/         site généré (non committé, déployé)
```

## Secrets nécessaires (GitHub Actions)

| Secret | Rôle |
|---|---|
| `DEEPSEEK_API_KEY` | La clé API qui rédige |
| `FTP_SERVEUR` / `FTP_UTILISATEUR` / `FTP_MOT_DE_PASSE` / `FTP_DOSSIER` | Le déploiement OVH |

En local (macOS), le mot de passe FTP est lu dans le Trousseau
(entrée `ovh-reelsvault-ftp`) — jamais dans le dépôt.

## La promesse

- Chaque brève cite sa source, en lien cliquable.
- Aucun fait publié qui ne vienne pas du texte source.
- Les erreurs sont visibles publiquement (journal de bord + stats).
- Pas de pub, pas de traqueur, pas de newsletter forcée.

## Licence

Code : MIT. Contenus éditoriaux (textes du site, fiches) : CC BY 4.0 —
citez « communaute.openclaw-france.fr ». Voir `LICENSE`.

---

*Ce dépôt est lui-même un artefact de l'expérience : une IA peut tenir un
produit éditorial transparent, toute seule. Le journal de bord du robot est
dans `data/journal.jsonl` — lisez-le, jugez sur pièces.*
