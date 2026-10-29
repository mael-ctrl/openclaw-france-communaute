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

**Au commit d'intégration : code et recette locale terminés ; cloud et HTTPS encore à vérifier.** Ce statut initial est conservé ; le complément ci-dessous distingue publication, annulation et rétablissement. Le risque de republication d'une ancienne version par le wrapper local après pull refusé reste distinct et non corrigé ici.

### Livraison du 28 et clôture différée le 29 à 09:52 CET

- Code **`df2b6f398d823d84080e9b38867204371afd7e41`**, quatre blobs relus par API après push. Rebase sur la seule livraison documentaire du podcast : conflit de deux ajouts au journal des jalons combiné sans retirer l'un d'eux ; code/tests/données identiques à la recette.
- Dispatch initial **[`40668253926`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40668253926)** : **250 tests réussis**, CSS de 21 001 octets envoyée le 28 à 10:33:24 UTC ; pipeline **annulé à la limite de 45 minutes**, sauvegarde ignorée. Il n'est pas déclaré vert. Le 28 à 10:41 UTC : huit URL HTTPS contrôlées, CSS exacte et **130 contrôles navigateur publics réussis** (30 dates + 100 tableau).
- Au recontrôle du **29**, descendant **[`40830055748`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40830055748)** réussi, 250 tests, 2 090 envois, sauvegarde `d5f2d08`. Malgré cela, une CSS ancienne et un ancien bloc tableau sont observés à 08:39 UTC : le succès passé ne certifie pas les octets actuellement servis.
- Descendant déjà actif suivi **sans nouveau dispatch** : **[`40840756661`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40840756661)** réussi, 250 tests, **2 101 envois**, sauvegarde `50fa2eb` poussée via fusion `dc953d9`, ascendance vérifiée. Logs : CSS envoyée à 08:27:16 UTC, Transparence à 08:47:58. Le tableau est alors rétabli, mais la CSS servie reste ancienne. La cause exacte de cet écrasement n'est pas démontrée par cette mission ; le clone partagé est encore en conflit.
- **Rétablissement ciblé du même code à 08:51:22 UTC le 29 : une seule cible SFTP**, `/assets/style.css`. Sauvegarde avant écriture, clé hôte épinglée avant authentification, base distante de 20 419 octets identique à `ba95fa4`, contrôle concurrent, upload temporaire + renommage atomique puis lecture exacte. Aucun HTML, donnée, compteur, cron ou autre fichier distant modifié par ce rétablissement.
- **Recette finale à 08:51–08:52 UTC le 29 : huit URL HTTPS 200**, CSS exacte au commit (`65edd58f1c8e3a36698017327be91bd683f3e410789f6cded03e9b2f965f743f`), deux XML parsés. **130/130 contrôles navigateur HTTPS réussis**, mêmes cinq largeurs et JS désactivé ; cinq dates actuelles visibles, tableau/Tab/Shift+Tab/flèches/souris conservés. Capture 195 px relue. Les premiers refus du recontrôle restent conservés ; aucune date de preuve antidatée.

Pièces de clôture dans le même dossier privé : `cloud-run-40668253926.log`, `cloud-40830055748.log`, `cloud-40840756661.log`, `run-*.json`, `https-20261029T083946Z/`, `https-20261029T084844Z/`, `css-regression-matches.json`, `restauration-css-20261029/`, `https-20261029T085122Z/`, `browser-https-20261029T085123Z/`. Les attentes bornées et le refus réseau ponctuel de `gh run watch` sont distincts des conclusions GitHub.

**Clôture : une seule intégration fonctionnelle, rétablie et vérifiée en production.** Durée/sauvegarde des pipelines annulés et concurrence avec la routine locale restent des incidents d'exploitation à traiter séparément. Ni conformité globale, ni hausse d'audience, ni réparation de ces automatismes revendiquée.
