# Parcours FTP relatif — intégration du 28 novembre 2026

## Choix et périmètre

**P9, priorité d'exploitation non résolue de la roadmap.** Les couvertures, dates HTML/JSON-LD, archives conservées, CSS intégrée et cache HTTP existent déjà ; les refaire ne résoudrait pas la publication interrompue. Le dernier relais privé garde à juste titre ses candidats de cache et de reprise Git fermés. Ce correctif indépendant ne les active pas : il retire seulement les allers-retours de navigation FTP redondants.

Avant : chaque fichier oblige à repartir du dossier `www`, redescendre tous les composants, envoyer, puis remonter. Après : le déployeur conserve le préfixe de dossier commun entre deux **envois effectifs**, remonte et descend seulement ce qui change. Les commandes restent relatives ; `STOR` utilise toujours le seul nom du fichier. Retour à la base avant `QUIT` conservé.

**Inchangés** : ordre des fichiers, corps, bloc de transfert, authentification, cache taille/mtime et son format, moment de sauvegarde du cache, propagation des erreurs, borne de 45 minutes, workflow, concurrence, annonces et données. Aucun contournement de conflit, nouveau cache de contenu, lecture distante de validation ou promesse de résolution globale des timeouts.

## Recherche et réemploi

- [basic-ftp, Client.ts](https://github.com/patrickjuchli/basic-ftp/blob/1850100bd6840f159f3cb5ccd8fe9c4861cf7d6a/src/Client.ts#L701-L715), licence MIT relue, dernier push API observé le 04/11/2026 : parcours de répertoires sans retour systématique à la base. Concept réimplémenté avec le déployeur Python existant ; aucun code TypeScript copié ni dépendance de production ajoutée.
- [pyftpdlib](https://github.com/giampaolo/pyftpdlib/tree/b657392af6a4d62fe8ba385a36679e204ef27b2f), MIT relue, dernier push API observé le 19/11/2026. Version PyPI **2.2.0** utilisée uniquement dans un venv de recette pour un serveur réel lié à `127.0.0.1`, pas en production. Le SHA lu du dépôt et la version installée sont des identifiants distincts.

Métadonnées, licences et fichier source conservés en privé, avec vérification de l'OID Git des corps téléchargés. Aucun secret de production dans la recette FTP.

## Vérifications exécutées

Base figée **`18da2bf661e26e19c9f0c8cbb572593ae0f01e5a`** ; pull partagé refusé pour conflits, laissés intacts. Pull réussi seulement dans le worktree propre. Les **98 pièces** du manifeste du relais du 27 ont été revérifiées avant intégration ; son kit est déjà publié, non réappliqué.

- TDD : test de deux fichiers frères **rouge avant** (traversée inutile), puis vert ; huit contrats de navigation couvrent racine, branches sœurs, profondeurs, Unicode/espaces, création, cache partiel/complet/invalide, no-op et refus CWD/MKD/STOR/QUIT. Pas de cache validé sur refus.
- **489 tests Python réussis** (`python3 -m unittest discover -s tests`).
- Deux appels réels à `construction.construire()` dans une copie isolée à horloge commune : **2 659 pages, 5 340 fichiers identiques**, **245 484 627 octets** ; **743 fichiers données/contenus préservés**.
- Vrai FTP local avant/après : **5 340 fichiers reçus**, tous les chemins et SHA-256 comparés au build ; **245 484 627 octets** dans chaque cas, états de cache identiques, deuxième passage `(0, 0)` de chaque côté. **23 935 → 7 985 commandes CWD** sur arborescence initialement absente, soit **−66,64 %**. Ce n'est pas une mesure de vitesse OVH : le replay final local prend environ 13 s avant et 14 s après ; aucune accélération chronométrique de production déduite.
- Première recette FTP conservée : tous les corps étaient exacts mais fermeture du serveur depuis un autre thread produisait `Bad file descriptor`. Banc corrigé dans un nouveau fichier/répertoire ; deuxième recette sans erreur de thread, sources produit inchangées.
- Pipeline isolé `--essai --sans-redaction` : code 0, collecte et build exécutés ; zéro rédaction, FTP ou post. Cinq flux tiers en erreur (timeout/502/404/403/429) consignés, non assimilés à une collecte exhaustive. **60 manifestes identiques**, préfixe de journal préservé ; aucune donnée de cette copie importée.

Preuves privées : `crabe-chantiers/site/2026-11-28/` (`red-navigation.log`, `full-suite.log`, `build-result.json`, `ftp-replay-02/ftp-result.json`, commandes complètes, états et journaux). Les copies du site et racines FTP locales restent des sorties de recette, pas des sauvegardes de production.

## Production et limites

Au commit initial, correctif complet testé localement ; cloud et HTTPS restent à contrôler après push. Run témoin antérieur **46127521282** : 481 contrats réussis, pipeline annulé à 45 minutes, sauvegarde ignorée. **1 490 vrais transferts**, après exclusion des flèches imprimées par les tests (premier comptage non borné de 1 500 conservé comme erroné).

Le nombre de commandes diminue sans modifier les contenus construits. Cela ne prouve pas à lui seul un déploiement complet, une sauvegarde durable, la coordination des producteurs ou une reprise Git. Le clone partagé et ses preuves ne sont pas réparés par cette intégration. Les erreurs de connexion et le cache taille/mtime préexistants conservent leurs limites.
