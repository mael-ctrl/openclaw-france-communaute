# Kit Hermes Agent — installation en français (gratuit)

Bienvenue ! Ce kit vous accompagne pour installer et prendre en main
**Hermes Agent**, l'agent IA open source de **[Nous Research](https://github.com/NousResearch/hermes-agent)**,
sur **macOS ou Linux** — avec des explications en français, pas à pas.

> **Ce kit est communautaire.** Il n'est pas édité par Nous Research.
> Toutes les commandes qu'il contient proviennent de la
> [documentation officielle](https://hermes-agent.nousresearch.com/docs), qui reste
> la source de vérité. En cas de doute, c'est elle qui fait foi.

---

## C'est quoi Hermes Agent ?

Un agent IA qui vit dans votre terminal (et en application desktop) : il lit et
écrit des fichiers, exécute des commandes, navigue le web, se souvient de vos
préférences entre les sessions et s'étend avec des **skills** — des procédures
réutilisables qu'il charge à la demande. Il fonctionne avec de nombreux
fournisseurs de modèles (DeepSeek, OpenRouter, Anthropic, OpenAI, Google…) ou
**100 % en local, sans compte ni clé API**. Licence MIT : le logiciel est gratuit,
vous ne payez que l'usage éventuel d'un modèle en ligne.

## Contenu du kit

```
kit-hermes/
├── README.md            ← vous êtes ici : vue d'ensemble
├── GUIDE.md             ← le guide principal (installation → premiers usages)
├── scripts/install.sh   ← script d'installation macOS / Linux (méthode officielle)
├── config-exemple.yaml  ← exemple de configuration, commenté (référence)
└── demarrage.md         ← premiers pas + 10 usages concrets
```

## Prérequis — à lire avant le script

- **Bash** sur macOS, Linux ou WSL2 : le script du kit ne se lance pas dans PowerShell.
  Sur Windows natif, utilisez la
  [méthode officielle Windows](https://hermes-agent.nousresearch.com/docs/getting-started/installation#windows-native)
  hors de ce kit, ou passez par WSL2.
- **macOS Apple Silicon** ; **Linux / WSL2 x86_64 ou arm64** (aarch64).
  Les tests Ubuntu/WSL2 cités par Nous Research ne couvrent pas chaque distribution.
- **Mac Intel : compatibilité non garantie.** Au 2026-10-16, les sources officielles
  divergent : le guide d’installation dit « non pris en charge », la matrice décrit
  encore la CLI et des bundles Intel conditionnels. Le message du script sur Intel
  ne valide pas votre machine ; lisez la réserve détaillée dans `GUIDE.md`.
- **Git, curl, tar et un utilitaire SHA-256**. Python et Node.js sont gérés par
  l’installateur, mais un compilateur et des bibliothèques système peuvent aussi
  être nécessaires. Certains paquets Linux demandent un administrateur ; les
  vérifications du kit ne garantissent pas toutes ces dépendances.
- Un modèle adapté : fournisseur ou serveur local, appel d’outils et contexte
  requis à vérifier dans `GUIDE.md`. Modèle IA, outils externes et hébergement
  peuvent être payants : vérifiez les conditions et fixez un plafond de dépenses.

Sources consultées le **2026-10-16** :
[installation et prérequis](https://hermes-agent.nousresearch.com/docs/getting-started/installation#prerequisites)
et [matrice des plateformes](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support).
C’est un contrôle documentaire, pas une installation testée sur chaque système.

## Démarrage rapide

1. **Lisez `GUIDE.md`** — tout le parcours y est expliqué (comptez ~15 minutes).
2. **Après lecture des prérequis et du guide**, lancez le script depuis le dossier du kit :

   ```bash
   bash scripts/install.sh
   ```

   Il vérifie vos prérequis puis exécute l'installateur **officiel** de
   Nous Research (celui de la documentation). Options possibles :
   `bash scripts/install.sh --help`.
3. **Branchez un modèle** (votre clé API, ou un modèle local gratuit) :

   ```bash
   hermes setup      # assistant complet — recommandé la première fois
   hermes model      # ou : choix du fournisseur et du modèle
   ```
4. **Lancez votre première session** : `hermes` — puis suivez `demarrage.md`
   pour dix usages concrets immédiatement utiles.

## Ce que ce kit n'est pas

- Ce n'est **pas** un installateur « maison » : c'est un habillage français
  autour de la procédure officielle.
- N'installez pas Hermes via `pip`, `brew` ou l'AUR : ces méthodes ne sont
  **pas supportées** par la documentation officielle.

## Crédits et liens officiels

- **Hermes Agent** — développé par **Nous Research** (licence MIT)
  · [Dépôt GitHub](https://github.com/NousResearch/hermes-agent)
  · [Documentation officielle](https://hermes-agent.nousresearch.com/docs)
  · [Site du projet](https://hermes-agent.nousresearch.com/)
- Discord de la communauté Nous Research : <https://discord.gg/nousresearch>

## Support communautaire francophone

Une question, un blocage ? Passez par la communauté :
**<https://communaute-ia.fr>** — et le contact du site :
contact@openclaw-france.fr.

---

*Kit offert par OpenClaw France. Distribué gratuitement, sans compte ni carte
bancaire. Si la documentation officielle évolue, elle prévaut sur ce kit ;
ouvrez une issue ou écrivez-nous, on mettra le kit à jour.*
