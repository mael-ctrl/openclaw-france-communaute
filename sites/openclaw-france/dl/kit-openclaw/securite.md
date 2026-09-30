# 🛡️ Checklist sécurité — OpenClaw

**Kit OpenClaw France — 100 % gratuit · [communaute-ia.fr](https://communaute-ia.fr)**

---

OpenClaw est un assistant qui a accès à votre machine et à vos comptes : la sécurité
n'est pas un extra, c'est le mode d'emploi. Bonne nouvelle : quelques réglages
suffisent, et tout ce qui suit vient de la **documentation officielle de sécurité
d'OpenClaw** ([docs.openclaw.ai/gateway/security](https://docs.openclaw.ai/gateway/security)).

**Comment l'utiliser :** parcourez les 12 points à votre installation, puis refaites
un tour une fois par mois (5 minutes). Chaque point est une case à cocher.

---

## Les 12 points

### 1. ☐ Tenir OpenClaw et le système à jour

Les failles connues sont corrigées dans les mises à jour. Appliquez-les vite.

```bash
openclaw update                  # mise à jour d'OpenClaw (voir mise-a-jour.sh)
sudo apt update && sudo apt upgrade -y    # mises à jour du serveur (Linux)
```

### 2. ☐ Utiliser un jeton d'accès fort (et rien d'autre)

Le tableau de bord et la passerelle sont protégés par un **jeton**. L'assistant en
génère un ; sinon créez-le vous-même et gardez-le secret :

```bash
openssl rand -hex 32             # génère un jeton solide → à coller dans .env
```

- Jamais le jeton d'exemple de la documentation (il est refusé, et c'est normal).
- Au moins 24 caractères (un avertissement s'affiche en dessous).
- S'il a pu fuiter : régénérez-le et vérifiez que l'ancien ne fonctionne plus.

### 3. ☐ Garder la passerelle en local (loopback)

Par défaut, OpenClaw n'écoute que sur la machine elle-même (`loopback`, port `18789`).
C'est **le réglage le plus sûr** — gardez-le, et accédez au tableau de bord par
tunnel SSH ou Tailscale (voir le GUIDE.md, « Accéder au tableau de bord »).

- ✅ Bien : `gateway.bind` vaut `"loopback"` (valeur par défaut).
- ⚠️ Si vous devez écouter sur le réseau (`lan`/`tailnet`) : jeton obligatoire **et**
  pare-feu strict (points 4 et 5).

### 4. ☐ Activer le pare-feu du serveur (ufw)

Sur un VPS, n'ouvrez que le strict nécessaire — jamais le port d'OpenClaw :

```bash
sudo apt install -y ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp     # SSH (indispensable pour administrer)
sudo ufw allow 80/tcp     # HTTP  (redirection vers HTTPS / certificats)
sudo ufw allow 443/tcp    # HTTPS (si vous exposez un reverse proxy)
sudo ufw enable
sudo ufw status verbose   # vérifiez : que 22, 80 et 443 (ouvertes)
```

### 5. ☐ Docker : ajouter la protection « DOCKER-USER »

Si vous utilisez Docker, les ports publiés contournent les règles ufw classiques.
La doc officielle fournit le bloc à ajouter dans `/etc/ufw/after.rules` :

```bash
# /etc/ufw/after.rules  (à ajouter tel quel, puis : sudo ufw reload)
*filter
:DOCKER-USER - [0:0]
-A DOCKER-USER -m conntrack --ctstate ESTABLISHED,RELATED -j RETURN
-A DOCKER-USER -s 127.0.0.0/8 -j RETURN
-A DOCKER-USER -s 10.0.0.0/8 -j RETURN
-A DOCKER-USER -s 172.16.0.0/12 -j RETURN
-A DOCKER-USER -s 192.168.0.0/16 -j RETURN
-A DOCKER-USER -s 100.64.0.0/10 -j RETURN
-A DOCKER-USER -p tcp --dport 80 -j RETURN
-A DOCKER-USER -p tcp --dport 443 -j RETURN
-A DOCKER-USER -m conntrack --ctstate NEW -j DROP
-A DOCKER-USER -j RETURN
COMMIT
```

Vérifiez ensuite de l'extérieur que rien d'autre n'est visible :

```bash
nmap -sT -p 1-65535 <votre-ip-publique> --open
# Attendu : uniquement SSH + les ports de votre reverse proxy (80/443).
```

### 6. ☐ SSH : clés uniquement, mot de passe désactivé

*Bonne pratique générale (pas spécifique à OpenClaw) mais indispensable sur un VPS.*

- Connectez-vous par **clé SSH**, pas par mot de passe.
- Dans `/etc/ssh/sshd_config` : `PasswordAuthentication no` puis
  `sudo systemctl restart ssh`.
- Optionnel : `fail2ban` pour bloquer les tentatives répétées.

### 7. ☐ HTTPS via reverse proxy : uniquement avec les précautions officielles

La doc officielle préfère le tunnel SSH ou Tailscale (point 3). Si vous exposez
quand même le tableau de bord derrière un domaine HTTPS (voir GUIDE.md) :

- La passerelle garde un **jeton obligatoire** (point 2) ;
- Le proxy est le **seul** chemin d'accès (port 18789 fermé au public) ;
- Vous déclarez le proxy dans la configuration — **uniquement son adresse** :

```json5
{
  gateway: {
    trustedProxies: ["172.17.0.1"],          // IP du proxy (127.0.0.1 si natif ; 172.17.0.1 si Docker)
    controlUi: { allowedOrigins: ["https://votre-domaine.fr"] }
  }
}
```

- Le proxy doit **écraser** les en-têtes de transfert (sinon un visiteur peut
  usurper son adresse) ;
- Jamais d'exposition sur `0.0.0.0` sans authentification. Si un avertissement de
  sécurité apparaît au démarrage ou dans les journaux, lisez-le avant de continuer.

### 8. ☐ Couper la découverte Bonjour/mDNS sur un serveur

Sur un VPS, la découverte locale diffuse des informations sur votre installation.

```bash
# Dans l'environnement d'OpenClaw (ou ~/.openclaw/openclaw.json) :
OPENCLAW_DISABLE_BONJOUR=1
# Équivalent en configuration :  discovery: { mdns: { mode: "minimal" } }
```

### 9. ☐ Protéger vos secrets

- `.env` : jamais publié, jamais sur GitHub — `chmod 600 .env` ;
- le jeton du tableau de bord ne se partage pas (même à un « ami ») ;
- les **sauvegardes contiennent des identifiants** : rangez-les dans un endroit
  sûr, et chiffrez si vous les copiez chez un hébergeur externe ;
- en cas de doute : générez de nouveaux secrets et remplacez les anciens.

### 10. ☐ Verrouiller les messageries connectées

Chaque messagerie branchée (Telegram, Discord…) est une porte d'entrée.

- Messages privés : mode **appairage** ou liste d'autorisation, jamais « ouvert à tous » ;
- dans les groupes : exiger une **mention** (ou liste stricte) avant que l'agent réponde ;
- si plusieurs personnes écrivent au bot, activer `session.dmScope: "per-channel-peer"`
  (chaque conversation reste isolée des autres).

### 11. ☐ Lancer l'audit de sécurité officiel

OpenClaw embarque un contrôle automatique — faites-le parler :

```bash
openclaw security audit            # bilan complet
openclaw security audit --deep     # encore plus détaillé
# En Docker : docker compose run --rm openclaw-cli security audit --deep
```

Corrigez d'abord les points **critiques**. Les avertissements restants : soit vous
les corrigez, soit vous notez pourquoi ils sont volontaires.

### 12. ☐ Tester les sauvegardes et préparer le retour arrière

Une sauvegarde jamais testée n'est pas une sauvegarde.

```bash
bash scripts/sauvegarde.sh         # sauvegarde vérifiée (script du kit)
# puis copiez le dossier « sauvegardes/ » ailleurs (disque, cloud privé).
```

Restaurer après un incident est une procédure volontairement manuelle et documentée :
[docs.openclaw.ai/install/backups](https://docs.openclaw.ai/install/backups)
(section « Restore »).

**En cas de doute (compte peut-être exposé) :** repassez la passerelle en `loopback`,
coupez les canaux, arrêtez le proxy, changez le jeton, puis relancez l'audit (point 11).

---

## Routine express — 5 minutes par mois

1. ☐ `openclaw update` puis `openclaw --version` (à jour ?)
2. ☐ `openclaw security audit` (des points critiques ? corrigés ?)
3. ☐ `sudo ufw status` (toujours aussi fermé ?)
4. ☐ Sauvegarde récente ? copiée ailleurs ? (point 12)

---

## Pour aller plus loin (doc officielle)

- Guide sécurité complet : [docs.openclaw.ai/gateway/security](https://docs.openclaw.ai/gateway/security)
- Checklist d'exposition (avant d'ouvrir un accès) : [docs.openclaw.ai/gateway/security/exposure-runbook](https://docs.openclaw.ai/gateway/security/exposure-runbook)
- Exposition réseau (bind, pare-feu, reverse proxy) : [docs.openclaw.ai/gateway/security/network-exposure](https://docs.openclaw.ai/gateway/security/network-exposure)
- Secrets et stockage : [docs.openclaw.ai/gateway/security/secrets-and-storage](https://docs.openclaw.ai/gateway/security/secrets-and-storage)

**Une question ?** Le support communautaire vit sur
[communaute-ia.fr](https://communaute-ia.fr) — et le code source du kit sur
[GitHub (mael-ctrl/openclaw-france-communaute)](https://github.com/mael-ctrl/openclaw-france-communaute).
