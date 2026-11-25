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

Au commit initial : recette locale terminée ; publication SFTP/HTTPS et issue du workflow média encore à vérifier. `maj.yml` ne déploie pas le hub. La publication de ces trois ressources sera vérifiée séparément de la sauvegarde cloud du média ; aucune clôture de P9 déduite.
