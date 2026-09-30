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

## ✅ Ce qu'il vous faut

- Une **machine à vous** (macOS ou Linux ; Windows fonctionne aussi via la
  méthode officielle — voir la doc) **ou** un petit **VPS** Linux (~5-10 €/mois).
- Un **accès à un modèle d'IA** : une clé API chez un fournisseur, ou une
  connexion existante (Claude Code / Codex) que l'assistant peut réutiliser.
- 30 minutes de calme. C'est tout.

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
