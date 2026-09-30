# Guide complet — Installer et utiliser Hermes Agent (macOS / Linux)

Ce guide vous emmène de zéro à un agent IA fonctionnel sur votre machine :
installation, branchement d'un modèle, première session, skills et astuces.
Comptez une quinzaine de minutes pour la mise en route.

**Toutes les commandes citées proviennent de la [documentation officielle](https://hermes-agent.nousresearch.com/docs)**
(méthode exacte de la doc, traduite et remise en ordre). En cas d'écart entre ce guide et la doc, la doc fait foi.

---

## 1. Hermes Agent, en bref

Hermes Agent est l'**agent IA open source de Nous Research** (licence MIT). Ce n'est pas
un simple chatbot : il agit. Il lit et écrit des fichiers, exécute des commandes dans
un terminal, navigue le web, analyse des images, et enchaîne les étapes d'une tâche
tout seul grâce à ses outils.

Ce qui le distingue :

- **Les skills** — des procédures réutilisables (déployer, rédiger une PR, analyser un
  document…) qu'il charge à la demande et que vous pouvez lui faire créer.
- **La mémoire persistante** — il retient vos préférences et votre contexte d'une
  session à l'autre.
- **Tous les fournisseurs de modèles** — DeepSeek, OpenRouter, Anthropic, OpenAI,
  Google… ou 100 % en local sur votre machine.
- **Plusieurs surfaces** — le terminal (CLI et TUI), une application desktop, un
  tableau de bord web, et même un « gateway » multi-plateformes (Telegram, Discord,
  Slack…).
- **Votre vie privée** — pas de télémétrie ; conversations, mémoire et skills restent
  dans `~/.hermes/`. Seuls les appels au fournisseur que vous configurez sortent de
  votre machine (et avec un modèle local, rien ne sort du tout).

**Combien ça coûte ?** Le logiciel est gratuit (open source). Vous ne payez que l'usage
du modèle que vous branchez — et les modèles locaux sont 100 % gratuits.

## 2. Avant de commencer

**Systèmes supportés** (selon la doc officielle) :

- **macOS Apple Silicon** (M1 et suivants) — plateforme Tier 1.
- **Mac Intel** : fonctionne aussi via l'installation en ligne de commande
  (celle de ce guide) ou le bundle `darwin-x64` ; l'installeur graphique `.dmg`
  est réservé aux puces Apple Silicon.
- **Linux et WSL2** (x86_64 ou arm64) — testé sur Ubuntu récent.
- Windows natif existe (PowerShell) mais ce kit vise macOS et Linux.

**Prérequis logiciels** : Git, curl, tar et un utilitaire SHA-256. C'est tout — vous
n'avez **pas** besoin d'installer Python ou Node.js : l'installateur fournit son
propre environnement isolé.

**Prérequis pour le modèle** : soit une clé API chez un fournisseur (DeepSeek,
OpenRouter…), soit un modèle local via Ollama (prévoir 8 Go de RAM pour un petit
modèle, 32 Go ou plus pour les plus gros). Dans tous les cas, un modèle avec au
moins 64 000 tokens de contexte est requis par Hermes.

## 3. Étape 1 — Installer Hermes Agent

### Méthode A — Application desktop (macOS)

Téléchargez le paquet depuis le [site officiel](https://hermes-agent.nousresearch.com/),
ouvrez le fichier `.dmg` et glissez `Hermes.app` dans Applications. Vous obtenez le
CLI **et** l'interface graphique. Si vous avez déjà installé la version terminal,
l'app desktop s'ajoute à tout moment avec :

```bash
hermes desktop
```

### Méthode B — Terminal (macOS, Linux, WSL2) — la méthode principale de ce kit

La commande officielle, telle qu'elle figure dans la documentation :

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Le script de ce kit fait exactement la même chose, avec des vérifications en plus
(système supporté, prérequis, pas de root) et des messages en français :

```bash
bash scripts/install.sh
```

Ce que fait l'installateur (résumé de la doc) : il récupère les sources, met en
place un Python dédié et les outils nécessaires (Node, npm, ripgrep, FFmpeg), crée
le lanceur `~/.local/bin/hermes`, prépare le dossier de données `~/.hermes/`, et — si vous êtes
dans un terminal interactif — lance l'assistant de configuration. Un journal détaillé
est écrit dans `logs/install.log` sous `~/.hermes/`.

Options utiles qui existent réellement (documentées) : `--skip-browser`,
`--skip-computer-use`, `--non-interactive`, `--verbose`, `--include-desktop`.

⚠️ **Trois pièges à éviter** :
1. **Ne lancez jamais l'installateur avec `sudo` ou en root.** Il installe dans votre
   dossier utilisateur (`~/.local/bin`), pas au niveau système.
2. N'installez pas Hermes via `pip`, `brew` ou l'AUR : ces méthodes ne sont pas
   supportées par la doc officielle.
3. Ne copiez pas de clé API dans les fichiers du kit — voyez l'étape 2.

### Vérifier l'installation

Rechargez votre shell, puis faites un bilan de santé :

```bash
source ~/.zshrc      # ou : source ~/.bashrc
hermes doctor
```

`hermes doctor` vous dit précisément ce qui manque, s'il manque quelque chose.

## 4. Étape 2 — Brancher un fournisseur de modèle

C'est l'étape la plus importante. Le plus simple est l'assistant :

```bash
hermes setup
```

Il propose trois modes : **Quick Setup (Nous Portal)** — un abonnement couvre
300+ modèles, sans gérer de clés ; **Full Setup** — vous apportez votre propre clé
parmi tous les fournisseurs ; **Blank Slate** — un agent minimal, tout le reste
désactivé (pour les utilisateurs avancés). Vous pouvez aussi viser directement le
choix du modèle :

```bash
hermes model
```

Quelques fournisseurs populaires et leurs variables de clé (documentés) :

| Fournisseur | Variable | Où obtenir une clé |
|---|---|---|
| **DeepSeek** | `DEEPSEEK_API_KEY` | site de DeepSeek |
| **OpenRouter** | `OPENROUTER_API_KEY` | openrouter.ai |
| **Anthropic** | `ANTHROPIC_API_KEY` | console Anthropic |
| **Google AI Studio** | `GOOGLE_API_KEY` ou `GEMINI_API_KEY` | Google AI Studio |
| **xAI (Grok)** | `XAI_API_KEY` | console xAI |

Pour enregistrer une clé proprement, la doc donne cette commande :

```bash
hermes config set OPENROUTER_API_KEY sk-or-...
```

Le même principe vaut pour les autres (par exemple `DEEPSEEK_API_KEY`). **Règle d'or
issue de la doc** : Hermes range automatiquement les secrets dans `~/.hermes/.env`
(jamais dans `config.yaml`) et les réglages dans `~/.hermes/config.yaml`. Utilisez
donc `hermes config set` plutôt que d'éditer des fichiers à la main.

### L'option 100 % gratuite : un modèle local

Si vous voulez essayer sans dépenser un centime, Hermes sait piloter un modèle qui
tourne sur votre machine via [Ollama](https://ollama.com/). La doc officielle décrit
ce flux :

```bash
# 1. Installez Ollama (ligne de commande donnée par le guide officiel Hermes)
curl -fsSL https://ollama.com/install.sh | sh

# 2. Téléchargez un modèle (choisissez selon votre RAM)
ollama pull qwen3.5:27b
```

Puis branchez-le dans Hermes (`hermes model` → **Custom endpoint**) ou en config :

```yaml
model:
  default: "qwen3.5:27b"
  provider: "custom"
  base_url: "http://localhost:11434/v1"
```

Deux conseils du guide officiel : choisissez un modèle qui **sait appeler des
outils** (c'est ce qui permet à l'agent d'agir, pas seulement de discuter), et montez
son contexte à 64 000 tokens minimum. Comptez 8 Go de RAM pour un petit modèle et
32 Go pour les gros (27B+). Appels, fichiers, commandes : tout reste chez vous.

## 5. Étape 3 — Votre première session

```bash
hermes            # interface classique
hermes --tui      # interface moderne (recommandée)
```

Vous verrez une bannière avec votre modèle, vos outils et vos skills. Lancez-vous
avec une demande précise et vérifiable, par exemple :

- « Résume ce dossier en 5 points et dis-moi quel fichier semble être le point d'entrée. »
- « Quelle est l'utilisation de mon disque ? Montre-moi le top 5 des dossiers les plus lourds. »
- « Aide-moi à mettre en place un workflow Git propre pour ce projet. »

**Ça marche si** : la bannière affiche votre modèle, Hermes répond sans erreur, il
utilise un outil (terminal, lecture de fichier…), et la conversation continue
normalement. Si c'est le cas, vous avez passé le plus dur.

Repères pendant la session :

| Action | Comment |
|---|---|
| Toutes les commandes | tapez `/help` |
| Changer de modèle | `/model` |
| Voir votre consommation | `/usage` |
| Compresser une longue session | `/compress` |
| Interrompre / rediriger l'agent | `Ctrl+C`, ou tapez un nouveau message |
| Saut de ligne (sans envoyer) | `Alt+Entrée` ou `Ctrl+J` |
| Coller une capture d'écran | `Ctrl+V` |
| Autocomplétion des commandes | tapez `/` puis `Tab` |

**Sessions** : `hermes -c` (ou `hermes --continue`) reprend la dernière session,
`hermes -r "titre"` reprend une session nommée (donnez-lui un nom avec `/title`),
et `hermes sessions list` liste tout.

## 6. Les skills, expliqués simplement

Une **skill** est un document d'instruction que l'agent charge **uniquement quand il
en a besoin** : une procédure pas-à-pas pour une tâche précise. Hermes en embarque un
catalogue dès l'installation (dans `~/.hermes/skills/`) et en télécharge d'autres à
la demande.

**Le principe malin** : chaque skill installée devient une **commande slash**.
Exemples issus de la doc : `/github-pr-workflow créer une PR`, `/gif-search des
GIFs de chats drôles`, ou juste `/excalidraw` pour charger la skill et laisser
l'agent vous demander ce que vous voulez. Vous pouvez même en enchaîner plusieurs :

```bash
/github-pr-workflow /test-driven-development corrige l'issue #123 et ouvre une PR
```

**Explorer et installer d'autres skills** (un scan de sécurité est fait avant
l'installation) :

```bash
hermes skills browse                  # tout le catalogue
hermes skills search kubernetes       # recherche par mot-clé
hermes skills install openai/skills/k8s
```

**Créer les vôtres** — c'est là que ça devient puissant. La commande `/learn` part
de n'importe quelle matière :

```bash
/learn comment je viens de déployer le serveur de staging
/learn https://docs.exemple.fr/api/quickstart
/learn mes notes sur la facturation : ouvrir le portail, Nouveau > Facture, joindre le justificatif, envoyer
```

L'agent rédige la skill, et elle devient disponible partout. Vous pouvez aussi lui
dire simplement : « sauvegarde ce que tu viens de faire en skill `deploy-staging` » —
et la prochaine fois, `/deploy-staging` suffit.

## 7. Astuces qui changent tout

- **Soyez précis.** « Corrige le TypeError dans `api/handlers.py` ligne 47 » vaut
  mieux que « corrige le code ». Collez vos messages d'erreur tels quels.
- **Utilisez `AGENTS.md`.** Un fichier `AGENTS.md` à la racine d'un projet
  (conventions, architecture, « on utilise pytest »…) est lu automatiquement à chaque
  session. Pour la personnalité globale de l'agent, la doc prévoit `~/.hermes/SOUL.md`.
- **Mémoire ou skill ?** La mémoire retient des **faits** (« je préfère les réponses
  courtes »), les skills des **procédures**. Dites-lui « retiens ça pour la prochaine
  fois » après une session utile.
- **Surveillez les coûts.** `/usage` en cours de route, et `/compress` quand une
  session devient longue. Évitez de changer de modèle sans arrêt dans une même
  longue session (ça « casse » le cache du fournisseur et ça coûte plus cher).
- **Déléguez le travail parallèle.** Demandez-lui de traiter plusieurs recherches en
  parallèle via des sous-agents : chaque sous-agent travaille dans son coin et ne
  renvoie qu'un résumé.
- **Sécurité d'abord.** Hermes demande votre approbation avant les commandes
  dangereuses (`rm -rf`, etc.) : préférez « une fois » ou « session » à « toujours ».
  Pour bidouiller du code que vous ne connaissez pas, passez les commandes en
  sandbox : `hermes config set terminal.backend docker`.
- **Bots : mettez une liste d'accès.** Si vous connectez Telegram ou Discord, la doc
  recommande des allowlists (`TELEGRAM_ALLOWED_USERS`, `DISCORD_ALLOWED_USERS`) et
  déconseille fortement `GATEWAY_ALLOW_ALL_USERS=true` pour un bot qui a accès au
  terminal.
- **MCP** : Hermes peut se connecter à des serveurs d'outils externes (MCP). Le
  principe et des exemples de configuration sont sur la page
  [MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) de la doc.

## 8. Dépannage express

Les problèmes les plus fréquents et leurs solutions (d'après la doc officielle) :

| Symptôme | Solution |
|---|---|
| `hermes: command not found` | Rechargez le shell (`source ~/.zshrc` ou `source ~/.bashrc`) ou ouvrez un nouveau terminal. Sinon : `export PATH="$HOME/.local/bin:$PATH"` |
| « API key not set » | `hermes model` pour configurer le fournisseur |
| Config incomplète après une mise à jour | `hermes config check` puis `hermes config migrate` |
| Réponses vides / cassées | Relancez `hermes model` et vérifiez fournisseur, modèle et clé |
| Un doute, quelque chose cloche | `hermes doctor` — il dit exactement quoi corriger |

Séquence de secours complète recommandée par la doc : `hermes doctor` → `hermes model`
→ `hermes setup` → `hermes sessions list` → `hermes --continue` →
`hermes gateway status`.

Besoin d'aide ? La [FAQ officielle](https://hermes-agent.nousresearch.com/docs/reference/faq)
et le [Discord de Nous Research](https://discord.gg/nousresearch) — et pour le français,
la communauté : <https://communaute-ia.fr>.

## 9. Mettre à jour, désinstaller

```bash
hermes update        # mise à jour de l'installation (sources)
hermes --version     # vérifier la version installée
```

L'app desktop se met à jour elle-même (bouton de mise à jour). Pour une installation
Docker, on tire simplement une nouvelle image ; sur le paquet Termux :
`pkg upgrade hermes-agent`.

Pour désinstaller, la doc fournit :

```bash
hermes uninstall --dry-run    # d'abord, pour voir ce qui sera supprimé
hermes uninstall              # désinstalle (les données peuvent être conservées)
```

`--full` supprime aussi vos données utilisateur ; en cas de doute, faites d'abord une
sauvegarde (`hermes backup` — l'archive complète inclut vos identifiants, à garder
en lieu sûr).

## 10. Pour aller plus loin

- **`demarrage.md`** (inclus dans ce kit) : dix usages concrets pour vos premiers jours.
- **Documentation officielle** : <https://hermes-agent.nousresearch.com/docs> —
  dont le [CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli), les
  [providers](https://hermes-agent.nousresearch.com/docs/integrations/providers),
  le [système de skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
  et la [messagerie](https://hermes-agent.nousresearch.com/docs/user-guide/messaging).
- **Dépôt GitHub** : <https://github.com/NousResearch/hermes-agent>.

---

**Crédits.** Hermes Agent est un projet de **Nous Research**, publié sous licence MIT.
Ce guide est un travail communautaire francophone (OpenClaw France) : il reformule la
documentation officielle sans la remplacer. Merci à Nous Research, et bon voyage avec
votre agent.
