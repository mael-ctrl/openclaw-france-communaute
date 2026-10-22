# Brèves concurrentes à la même URL — 22 octobre 2026

## Incident et amélioration unique

Les contrats cloud refusent une URL dupliquée depuis la fusion `04ed0c5` :
`amazon-investit-16-milliards-d-euros-en-allemagne-dans-le-cloud-et-l-i-ad21a5`.
Le parent `775e103` contient la rédaction de 10:21:40 UTC, le parent `2f58ec9`
celle de 09:50:10 UTC ; leur fusion contient les deux, avec le même ID complet,
le même slug et la même source exacte, mais des résumés distincts.
Le run `39787508986` échoue avant publication (six erreurs, 183 tests).
La lecture HTTPS avant correction sert déjà la rédaction de 10:21:40 UTC.
Le correctif maintient donc ce texte à cette URL, sans choisir une nouvelle
version sur la seule base d'un identifiant tronqué.

## Règle bornée de rendu

`engine/construction.py::breves_pour_publication` produit une vue de publication :

- groupement par **chemin exact**, jamais par ID seul ;
- plusieurs lignes à ce chemin exigent un ID complet, un nom de source et une
  URL source non vides et strictement identiques ;
- copies entièrement identiques : un seul rendu ;
- versions distinctes : dates `date_redac` valides et munies d'un fuseau,
  comparées comme instants ; retenir la plus récente, sans réécrire son contenu ;
- deux contenus différents au même instant, même anciens et même en présence
  d'une version plus récente : refus avant tout HTML ;
- identité différente/incomplète, date ambiguë, chemin dangereux : refus conservé.

L'ordre relatif des enregistrements retenus est préservé. La même sélection
alimente accueil, fil, archives, pages individuelles, flux et sitemaps.
Le contrôle distinct des collisions d'articles reste inchangé.
Les variantes restent intégralement dans `data/breves.json` ; aucune ligne de
journal, aucun sceau, aucune URL historique ni date source n'est retouché.
Un message de build indique le nombre de variantes non rendues séparément.

Cette règle ne valide pas les faits d'une rédaction, ne garantit pas sa première
publication et n'empêche pas deux producteurs concurrents de rédiger la même
source. `date_redac` sert uniquement à départager les versions d'un chemin connu.
Le registre historique continue à décrire ses versions sources ; ce n'est pas
un inventaire des seules pages actuellement rendues. Le compositeur privé de
newsletter conserve son refus propre des collisions : non modifié ici.

## Réemploi

Reconnaissance GitHub : `more-itertools/more-itertools`, licence **MIT**, dernier
push observé **14/10/2026 18:51:51 UTC** ; fonction `unique_everseen` de
`more_itertools/recipes.py` consultée. Sa conservation de la première occurrence
par clé ne vérifie ni identité ni ambiguïté temporelle : **non adoptée**.
Réemploi du préflight et des fixtures du moteur interne, sans dépendance nouvelle
ni copie de code tiers.

## Recette locale vérifiée

- Base : `1f74e0858d5dc32e57c6fe3ed79242e962aed56d`, worktree dédié hors Bureau.
- Test de build reproduisant l'erreur avant correction ; seconde phase rouge
  sur les permutations d'une ambiguïté ancienne, puis cinq contrats verts.
- **191 tests Python et quatre Node réussis**. Identités divergentes, dates
  naïves/invalides/égales, offsets, copies identiques, chemins distincts et
  non-mutation couverts ; anciens contrats archives/couvertures maintenus.
- `engine/run.py --essai --sans-redaction` dans une copie isolée : retour 0,
  **1 574 sorties**, aucune rédaction payante, aucun FTP ni post social.
  Certaines sources tierces répondent 403/429/502 : collecte partielle, pas une
  validation de leur disponibilité. Budget conservé à 30 €/mois.
- **391 fichiers data originaux inchangés** ; dans la copie d'essai, préfixe du
  journal et manifestes préservés, données de collecte non reprises.
- Sitemap de l'essai : **1 568 URL uniques**, chemin litigieux présent une fois.
- Pièces privées : chantier `croissance/2026-10-22/evidence/`, dont les premiers
  échecs, parents Git, corps HTTPS initial et empreintes de données.

## Publication

**En production, vérifiée le 22/10 à 14:35:53 UTC.** Code `fe1e1ba8f1e8e552cf877dc75ad286b0867938f3` ; run [39790842112](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39790842112).

- Étapes contrats, pipeline et sauvegarde : toutes `completed/success`.
  Déploiement journalisé à **14:27:14 UTC : 1 623 fichiers envoyés**, six
  nouvelles brèves et un article rédigés par le pipeline normal.
- Sauvegarde cloud `c814fb6`, fusion `116892ad7ba36aace7940fd23b496fb242280af7`
  relue ; les deux variantes de la brève restent présentes, code distant exact.
- Huit réponses HTTPS 200 conservées. **Trois HTML identiques octet pour octet**
  au rendu du commit sauvegardé : brève litigieuse, Actus et catalogue conservé.
  **RSS général et News sitemap identiques** au rendu à horloge de build commune.
- Sitemap : **1 575 URL uniques**, toutes les **1 191 URL de brèves** attendues,
  issues de 1 192 enregistrements conservés. Brève litigieuse présente une fois,
  rédaction de 10:21:40 UTC conservée ; aucune variante renommée ou supprimée.
- `version.txt` identique aux deux bornes du contrôle : build **13:56:12 UTC**.
  IndexNow 200 dans le journal : acceptation, pas preuve d'indexation.
- À ce relevé, l'API GitHub affiche encore le statut global `in_progress`, malgré
  toutes les étapes terminées ; logs globaux indisponibles. **Ne pas qualifier
  le workflow entier de réussi** sur ces seules étapes. Production et sauvegarde
  sont vérifiées séparément ; aucune relance aveugle.
- Complément : le journal direct du job `119866143292`, récupéré par l'API
  `actions/jobs/{id}/logs` malgré le statut global encore en attente, confirme
  **191 contrats réussis**, la variante conservée et le bilan réel de six brèves,
  un article et 1 623 envois. `gh run view --log` restait indisponible ; le corps
  direct est conservé dans `evidence/cloud-job.log`.

Pièces : `evidence/production-20261022T143546Z/result.json` et corps bruts dans le
chantier privé. Le bénéfice attendu est la reprise de la fraîcheur éditoriale,
pas une hausse de trafic démontrée. Aucun autre chantier intégré par cette mission.
