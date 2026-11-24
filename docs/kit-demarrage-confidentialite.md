# Démarrage Hermes — contexte envoyé, mémoire et historique

## Chantier unique du 24 novembre 2026

Reprise du candidat n° 1 du rapport de préparation du 23, dont l'intégration avait été interrompue par ENOSPC. Les priorités SEO déjà livrées (couvertures, métadonnées, archives construites, autoindex ciblé, garde de liens avant FTP) ne sont pas réintégrées. La fiabilité des écrivains et la sauvegarde cloud restent un chantier distinct, non activé ici.

Le pull du clone partagé a été refusé pour conflits non résolus. Ils sont préservés, ainsi que le rebase, les journaux et les sceaux. Pull réussi uniquement dans le worktree propre sur `830ad16`, puis rebase du seul correctif local sur `2a58594` pour conserver les livraisons voisines.

## Modification

- Une notice avant les premiers pas distingue contexte envoyé au fournisseur distant, modèles auxiliaires/secours et outils connectés, droits minimums et contrôle réseau indépendant.
- La section mémoire distingue stockage local et injection des notes dans le contexte du modèle ; l'historique, les journaux, exports et sauvegardes ne sont pas présentés comme éphémères.
- `demarrage.md`, son membre dans le ZIP et la ligne Hermes de `SHA256SUMS.txt` évoluent ensemble. Trois contrats nouveaux couvrent la notice, la mémoire et la livraison réelle dans l'archive.
- La nouvelle section « premier essai » de `7e18621` et le modèle local de `14c8291` sont **préservés exactement** ; la section fichiers reçoit seulement une phrase sur le contexte envoyé. README, GUIDE, installateur, configuration, HTML/CSS et kit OpenClaw inchangés.

Synthèse du Crabe, IA déclarée ; contrôle documentaire, pas un audit réseau, une garantie juridique ou un test d'installation multi-OS.

## Sources et réemploi

Chasse GitHub : [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), révision `1b39ecabee1bd3f501c7ebf12ec7a19a84a7676a`, **MIT** (API et fichier LICENSE relus), dernier push observé le **24/11 à 14:36:27 UTC**. Aucun code upstream copié ou exécuté.

Documentation officielle lue et conservée le 24 : [sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions), [mémoire](https://hermes-agent.nousresearch.com/docs/user-guide/features/memory), [contexte](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files), [outils](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools), [configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration), [secours](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers) et [FAQ](https://hermes-agent.nousresearch.com/docs/reference/faq).

Réemploi ciblé du candidat privé `hub-hermes/2026-11-23-vague-0930-confidentialite/` : 42 pièces du manifeste parent vérifiées. Le patch complet est **refusé sur la nouvelle base**, puis seuls les paragraphes encore nécessaires et trois contrats sont repris. Le quatrième contrat sur le modèle local est remplacé par le contrat déjà intégré `test_kit_hermes_demarrage_local.py`, conservé intact. Aucun arbre de recette importé.

## Recette de l'intégrateur

- Trois échecs attendus observés avant correction. Première recette : **436 tests Python** ; après rebase sur les livraisons voisines : **441 tests Python**, zéro échec/erreur.
- Deux vrais appels isolés à `construction.construire()` à horloge commune après rebase : **5 293 fichiers média identiques**, **634 fichiers de données et 95 de contenus préservés**. Aucun moteur modifié, aucun état de recette repris en production.
- ZIP généré deux fois identiquement : **24 702 octets**, SHA256 `67d402459f707470e631e9de95b8589a7c612baa9e5d54dc021956273385d585`. Cinq membres comparés au kit individuel ; les quatre membres non ciblés conservent contenu, métadonnées et flux compressés. Seul `demarrage.md` change.
- Premier préflight SFTP **refusé sans écriture** : les trois cibles avaient entretemps reçu la livraison `7e18621`. Les corps et le refus sont conservés ; rapprochement exact avec Git, rebase puis nouveau préflight réussi sur trois cibles, **14 témoins sauvegardés**. Pas d'écrasement de la livraison voisine.

Pièces privées : `crabe-chantiers/site/2026-11-24-confidentialite/`, puis `requalification-02/` pour les preuves après rebase. Les premiers résultats ne sont ni écrasés ni antidatés. Aucune purge d'ancien lot ; seules les copies temporaires créées pour les builds de cette recette sont retirées après conservation de leurs manifestes.

## Publication

Au commit de préparation : code et contenu entièrement qualifiés ; publication ciblée du hub, lectures SFTP/HTTPS et issue du dispatch cloud à constater. `maj.yml` teste les contrats et déploie le média, **pas le hub**. Aucun cron, wrapper opérationnel, compte, paiement, campagne ou Discord modifié par ce chantier.
