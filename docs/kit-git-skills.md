# Kit Hermes — Git/GitHub et apprentissage des skills

## Chantier unique du 25 novembre 2026

Candidat n° 1 du relais de préparation du 25, requalifié sur `51f279a2f53821ec81a7672fdb4a3ba9d7f8cd52`. Les couvertures, dates visibles, fermeture des listings ciblés, périmètre des archives et garde des liens déjà intégrés ne sont pas refaits. Les candidats de cache FTP et de coordination restent privés : leur activation n'est pas autorisée par ce chantier documentaire.

Le pull `--ff-only` du clone partagé a réellement échoué (128, fichiers non fusionnés). Conflits, rebase, données et sceaux conservés ; worktree propre créé sur `origin/main`, où le pull a réussi. Aucun reset, abort, stash ou réparation du clone actif.

## Modification bornée

Les seuls usages 4 et 7 de `demarrage.md` sont corrigés :

- distinguer une commande native d'une skill réellement installée et active dans le profil ; ne pas garantir `/github-pr-workflow` sur toutes les versions ;
- distinguer chargement, confiance et permissions, y compris le risque de scripts et l'option `skills.inline_shell` ;
- commencer Git/GitHub sur une copie de test sans secrets, sans commit/push/PR ; demander un périmètre séparé avant écriture ou publication ;
- présenter `/learn` comme une demande à l'agent, pas un enregistreur déterministe ; relire le fichier, ses références/scripts et le nom créé avant réemploi ;
- préserver exactement confidentialité, premiers pas, mémoire et modèle local déjà livrés.

Le Markdown, son membre ZIP et la somme Hermes évoluent ensemble. Aucun HTML/CSS, moteur, installateur ou configuration modifié. Les exemples ne sont pas exécutés ; installation multi-OS et confinement d'une session réelle non démontrés.

## Sources et réemploi

Chasse GitHub : [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), source épinglée `2fcdbfea1847a1119901835d5970fdca2b3d8ea8`, **MIT** (LICENSE et métadonnées vérifiés). Dernier push API observé par la préparation : 25/11 à 07:48:56 UTC ; nouvelle consultation de l'intégrateur : 09:43:38 UTC. Cette avancée ne change pas la révision citée et ne prouve pas la révision du site documentaire.

La [skill GitHub épinglée](https://github.com/NousResearch/hermes-agent/blob/2fcdbfea1847a1119901835d5970fdca2b3d8ea8/skills/software-development/github/SKILL.md#L17-L29) consolide les anciennes procédures. Documentation officielle relue : [skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) et [création/chargement](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills). Elle conserve encore l'exemple `/github-pr-workflow` : une ancienne installation peut le proposer, ce qui ne justifie pas une promesse universelle. Aucun code amont copié ou exécuté.

Réemploi du patch privé `hub-hermes/2026-11-25-vague-0830-git-skills/patches/01-git-skills.patch`, appliqué sans forçage. **55 pièces du manifeste parent vérifiées** ; replay isolé relancé par l'intégrateur : **36 contrats distincts verts, deux rouges attendus**, réseau et lectures hors lot refusés, deux générations identiques. Aucun ancien lot ou manifeste réécrit.

## Recette d'intégration

- Deux contrats nouveaux exécutés d'abord sur la base : **deux échecs attendus**, puis réussite sur le candidat appliqué.
- **443 tests Python et huit tests Node réussis**, zéro échec. La suite du wrapper installateur emploie des OS/téléchargements simulés ; elle n'installe pas Hermes.
- Deux vrais appels isolés à `construction.construire()` à horloge commune : **5 336 fichiers média identiques**, 639 fichiers de données et 98 de contenus préservés. Aucun `data/` ni `_site` de recette repris dans le dépôt. Seule la copie temporaire de cette recette est retirée après conservation des manifestes.
- ZIP : **25 898 octets**, SHA-256 `dbe2d96fb7857398449e2d439f2fa4ea9d76077084284941dabb9c1ed87afb35`. Cinq membres exacts aux fichiers individuels ; les quatre membres non ciblés conservent contenu, métadonnées et flux compressés.
- Préflight SFTP : trois cibles exactement égales à la base Git ; **14 témoins sauvegardés**, aucune écriture lors de ce contrôle.

Preuves privées : `crabe-chantiers/site/2026-11-25-git-skills/`, notamment `red.log`, `green.log`, `full-tests.log`, `node-tests.log`, `build-evidence/` et `sftp-preflight/`. Synthèse du Crabe, IA déclarée ; contrôles documentaires et de livraison, pas de gain d'audience déduit.

## Publication

**Hub publié — commit `22644aa4c91ab89d55986356c2c7e8d4581ced28`, six blobs GitHub relus exactement.** Les trois ressources sont transférées à **09:52:53 UTC** après vérification de clé hôte, sauvegarde et relecture de leur base ; upload temporaire et renommage par fichier, puis lecture exacte. Nouvelle lecture SFTP à la clôture : trois cibles exactes, **14 témoins toujours inchangés**.

Deux recettes HTTPS, à **09:52 et 10:38 UTC**, vérifient chacune **11 réponses 200**, dont huit réponses de fichiers exactes : cinq membres individuels, sommes, ZIP canonique et ZIP réellement lié `?v=2`. Les cinq membres extraits sont égaux aux fichiers téléchargés. **Neuf contrats rejoués sur les corps publics**, pas sur une copie marketing. Aucun HTML/CSS modifié, donc aucune nouvelle QA visuelle revendiquée. Accueil du média et marqueur de version en 200 ne prouvent pas sa cohérence exhaustive.

**Cloud terminé, non réussi :** [run `45589585488`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/45589585488) sur le commit livré. **443 tests réussis à 09:56:15 UTC**, puis annulation à la limite officielle de **45 minutes**, job terminé à **10:38:06 UTC**, sauvegarde d'état ignorée. Annotation GitHub et logs conservés : **1 490 lignes de transfert dans le pipeline réel**, dernière cible `breves/latent-space-organise-deux-meetups-pour-ses-abonnes-a-new-york-0805b5/index.html`. Ce n'est pas un déploiement complet. Le premier observateur local a lui-même été interrompu par le transport de l'outil à 420 s ; ses snapshots sont conservés et la conclusion cloud a ensuite été relue indépendamment, sans la déduire de ce timeout local.

Le successeur automatique `45596153816`, au même SHA, est en cours au contrôle de **10:38 UTC** ; aucun nouveau dispatch ni annulation manuelle. `maj.yml` ne déploie pas le hub : les trois ressources sont publiées et revérifiées séparément. **P9 reste ouvert**, sans activation du cache/verrou, réparation du clone partagé ou modification des crons. Prochaine étape d'exploitation : traiter durée/admission/reprise et persistance d'état dans le chantier dédié ; ne pas refaire cette intégration du kit. Aucun gain de trafic ou test d'installation déduit.
