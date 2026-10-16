# Couvertures éditoriales automatiques — 16 octobre 2026

## Décision et périmètre

Action SEO #3, première action non intégrée après les grands aperçus et le news-sitemap. L'état du dépôt après pull (`bb976c1af93168e0df6e572480a9dcdf9bd91e4f`) confirme l'absence de couvertures par contenu. Le lot du matin a été relu, ses 57 artefacts contrôlés contre le manifeste, puis adapté et retesté ; les autres lots (podcast, B2B, hub) ne sont pas intégrés ici.

Un JPEG RGB 1280×720 par page éditoriale construite : 400 brèves et tous les articles. Le même fichier est affiché dans la page et déclaré dans Open Graph, Twitter et `NewsArticle.image`. Dimensions réservées, image principale non différée, CSS fluide, texte alternatif et légende explicites. Les index/annexes conservent leur image de marque. Aucun texte, date, source, prix, paiement ou sceau n'est modifié.

**Choix assumé : JPEG seul**, sans déclinaisons AVIF/WebP ni trois ratios. C'est une intégration fonctionnelle complète de la génération et de son affichage, pas l'ensemble des optimisations suggérées dans la proposition. Les variantes ne sont pas requises pour ce premier service. Les motifs sont des schémas thématiques originaux, pas des photographies ni des représentations fidèles d'événements. Sur l'instantané testé : **108 replis génériques sur 612 images**. Aucune garantie Discover, indexation, trafic ou amélioration des Core Web Vitals.

## Chasse open source et licences

- [python-pillow/Pillow](https://github.com/python-pillow/Pillow) : API GitHub relue le 16/10, dernier push observé `2026-10-16T08:09:40Z`. SPDX API `NOASSERTION`, mais LICENSE officielle vérifiée : **MIT-CMU permissive**. Bibliothèque retenue, wheel `Pillow==12.3.0`, aucun code tiers recopié. Primitives de dessin et encodeur JPEG audités dans la préparation.
- [vercel/satori](https://github.com/vercel/satori) : **MPL-2.0**, dernier push observé `2026-10-16T07:37:28Z` ; non adopté, chaîne Node/WASM inutile pour ce moteur Python.
- Documents de référence : [Google Discover](https://developers.google.com/search/docs/appearance/google-discover), [Article structured data](https://developers.google.com/search/docs/appearance/structured-data/article). Taille et balisage ne prouvent pas la pertinence d'une image.

## Cache et chemins d'exécution

Cache `.cache-couvertures/`, hors des assets nettoyés au build, non versionné et non publié. Clé incluant contenu, genre, version du dessin, Pillow et encodeurs ; empreinte et décodage vérifiés avant réemploi. Slugs non sûrs, doublons et liens symboliques refusés avant écriture des pages. Augmenter `couvertures.VERSION` après modification du dessin ou des réglages.

**Correctif d'intégration supplémentaire :** un runner cloud neuf changeait le `mtime` de tous les JPEG et aurait provoqué un renvoi intégral à chaque run. Un test a reproduit cet échec, puis un horodatage technique constant a été appliqué aux seuls JPEG adressés par contenu. Le déployeur garde ainsi la même empreinte taille/mtime avec cache froid ou chaud. Cet horodatage n'est jamais une date de publication ni une modification des preuves.

Cloud : installation depuis `requirements-couvertures.txt` puis suite Python avant le pipeline ; déclencheurs, droits, secrets et sauvegarde d'état inchangés. Local : Pillow 12.3.0 installé dans le site utilisateur de l'interpréteur Python.org `/usr/local/bin/python3` effectivement utilisé par le script de mise à jour ; import vérifié et recette exécutée avec cet interpréteur. Pas de modification de cron ni du script local. Pour un nouvel environnement, préférer un venv et `python -m pip install --only-binary=:all: -r requirements-couvertures.txt`.

## Recettes exécutées avant publication

- RED constaté sur la base sans générateur (couverture HTML absente), puis GREEN ; autre RED/GREEN pour l'empreinte FTP sur deux caches froids.
- **93 tests Python + 4 tests Node réussis**, copie isolée du SHA figé avec le patch final.
- Build réel `import construction; construction.construire()` : **633 sorties, dont 612 pages éditoriales** ; 400 brèves, 212 articles, 14 HTML non éditoriaux inchangés.
- Chaque JPEG décodé : 1280×720, **38 989 à 62 802 octets**, total **28 717 134 octets**. Cohérence HTML/OG/Twitter/JSON-LD vérifiée sur les 612 pages.
- Build froid **4,47 s**, chaud **1,67 s**, nouveau cache **4,55 s** sur ce Mac ; octets identiques dans les trois cas. Pas une mesure Linux ou terrain.
- Corps HTML historique identique après retrait de la seule figure ajoutée ; dates/citations JSON-LD intactes. Fichiers `data/` et sceaux inchangés dans la recette.
- Essai CLI isolé `--essai --sans-redaction`, code 0 : 633 sorties, aucune rédaction, aucun FTP, aucune annonce. Une source (Siècle Digital) répond 403 ; les autres contrôles ne masquent pas cet échec de collecte. Préfixe du journal et sceaux préservés ; aucun état d'essai repris en production.
- Chrome avec profil jetable, JavaScript désactivé : brève et article aux largeurs 390/1440, images chargées et aucun débordement horizontal. Le grand en-tête sticky mobile préexistant est conservé, pas masqué pour les captures. Le navigateur personnel verrouillé n'a pas été fermé.

Preuves détaillées conservées localement dans `crabe-chantiers/integration-couvertures/2026-10-16/` : `red.log`, `red-cache-froid.log`, `final/verification-20261016T085032545786Z/resultat.json`, journaux de tests, `pages-verifiees.json`, `essai-resultat.json`, captures et manifestes navigateur.

## Publication

- Code `d2dae09f912e4b33bbe80de42f2c1849d0ef9c1e` poussé ; neuf blobs relus par l'API GitHub et identiques au commit local.
- [Run 38876861356](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/38876861356) **réussi**, fin à **09:23:14 UTC**. Ubuntu/Python 3.12.15, Pillow 12.3.0 ; **93 tests réussis dans le cloud** avant publication.
- Pipeline : **634 sorties**, **1 266 fichiers envoyés dont 613 JPEG** ; 4 nouvelles brèves et 1 article ont été rédigés par le pipeline habituel. Durée pipeline **1 212 s** pour ce premier envoi des couvertures. Zéro publication Bluesky dans ce run.
- État du pipeline committé dans `7d4c96f6a0fcfa614d3e2d9adc650c67ce08c98a`, puis sauvegardé sur main par fusion `245675d`. Le contrôle reproductible utilise **le commit de sortie du pipeline avant fusion**, pas les données concurrentes ajoutées à main.
- Reconstruction propre de `7d4c96f` : **613 images**, toutes leurs empreintes taille/mtime concordent avec l'état FTP sauvegardé. Cela valide l'état consigné, pas à lui seul la présence distante ni les transferts du prochain run.
- **20 URL HTTPS contrôlées après succès** : 8 pages couvrant les six familles et les nouveaux contenus, leurs 8 images, accueil, CSS, news-sitemap et version. Les **8 HTML et 8 JPEG** sont identiques octet pour octet au rendu reconstruit ; JPEG décodés intégralement, MIME `image/jpeg`, 1280×720. CSS également identique. Preuve locale `https-resultat.json`, datée **09:24:11 UTC** ; réponses sauvegardées dans `https/`.
- Production inspectée sans JS sur mobile 390 px et desktop 1440 px : brève et article, images chargées, légendes visibles, aucun débordement horizontal. Captures `browser/live-*.png`, contrôles `browser/live.json`.

La génération automatique est livrée ; les variantes de formats/ratios restent non retenues et les motifs demeurent symboliques. Les dates visibles/JSON-LD hors image et la fermeture de l'autoindex appartiennent aux prochains chantiers. Aucun gain SEO ou trafic mesuré par cette livraison.
