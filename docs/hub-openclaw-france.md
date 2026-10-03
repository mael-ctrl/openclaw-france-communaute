# Hub `openclaw-france.fr` — architecture et exploitation

**Depuis le 30/09/2026 (soir) : le site est 100 % GRATUIT.** Fini le pack payant
(97 €) — le hub délivre désormais gratuitement les kits d'installation
**OpenClaw** et **Hermes Agent** : guides pas-à-pas, fichiers prêts, checklists
sécurité, sauvegardes. Aucun compte, aucune carte bancaire.

## Architecture

- **Sources du site** — `sites/openclaw-france/` (design maison `static/style.css`,
  zéro dépendance externe). Pages : accueil, `/openclaw/`, `/hermes/`,
  `/gratuit/` (l'annonce), `/guides/demarrer-openclaw-hermes/` (choix par usage,
  coûts, premier essai limité, sources officielles), `/cgv/` (gratuité & conditions), `/temoignages`,
  `/mentions-legales`, `/politique-de-confidentialite`, `404.html`,
  `sitemap.xml`, `robots.txt`.
- **Kits téléchargeables** — `sites/openclaw-france/dl/kit-openclaw/` et
  `dl/kit-hermes/` ; les `.zip` sont (re)fabriqués automatiquement par le
  déploiement (`preparer_zips()`).
- **Déploiement** — `python3 outils/deployer_openclaw.py` (FTP `communo`,
  dossier `openclaw-france/` ; identité au Trousseau `ovh-communo-ftp`).
- **DNS (Cloudflare, zone `885b27260792f05b29d664a9d98ffb07`)** — CNAME `@` et
  `www` → `communo.cluster131.hosting.ovh.net`, **proxied** (l'edge CF fournit
  le TLS ; l'attachement OVH est en `ssl:false`).
- **Contact** — `support@openclaw-france.fr` (redirection OVH → `crabe@blockos.fr`,
  créée le 30/09) + téléphone `+33 7 45 88 68 20`.
- **IndexNow** — clé `c7a3e9f15b8d2460f8a3e1b9d4c7260e` déposée à la racine.

## Historique

1. **30/09 matin** — rapatriement depuis Cloudflare Pages vers notre hébergement
   `communo` (miroir assaini de l'ancien site payant).
2. **30/09 soir** — pivot complet vers la gratuité : nouveau design maison,
   nouvelles pages (kits OpenClaw + Hermes Agent), retrait du lien Qonto,
   remplacement de la CGV par « Gratuité & conditions », création de la
   redirection `support@`, mise en avant croisée avec `communaute-ia.fr`
   (bandeau + bloc « NOS OUTILS » sur l'accueil du média + liens de pied).

## Guide de démarrage — livraison du 02/10/2026

- Route canonique : `https://openclaw-france.fr/guides/demarrer-openclaw-hermes/`.
- Contenu indépendant et attribué au Crabe (IA) : choix par usage, coûts distincts
  du modèle et de l'hébergement, première tâche en lecture seule, accès minimaux,
  fichiers publics et documentation officielle. Aucun comparatif de prix extrapolé,
  aucune promesse de revenu ni de compatibilité universelle.
- Liens depuis l'accueil, les pages des deux kits et l'annonce gratuité ; présence
  vérifiée dans `sitemap.xml` et `llms.txt`. Canonical, Open Graph, Article et
  BreadcrumbList cohérents avec l'URL. Ceci prépare l'indexation sans la prouver.
- Validation : `python3 -m unittest discover -s tests -v` — **5 tests OK** ; tests
  du nouveau parcours vus rouge puis vert. Contrôle Chrome sur l'URL canonique
  aux largeurs **1440, 1024, 430, 390, 375 et 360 px** : largeur de défilement
  égale au viewport, styles appliqués, CTA principal dans le premier écran,
  ancres et FAQ natives fonctionnelles, navigation vers Hermes effective.
  Une passe avec JavaScript désactivé valide le contenu et la FAQ.
- Téléchargements HTTPS : les deux archives sont identiques aux fichiers locaux,
  ZIP intègres, guide présent, aucun fichier `.env` réel embarqué. Les 4 scripts
  shell passent `bash -n` : **cela ne prouve pas une installation sur chaque OS**.
- Mise en ligne ciblée : **8 fichiers** par SFTP OVH, sauvegarde privée avant
  remplacement, renommage atomique par fichier et relecture exacte. Les kits,
  le moteur du média et les fichiers serveur ne sont pas modifiés.

## Aperçus de partage — livraison du 03/10/2026

- Une amélioration : métadonnées de partage complètes sur `/`, `/openclaw/`,
  `/hermes/` et `/gratuit/`. Images Open Graph en URL HTTPS absolue, URL de page
  cohérente avec la canonical, langue, nom du site, type et dimensions PNG,
  texte alternatif et cartes Twitter/X avec titre, description et image.
  Aucun changement du contenu visible, des offres ou des kits.
- Test de régression `tests/test_hub_partage.py` : défauts reproduits sur les
  quatre pages avant correction ; suite complète **10 tests OK** après correction.
  Les **2 tests de partage du hub** passent aussi sur les réponses HTTPS publiques.
- Publication avec `python3 outils/deployer_openclaw.py` depuis le clone isolé
  `~/.hermes/workspaces/hub-openclaw-20261003` (hors Bureau pour éviter FileProvider
  en cron). Sauvegarde préalable et comparaison de la production à Git ;
  **35 fichiers relus via FTP et identiques aux sources** après envoi.
- Contrôle final : les quatre pages et les deux archives répondent **HTTP 200** ;
  en-têtes HTML publics identiques aux sources ; image PNG **1200 × 630** accessible.
  Les archives sont intègres et inchangées octet pour octet (dates/modes des sources
  restaurés depuis les archives existantes avant leur régénération automatique).
- Sitemap actualisé sur ces quatre URL. Notification **IndexNow HTTP 200** pour
  ces pages ; acceptation de la notification, pas preuve de leur indexation.
- **Aucune nouvelle distribution** : la demande LinuxFr du jour consomme déjà
  le quota, selon `docs/distribution-textes.md`. Prochaine étape : vérifier le
  retour de la modération avant toute publication LinuxFr, sans relance aujourd’hui.

## Retour arrière (si besoin)

Le site payant d'origine existe encore dans le projet Cloudflare Pages : les
CNAME CF `@`/`www` peuvent être repointés vers `openclaw-france.pages.dev`
(proxied). L'ancien index payant est aussi dans l'historique git du dépôt
(commit `780dcfc`).
