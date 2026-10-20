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

## Prérequis dans le kit OpenClaw — livraison du 15/10/2026

- **Une amélioration livrée** : les prérequis du `GUIDE.md` et du `README.md`
  sont désormais cohérents avec `/openclaw/#prerequis`, y compris dans le ZIP.
  Bash/curl, Windows natif/WSL2, Node.js et Docker facultatif sont distingués ;
  la mémoire de construction ne devient pas une promesse de dimensionnement.
  Le README place ces vérifications avant les commandes de démarrage.
- Budget clarifié dans ces deux fichiers : modèle et hébergement potentiellement
  payants, plafond conseillé, pas de réutilisation automatique garantie d’un
  abonnement. Retrait des tarifs, rabais et minima RAM non vérifiés du bloc
  remplacé ; lien partenaire conservé et déclaré. Les sections d’installation,
  les scripts, le Compose et la configuration restent inchangés.
- Sources officielles relues le 15/10 : installation, Docker et Windows. Une
  extraction intermédiaire renvoyait des versions/mémoires divergentes : les
  réponses HTTPS directes `.md` et les fichiers du dépôt officiel GitHub ont
  été comparés, identiques pour installation/Docker (Node 24.16+ ou 26.1+ ;
  6 Go pour construire localement). Aucune installation réelle revendiquée.
- Tests : trois nouveaux contrôles de contenu échouent avant correction ;
  **82 tests OK** après correction, dont quatre nouveaux tests sur le kit.
  **7 tests OK sur les fichiers HTTPS publics**, intégrité/exhaustivité du ZIP
  et correspondance exacte avec ses sources. Les deux seules entrées modifiées
  dans le ZIP OpenClaw sont `GUIDE.md` et `README.md` ; ZIP Hermes inchangé.
  Les quatre scripts passent `bash -n`, sans exécuter d’installation.
- Chrome sans JavaScript : ancre et FAQ au clavier, styles appliqués et absence
  de débordement horizontal contrôlés localement puis en production à **1440,
  1024, 430, 390, 375 et 360 px**. Le guide téléchargé par le navigateur public
  correspond exactement à la source.
- Déploiement par `python3 outils/deployer_openclaw.py` depuis le clone cron
  hors Bureau `~/.hermes/workspaces/hub-openclaw-20261003`. Sauvegarde privée
  et comparaison des **35 fichiers** avant envoi : aucune divergence. Les
  **35 fichiers relus via FTP** après envoi correspondent tous aux sources.
  Aucun autre clone, moteur, donnée ni cron modifié.
- Santé : les **six URL demandées répondent HTTP 200**, avant et après envoi.
  Contrôle étendu : **18 URL en HTTP 200**, dont les fichiers du kit, sitemap,
  clé et les deux ZIP avec/sans `?v=2`. Section publiée et fichiers non HTML
  identiques aux sources. Sitemap actualisé pour OpenClaw uniquement.
  **IndexNow HTTP 200** pour la page et les deux fichiers Markdown : notification
  acceptée, sans prétendre à l’indexation ni à une hausse du trafic.
- **Aucune nouvelle distribution** : journal du 15/10 relu, accès bloquants
  déjà consignés ; promotion Bluesky du 12/10 excluante cette semaine. Son fil
  public est relu en HTTPS : URI/CID conformes, zéro réponse au contrôle.
  Prochaine priorité : aligner à son tour le guide téléchargeable Hermes sur
  les prérequis et réserves de sa page, sans inventer une compatibilité testée.
  Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-15/hub-kit-openclaw/`.

## Prérequis dans le kit Hermes — livraison du 16/10/2026

- **Une amélioration livrée** : prérequis du `GUIDE.md` et du `README.md`
  alignés sur `/hermes/#prerequis`, en ligne et dans le ZIP. Lecture avant
  exécution, Bash/WSL2 versus PowerShell, outils requis, compilateur et
  bibliothèques système Linux (dont libatomic), contexte du modèle et budget.
  Les étapes suivantes et les scripts restent inchangés ; pas de nouvelle
  promesse de compatibilité, de mémoire minimale ou de tarif VPS.
- **CONTRADICTOIRE — Mac Intel** : les pages officielles installation et matrice
  divergent encore au contrôle HTTPS direct du 16/10. Le kit reprend cette
  réserve et précise que son message de script ne valide pas la machine.
  Installation, matrice et Quickstart officiels relus et archivés hors dépôt.
  Il s’agit de documentation, pas d’une installation réalisée sur chaque OS.
- Tests : les trois nouveaux contrôles de contenu ont reproduit les manques
  avant correction ; **103 tests OK** après correction, dont quatre nouveaux
  tests du kit. Première passe bloquée par le chemin temporaire macOS sous
  `/var` (lien symbolique), puis reprise avec `TMPDIR` dans le scratch Hermes
  et les dépendances déclarées du dépôt : aucun code moteur changé pour cela.
  **7 tests OK sur les ressources HTTPS publiques** ; ZIP intègre, exhaustif,
  identique aux sources. Seuls README/GUIDE changent dans le ZIP Hermes ;
  ZIP OpenClaw inchangé octet pour octet. Quatre scripts valides avec `bash -n`.
- Chrome sans JavaScript : ancre au clavier, FAQ visible, styles et absence de
  débordement vérifiés localement puis en production aux largeurs **1440, 1024,
  430, 390, 375 et 360 px**. Le guide public téléchargé est identique à la source.
- Bureau inaccessible au cron (`Resource deadlock avoided`) : déploiement par
  `python3 outils/deployer_openclaw.py` depuis le clone cron hors Bureau
  `~/.hermes/workspaces/hub-openclaw-20261003`. Sauvegarde des **35 fichiers**
  avant envoi, sans divergence production/Git ; **35 fichiers relus via FTP**
  après envoi, tous identiques aux sources. Aucun autre clone ou cron modifié.
- Santé : les **six URL demandées sont en HTTP 200**, avant et après envoi.
  Contrôle étendu : **15 URL en HTTP 200**, dont les fichiers Hermes, sitemap,
  clé IndexNow et ZIP avec/sans `?v=2`. Section publiée et fichiers non HTML
  conformes aux sources. Sitemap actualisé pour Hermes uniquement.
  **IndexNow HTTP 200** pour la page et les deux Markdown : notification
  acceptée, pas preuve d’indexation ou de croissance du trafic.
- **Aucune distribution supplémentaire** : contrôle du 16/10 déjà consigné
  dans `docs/distribution-textes.md`, avec accès bloquants ; le post du 12/10
  exclut une nouvelle promotion Bluesky cette semaine. Prochaine priorité :
  aligner le message Mac Intel du script avec la réserve documentaire, sans
  inventer une compatibilité testée. Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-16/hub-kit-hermes/`.

## Réserve Mac Intel dans le script Hermes — livraison du 17/10/2026

- **Une amélioration livrée** : le script et son `--help` signalent maintenant
  explicitement la compatibilité Mac Intel non garantie, les sources officielles
  divergentes et leurs deux URL. Une architecture macOS inconnue ne se présente
  plus comme un Mac Intel. La réserve reste informative : aucun nouveau blocage,
  aucune option ajoutée, téléchargement et transmission des arguments inchangés.
- Installation et matrice officielles relues en HTTPS direct le 17/10 : divergence
  toujours présente. Aucune installation réelle sur Intel ou autre OS revendiquée.
  La page, le guide et le README portaient déjà cette réserve et restent inchangés.
- Tests : les trois nouveaux contrôles de message ont échoué avant correction ;
  **129 tests OK** après correction, dont six sur le wrapper avec OS, identité et
  téléchargement simulés. Options avec espaces, aide sans réseau, refus root,
  erreurs et chemins Apple Silicon/Linux contrôlés sans installer Hermes.
  Les **six tests passent aussi sur le script HTTPS public** ; `--help` exécuté
  directement, quatre scripts validés par `bash -n`.
- Bureau inaccessible au cron (`Resource deadlock avoided`) : déploiement avec
  `python3 outils/deployer_openclaw.py` depuis le clone hors Bureau
  `~/.hermes/workspaces/hub-openclaw-20261003`. Sauvegarde privée des **35 fichiers**,
  sans divergence initiale ; **35 fichiers relus via FTP**, identiques aux sources.
  Seule entrée modifiée du ZIP Hermes : `scripts/install.sh`. ZIP OpenClaw inchangé
  octet pour octet ; intégrité et contenu exhaustif des deux ZIP publics contrôlés.
- Santé : les **six URL demandées répondent HTTP 200**, avant et après envoi ;
  **neuf URL HTTP 200** au contrôle étendu, dont le script et les ZIP avec `?v=2`.
  Aucun HTML ni sitemap modifié : aucune notification IndexNow requise aujourd’hui.
- **Aucune distribution supplémentaire** : la relance JDH du matin, déjà inscrite
  dans `docs/distribution-textes.md`, occupe le quota du jour ; pas de répétition
  Bluesky après le post du 12/10. Prochaine priorité : vérifier les indications
  de coût encore présentes dans la FAQ Hermes, sans estimation universelle.
  Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-17/hub-script-hermes/`.

## Budget Hermes sans promesse de coût universel — livraison du 18/10/2026

- **Une amélioration livrée** : distinction entre kit gratuit et coûts d’usage
  avant les boutons de `/hermes/`, reliée à la FAQ `#budget`. API, abonnement,
  modèle local, outils et hébergement sont distingués ; contrôle des tarifs,
  limite de dépense lorsque le fournisseur la permet et premier essai court.
  Retrait des « centimes par jour », du tarif VPS approximatif et du rabais
  non vérifié. Lien partenaire conservé, signalé et explicitement facultatif.
  Aucun kit, script, style ou contenu du média modifié.
- Source officielle Quickstart relue le 18/10, également en HTTPS direct
  **200**, ancre fournisseur confirmée. Pas de tarif universel, de gratuité
  du matériel ou de l’électricité, ni de compatibilité serveur garantie.
- Les **3 nouveaux tests** échouent avant correction, puis passent ; suite
  complète **137 tests OK**. Première passe bloquée par les chemins temporaires
  macOS sous `/var` ; reprise avec `TMPDIR` dans le scratch Hermes, sans modifier
  le moteur. Les **3 tests budget passent aussi sur le HTML HTTPS public**.
- Chrome sans JavaScript : mention avant les boutons, ancre budget et deux FAQ
  au clavier, navigation vers le guide des coûts et absence de débordement
  vérifiées localement puis en production à **1440, 1024, 430, 390, 375 et 360 px**.
  Sections publiées identiques aux sources ; aucune installation Hermes prétendue.
- Bureau inaccessible au cron (`Resource deadlock avoided`) : déploiement par
  `python3 outils/deployer_openclaw.py` depuis le clone hors Bureau
  `~/.hermes/workspaces/hub-openclaw-20261003`. Sauvegarde des **35 fichiers**
  sans divergence production/Git ; **35 fichiers relus via FTP**, tous identiques
  aux sources après envoi. Les deux ZIP sont intègres et inchangés octet pour octet,
  après restauration des dates et modes avant leur régénération.
- Santé : **six URL demandées en HTTP 200**, avant et après déploiement ;
  **11 URL en HTTP 200** au contrôle étendu, dont les ZIP avec `?v=2`, le guide,
  le sitemap et la clé. Sitemap actualisé pour Hermes uniquement ;
  **IndexNow HTTP 200** pour `/hermes/` : notification acceptée, pas indexation prouvée.
- **Aucune distribution supplémentaire** : contrôle du 18/10 relu dans le journal,
  accès bloquants déjà consignés ; pas de répétition Bluesky après le 12/10.
  Fil public de ce post relu aujourd’hui : URI/CID conformes, zéro réponse.
  Prochaine priorité : aligner l’explication des coûts dans le guide téléchargeable
  Hermes, notamment la formule « sans dépenser un centime » sur le modèle local.
  Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-18/hub-budget-hermes/`.

## Budget du kit Hermes — livraison du 19/10/2026

- **Une amélioration livrée** : le `GUIDE.md` téléchargeable distingue désormais
  kit gratuit, API, abonnement, outils, hébergement, matériel et électricité.
  Retrait des promesses « 100 % gratuite » et « sans dépenser un centime », ainsi
  que des minima RAM universels. Plafond conditionnel au fournisseur, distinction
  alerte/blocage, premier essai court et contrôle de facturation en plus de `/usage`.
- Quickstart et page Providers officiels relus le 19/10 ; HTTPS 200 et ancres
  vérifiées. Aucun bloc de commandes, script, configuration, HTML ou sitemap
  modifié ; aucune installation réelle ni économie mesurée prétendue.
- Les **3 nouveaux tests** reproduisent les manques avant correction et passent
  après correction, également sur le GUIDE public. Suite complète : **147 tests OK**
  après correction du `TMPDIR` macOS vers le scratch Hermes ; aucun moteur modifié.
  Intégrité et contenu exact des deux archives vérifiés ; scripts validés par `bash -n`.
- Déploiement avec `python3 outils/deployer_openclaw.py` depuis le clone cron
  `~/.hermes/workspaces/hub-openclaw-20261003`, le Bureau étant illisible.
  Sauvegarde préalable de **35 fichiers**, sans divergence production/Git ;
  **35 fichiers relus via FTP**, identiques aux sources après envoi. Seuls
  `dl/kit-hermes/GUIDE.md` et son ZIP changent ; seul le GUIDE change à l’intérieur
  du ZIP. Archive OpenClaw inchangée octet pour octet, dates/modes restaurés.
- Santé : **les six URL demandées en HTTP 200** avant et après ; **10 URL en 200**
  au contrôle final étendu, dont le GUIDE, les ZIP avec `?v=2` et la clé IndexNow.
  GUIDE et archives publics identiques aux sources. **IndexNow HTTP 200** pour
  l’URL du GUIDE Markdown modifié ; notification acceptée, pas indexation prouvée.
- **Aucune distribution supplémentaire** : la proposition BDM de ce matin occupe
  déjà le quota quotidien selon `docs/distribution-textes.md`, relu après sync Git.
  Prochaine priorité : vérifier et corriger les promesses de confidentialité du
  guide (« rien ne sort du tout »), en distinguant modèle local et outils connectés.
  Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-19/hub-kit-hermes-budget/`.

## Confidentialité du kit Hermes — livraison du 20/10/2026

- **Une amélioration livrée** : le `GUIDE.md` retire les promesses « rien ne sort
  du tout » et « tout reste chez vous ». Il distingue stockage local, contexte
  envoyé au modèle, outils/services connectés, modèles auxiliaires et fournisseurs
  de secours. Une checklist précède la première session : destinations, outils,
  fichier sans secrets et contrôle réseau indépendant si le hors-ligne est exigé.
- FAQ, Providers, Tools et Configuration officiels relus le 20/10 : HTTPS 200
  et ancres vérifiées. La mention de non-télémétrie est attribuée à la documentation,
  pas transformée en garantie de confinement. Aucun audit réseau ni installation
  réelle prétendu ; aucun bloc de commandes, script, configuration, HTML ou sitemap
  modifié.
- Les **3 nouveaux tests** échouent avant correction puis passent ; suite complète
  **168 tests OK** avec `TMPDIR` fixé au scratch Hermes. Les 3 nouveaux contrôles
  passent aussi sur le GUIDE téléchargé en HTTPS. ZIP intègres et exacts ; seuls
  le GUIDE et son ZIP changent, et seul `GUIDE.md` change à l’intérieur de l’archive.
  Les 4 scripts shell passent `bash -n` ; cela ne valide pas leur installation.
- Déploiement avec `python3 outils/deployer_openclaw.py` depuis le clone cron
  `~/.hermes/workspaces/hub-openclaw-20261003`, le Bureau étant toujours illisible.
  Sauvegarde préalable de **35 fichiers**, sans divergence production/Git ;
  **35 fichiers relus via FTP**, tous identiques aux sources après envoi.
  Dates/modes restaurés avant régénération : ZIP OpenClaw inchangé octet pour octet.
- Santé : **les six URL demandées en HTTP 200** avant et après publication ;
  **10 URL en HTTP 200** au contrôle final étendu. GUIDE et archives publics,
  y compris les téléchargements `?v=2`, identiques aux sources. **IndexNow HTTP 200**
  pour l’URL du GUIDE Markdown : notification acceptée, pas indexation prouvée.
- **Aucune distribution supplémentaire** : le post Bluesky RSS de ce matin occupe
  déjà le quota quotidien et hebdomadaire de cette plateforme, selon le journal
  `docs/distribution-textes.md` resynchronisé. Prochaine priorité : harmoniser les
  précautions de confidentialité dans le README du kit Hermes.
  Preuves privées :
  `~/.hermes/workspaces/crabe-growth-evidence/2026-10-20/hub-kit-hermes-confidentialite/`.

## Retour arrière (si besoin)

Le site payant d'origine existe encore dans le projet Cloudflare Pages : les
CNAME CF `@`/`www` peuvent être repointés vers `openclaw-france.pages.dev`
(proxied). L'ancien index payant est aussi dans l'historique git du dépôt
(commit `780dcfc`).
