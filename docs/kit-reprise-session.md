# Kit Hermes — reprise de session et raccourcis (27 novembre 2026)

## Choix et périmètre

Une seule intégration : premier candidat public admissible du relais du 27 novembre. La garde locale livrée le 26 n'est pas réinstallée. Les lots privés de matrice Git et de cache distant ne sont pas prêts à résoudre l'exploitation : aucun raccord ou activation implicite. Les couvertures, dates visibles, métadonnées et fermetures de listings déjà présentes ne sont pas refaites ; leurs dettes historiques restent distinctes.

Le pull du clone partagé est refusé pour six conflits et journal indexé ; ils sont préservés. Pull réussi uniquement dans un worktree propre du même dépôt, sur `2f60dc74f872c3e28b88c65a955d6d055545a937`. Aucun reset, abort, stash, réparation de rebase, modification du wrapper ou de cron.

Cibles : `sites/openclaw-france/dl/kit-hermes/demarrage.md`, `kit-hermes.zip`, `SHA256SUMS.txt` et `tests/test_kit_hermes_reprise_session.py`. Seuls les premiers pas 4/5 et le conseil image changent ; les douze sections voisines contrôlées restent exactement identiques. Aucun changement aux installateurs, prix ou services tiers.

## Sources et réserve ajoutée à l'intégration

Réemploi du candidat privé, après vérification des **98 pièces du manifeste de relais** et des 12 entrées de base. Chasse amont : [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent), licence MIT relue ; préparation épinglée à `1d15aad1dfa8e9e5fcbd2082cad5666a0907a07d`, dernier push observé alors à 08:25:49 UTC. Nouvelle lecture API pendant l'intégration : push à 09:42:13 UTC ; cette fraîcheur n'est pas une version installée chez le lecteur.

Sources officielles relues : [sessions](https://hermes-agent.nousresearch.com/docs/user-guide/sessions) et [interface CLI](https://hermes-agent.nousresearch.com/docs/user-guide/cli). Le détail du compositeur et le client récent du gateway ne sont pas interchangeables : l'implémentation [gateway_chat.py](https://github.com/NousResearch/hermes-agent/blob/1d15aad1dfa8e9e5fcbd2082cad5666a0907a07d/hermes_cli/gateway_chat.py#L395-L399) peut signaler un détachement plutôt qu'un arrêt du travail. Un troisième contrat et une réserve explicite ont donc été ajoutés au candidat : `/help`, `/stop` lorsqu'il est proposé, `/title` conditionnel, reprise directe par ID. L'ancien lot et ses preuves ne sont pas réécrits.

Il s'agit d'une synthèse française sourcée, pas d'une adoption/exécution du framework. Ni raccourcis physiques, ni session réelle, ni installation multi-OS testés. Reprendre l'historique ne restaure pas les fichiers et ne garantit pas le contexte intégral du modèle ; le texte le précise.

## Recette exécutée

- Deux tests rouges attendus sur la base puis verts ; troisième rouge sur la confusion de surface CLI/gateway puis vert.
- **474 tests Python**, `python3 -m unittest discover -s tests` : succès ; **huit tests Node** réussis.
- Deux générations ZIP identiques : **29 208 octets**, SHA256 `8b83ffc366bb06480e1e609021745856cb9620e96a3b81ab83d113e3a5a04c31`.
- Cinq membres exacts aux fichiers individuels ; quatre non ciblés inchangés, y compris métadonnées et flux compressés. Somme de l'autre kit inchangée.
- Deux vrais builds par `construction.construire()` dans une copie scratch, horloge commune **09:52:43 UTC** : **5 337 fichiers média identiques**, dont 2 652 HTML. **639 fichiers data et 101 contenus préservés** ; seules les trois ressources du hub changent. Copie scratch jetable retirée après conservation des manifestes.
- Préflight SFTP chiffré : clé hôte épinglée avant lecture du secret, **trois cibles exactes à la base**, **14 témoins sauvegardés**. La publication impose une nouvelle lecture avant chaque remplacement.

Preuves privées : `crabe-chantiers/site/2026-11-27-reprise-session/` (journaux rouge/vert, suite complète, ZIP, sections, `build-evidence/`, snapshots SFTP et sources). Aucun secret dans les pièces publiques.

## Publication

Au commit initial : recette complète et préflight réussis ; publication et lectures de retour à consigner après exécution. **`maj.yml` ne publie pas le hub** : transfert ciblé SFTP des trois ressources requis, sans déployeur intégral. Aucun succès global du média ou résolution de P9 déduit de la livraison documentaire.
