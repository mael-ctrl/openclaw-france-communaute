# Veille : blog officiel LangChain

## Une seule évolution — 30 octobre 2026

Ajout de `https://www.langchain.com/blog/rss.xml` dans `data/sources.json` :
anglais, priorité 4. Les 23 sources existantes sont conservées à l'identique ;
le catalogue contient 24 flux. Réemploi du collecteur et de l'export OPML existants,
sans dépendance ni modification des quotas, du style ou du plafond DeepSeek de 30 €/mois.

Effet attendu : suivre à la source les annonces et retours techniques sur les agents,
LangChain et LangGraph. Le blog du fournisseur reste une source intéressée : ses
comparatifs et performances ne constituent pas une validation indépendante.
Aucun gain de trafic ni nouvelle brève publiée n'est déduit de cet ajout.

## Vérification de la source et recherche GitHub

- Site officiel : `https://www.langchain.com/blog`, atteint également depuis
  `https://blog.langchain.com/`.
- **Ancienne URL écartée** : `https://blog.langchain.com/rss/` redirige désormais
  vers la page HTML du blog avec un HTTP 200 ; ce n'est pas un flux XML.
- Flux retenu : HTTPS 200, `application/rss+xml`, XML RSS contenant 100 items,
  relevé du 30/10 à 20:19:05 UTC ; 78 865 octets,
  SHA-256 `3f1b3a38797f7bc092b2109e2c9336962e3ca864d5ff9f2d32b5b72a309c895d`.
- Dépôt examiné : [`langchain-ai/langchain`](https://github.com/langchain-ai/langchain),
  révision `5b0aeb7637fc415eb408dc31523609272bbb38e1`, dernier push API
  `2026-10-30T19:39:55Z`. Licence MIT confirmée dans l'API et le fichier LICENSE
  épinglé. **Aucun code amont n'est adopté ni exécuté** : seul le lien RSS public
  est configuré. La licence du code n'est pas étendue aux articles du blog.

Les dates du flux sont celles fournies par l'éditeur et servent au filtre existant.
Elles peuvent différer des jours affichés sur le site ; elles ne prouvent pas une
première publication publique. Aucune date historique du média n'est modifiée.

## Recette locale exécutée

`tests/test_source_langchain.py` : rouge avant ajout, vert après. Vérifie l'unicité,
l'URL XML retenue, l'export OPML et le compteur de sources de Transparence.
**264 tests Python réussis** dans une copie isolée, puis exécution réelle de
`python3 engine/run.py --essai --sans-redaction` : code 0, 2 134 pages construites,
aucune rédaction payante, aucun transfert ni publication sociale.

Le vrai parseur a lu 25 entrées et reconnu leurs 25 dates, dont 8 dans la fenêtre
existante de trois jours au contrôle de 20:23 UTC. La collecte d'essai annonce
également 8 nouveaux candidats LangChain, pas 8 brèves publiées. Le refus 429 du
flux Reddit Claude reste consigné séparément, sans masquer la réussite du flux ajouté.

OPML construit reparsé : 24 noms/adresses exactement conformes au catalogue.
Manifestes inchangés, préfixe du journal intact, données du worktree non modifiées
par la recette ; aucun fichier de données de test n'est intégré.

Preuves privées : `crabe-chantiers/croissance/2026-10-30/` (captures, métadonnées,
logs rouge/vert/suite/essai, recette et résultats JSON). Bureau inaccessible et
clone partagé en conflit laissés intacts : worktree propre depuis
`cac69c855cffae8c519de7fc015d345a46fcc45f`, pull rapide vérifié avant préparation.
La livraison Git/cloud et la vérification HTTPS doivent être constatées séparément.
