# Sommaire natif des articles — 3 novembre 2026

## Choix du chantier unique

Relais P2 de la roadmap du 2 novembre et lot préparatoire du 3 : sommaire des articles, encore absent du moteur et du rendu de la base `49cfea858bc14fe4e4e8d0a1fcec1da3b0be7ea6`. Les images, dates visibles, JSON-LD et catalogue déjà livrés ne sont pas refaits. Le contrôle de clôture de l'auteur est séparé et ne modifie pas son code. Aucun lot cache FTP, wrapper, newsletter, archive historique ou préchargement n'est activé.

Les trois patches privés du 2 novembre, requalifiés le 3, sont réemployés sans modification : `engine/sommaire.py`, raccordement de `page_article()`, styles préfixés et neuf tests. Le générateur ajoute un `<details>` fermé et une liste de liens natifs seulement si le corps comporte au moins trois h2 éligibles. Les titres, IDs existants et le contenu restent inchangés ; les seules ancres absentes sont ajoutées avec préfixe `section-`, dédoublonnées contre toute la page. Aucun JavaScript ni dépendance nouvelle.

## Réemploi et provenance

[allejo/jekyll-toc](https://github.com/allejo/jekyll-toc/tree/45a53cbc5ced9f89a712f939d8d2f0b219162af6), HEAD et trois blobs relus indépendamment le 03/11. Dernier push API : **15/01/2024 23:43:51 UTC** ; licence API non renseignée. Le [source](https://github.com/allejo/jekyll-toc/blob/45a53cbc5ced9f89a712f939d8d2f0b219162af6/_includes/toc.html) contient une autorisation MIT ; fichiers MIT et BSD-3-Clause présents. OID Git et SHA-256 concordants. **Concept seulement : aucun code Liquid/Jekyll copié ni exécuté.** L'implémentation Python est indépendante et réemploie les préparations locales vérifiées.

## Tests et builds avant livraison

- Rouge fonctionnel reproduit : trois vrais titres sans sommaire sur la base ; neuf tests dédiés verts après application.
- **286 tests Python + huit Node réussis**, suite originale complète `python3 -m unittest discover -s tests` dans une copie isolée ; aucune fixture `mktemp` modifiée. Cette recette ordinaire n'est pas le replay macOS confiné des préparations, dont les refus restent conservés dans leur lot.
- Deux vrais builds `construction.construire()` hors réseau, horloge commune de comparaison **03/11 à 10:15 UTC**, pas une heure de publication : **4 453 fichiers**, mêmes chemins. **502 articles enrichis sur 503** ; un article court intact. Après retrait du seul sommaire et des IDs ajoutés, tous les HTML articles sont identiques. **1 684 brèves inchangées**, tous les flux/sitemaps et les autres sorties exacts ; seule autre différence : le bloc CSS prévu. **3 950 fichiers identiques** au total.
- **650 fichiers data/contenus/sites préservés** après suites et builds. L'essai isolé `--essai --sans-redaction` réussit ensuite, sans reprise de ses données.
- **99 contrôles Chromium / 12 configurations** sans JavaScript : deux articles réels, un article court, une brève, à 320/390/1 440 px. Tab/Shift+Tab, Entrée/Espace, clics sur toutes les ancres échantillonnées, unicité des cibles, visibilité sous l'en-tête et absence de débordement horizontal. Captures mobile/ordinateur relues. Ni lecteur d'écran, ni Safari/Firefox, ni mobile physique éprouvés.

Pièces privées : `crabe-chantiers/integrations/sommaire-20261103/` (manifestes de provenance vérifiés, rouge, suites, inventaires des deux builds, comparaison HTML complète, données protégées, recette navigateur et essai).

Pull initial partagé refusé (128, données non fusionnées), état laissé intact. Intégration dans un worktree propre du même dépôt sur `origin/main`, pull réussi ici seulement. Aucun reset, abandon de rebase, fusion forcée de données ou modification des sceaux.

## Déploiement

**En attente au commit initial :** workflow `maj.yml`, contrats/transfert/sauvegarde et comparaison HTTPS sur le descendant sauvegardé. Le code testé et la recette locale ne sont pas une preuve de publication.

## Limites

Le helper lit un sous-ensemble fermé avec HTMLParser ; ce n'est ni un parser HTML5 complet, ni un sanitizer. Un fragment inconnu ou ambigu reste entièrement inchangé sans sommaire. Le seuil porte sur les sections, pas sur une durée de lecture ; les IDs générés restent stables pour un contenu identique, pas après réécriture éditoriale. Les classes CSS arbitraires ne sont pas interprétées.

Ce changement facilite la navigation, sans gain d'audience ou de référencement mesuré. Il ne valide pas les faits des articles ni la conformité globale. Les courses local/cloud, le timeout du pipeline et les anciennes pages absentes du catalogue restent des dettes distinctes.
