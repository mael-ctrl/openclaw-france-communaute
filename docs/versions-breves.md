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

Recette locale terminée ; publication cloud et lecture HTTPS à confirmer dans
la mise à jour de cette section. Aucun gain de trafic revendiqué.
