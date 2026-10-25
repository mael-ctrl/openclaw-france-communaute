# Navigation mobile — correctif du 25 octobre 2026

## Choix unique et provenance

Priorité P2 de la roadmap du 24 au soir et premier lot prêt de la vague du 25 : corriger le menu rogné à 320 px. Les couvertures, dates JSON-LD, catalogue des sources conservées et fermetures ciblées d'autoindex sont déjà intégrés ; les inconnus historiques et l'alias OVH restent ouverts, sans restauration ni purge improvisée. Le wrapper externe et le prototype de mesure du Pack ne sont pas intégrés ici.

Pull initial du clone opérationnel réussi ; préparation/livraison dans un worktree séparé sur `origin/main`, base `9433cae412d48e8ebacebbc77bf4850356fb367d`. Les 966 entrées du manifeste de la vague du matin ont été comparées à leurs fichiers avant reprise. Seul le patch CSS du lot navigation est appliqué, avec un nouveau contrat stdlib et cette documentation. Aucune donnée de fixture n'est copiée en production.

Chasse GitHub relue puis métadonnées revérifiées : [alphagov/govuk-frontend](https://github.com/alphagov/govuk-frontend), MIT, dernier push observé `2026-10-23T15:26:02Z`. Référence épinglée : [`service-navigation/_mixin.scss` à `69b59f5`](https://github.com/alphagov/govuk-frontend/blob/69b59f558003f05e7f444eae1c6f5bc570cf7226/packages/govuk-frontend/src/govuk/components/service-navigation/_mixin.scss). Réemploi conceptuel du retour à la ligne ; CSS maison, aucun code Sass copié, aucun framework ni paquet de production ajouté.

## Correction bornée

- Navigation sur sa propre ligne flex, sans rétrécissement ni défilement horizontal imposé ; texte long et marque peuvent revenir à la ligne.
- Ordre visuel aligné sur le DOM : marque, navigation, actions. Destinations et textes inchangés ; aucun menu caché exigeant JavaScript.
- Header mobile ou de faible hauteur dans le flux normal ; sticky desktop conservé, hauteur souple et espace de défilement pour le lien d'évitement.
- Podcast : gabarit distinct inchangé et toujours sans script/iframe. Bandeau décoratif toujours hors de Tab.

## Recette locale réellement exécutée

`python3 -m unittest discover -s tests` : **219 tests réussis** ; `node --test tests/test_pack_copie.cjs` : **quatre réussis**. Le nouveau test `test_navigation_mobile.py` échoue avant le patch sur l'absence d'une ligne flex non rétrécissable, puis passe après. Il protège le contrat CSS, pas une géométrie de navigateur simulée.

Deux extractions isolées du SHA de base dans le scratch Hermes, deux `construction.construire()` à horloge commune de recette : **3 598 sorties**, **3 597 identiques**, seule `assets/style.css` diffère ; **456 fichiers de données préservés**. Horloge figée uniquement en mémoire dans la recette, jamais dans les dates de production. Aucun moteur Python modifié.

Chromium existant, sans JavaScript et avec mouvement réduit : quatre pages réelles construites (accueil, Pack, article, podcast), 320/390/768/1 440 px et équivalent reflow 200 %. **872 contrôles : 51 refus avant, 872 réussites après.** Complément réel à 901 px : **109/109**. Total après correction : **981 contrôles sur 36 configurations**. Tab, Shift+Tab, Entrée, clic, visibilité des liens/focus, évitement, ordre et sticky sont mesurés sous le vrai header. Aucun masquage de l'en-tête ni neutralisation du style fautif. Les liens internes utilisent les vraies pages du build ; aucune destination tierce/paiement visitée.

Captures 320 px avant/après et desktop après évitement relues visuellement : les libellés rognés à droite deviennent intégralement lisibles sur trois lignes. Les débordements de contenu hors navigation à 160/195 CSS px sont conservés dans les mesures : **pas de conformité WCAG globale revendiquée**. Le reflow simule une largeur CSS divisée par deux, pas un geste de zoom mobile. Aucun gain de trafic/conversion mesuré.

## Livraison

Recette locale acquise ; commit/push, run cloud et vérification HTTPS à consigner après leur exécution. Cette section intermédiaire ne vaut pas preuve de production.

Pièces privées : `crabe-chantiers/site/2026-10-25-navigation-mobile/` — manifeste de préparation vérifié, source/patch de la recette navigateur, rouge/vert, inventaires des deux builds, sorties unitaires, JSON DOM et captures. Les copies complètes de recette restent hors dépôt public.
