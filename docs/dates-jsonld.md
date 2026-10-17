# Dates JSON-LD : ne pas confondre rédaction et publication

Audit de la base `12b60dc0ed4179fe2c568b2a8fb2309e381ae8b3` (17 octobre 2026).

## Contrat ciblé

- `date_source` vient de la date du flux tiers ; le collecteur peut choisir `updated`
  à défaut de `pubDate` / `published`, et ne conserve pas le nom de la balise.
- `date_redac` des brèves et `date` des articles sont créées à la rédaction,
  **avant construction et déploiement** (`engine/redaction.py`).
- Le registre `publications.jsonl` redérive ces dates ; ses empreintes de contenu
  et les sceaux ne les transforment pas en instants de première mise en ligne.
  Le journal de déploiement est agrégé, sans reçu HTTPS par URL/version.
- Les deux gabarits passent donc `None` pour `datePublished` et `dateModified`.
  `jsonld_item()` omet séparément chaque date inconnue, sans valeur `null`, chaîne
  vide, repli sur la publication, date du build ou nouveau champ historique.
  Les arguments du sérialiseur ne sont pas un validateur de preuves : tout futur
  appel avec une date doit établir sa provenance avant de l'utiliser.

Schema.org définit la première publication et la dernière modification.[16][9]
Google précise que les propriétés Article sont recommandées, non obligatoires :
omettre une date non établie évite une assertion plus forte que les données.[10]
Cette prudence n'est ni une garantie d'éligibilité Google News, ni une promesse SEO.

## Préservation et limite explicite

Dates HTML `<time>` et affichage Europe/Paris conservés exactement ; sources,
textes, images, liens, flux RSS, sitemaps et Open Graph inchangés. Le correctif
ne change que les dates de l'objet NewsArticle. Les anciennes assertions de
conservation des dates JSON-LD dans les tests HTML/citations sont remplacées par
l'omission ; toutes leurs assertions d'affichage/citations restent actives.

**Dette distincte, non résolue ici :** `article:published_time` Open Graph reprend
encore `date` de rédaction ; RSS `pubDate`, sitemap `lastmod` et news-sitemap
réemploient les dates éditoriales. Leur présence n'atteste pas une publication.
Google exige pour `news:publication_date` la première publication sur notre site,
non la date d'ajout au sitemap.[12] L'audit ne valide donc pas cette sémantique
existante ; un lot séparé devra arbitrer omission des entrées News sans preuve
et compatibilité des flux. Ne pas supprimer seulement la balise requise d'une
entrée News, ni remplacer sa valeur par l'heure du build.

## Conditions avant toute réactivation

Établir une preuve par URL canonique et version de contenu, distinguer un reçu
de mise en ligne d'une simple observation ultérieure, conserver séparément les
instants de création, publication et modification éditoriale. Un GET 200 aujourd'hui,
un Last-Modified, un commit ou une réussite FTP ne prouvent pas à eux seuls la
première publication historique. Aucune rétrodatation, migration de données,
réécriture du journal ou réparation de sceau n'est incluse dans ce lot.

Tests : `python3 -B -m unittest discover -s tests -p 'test_dates*.py' -v`, puis
suite complète ; audit/comparaison avant-après rejouables dans le dossier privé
du chantier. Aucun code tiers copié ; inspirations de structure Next SEO et
Jekyll SEO Tag (MIT), mais leur repli modification → publication est écarté.[2][6]
Licences relues dans les dépôts, sans ajout de dépendance.[1][5]

## Recette d'intégration du 17 octobre 2026

Premier chantier SEO restant selon l'ordre d'impact : volet dates de #4. Les
couvertures et `<time>` sont déjà livrés ; aucun lot podcast/B2B/newsletter ni
autoindex n'est intégré dans cette livraison. Le patch du matin est réemployé
après contrôle de ses **127 artefacts** (taille et SHA-256), sans importer ses données.

- Base d'intégration : `5ff210207655265faf57faa5bdec9322d2ce5e38`.
- RED puis GREEN du nouveau contrat rejoués ; **105 tests Python + 4 Node** réussis.
  Les 105 tests passent aussi depuis le clone d'intégration. Un premier essai
  de cette seconde commande sans `TMPDIR` a rencontré 15 erreurs de confinement
  dues au symlink macOS `/var` ; relance avec scratch explicite, aucun garde-fou
  ni code modifié pour les masquer.
- Deux vrais `construction.construire()` à horloge de recette identique :
  **1 310 fichiers**, dont **635 pages éditoriales** ne différant que par les deux
  dates JSON-LD retirées ; **675 autres fichiers identiques**. Corps, dates visibles,
  images, citations et autres métadonnées conservés. RSS et sitemaps inchangés.
- **266 fichiers `data/` inchangés** dans les copies de build et le clone réel.
- Vrai CLI `--essai --sans-redaction` en troisième copie : retour 0, aucune
  rédaction, aucun envoi FTP/social ; journal initial préservé, registre et sceaux
  identiques. Collecte partielle : Siècle Digital 403, Reddit Claude 429 ; clé IA
  volontairement absente. Aucun état de recette repris en production.
- Les anomalies de liens des manifestes du 10 et du 11 octobre préexistent et
  restent non réparées ; la recette ne certifie pas toute la chaîne historique.

Recette et logs privés : `crabe-chantiers/dates-jsonld/integration-2026-10-17/`,
résultat `dates-jsonld-_2nh3bk8/resultat.json`. Publication cloud/HTTPS à confirmer.

Provenance réinterrogée le 17/10 : `garmeeh/next-seo` (**MIT**, dernier push
`2026-07-29T19:47:06Z`) et `jekyll/jekyll-seo-tag` (**MIT**, dernier push
`2026-09-29T23:58:38Z`). Sources à SHA ci-dessous ; aucun code tiers incorporé.
La recommandation initiale « headline ≤ 110 » n'est pas imposée ici : conserver
le titre réel, sans le tronquer pour un seuil non démontré comme obligatoire.
L'ajout d'`author.url` reste une amélioration distincte, pas une condition de ce correctif.

## Sources

[1] https://raw.githubusercontent.com/garmeeh/next-seo/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4/LICENSE.md
[2] https://raw.githubusercontent.com/garmeeh/next-seo/738ef7e774ee6216f6e90c26a3b5b99dd5d166b4/src/components/ArticleJsonLd.tsx
[5] https://raw.githubusercontent.com/jekyll/jekyll-seo-tag/ce38a841785d18dabb58443dd12d0616f39c2cc1/LICENSE.txt
[6] https://raw.githubusercontent.com/jekyll/jekyll-seo-tag/ce38a841785d18dabb58443dd12d0616f39c2cc1/lib/jekyll-seo-tag/drop.rb
[9] https://schema.org/dateModified
[10] https://developers.google.com/search/docs/appearance/structured-data/article
[12] https://developers.google.com/search/docs/crawling-indexing/sitemaps/news-sitemap
[16] https://schema.org/datePublished
