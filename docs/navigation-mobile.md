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

## Livraison confirmée — 25/10, après 11:40 CET

Code **`ba95fa4d572f3713e41e8fbd91ff8f38f94fe267`**, quatre fichiers relus exactement via l'API GitHub après push. Une seule intégration fonctionnelle. L'avancée cloud avant push ne concernait que `data/` : rebase du seul correctif, puis **219 tests rejoués avec succès**. Aucun merge forcé de données/sceaux.

[Run `40182701180`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40182701180) **`completed/success`**, terminé à 10:40:16 UTC : **219 tests cloud**, pipeline et sauvegarde réussis. Log explicite `assets/style.css (20419 o)` ; bilan **1 847 fichiers envoyés**, 4 brèves/1 article produits par la routine existante, aucune publication Bluesky. Sauvegarde `030db4ee9bac9cb1975dd29b2d14f2a7a146d5f5`, intégrée dans `6a1200cc94dd76228e4add41e08244faf6e4783b`, ascendance vérifiée. Les attentes bornées du client n'étaient pas des échecs du workflow ; aucun redéclenchement ni annulation.

**Après la fin du run, à 10:40:52 UTC : 14 URL HTTPS canoniques en 200**, CSS identique octet pour octet au correctif ; en-têtes HTML de **dix pages** identiques à la base (destinations, textes et ordre DOM préservés). Accueil, Pack, article, podcast, Actus, articles, Skills, Pro, manifeste, transparence, RSS, sitemap, version et CSS contrôlés. Ceci ne prétend pas comparer le contenu éditorial dynamique complet de toutes ces pages.

**387 contrôles navigateur publics sur 36 configurations** après mise à disposition de la CSS, puis **43/43 rejoués sur les quatre pages à 320 px après la fin du pipeline**. Géométrie, Tab/Shift+Tab, Entrée sur le lien d'évitement, focus et défilement sous header réel ; souris/destinations testées dans le build local, pas répétées pour tous les liens publics. Captures mobile et desktop relues. Premier lanceur public interrompu sur une largeur `901/2 = 450,5 px` refusée par Playwright : preuve conservée, reprise neuve aux largeurs paires et test distinct à 901 px réussis ; pas un défaut du site ni un arrondi silencieux.

Essai supplémentaire du code livré : `engine/run.py --essai --sans-redaction`, copie neuve isolée, retour 0 et 1 802 pages ; aucun transfert, rédaction ou post. Collecte partielle : 403 Siècle Digital et 429 Reddit-Claude conservés. Manifestes identiques, préfixe du journal intact (ajouts locaux attendus), aucune donnée de cette recette importée. Aucun autre chantier, cron, secret, serveur ou suivi ajouté.

Limites : les débordements hors navigation aux très petites largeurs, les inconnus des archives et la concurrence opérationnelle restent distincts. Ni conformité globale ni hausse d'audience revendiquées. L'attente cloud de la mission du 24 est également levée : run `40116677135` relu `completed/success`, sans deuxième intégration.

Pièces privées : `crabe-chantiers/site/2026-10-25-navigation-mobile/` — manifeste de préparation vérifié, source/patch de la recette navigateur, rouge/vert, inventaires des deux builds, sorties unitaires, JSON DOM et captures. Les copies complètes de recette restent hors dépôt public.
