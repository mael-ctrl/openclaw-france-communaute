# Guide d'installation OpenClaw — pas-à-pas, en français

**Kit OpenClaw France — 100 % gratuit.**
Support communautaire : [communaute-ia.fr](https://communaute-ia.fr) · Code source du kit :
[GitHub — mael-ctrl/openclaw-france-communaute](https://github.com/mael-ctrl/openclaw-france-communaute)

Ce guide vous emmène de « je n'ai rien installé » à « mon assistant tourne, il est
sécurisé, sauvegardé, et je sais le mettre à jour ». Comptez environ **30 minutes**.

Deux principes avant de commencer :

1. **On suit la documentation officielle.** OpenClaw est un logiciel open source
   indépendant ; sa référence est [docs.openclaw.ai](https://docs.openclaw.ai).
   Chaque commande de ce guide vient de là. En cas de doute, la doc officielle tranche.
2. **On ne devine pas.** Si une information n'a pas pu être vérifiée dans la doc
   officielle, elle est marquée **[À VÉRIFIER]** — vous ne lisez pas d'invention.

---

## 1. Ce dont vous avez besoin (prérequis)

OpenClaw tourne « chez vous » : soit sur **votre ordinateur**, soit sur un
**petit serveur loué** (un « VPS »). Pour un assistant disponible 24 h/24, branché
à vos messageries, le VPS est le choix habituel — mais on peut commencer sur un
ordinateur et déménager plus tard.

**Option A — votre ordinateur (macOS ou Linux).**
Rien de particulier à préparer : l'installateur officiel installe lui-même ce qui
manque (Node.js, etc.). Sous Windows, la doc officielle propose une méthode
PowerShell dédiée et une application de bureau ; ce guide-ci vise macOS/Linux.

**Option B — un VPS Ubuntu/Debian (~5–10 €/mois).**
Prenez une petite formule : 2 Go de RAM est le minimum constaté en pratique pour
un usage tranquille — **[À VÉRIFIER]** (la documentation officielle ne publie pas
de minimum matériel formel ; en cas de doute, prenez 4 Go). Vous recevez de votre
hébergeur une adresse IP et un accès SSH. Le kit fonctionne avec n'importe quel
hébergeur.

**Dans les deux cas, il vous faut un accès à un modèle d'IA :** une clé API chez
un fournisseur (OpenAI, Anthropic, Gemini, OpenRouter…), ou une connexion
existante Claude Code / Codex CLI que l'assistant peut réutiliser tout seul.
Les clés API sont en général facturées à l'usage par le fournisseur — c'est le
seul coût possible, OpenClaw lui-même étant gratuit.

---

## 2. Étape 1 — Installer OpenClaw (méthode officielle)

La méthode recommandée par la documentation officielle est l'**installateur
officiel** : il détecte votre système, installe Node.js si nécessaire, installe
OpenClaw, et lance l'assistant de configuration.

### 2.1 Lancer l'installation

Depuis le dossier du kit, la commande la plus simple est notre script, qui
enveloppe l'installateur officiel avec des vérifications et des messages en
français :

```bash
bash scripts/install.sh
```

Vous préférez la commande brute officielle ? C'est celle-ci (elles font la même
chose) :

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

> 💡 Si vous gérez déjà Node.js vous-même, la doc officielle propose aussi :
> `npm install -g openclaw@latest --allow-scripts=openclaw` puis
> `openclaw onboard --install-daemon`.

### 2.2 L'assistant de configuration (« onboarding »)

L'installateur ouvre un assistant. Choisissez **« Quick start »** : il cherche
une connexion IA déjà présente sur la machine ou une clé, la vérifie, puis ouvre
le tableau de bord. Si rien n'est trouvé, il vous guide pour saisir une clé de
fournisseur. Vous pourrez tout régler plus tard avec `openclaw configure`.

### 2.3 Installer le service en arrière-plan

Pendant l'assistant, la passerelle tourne dans le terminal qui l'a lancée. Pour
qu'elle tourne en permanence (et redémarre toute seule), arrêtez d'abord la
passerelle du premier plan avec **Ctrl+C** *(votre configuration est conservée)*,
puis installez le service :

```bash
openclaw gateway install
```

Sur un VPS Linux, pour que le service survive à votre déconnexion SSH :

```bash
sudo loginctl enable-linger $USER
```

*(L'installateur officiel tente de l'activer pour vous ; si le service ne
redémarre pas après déconnexion, la commande ci-dessus est celle de la doc.)*

### 2.4 Vérifier

```bash
openclaw --version        # la commande existe ?
openclaw doctor           # un contrôle de configuration
openclaw gateway status   # doit indiquer la passerelle à l'écoute sur le port 18789
openclaw dashboard        # ouvre le tableau de bord dans votre navigateur
```

Écrivez un message dans le tableau de bord : si l'IA répond, **c'est gagné. 🎉**
Toutes les commandes `openclaw …` se lancent normalement, sans `sudo`.

---

## 3. Étape 2 (option) — Installer avec Docker

Docker est une **option** dans la documentation officielle (utile pour isoler
OpenClaw sur un serveur, ou si vous connaissez déjà Docker). L'installation
classique de l'étape 1 reste le chemin recommandé. Le kit fournit un
`docker-compose.yml` prêt à l'emploi.

### 3.1 Préparer le serveur

1. **Docker Engine + Docker Compose v2** — installez-les par la méthode officielle
   de Docker (<https://docs.docker.com/engine/install/>), puis autorisez votre
   utilisateur : `sudo usermod -aG docker $USER` et re-connectez-vous.
2. **Copier le kit sur le serveur** depuis votre ordinateur :
   `scp -r kit-openclaw utilisateur@votre-serveur:/home/utilisateur/`
   (ou téléchargez le kit directement sur le serveur depuis openclaw-france.fr).

### 3.2 Préparer la configuration

```bash
cd kit-openclaw
cp .env.example .env
openssl rand -hex 32        # copiez la valeur générée…
nano .env                   # …collez-la dans OPENCLAW_GATEWAY_TOKEN, enregistrez (Ctrl+O, Entrée, Ctrl+X)
chmod 600 .env              # protège vos secrets
```

Ce jeton est la clé du tableau de bord : il ne se partage jamais.

### 3.3 Préparer les dossiers de données

Le conteneur tourne avec l'utilisateur interne `node` (identifiant 1000) — la
doc officielle recommande donc de préparer les dossiers ainsi :

```bash
mkdir -p donnees/etat donnees/secrets-auth sauvegardes
sudo chown -R 1000:1000 donnees sauvegardes
```

### 3.4 Premier lancement : l'assistant de configuration

```bash
docker compose pull
docker compose run --rm --no-deps --entrypoint node openclaw-gateway \
  dist/index.js onboard --mode local --no-install-daemon
```

Répondez aux questions comme à l'étape 2.2 (valeurs déjà présentes dans `.env`
réutilisées automatiquement).

### 3.5 Démarrer la passerelle

```bash
docker compose up -d openclaw-gateway
docker compose ps                          # « healthy » après quelques dizaines de secondes
curl -fsS http://127.0.0.1:18789/healthz   # doit répondre (test de vie, sans jeton)
```

### 3.6 Ouvrir le tableau de bord

```bash
docker compose run --rm openclaw-cli dashboard --no-open
```

L'URL s'affiche : ouvrez-la et collez le jeton (celui de `.env`). Les commandes
du quotidien passent par `docker compose run --rm openclaw-cli <commande>`
(voir la doc : [docs.openclaw.ai/install/docker](https://docs.openclaw.ai/install/docker)).

---

## 4. Étape 3 — Accéder au tableau de bord en toute sécurité

**Retenez ceci :** le tableau de bord d'OpenClaw n'est pas conçu pour être exposé
directement à Internet. La doc officielle classe les accès du plus sûr au plus
risqué ; voici les trois options, dans cet ordre.

### Option A — Tunnel SSH (recommandé, le plus simple)

Gardez la passerelle en local, et faites passer votre navigateur « à l'intérieur »
du serveur :

```bash
ssh -L 18789:127.0.0.1:18789 utilisateur@votre-serveur
# laissez ce terminal ouvert, puis ouvrez http://127.0.0.1:18789 dans votre navigateur
```

Aucun port ouvert vers l'extérieur, aucun certificat à gérer. C'est la méthode
préférée de la doc officielle.

### Option B — Tailscale (réseau privé entre vos appareils)

Tailscale crée un réseau privé : installez-le sur le serveur et sur votre
ordinateur, activez « Serve », puis accédez à la passerelle par son nom
Tailscale. Détails officiels : [docs.openclaw.ai/gateway/tailscale](https://docs.openclaw.ai/gateway/tailscale).

### Option C — Reverse proxy HTTPS (domaine public) — pour les plus avancés

À réserver au cas où vous avez vraiment besoin d'une URL publique
(`https://claw.mondomaine.fr`). La doc officielle la classe comme déploiement
« rare et à haut risque » : faites d'abord la checklist `securite.md` (points 4–5).

1. **Pare-feu** : seuls 22, 80 et 443 ouverts vers l'extérieur (le port 18789 du
   tableau de bord ne doit **jamais** être public).
2. **Installez Caddy** (certificat HTTPS automatique — voir
   <https://caddyserver.com/docs/install>) et créez un `Caddyfile` :

   ```
   votre-domaine.fr {
       reverse_proxy 127.0.0.1:18789 {
           header_up X-Forwarded-For {remote_host}
           header_up X-Real-IP {remote_host}
       }
   }
   ```

   Ces deux lignes **écrasent** les en-têtes de transfert : c'est exigé par la
   doc officielle (sinon un visiteur peut se faire passer pour une autre adresse).
   *(Variante nginx : utilisez `proxy_set_header X-Forwarded-For $remote_addr;`
   et `proxy_set_header X-Real-IP $remote_addr;` — les mêmes lignes que la doc.)*
3. **Déclarez le proxy dans OpenClaw.** Ajoutez à votre configuration
   (`openclaw configure`, ou le fichier `openclaw.json`) :

   ```json5
   {
     gateway: {
       trustedProxies: ["172.17.0.1"],   // l'adresse du proxy vu par OpenClaw
       controlUi: { allowedOrigins: ["https://votre-domaine.fr"] }
     }
   }
   ```

   Remplacez `172.17.0.1` par l'adresse de votre proxy : `127.0.0.1` si OpenClaw
   est installé normalement, l'adresse du pont Docker (souvent `172.17.0.1`,
   parfois `172.18.0.1`…) si OpenClaw tourne dans Docker. En cas de difficulté,
   le message d'aide du tableau de bord (`trustedProxies`) vous met sur la voie.
   Puis redémarrez : `openclaw gateway restart` (ou `docker compose restart openclaw-gateway`).
4. **Testez depuis l'extérieur** : le site répond en HTTPS, votre jeton ouvre le
   tableau de bord, et le port 18789 est injoignable de l'extérieur.

Si tout cela vous semble trop technique : restez aux options A ou B. C'est le
choix recommandé — et vous ne perdez rien.

---

## 5. Étape 4 — Sauvegardes automatiques (cron)

Une sauvegarde permet de tout restaurer après une erreur, une mise à jour ratée
ou un serveur perdu. Elle contient l'état, la configuration, les identifiants et
les espaces de travail. **Règle d'or officielle : jamais de copie « à chaud » des
fichiers `.sqlite`** — il faut passer par la commande de sauvegarde dédiée (c'est
ce que fait notre script).

**Test immédiat** (dans le dossier du kit) :

```bash
bash scripts/sauvegarde.sh
ls -lh sauvegardes/          # une archive .tar.gz vérifiée doit apparaître
```

**Programmation automatique** — tous les jours à 3 h 30 :

```bash
crontab -e
# puis ajoutez cette ligne (remplacez le chemin par le vôtre) :
30 3 * * * /chemin/vers/kit-openclaw/scripts/sauvegarde.sh >> /chemin/vers/kit-openclaw/sauvegardes/journal.log 2>&1
```

*(nano s'ouvre : collez la ligne à la fin, puis Ctrl+O, Entrée, Ctrl+X.)*

Le script conserve 14 jours de sauvegardes par défaut (`RETENTION_JOURS` en tête
du fichier pour changer), et la doc officielle propose aussi un planificateur
intégré (`openclaw backup enable`, avec ses options : voir
[docs.openclaw.ai/install/backups](https://docs.openclaw.ai/install/backups)).

**Deux réflexes en plus :**

- Une sauvegarde vit ailleurs : copiez de temps en temps le dossier `sauvegardes/`
  sur un disque externe ou un stockage cloud privé.
- Les archives contiennent des secrets : traitez-les comme vos mots de passe.

**Restauration (en cas de pépin)** — elle est volontairement manuelle, en deux
temps (vérifier/extraction, puis activation), tout est documenté :
`openclaw backup restore archive.tar.gz --target ./restauration` puis suivez
[docs.openclaw.ai/install/backups](https://docs.openclaw.ai/install/backups).

---

## 6. Étape 5 — Mises à jour

Une mise à jour, c'est : sauvegarde → mise à jour → vérifications. Notre script
fait les trois d'un coup :

```bash
bash scripts/mise-a-jour.sh
```

Manuellement, la commande officielle est `openclaw update`, suivie de
`openclaw doctor` et `openclaw health` pour vérifier. En Docker :
`docker compose pull && docker compose up -d openclaw-gateway`
(l'image officielle lance elle-même ses contrôles au redémarrage).

- La doc officielle recommande de **sauvegarder avant toute mise à jour
  importante** — le script le fait pour vous.
- Si votre installation date de plusieurs mois, la doc indique un passage
  intermédiaire (« version pont » 2026.9.5) : voir
  [docs.openclaw.ai/install/updating](https://docs.openclaw.ai/install/updating).
- OpenClaw sait aussi se mettre à jour tout seul ; les nouveautés sont listées
  dans les notes de version officielles.

---

## 7. Dépannage de base

Quatre commandes officielles à connaître :

```bash
openclaw doctor            # diagnostic de la configuration
openclaw triage            # diagnostic complet, et résumé exploitable si vous demandez de l'aide
openclaw gateway status    # la passerelle tourne-t-elle ?
openclaw logs --follow     # journaux en direct (Ctrl+C pour quitter)
```

Le message `openclaw triage` ne quitte **pas** votre machine sans votre accord :
secrets, jetons et journaux bruts en sont exclus.

**Les soucis les plus fréquents :**

| Symptôme | À essayer |
| --- | --- |
| `openclaw: command not found` | Ouvrez un nouveau terminal ; vérifiez `node -v`, `npm prefix -g`, `echo $PATH` (doc officielle : « Node.js troubleshooting »). |
| La passerelle ne tourne pas | `openclaw gateway install` puis `openclaw gateway restart`. En Docker : `docker compose up -d openclaw-gateway` puis `docker compose logs -f openclaw-gateway`. |
| Node.js trop ancien | Relancez l'installateur officiel : il met Node à jour (`bash scripts/install.sh`). |
| Le port 18789 est occupé | Changez `OPENCLAW_GATEWAY_PORT` dans `.env` (Docker) ou `gateway.port` dans la configuration. |
| Docker : erreurs de permission (EACCES) | `sudo chown -R 1000:1000 donnees sauvegardes` (la doc officielle prévoit exactement ce cas). |
| Le tableau de bord refuse la connexion | Vérifiez le jeton (celui de `.env`). En Docker : `docker compose run --rm openclaw-cli devices list` puis `devices approve <id>` (doc officielle). |
| L'IA ne répond pas | Vérifiez la clé du fournisseur dans `.env` / `openclaw configure`, puis `openclaw doctor`. |

Toujours bloqué ? `openclaw triage` prépare un résumé propre, et la communauté
est là (section 9). Ne forcez pas des commandes au hasard sur un serveur.

---

## 8. Et maintenant ?

- **Branchez une messagerie.** Le plus simple : Telegram (un simple jeton de bot) —
  voir [docs.openclaw.ai/channels](https://docs.openclaw.ai/channels).
- **Renforcez la sécurité.** Parcourez `securite.md` (12 points, 5 minutes) et
  lancez `openclaw security audit`.
- **Explorez.** Outils, tâches planifiées, navigateur, mémoire… la doc officielle
  est riche : [docs.openclaw.ai](https://docs.openclaw.ai).

---

## 9. Besoin d'aide ?

- **Support communautaire (français)** : <https://communaute-ia.fr>
- **Code source du kit et retours** : <https://github.com/mael-ctrl/openclaw-france-communaute>
- **Documentation officielle OpenClaw** : <https://docs.openclaw.ai>

Dernier mot d'honnêteté : ce kit est communautaire et gratuit. Il vous simplifie
l'installation officielle, rien de plus — et c'est déjà beaucoup. Si une
information de ce guide divergeait un jour de la documentation officielle,
c'est la documentation officielle qui fait foi.

🦀 Bonne installation !
