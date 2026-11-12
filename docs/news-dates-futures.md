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
Au commit initial : publication cloud et contrôle HTTPS restaient à confirmer.

## Comparaison et publication ciblée vérifiées

Commit moteur : `9d5cb715b2294b088cafab6e7ca5cc69505dd610`. Les trois blobs ont été
relus identiques sur `main` distant. Deux builds complets à horloge commune avec
les données exactes de la base : **4 977 fichiers identiques sur 4 978** ; seul
`news-sitemap.xml` change. 603 fichiers de données intacts, moteur identique hors
fonction News. À l'horloge de recette du 11 à 23:53 UTC, 22 dates du snapshot du 12
sont futures : ce résultat de replay n'est PAS un constat de 22 erreurs en production.

Le run antérieur `43225412389`, sur l'ancien moteur, a été attendu : **annulé pendant
pipeline**, sauvegarde ignorée, 1 575 transferts consignés, dernier chemin affiché
sous `breves/meta-…`. Aucune annulation ni modification du workflow par cette mission.
Le wrapper de suivi local a lui-même subi un timeout ; le statut distant a été
relu séparément. Le clone opérationnel et cette dette d'exploitation restent ouverts.

Après la fin du run ancien, publication **du seul `news-sitemap.xml`** à 14:03 UTC :
base HTTPS/SFTP exactement égale au rendu ancien des données figées, à l'heure du
`version.txt` servi (10:29:07 UTC). Nouveau rendu par le moteur corrigé, à 14:03:27 UTC :
**78 URL, toutes dans la fenêtre ; zéro retrait nécessaire, octets inchangés**.
C'est une garde prospective intégrée, pas une correction de 78 dates fautives.

Préflight paginé des runs actifs : seul le run du moteur corrigé était actif.
Clé hôte épinglée avant secret, sauvegardes, staging exclusif `.part` relu,
renommage et relecture SFTP ; racine Apache, robots, sitemap général et version
préservés. Deux lectures HTTPS canoniques identiques à **14:03:34 UTC**, empreinte
`fbfb1a1d78281c96c4b140bc127e182d45b8e1eddb38c32be7eaae5502cfcb9a`.
Pièces : `comparaison/` et `livraison-news-02/`. Premier échec d'import Pillow du
venv SFTP conservé : dépendance existante exposée à ce seul processus, sans installation.

Le dispatch `43225735528` porte exactement le commit moteur : **contrats cloud
réussis à 14:02:52 UTC**, pipeline en cours au contrôle suivant. Publication ciblée
confirmée, mais déploiement intégral et sauvegarde finale de ce run non clôturés.
La livraison voisine du hub `6792471` conserve le moteur ; elle n'est pas incluse
dans le compteur de tests ci-dessus. Aucun nouveau cron ni budget modifié.
