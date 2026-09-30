# Hub `openclaw-france.fr` — architecture et exploitation

Depuis le 30/09/2026, `openclaw-france.fr` (et `www`) est **servi par notre
hébergement OVH `communo`** (cluster131), et non plus par un projet Cloudflare
Pages externe. Objectif : maîtrise totale (« gérer les hébergements comme il se
doit ») tout en **préservant le tunnel de vente du pack 97 €** (lien Qonto).

## Architecture

- **Sources du site** — `sites/openclaw-france/` (miroir assaini de l'ancien
  site + bandeau « La Communauté » + lien de pied + favicon 🦀 + og-image).
- **Déploiement** — `python3 outils/deployer_openclaw.py` (FTP `communo`,
  dossier `openclaw-france/` à la racine ; identité au Trousseau
  `ovh-communo-ftp`).
- **DNS (Cloudflare, zone `885b27260792f05b29d664a9d98ffb07`)** — CNAME `@` et
  `www` → `communo.cluster131.hosting.ovh.net`, **proxied** (l'edge CF fournit
  le TLS ; l'attachement OVH est en `ssl:false` — pas de cert OVH nécessaire).
- **Routage multi-sites OVH** — domaines attachés à l'hébergement `communo`
  avec le dossier `openclaw-france` comme racine web (`attachedDomain`).

## Contenu conservé (ne pas casser)

- Lien de paiement Qonto (×3 sur l'accueil) :
  `https://pay.qonto.com/payment-links/019c4c00-b1b2-7847-ba80-91e2598a7cff?resource_id=019c4c00-b1b3-73a7-84f9-403ba548683a`
- Téléphone `+33 7 45 88 68 20` (lien `tel:` réparé — il était cassé `tel:+337****6820`).
- Pages : `/`, `/temoignages`, `/cgv`, `/politique-de-confidentialite`,
  `/mentions-legales` (URLs sans slash → 301 vers `/…/` : normal côté OVH).

## Retouches appliquées au miroir

1. E-mails obfusqués Cloudflare décodés en clair (XOR premier octet) ;
   script `email-decode` retiré.
2. Téléphone `tel:` réparé ; favicon remplacé par `static/favicon.svg` 🦀 ;
   og-image créée `static/og-image.png` (1200×630).
3. Bandeau (accueil) + lien « La Communauté 🦀 » (pied de toutes les pages)
   → `https://communaute-ia.fr`.

## Retour arrière (si besoin)

Remettre les CNAME CF `@`/`www` sur `openclaw-france.pages.dev` (proxied) — le
projet Cloudflare Pages d'origine n'a pas été touché.
