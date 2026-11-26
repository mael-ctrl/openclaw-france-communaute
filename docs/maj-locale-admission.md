# Mise à jour locale : admission Git et propagation des erreurs

## Périmètre livré le 26 novembre 2026

Un seul correctif d'exploitation P9, prioritaire avant une nouvelle retouche du
site. `outils/communaute_maj.sh` versionne le script effectivement installé dans
`~/.hermes/scripts/communaute_maj.sh`. Le job existant continue de référencer ce
fichier via Bash, en mode script seul et livraison locale. **Sa définition, sa
cadence et son état n'ont pas été modifiés.** Ce fichier n'est pas déployé par FTP.

Le wrapper refuse, avant la lecture de clé et avant le moteur : opération Git en
cours, index non fusionné, arbre sale, branche/suivi inattendus, avance locale ou
divergence. La synchronisation est une avance rapide uniquement ; un pull refusé
arrête l'exécution, sans abort, stash, reset ou fusion automatique. Il recontrôle
la pointe distante et l'état local avant le moteur.

Les erreurs de lecture de clé, pipeline, `git add`, `diff`, `commit` et `push`
remontent désormais au processus appelant. `diff` distingue absence de changement,
changement et erreur. Un push refusé conserve le commit local et appelle une
inspection : il n'est plus présenté comme un succès à retenter aveuglément.

**Ce n'est pas un verrou.** Les courses après contrôle, les écrivains cloud et les
transferts partiels restent possibles. Ce correctif ne répare ni le clone
conflictuel, ni la persistance du cache FTP, ni les limites de durée cloud, ni les
anciennes chaînes de preuves. Il ne récupère pas une sauvegarde manquée.

## Réemploi et choix de chantier

Rapport privé du 26 novembre et ses **42 pièces manifestées** relus et vérifiés.
Le candidat wrapper est le seul lot prêt pour une pose indépendante ; le cache v3
reste refusé après son témoin de retour d'une vieille sauvegarde. Ni cache ni
verrou ne sont activés. Les couvertures, dates/auteur étayés, archives, CSS, cache
HTTP et kits déjà livrés ne sont pas réintégrés.

Chasse GitHub : [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent),
licence **MIT**, révision préparatoire
`76b55a46791914921da552c91a2264569dca2055`, push observé par ce lot à
08:37:27 UTC ; métadonnées reconsultées à l'intégration, push courant
09:31:50 UTC. [Source du lanceur](https://github.com/NousResearch/hermes-agent/blob/76b55a46791914921da552c91a2264569dca2055/cron/scheduler_script.py)
et [licence](https://github.com/NousResearch/hermes-agent/blob/76b55a46791914921da552c91a2264569dca2055/LICENSE)
conservées dans le dossier privé. [Documentation officielle](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron/)
consultée. Aucun code Hermes importé dans le produit, aucun framework installé :
réemploi exact du candidat Bash du projet, tests publics autonomes stdlib.

## Tests et construction

- **17 contrats publics** dans `tests/test_maj_locale.py` : **14 échecs attendus**
  sur l'ancien script, zéro erreur de banc, puis 17 réussites sur le candidat.
  Bash et petits dépôts Git réels, remote `file://`, HOME/config neufs, réseau Git
  limité au protocole fichier, clé et moteur synthétiques. Aucun secret réel.
- **466 tests Python** (`python3 -m unittest discover -s tests`) réussis ;
  **huit tests Node** réussis. Les états Git et erreurs injectées sont distincts.
- Banc privé réexécuté : **87 contrats distincts**, dont 12 de classement du
  runtime capturé ; onze rouges attendus avant le vert. Ne pas additionner ces
  nombres aux contrats publics comme des scénarios indépendants. Les frontières
  scheduler/stockage/transport sont substituées : ce n'est pas un cron vivant.
- Deux appels réels à `construction.construire()` sur archive Git isolée de
  `41aa332817b262aa8f48ba73f4ac61237a929cc5`, horloge de recette commune :
  **2 659 pages par build, 5 337 fichiers identiques**, 776 fichiers sources
  données/contenus/sites préservés. Réseau interdit, aucun transfert ni sceau.
  Le wrapper n'a aucun effet sur le HTML ou les dates de production.

## Pose opérationnelle et lecture de retour

Base active SHA-256 :
`31fcd50dd033c6fc5e0f66ced54c03d935f9ce4cce142469b54af3fc0f66070c`.
Candidat et fichier installé :
`803691db1f4e3e206562e940d4b5f18b0e5abcb2444d3eb43a49b717680c27fc`.

Pose bornée : absence de wrapper/moteur local observée, prochain créneau existant
le lendemain, base/mode exacts, sauvegarde privée exclusive et métadonnées,
copie préparée puis remplacement atomique. Relecture des octets, mode **0644**,
propriétaire/groupe, attributs étendus et `bash -n` conformes.

**À 10:00:21 UTC : invocation du vrai chemin installé dans un bac à sable**, sans
réseau, écritures interdites hors `/dev/null`, fichier de clé et trousseau
inaccessibles. Résultat **65**, « opération Git en cours (rebase-merge) », sans
entrée dans le moteur. HEAD, branche locale, index, conflits, données ciblées et
état de rebase inchangés ; configuration du job identique. **Aucun job réel
redéclenché**, aucun succès de mise à jour locale revendiqué. Le prochain passage
planifié doit maintenant signaler ce refus tant que le clone n'est pas réconcilié.

Deux incidents de recette conservés : premier préflight arrêté avant pose
(`os.listxattr` absent de ce Python macOS), puis première sonde en lecture seule
refusée sur `/dev/null` après pose. Utilitaire natif `xattr`/copie préservant les
métadonnées, puis seule exception `/dev/null` ajoutée au bac à sable ; aucune
réinstallation ou ouverture du réseau/secrets pour faire réussir le contrôle.

Preuves privées : `crabe-chantiers/integration-site/2026-11-26-wrapper/preuves/` ;
rouge/vert, suite globale, Node, inventaires des builds et
`installation-02/readback-03.json`. Les premiers refus ne sont pas remplacés.

## Clôture Git/cloud/HTTPS

Au relevé de pose : commit/push et dispatch du workflow à suivre dans la clôture
ci-dessous. Les sondes HTTPS vérifient la disponibilité du média, **pas le
chargement d'un wrapper local**. La correction du faux vert local est distincte
d'une publication complète du catalogue ou d'une sauvegarde cloud réussie.
