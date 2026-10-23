# Bandeau : navigation clavier — 23 octobre 2026

## Périmètre et choix

Une seule amélioration : retirer les liens décoratifs du bandeau de l'ordre séquentiel Tab/Shift+Tab, sans enlever leurs clics. Le conteneur était déjà `aria-hidden="true"`, mais ses vingt ancres restaient tabulables. Ajout de `tabindex="-1"` avant duplication dans `bandeau_defilant()` ; aucun autre corps de fonction, CSS, JavaScript, texte, date, flux ou CTA changé.

C'est le premier lot prêt du relais P2 du 22 au soir et du rapport de la vague du 22. Les priorités SEO #1–4 et la couverture des sources conservées de #5 sont déjà livrées ; la fermeture de l'alias OVH et les identités historiques inconnues restent des chantiers distincts, non résolus par ce correctif. Le patch RSS n'est pas intégré.

## Réemploi

Lot privé `accessibilite/2026-10-22`, 97 pièces vérifiées avant reprise. Patch ciblé et trois contrats unitaires réemployés sur la base courante `10f1882485e20dee15c051b49c52ef85edf9e61b`.

Reconnaissance GitHub du 23 : [axe-core](https://github.com/dequelabs/axe-core), MPL-2.0, dernier push observé le 22/10 à 22:11:27 UTC, référence de règle seulement ; [Playwright](https://github.com/microsoft/playwright), Apache-2.0, push le 22/10 à 23:29:21 UTC, outil de recette privé déjà installé. Aucun code axe-core ni dépendance de production ajouté.

## Recette rejouée sur la base courante

- Rouge unitaire : quatre sous-cas échouent uniquement parce que les liens masqués sont encore dans Tab ; vert : trois méthodes réussies.
- Suite complète : **194 tests Python + 4 Node réussis**.
- Deux appels réels à `construction.construire()` dans une copie scratch, horloge commune : **3 335 sorties**, **3 334 identiques** ; seule la page d'accueil change, exactement par ses vingt attributs. **410 fichiers de données inchangés**.
- Chromium 155, 1 440×1 000 et 390×844, avec/sans JS, mouvement normal/réduit : défaut reproduit dans les huit configurations, vingt arrêts masqués dans chaque sens avant ; zéro après. **144 contrôles après correction**, ordre des autres liens, dix destinations accessibles via Actus, Entrée sur une brève, clic du bandeau et animation conservés. Deux captures avant/après identiques en octets et relues visuellement.
- Essai isolé `--essai --sans-redaction` : retour 0, aucun transfert/rédaction/post ; quatre éléments collectés. Trois sources en erreur (timeout, 403, 429), sans les qualifier de collecte complète. Manifestes et préfixe du journal préservés ; aucune donnée de recette reprise.

Le premier passage navigateur a rencontré ENOSPC sur une capture : résultat initial conservé, second passage dans un dossier neuf réussi. Aucune purge d'anciens lots. Le clone partagé divergeait entre sa mise à jour locale et le cloud : son pull `--ff-only` a été refusé. Intégration dans un worktree du même dépôt à partir d'`origin/main`, avec pull réussi ; aucun arbitrage ni fusion de données/sceaux et aucun commit local abandonné.

## Publication

Recette locale terminée ; publication cloud et vérification HTTPS à consigner après exécution, sans succès anticipé.

Pièces privées datées : `crabe-chantiers/accessibilite/2026-10-23-integration/` (base, empreintes, rouge/vert, suites, builds, essai, navigateur et captures).

## Limites

Ce correctif porte sur la navigation séquentielle : `tabindex=-1` n'interdit pas tout focus programmatique. Aucun audit VoiceOver/NVDA, Safari/Firefox, appareil physique ni conformité WCAG/RGAA globale. L'en-tête mobile haut et le mécanisme de pause préexistant ne sont pas redessinés. Aucun gain de trafic, de conversion ou de référencement mesuré.
