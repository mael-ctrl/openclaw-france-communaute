# Retour au formulaire de La Brève — 9 novembre 2026

## Une seule nouvelle intégration

Le lien natif **« Retour au formulaire de La Brève »**, dans la section newsletter de `/transparence/`, mène à `/#la-breve`. Aucun nouveau formulaire, JavaScript, mesure d'événement ou changement d'abonnement. Le lien de fin de lecture déjà publié n'est pas recréé.

Choix : premier candidat prêt du relais P2 du 9 novembre et de la roadmap, après requalification. La priorité SEO #6 fait l'objet d'une clôture séparée, sans réapplication de son code. #1–5 sont déjà traités dans les limites documentées (archives inconnues et alias OVH distincts). #7, cache/compression, reste **non livré** : noms d'assets non tous versionnés et règles distantes non qualifiées ; ne pas appliquer `immutable` globalement aux ressources modifiables ni mêler une demi-refonte d'hébergement à ce lien.

## Réemploi et admission

- Pull du clone partagé tenté, refusé pour fichiers non fusionnés ; aucun reset, abort, stash ou fusion des données. Worktree séparé sur **`189371814fdb918c81f1111eebc7deb33941bd0e`**, pull réussi ici seulement.
- Lecture du rapport de vague du 9 et vérification du lot privé : **453 références de livrables**, entrées et **395 références historiques intactes**. Le patch HTML reste applicable ; source produit identique au candidat. Test réemployé, mis en forme et diagnostic neutralisé, avec assertion complémentaire d'unicité de l'ancre.
- Chasse GitHub réactualisée : [mdn/learning-area](https://github.com/mdn/learning-area/tree/21973263ba859ff3477919087b488157f9d618a6), **CC0-1.0**, dernier push observé le 20/10/2026 à 11:04:14 UTC. Exemples de formulaires natifs consultés comme référence sémantique ; aucune bibliothèque ou source amont copiée/installée. Réemploi des patches et du banc local distinct de cette référence.

## Contrôles réellement rejoués

- Rouge pertinent observé : retour absent (`0 != 1`) ; vert après ajout d'une seule ligne dans `engine/annexes.py`.
- **314 tests Python + huit Node réussis**, suite complète originale dans une copie isolée, sans modifier les fixtures.
- Deux builds complets à horloge commune : **2 398 sorties de pages**, **4 798 fichiers** ; seule `transparence/index.html` change. Retirer la ligne ajoutée redonne exactement la page initiale ; **4 797 fichiers identiques**, **716 fichiers d'entrée du worktree préservés**. Aucun catalogue/manifestes/journal de recette importé.
- `--essai --sans-redaction` dans la copie isolée : code 0, aucune rédaction/transfert/publication Bluesky ; manifestes identiques et préfixe du journal intact. Collecte partielle : Usine Digitale 403 et Reddit Claude 429, conservés dans le log ; aucune donnée de recette importée.
- **390 assertions Chromium, huit parcours** sur le vrai build courant, sans JS à **320/1 280 px** : article/brève → formulaire → confidentialité → retour par clic ou Tab/Entrée. Contours de focus, géométrie et absence de débordement contrôlés ; premier Tab après le lien de retour sur l'email. Captures mobile/desktop relues.
- Réseau OS refusé pour le banc local, toutes les pages servies par interception des fichiers ; **aucun POST, abonnement tenté ou ressource externe**. Formulaire/action/méthode/honeypot/prix/ressources inchangés.

Les restaurations variables de l'historique ne sont pas présentées comme corrigées. Pas de test Safari/Firefox, de certification d'accessibilité, de contrôle courant des abonnés, du double opt-in backend, de la délivrabilité ni de la désinscription. Aucun gain de conversion ou d'audience mesuré.

## Publication

Au commit d'intégration : code et recettes locaux complets ; **cloud, sauvegarde et recette HTTPS à confirmer** dans la clôture ci-dessous. Le service tiers n'est jamais appelé par la recette.

Preuves privées : `crabe-chantiers/site/2026-11-09/` — `rouge.log`, `suite-complete.log`, `suite-node.log`, `recette.json`, `browser-local/`. Les remises de préparation ne sont pas modifiées ; aucun script d'exploitation, cron, cache/checkpoint, paiement ou prospection activé.
