# Dates de « Mes derniers ratés » — intégration du 28 octobre 2026

## Choix et périmètre

Une seule intégration fonctionnelle : permettre le retour à la ligne des dates de la liste d'erreurs sur `/transparence/`, à largeur CSS très réduite. La règle est strictement `.erreurs-liste .j-ts { white-space: normal; }`. Les cellules du tableau horizontal gardent `nowrap` ; aucune date, donnée, structure HTML, navigation ou destination n'est changée.

Premier candidat site non livré du relais de l'orchestrateur du 28. Grands aperçus, news-sitemap, couvertures, dates éditoriales, catalogue conservé, navigation, reflow général et tableau sont déjà intégrés. Leurs limites historiques restent ouvertes : cette correction ne ferme ni l'alias OVH, ni les anciennes URL inconnues, ni la sémantique des autres horodatages. Aucun lot compteur, wrapper ou reprise Git importé.

Le pull demandé dans le clone partagé a refusé (six fichiers non fusionnés, rebase en cours). État préservé. Worktree propre créé sur `86006cb75aa09e79472a3e43ffae413ff28fad16`, où le pull a réussi. Le commit de clôture du tableau est documentaire : ce chantier ne le refait pas.

## Réemploi et provenance

Lot privé `accessibilite/2026-10-28-dates-transparence`, préparé sur `9e61d486d907d4d4f3237aee6edc0b62be74f53a`. **1 028 références** du manifeste de vague vérifiées avant intégration. Source CSS et constructeur concernés identiques entre les deux bases. Vérificateur du lot réellement rejoué sous confinement OS : **303 pièces**, 13 contrats, six refus géométriques attendus avant / 30 contrôles dates verts après, tableau 100/100 avant et après.

Chasse GitHub réemployée et refetch indépendant des deux blobs : [`twbs/bootstrap@05331e1`](https://github.com/twbs/bootstrap/tree/05331e182f29d02a684516bd804b80a53f9fdfc3), [licence MIT](https://github.com/twbs/bootstrap/blob/05331e182f29d02a684516bd804b80a53f9fdfc3/LICENSE), [`scss/_utilities.scss`](https://github.com/twbs/bootstrap/blob/05331e182f29d02a684516bd804b80a53f9fdfc3/scss/_utilities.scss#L769-L781), push API relevé dans la préparation le 27 octobre à 20:19:27 UTC. Concept de wrap/nowrap seulement, règle maison : aucune bibliothèque installée ni code amont copié.

## Recette d'intégration réellement exécutée

- Nouveau `tests/test_dates_transparence.py` appliqué avant la CSS : **trois tests, un échec attendu** sur le retour à la ligne absent ; trois verts après correction.
- **250 tests Python + quatre tests Node réussis**, suite originale sans adaptation de fixture ; exécution dans une copie scratch neuve avec HOME explicite.
- Deux appels réels de `construction.construire()` dans des copies isolées, à horloge commune `2026-10-28T10:00:00+00:00` : **4 007 sorties, 4 006 identiques**, seule `assets/style.css` différente ; **506 fichiers de données intacts**. Pas de `data/` de recette repris en production.
- Chromium 156, JavaScript du site désactivé, largeurs 160/195/320/390/1440 px, sur le HTML complet effectivement construit : **six échecs dates attendus avant**, **30/30 après**, et **100/100 contrôles du tableau avant/après**. En-tête réel conservé, souris/Tab/Shift+Tab/flèches et arbre d'accessibilité vérifiés.
- Premier passage d'intégration : une flèche droite sans déplacement mesuré à 320 px dans le témoin avant, 99/100 au tableau. Échec conservé ; même recette et mêmes octets rejoués dans une sortie neuve, 100/100 avant et après. Cause non établie, aucun changement produit ni assertion retirée pour masquer cet échec.
- Captures avant/après à 160 px relues : dates auparavant coupées, désormais complètes sur plusieurs lignes ; bloc plus haut et mots fortement repliés. Cela ne démontre pas une conformité globale ni un gain de trafic.

Pièces privées : `crabe-chantiers/integrations/dates-transparence-20261028/` (`red-unit.log`, `full-python.log`, `full-node.log`, `build-comparison.json`, `browser-integration/`, `browser-integration-retry/`). Replay préparatoire séparé : `accessibilite/2026-10-28-dates-transparence/replay-integration-1045/`. Ces preuves ne sont pas publiées dans le dépôt.

## Publication

**Au commit d'intégration : code et recette locale terminés ; cloud et HTTPS encore à vérifier.** Le complément de livraison sera consigné après lecture du run, de sa sauvegarde et des octets servis. Le risque de republication d'une ancienne version par le wrapper local après pull refusé reste distinct et non corrigé ici.
