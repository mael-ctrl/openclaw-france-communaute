# Croissance du 12 novembre — exclure les dates futures du sitemap News

## Une correction bornée

`construction.news_sitemap_xml()` capture une seule fois l'heure UTC et ne retient
que les dates dans la fenêtre inclusive `[maintenant − 48 h, maintenant]`.
Articles et brèves sont couverts ; tri, limites, titres, URL et données historiques
sont préservés. Aucun nouveau flux, moteur, quota ou coût de rédaction ajouté.

Effet attendu : ne plus transmettre à Google News des entrées datées dans le futur.
Ce contrôle ne prouve ni indexation, ni gain d'audience, ni première publication.
La sémantique héritée `article.date` / `date_source || date_redac` reste à qualifier ;
aucune date n'a été inventée ou corrigée pour la rendre conforme.

## Réemploi et provenance

Réemploi du petit lot préparé `indexation/2026-11-12-dates-futures`, et non d'une
nouvelle source RSS : priorité P1 du rapport d'orchestration du jour, encore absente
sur la base d'intégration `bc93647d0a3bb682ecda9f73b4753bf520ce734e`.
814 pièces du manifeste du lot puis 978 références correspondantes du manifeste
parent vérifiées par empreinte avant intégration. Aucun fichier de recette repris.

Chasse GitHub requalifiée :
[callowayproject/django-news-sitemaps](https://github.com/callowayproject/django-news-sitemaps)
à `55da6b72580dd6d79380f2bb17240e7afa00555a`, Apache-2.0, archivé,
dernier push observé `2017-10-01T02:28:28Z`. Licence et sources épinglées conservées
dans le lot ; métadonnées relues le 12 novembre. Framework non adopté, aucun code
amont copié ni exécuté : le moteur local suffit. Référence de portée :
[documentation Google News](https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap).

## Vérification exécutée pour cette intégration

- Bureau inaccessible à Git ; pull du clone opérationnel refusé pour conflits
  préexistants. Aucun reset, abort, stash, fusion ou réparation implicite.
- Worktree propre hors Bureau, fetch et pull réussis ici seulement.
- Dix tests nouveaux exécutés avant le correctif : échecs sur les dates futures
  reproduits ; mêmes tests verts après le patch minimal.
- **348 tests Python réussis**, puis vrai `engine/run.py --essai --sans-redaction`
  dans une copie isolée : **2 484 pages**, zéro rédaction, transfert ou post social.
  Clé chargée pour lire le solde uniquement ; plafond 30 €/mois inchangé.
- Deux erreurs tierces pendant l'essai : HN OpenClaw 502, L'Usine Digitale 403.
  Elles ne sont ni masquées ni présentées comme corrigées par cette livraison.
- 55 fichiers de preuves/publications identiques et préfixe du journal intact.
  Aucune donnée de l'essai importée dans le dépôt de production.

Pièces privées : `crabe-chantiers/croissance/2026-11-12/`, dont `red.log` et
`validation/{green.log,suite.log,essai.log,result.json}`.
Au commit initial : publication cloud et contrôle HTTPS restent à confirmer.
