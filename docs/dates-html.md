# Dates HTML sémantiques — croissance du 16 octobre 2026

## Une seule amélioration

Les cartes, la une, les pages de brèves et d'articles et leurs signatures utilisent
maintenant une même balise `<time datetime="…">`. La valeur machine conserve
**exactement la date enregistrée** ; l'affichage indique l'heure de Paris, avec
prise en compte du passage été/hiver par `zoneinfo`, sans JavaScript.

Une date absente n'engendre pas de balise vide. Une date invalide ou sans fuseau
reste un texte échappé, sans fabriquer d'instant à partir du fuseau de la machine.
Aucune dépendance ajoutée, aucun appel de rédaction supplémentaire.

**Périmètre délibérément limité :** les champs choisis restent ceux du moteur :
`date_source` (à défaut `date_redac`) pour les métadonnées visibles des brèves,
`date_redac` pour leur signature, `date` pour les articles. Le JSON-LD, les dates
Open Graph, les flux, les sitemaps, les textes éditoriaux, les images et les données
historiques ne sont pas réécrits. Ce lot ne clôt pas l'audit de la sémantique
`datePublished`/`dateModified` des brèves ; la date de source n'est pas une preuve
de première mise en ligne sur notre site.

## Reconnaissance et provenance

- Dépôt examiné : [jekyll/jekyll-seo-tag](https://github.com/jekyll/jekyll-seo-tag),
  licence **MIT**, dernier push renvoyé par l'API GitHub au contrôle du 16/10 :
  **2026-09-29T23:58:38Z**. Lecture de `lib/jekyll-seo-tag/drop.rb` : dates de
  publication/modification tirées des données de page, sans fabriquer une date
  de build. **Non adopté** : pile Ruby/Jekyll inutile pour notre générateur Python.
  Aucune copie de code ; réemploi de `jolie_date()` et stdlib existantes.
- [MDN — élément time](https://developer.mozilla.org/fr/docs/Web/HTML/Reference/Elements/time) :
  `datetime` fournit un format machine distinct de l'affichage humain.
- [Google Search Central — dates](https://developers.google.com/search/docs/appearance/publication-dates?hl=fr) :
  cohérence des instants et fuseaux, prise en compte de l'heure d'été ; l'affichage
  effectif d'une date dans les résultats reste décidé par Google.

## Recette avant livraison

- Base figée : `530b50d165b75ffd0de0574d327097a7b1a3ed02` ; travail sur clone isolé
  hors Bureau (ce dernier illisible depuis le cron).
- TDD : attribut `datetime` manquant reproduit, puis dates malformées/sans fuseau
  et emplacements non raccordés reproduits avant correction.
- **99 tests Python + 4 tests Node réussis**, dont 6 contrats de dates : heure
  été/hiver, changement de jour, deux instants de l'heure répétée d'octobre,
  décalage source non UTC, repli, échappement et dates absentes.
- Sur les données réelles : **400 brèves et 216 articles** comparés à la base ;
  HTML strictement identique après neutralisation des seuls affichages de dates.
  JSON-LD préservé. **637 fichiers de build**, données sources inchangées.
- `engine/run.py --essai --sans-redaction` dans une seconde copie : code 0,
  aucune rédaction, aucun FTP/social ; sceaux identiques et préfixe du journal
  intact. Collecte partielle : deux flux HN en 502, Siècle Digital en 403,
  Reddit Claude en 429 ; ce ne sont pas des erreurs du changement de dates.
- Chromium isolé, JavaScript désactivé : accueil, actus, index articles, brève
  et article aux largeurs **390 et 1440 px** ; dates présentes, aucun débordement
  horizontal. Date mobile et date desktop relues visuellement.
- Pour la recette macOS, `TMPDIR` est explicitement dirigé vers le scratch Hermes :
  `/var` est un lien symbolique et le garde-fou des couvertures rejette ces chemins.

## Effet attendu et limites

Dates moins ambiguës pour le lectorat francophone et exploitables directement par
les outils qui lisent le HTML. Aucun gain de classement, de trafic ou d'apparence
dans Google n'est mesuré ni garanti. La livraison cloud/HTTPS est à vérifier après
push ; les preuves de production seront consignées ci-dessous.
