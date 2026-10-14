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

## Dépannage Hermes — livraison du 06/10/2026

- **Une amélioration** : aide de dépannage sur `/hermes/#depannage`, accessible
  depuis le haut de page. Trois cas : commande introuvable, fournisseur/modèle
  non configuré, diagnostic et demande de support sans exposer de secrets.
  Commandes et chemins recoupés avec la documentation officielle d’installation
  Nous Research, consultée le 06/10. Aucun changement des kits ni de leurs scripts.
- Tests : les 3 nouveaux contrôles ont échoué avant ajout, puis réussi ; suite
  complète **15 tests OK**. Les 3 contrôles passent aussi sur le HTML public
  après décodage de la protection e-mail Cloudflare (seule transformation HTML).
- Chrome sans JavaScript : ancre et FAQ au clavier vérifiées localement à 1440,
  1024, 430, 390, 375 et 360 px ; en production à **1440, 390 et 360 px**.
  Aucun débordement horizontal constaté. Ceci ne teste pas une installation Hermes.
- Déploiement via `python3 outils/deployer_openclaw.py` depuis le clone cron
  hors Bureau ; sauvegarde privée et comparaison préalable production/Git.
  **35 fichiers relus via FTP**, identiques aux sources après envoi. Archives
  régénérées après restauration de leurs dates/modes : ZIP intègres et inchangés.
- Santé finale : les 4 pages demandées et les 2 ZIP répondent **HTTP 200**.
  Page Hermes publique conforme après normalisation Cloudflare ; sitemap et ZIP
  identiques octet pour octet. Sitemap actualisé pour Hermes uniquement.
  **IndexNow HTTP 200** pour `/hermes/` (notification acceptée, pas indexation prouvée).
- **Aucune distribution supplémentaire** : Bluesky a déjà été utilisé cette
  semaine (05/10). La tentative Uneed du 06/10 est documentée comme bloquée avant
  envoi dans `docs/distribution-textes.md` ; aucun nouveau contact ni formulaire.
  Prochaine priorité de distribution : finaliser l’accès sécurisé Uneed avant
  la soumission gratuite autorisée, sans nouvelle promotion Bluesky cette semaine.

## Dépannage OpenClaw — livraison du 07/10/2026

- **Une amélioration** : aide sur `/openclaw/#depannage`, reliée depuis le haut
  de page. Trois cas : passerelle arrêtée, tableau de bord inaccessible depuis
  un VPS, refus d’authentification ou appairage. Les instructions distinguent
  installation classique et Docker, ordinateur et serveur. Pas d’ouverture de
  port public, de désactivation de sécurité, de suppression de données ni
  d’approbation aveugle ; consignes de masquage des secrets avant toute aide.
- Sources officielles OpenClaw (diagnostic, Docker, accès distant) et Docker
  Compose (état et journaux) consultées le 07/10. Les services cités correspondent
  au Compose du kit ; aucun kit ni script d’installation modifié.
- Tests : **3 nouveaux tests** échouent avant ajout puis passent ; suite complète
  **22 tests OK**. Les 3 nouveaux tests passent aussi sur le HTML public après
  décodage de la protection e-mail Cloudflare ; section publiée identique.
- Chrome sans JavaScript : ancre, FAQ au clavier et styles vérifiés localement
  à **1440, 1024, 430, 390, 375 et 360 px**, puis en production à **1440, 390 et
  360 px**. Aucun débordement horizontal détecté, FAQ ouvertes comprises.
  Ceci valide la page, pas une installation réelle d’OpenClaw ou de Docker.
- Déploiement avec `python3 outils/deployer_openclaw.py` depuis le clone cron
  `~/.hermes/workspaces/hub-openclaw-20261003`, hors Bureau. Le conflit préexistant
  de l’autre clone dans `data/stats.json` est laissé intact. Sauvegarde privée
  préalable et absence de divergence production/Git vérifiées ; **35 fichiers
  relus via FTP et identiques aux sources** après envoi. Les deux ZIP sont
  intègres et inchangés octet pour octet (dates/modes restaurés avant régénération).
- Santé finale via curl : les quatre pages et les deux ZIP demandés répondent
  **HTTP 200** ; sitemap et clé IndexNow aussi. Une lecture urllib sans en-tête
  particulier a reçu 403 ; vérification reprise avec curl et Chrome, sans
  désactiver TLS ni changer les règles de sécurité du site.
- Sitemap actualisé pour OpenClaw uniquement. **IndexNow HTTP 200** pour
  `/openclaw/` : notification acceptée, pas preuve d’indexation.
- **Aucune distribution supplémentaire** : journal du 07/10 relu après mise à
  jour Git ; les accès/permissions bloquants y sont déjà documentés. Bluesky
  reste exclu cette semaine après le post du 05/10. Prochaine priorité : accès
  sécurisé Uneed pour la soumission gratuite autorisée, sans nouveau contact
  ni répétition promotionnelle en attendant.

## Parcours de consultation des kits — livraison du 08/10/2026

- **Une amélioration** : le bouton « Parcourir les fichiers » des pages
  `/openclaw/` et `/hermes/` mène désormais à leur catalogue expliqué
  (`#fichiers`), plutôt qu’à un index Apache sans contexte. Ordre de lecture
  indiqué (README puis GUIDE avant les scripts), accès sans compte ni ZIP et
  rappel de ne pas exposer les clés API. Le fichier `config-exemple.yaml`
  manquant du catalogue Hermes est maintenant lié : les **8 fichiers OpenClaw**
  et les **5 fichiers Hermes** sont tous accessibles avec une description.
  Aucun ajout dans les archives, aucune commande ni configuration de kit modifiée.
- Les **3 nouveaux tests** de `tests/test_hub_fichiers.py` reproduisent les
  manques avant correction ; suite complète **31 tests OK** après correction.
  Catalogue exhaustif comparé aux dossiers réels, liens locaux valides, ancres
  uniques et section nommée pour les technologies d’assistance. Les 4 scripts
  shell passent `bash -n` ; cela ne teste pas une installation des logiciels.
- Chrome sans JavaScript : accès au catalogue au clavier, styles et absence de
  débordement vérifiés sur les deux pages à **1440, 1024, 430, 390, 375 et 360 px**
  en local, puis à **1440, 390 et 360 px** en production. L’ancre positionne le
  titre sous l’en-tête fixe ; captures mobiles conservées hors dépôt.
- Déploiement avec `python3 outils/deployer_openclaw.py` depuis le clone cron
  `~/.hermes/workspaces/hub-openclaw-20261003`, hors Bureau. Le clone partagé
  avec conflit préexistant reste intact. Sauvegarde privée préalable et absence
  de divergence production/Git vérifiées ; **35 fichiers relus via FTP** et
  identiques aux sources après envoi. FTPS essayé mais non pris en charge par
  ce serveur ; lecture reprise avec le protocole du déployeur existant.
  Les deux ZIP sont intègres et inchangés octet pour octet après restauration
  des dates/modes avant régénération.
- Santé finale : **HTTP 200** pour les six URL demandées. Les **21 URL** du
  contrôle étendu (pages, archives, fichiers des kits, sitemap et clé IndexNow)
  répondent 200 ; les fichiers non HTML sont identiques aux sources. Les deux
  liens ZIP effectivement utilisés par les boutons (`?v=2`) sont aussi relus,
  HTTP 200 et identiques. Catalogues et nouveaux boutons publics conformes aux
  sources. Sitemap actualisé sur les deux pages ; **IndexNow HTTP 200** pour
  `/openclaw/` et `/hermes/` : notification acceptée, pas indexation prouvée.
- **Aucune distribution supplémentaire** : le contrôle du 08/10 est déjà
  consigné dans `docs/distribution-textes.md` ; accès et permissions bloquants
  inchangés selon ce journal. Pas de répétition Bluesky après le post du 05/10,
  ni de nouveau contact. Prochaine priorité : disposer d’un accès sécurisé
  Uneed pour la soumission gratuite autorisée, avec indépendance explicite.

## Gratuité et budget sur l’accueil — livraison du 09/10/2026

- **Une amélioration** : distinguer le prix des kits des coûts d’usage dès
  l’accueil. Mention visible **avant les boutons** : kits et guides à 0 €,
  modèle IA et hébergement potentiellement payants. Lien direct vers le guide
  existant `#couts` ; FAQ gratuité et serveur rendues cohérentes. Retrait du
  tarif VPS approximatif et du rabais non vérifié, lien partenaire conservé
  et signalé, sans obligation. Aucun kit, script ou style modifié.
- Contenu recoupé avec le guide existant et les documentations officielles
  OpenClaw Getting started et Hermes Quickstart (choix du fournisseur), relues
  le 09/10. Aucune estimation de coût universelle ni installation réelle prétendue.
- Les **3 nouveaux tests** de `tests/test_hub_couts.py` échouent avant la
  correction, puis passent ; suite complète **42 tests OK**. Les 3 tests
  passent aussi sur les pages HTTPS téléchargées ; contenu `<main>` public
  de l’accueil strictement identique aux sources locales.
- Chrome sans JavaScript : mention avant les CTA, liens vers `#couts`, FAQ
  ouverte au clavier et absence de débordement horizontal vérifiés à
  **1440, 1024, 430, 390, 375 et 360 px** localement, puis à **1440, 390 et
  360 px** en production. Captures mobiles conservées hors dépôt.
- Déploiement avec `python3 outils/deployer_openclaw.py` depuis le clone cron
  `~/.hermes/workspaces/hub-openclaw-20261003`, hors Bureau. Le clone partagé
  avec conflit préexistant reste intact. Sauvegarde privée et comparaison
  production/Git avant envoi : aucune divergence ; **35 fichiers relus via
  FTP**, identiques aux sources après déploiement. Les dates et modes des
  fichiers des kits sont restaurés avant régénération : les deux ZIP restent
  intègres et identiques octet pour octet aux archives précédentes.
- Santé finale : **HTTP 200 pour les six URL demandées**, ainsi que pour le
  guide, le sitemap et la clé IndexNow. Sitemap actualisé pour l’accueil
  uniquement ; **IndexNow HTTP 200** pour `https://openclaw-france.fr/`.
  Notification acceptée, pas preuve d’indexation ni de hausse du trafic.
- **Aucune distribution supplémentaire** : contrôle du 09/10 déjà consigné
  dans `docs/distribution-textes.md`, avec accès et permissions bloquants.
  Pas de répétition Bluesky après la promotion du 05/10, ni de nouveau contact.
  Prochaine priorité sur le hub : vérifier les prérequis des kits face aux
  documentations officielles ; Uneed reste en attente d’un accès sécurisé.

## Prérequis Hermes visibles avant téléchargement — livraison du 12/10/2026

- **Une amélioration** : `/hermes/#prerequis`, avec un lien avant le bouton ZIP.
  Systèmes et outils nécessaires, distinction Bash/WSL2 et Windows natif, lien
  vers la méthode officielle Windows, dépendances système possibles sous Linux.
  Sources officielles installation et matrice des plateformes relues le 12/10.
- **CONTRADICTOIRE — Mac Intel** : le guide officiel d’installation le déclare
  non pris en charge, tandis que la matrice décrit encore CLI et bundles Intel
  conditionnels. La page montre cette réserve et signale les indications plus
  anciennes du kit, sans inventer une garantie ou interdire une méthode sur la
  base d’une seule source. Aucun script ni fichier des kits modifié ; aucune
  installation réelle sur ces plateformes prétendue.
- Les **3 nouveaux tests** reproduisent le manque avant ajout, puis passent ;
  suite complète **49 tests OK**. Les 3 passent aussi sur le HTML public et la
  section publiée est identique à la source. Chrome sans JavaScript : ancre et
  FAQ au clavier, styles et absence de débordement vérifiés à **1440, 1024,
  430, 390, 375 et 360 px** localement, puis **1440, 390 et 360 px** en production.
- Déploiement par `python3 outils/deployer_openclaw.py` depuis le clone cron
  hors Bureau `~/.hermes/workspaces/hub-openclaw-20261003` ; clone partagé en
  conflit laissé intact. Sauvegarde privée et comparaison production/Git avant
  envoi : aucune divergence. **35 fichiers relus via FTP**, identiques aux
  sources. Dates/modes des fichiers de kits restaurés avant régénération :
  les deux ZIP restent intègres et inchangés octet pour octet, y compris en HTTPS.
- Santé : **HTTP 200 pour les six URL demandées**, le sitemap et la clé.
  Sitemap actualisé pour Hermes uniquement ; **IndexNow HTTP 200** pour cette
  page. Notification acceptée, aucune indexation ni hausse de trafic prétendue.
- **Aucune distribution supplémentaire** : le post Bluesky de 06:43 UTC,
  consigné dans `docs/distribution-textes.md`, occupe déjà le quota du jour et
  celui de Bluesky cette semaine. Prochaine priorité : contrôler les prérequis
  OpenClaw ; suivre les retours du post existant sans republier.

## Prérequis OpenClaw — préparés le 13/10/2026, publication bloquée

- **Une amélioration préparée, non publiée** : `/openclaw/#prerequis`, avec
  accès avant le bouton ZIP et FAQ cohérente. Distinction entre script Bash
  macOS/Linux, Windows natif/WSL2 et Docker facultatif. Versions Node.js
  documentées ; les 6 Go cités par la doc Docker concernent la construction
  locale depuis les sources, pas un minimum universel à l’exécution.
  Réserve explicite sur les anciennes estimations mémoire du guide.
- Sources officielles `https://docs.openclaw.ai/install`, `/install/docker`
  et `/platforms/windows` relues le 13/10 via leurs versions `.md` (HTTP 200).
  Aucun script, fichier de kit ni style modifié ; aucune installation réelle
  d’OpenClaw ou Docker prétendue.
- Les **3 nouveaux tests** échouent avant ajout puis passent ; suite complète
  **52 tests OK**. Chrome sans JavaScript, à **1440, 1024, 430, 390, 375 et
  360 px** : ancre au clavier, trois FAQ ouvertes au clavier, styles,
  absence de débordement et accès au guide vérifiés **localement seulement**.
- **Incident OVH confirmé** : les six URL de santé répondent **HTTP 503**
  dès 14h35 CEST, encore à 14h44 ; la clé IndexNow répond également 503.
  Réponse identique sur l’origine HTTP directe, sans Cloudflare. L’API OVH
  rattache `communo.cluster131.hosting.ovh.net` au **filer 1593 / cluster131**,
  service toujours actif. Incident matériel officiel commencé à **10h53 UTC**,
  statut `identified` au contrôle :
  <https://web-cloud.status-ovhcloud.com/incidents/tv9r4xs5t6r3>.
  L’accueil du média `communaute-ia.fr` répond aussi 503.
- `python3 outils/deployer_openclaw.py` exécuté depuis le clone cron hors
  Bureau : **sortie 1, FTP `421 Home directory not available - aborting`**
  avant tout transfert. Aucun fichier distant changé, aucune sauvegarde FTP
  possible pendant cette panne. Les deux ZIP régénérés sont intègres et
  inchangés octet pour octet après restauration des dates/modes des sources.
  Les conflits préexistants du clone partagé restent intacts.
- Repli Cloudflare Pages examiné en lecture seule : les deux jetons disponibles
  retournent **403** sur le projet `openclaw-france`. Aucun DNS, droit, jeton,
  serveur ou hébergement modifié ; surtout ne pas basculer vers l’ancien site
  payant sans avoir publié et vérifié la version gratuite sur le repli.
- **IndexNow HTTP 200** pour `/openclaw/` à 12h44 UTC : notification acceptée
  uniquement. Cela ne prouve ni disponibilité, ni publication de la nouvelle
  section, ni indexation (la page publique et la clé restent en 503).
- **Aucune distribution** : site indisponible ; le contrôle des accès du jour
  figure déjà dans `docs/distribution-textes.md`, et Bluesky a été utilisé le
  12/10. Aucun nouveau contact ni publication de substitution.
- **À reprendre en priorité** : une fois OVH rétabli, sauvegarder et comparer
  les fichiers distants, déployer cette modification avant d’en ajouter une
  autre, puis relire la section publique, les ZIP et les six URL de santé.
  Refaire le ping IndexNow après publication effective. Preuves privées sous
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-13/hub-prerequis-openclaw/`.

## Prérequis OpenClaw — publiés le 14/10/2026 après reprise OVH

- **Une amélioration livrée** : publication de `/openclaw/#prerequis`, préparée
  le 13/10 mais bloquée par la panne OVH. Le lien avant téléchargement et la FAQ
  distinguent Bash macOS/Linux, Windows natif/WSL2 et Docker facultatif, avec
  versions Node.js, mémoire de construction et réserves sur les anciennes
  estimations du guide. Sources officielles installation, Docker et Windows
  relues le 14/10 ; date de consultation et sitemap actualisés. Aucun autre
  contenu du hub ni fichier de kit modifié ; aucune installation réelle prétendue.
- **Santé rétablie au contrôle** : les six URL demandées répondent HTTP 200
  avant et après publication. Ceci constate la disponibilité du hub, sans
  attribuer à cette mission la réparation de l’infrastructure OVH.
- Déploiement par `python3 outils/deployer_openclaw.py` depuis le clone cron
  hors Bureau `~/.hermes/workspaces/hub-openclaw-20261003`. Le clone partagé et
  ses conflits préexistants restent intacts. Sauvegarde privée des **35 fichiers**
  et comparaison à la version Git précédant la panne : aucune divergence.
  Après envoi, les **35 fichiers relus via FTP** sont identiques aux sources.
- Dates/modes des sources des kits restaurés avant régénération : les deux ZIP
  restent intègres et inchangés octet pour octet, vérifiés aussi en HTTPS sur les
  URL simples et celles des boutons (`?v=2`). Sitemap et clé IndexNow relus en
  HTTPS, HTTP 200 et contenu exact.
- Suite complète : **54 tests OK**. Les **3 tests des prérequis OpenClaw** passent
  aussi sur les ressources HTTPS publiques ; section publiée identique à la
  source. Les 4 scripts shell passent `bash -n`, sans exécution d’installation.
  Chrome sans JavaScript en production à **1440, 1024, 430, 390, 375 et 360 px** :
  ancre et trois FAQ utilisables au clavier, styles appliqués, aucun débordement
  horizontal, guide accessible en HTTP 200.
- **IndexNow HTTP 200** pour `/openclaw/` après publication effective :
  notification acceptée, pas preuve d’indexation ou de hausse du trafic.
- **Aucune distribution supplémentaire** : journal du 14/10 relu après
  synchronisation Git ; les accès et permissions bloquants y sont déjà consignés.
  Bluesky a été utilisé le 12/10 : pas de nouvelle promotion cette semaine.
  Prochaine priorité : aligner les indications anciennes du guide OpenClaw avec
  ces prérequis, en conservant la distinction entre documentation et installation
  réellement testée. Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-14/hub-prerequis-openclaw/`.

## Retour arrière (si besoin)

Le site payant d'origine existe encore dans le projet Cloudflare Pages : les
CNAME CF `@`/`www` peuvent être repointés vers `openclaw-france.pages.dev`
(proxied). L'ancien index payant est aussi dans l'historique git du dépôt
(commit `780dcfc`).
