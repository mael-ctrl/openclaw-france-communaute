# 📦 Kit d'installation OpenClaw — 100 % gratuit

**Installez OpenClaw proprement, en français, même sans être technique.**

Ce kit vous accompagne pas-à-pas pour installer **OpenClaw** — l'assistant
personnel open source qui vit sur votre machine ou votre serveur, et que vous
pilotez depuis un tableau de bord ou vos messageries. Prévoyez environ
**30 minutes**, un terminal, et de quoi suivre des étapes numérotées.

> ℹ️ **À savoir.** Ce kit est un travail **communautaire** (projet OpenClaw
> France, distribué via [openclaw-france.fr](https://openclaw-france.fr)).
> OpenClaw lui-même est un logiciel **open source et indépendant** : sa
> référence officielle est [openclaw.ai](https://openclaw.ai) et sa
> documentation [docs.openclaw.ai](https://docs.openclaw.ai). En cas de doute,
> la doc officielle fait foi — c'est elle que nous avons suivie pour écrire
> ce kit.

---

## 📂 Contenu du kit

| Fichier | Rôle |
| --- | --- |
| **GUIDE.md** | Le guide pas-à-pas principal : prérequis, installation, accès sécurisé, sauvegardes, mises à jour, dépannage. **Commencez ici.** |
| **docker-compose.yml** | Démarrage d'OpenClaw en Docker (option containers), adapté du fichier officiel. |
| **.env.example** | Modèle de configuration à copier en `.env` (jeton, réglages, clés IA). |
| **scripts/install.sh** | Installation en une commande via l'installateur **officiel** (Linux/macOS). |
| **scripts/sauvegarde.sh** | Sauvegarde vérifiée + purge automatique (prêt pour cron). |
| **scripts/mise-a-jour.sh** | Mise à jour en sécurité : sauvegarde → mise à jour → vérifications. |
| **securite.md** | La checklist sécurité en 12 points (pare-feu, HTTPS, secrets…). |
| **README.md** | Ce fichier : vue d'ensemble et démarrage express. |

---

## ✅ Ce qu’il vous faut — avant de lancer les scripts

- **macOS ou Linux, Bash et curl** pour `scripts/install.sh`. Sur un VPS,
  travaillez sur le serveur via **SSH**, avec un compte dédié.
- Pour le chemin classique, **Node.js 24.16+ dans la branche 24 ou 26.1+ dans
  la branche 26** ; vérifiez `node -v` s’il est déjà installé. L’installateur
  officiel peut le provisionner s’il manque.
- **Windows** : méthode officielle native (PowerShell / Windows Hub) ou **WSL2**.
  Dans WSL2, les commandes Bash se lancent dans le terminal Linux,
  **pas dans PowerShell**. Le kit ne fournit pas d’installateur PowerShell.
- **Docker reste une option** : Docker Engine ou Desktop, **Docker Compose v2**,
  moteur démarré et espace disque. Les **6 Go** indiqués par la documentation
  concernent la **construction locale depuis les sources** ; le kit utilise
  une image officielle **préconstruite**. Ce n’est pas une garantie de mémoire
  suffisante à l’exécution : les outils et les autres services changent les besoins.
- Un accès à un **modèle IA** compatible. Le modèle et l’**hébergement** peuvent
  être **payants**, contrairement au kit. Vérifiez les conditions et quotas ;
  fixez un **plafond de dépense**. Un abonnement à une application ne garantit
  pas un accès à son API.

Prérequis relus le **2026-10-15**, d’après les sources officielles liées dans
[GUIDE.md](GUIDE.md). C’est une vérification documentaire, **pas une installation testée**
sur chaque plateforme. Lisez la section 1 du guide avant toute exécution.

---

## 🚀 Démarrage express

### 1. Lisez le guide

Tout est expliqué dans **GUIDE.md** : il vous laisse choisir entre deux chemins
(machine personnelle ou serveur, installateur officiel ou Docker).

### 2. Le chemin classique (le plus simple, recommandé)

Sur votre ordinateur **ou** votre serveur, dans le dossier du kit :

```bash
bash scripts/install.sh
```

Le script vérifie vos prérequis, utilise l'installateur officiel, puis vous
indique les commandes suivantes (`openclaw onboard`, `openclaw gateway status`,
`openclaw dashboard`…).

### 3. Le chemin Docker (pour isoler OpenClaw sur un serveur)

Dans le dossier du kit :

```bash
cp .env.example .env      # puis générez et collez votre jeton : openssl rand -hex 32
chmod 600 .env
mkdir -p donnees/etat donnees/secrets-auth sauvegardes
sudo chown -R 1000:1000 donnees sauvegardes   # Linux uniquement
docker compose pull
docker compose up -d openclaw-gateway
```

La suite (assistant de configuration, tableau de bord) est détaillée dans le
**GUIDE.md**.

### 4. Après l'installation

```bash
bash scripts/sauvegarde.sh        # une première sauvegarde tout de suite
# puis programmez-la tous les jours (voir GUIDE.md, section « Sauvegardes »)
bash scripts/mise-a-jour.sh       # pour mettre à jour en toute sécurité
```

Et parcourez **securite.md** : 12 points, 5 minutes, et vous dormez tranquille.

---

## 🔗 Liens utiles

- **Documentation officielle OpenClaw** : <https://docs.openclaw.ai>
- **Support communautaire (La Communauté)** : <https://communaute-ia.fr>
- **Code source de ce kit et du site** :
  <https://github.com/mael-ctrl/openclaw-france-communaute>
- **Site du kit** : <https://openclaw-france.fr/openclaw/>

---

## ⚖️ Honnêteté et limites

- Ce kit est **gratuit, sans compte, sans carte bancaire** — et le restera.
- Il ne fait que **faciliter** l'installation officielle : aucun composant
  modifié, aucun code caché. Les scripts sont courts, commentés en français et
  lisibles : ouvrez-les dans un éditeur de texte pour vérifier par vous-même.
- Il est fourni « tel quel », sans garantie : vous restez maître de votre
  machine et de vos données. En cas de doute sur une commande, la
  [documentation officielle](https://docs.openclaw.ai) tranche toujours.

🦀 Bonne installation, et bienvenue dans la communauté !
