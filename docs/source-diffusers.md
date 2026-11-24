# Veille Diffusers — 24 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/huggingface/diffusers/releases.atom`,
libellé « Diffusers (releases, préversions incluses) », anglais, priorité 3.
Les 41 sources précédentes restent identiques et dans le même ordre ; le catalogue,
l'export OPML et le compteur de Transparence passent à 42 sources.

Effet attendu : compléter les blogs et Transformers par une veille directe des
versions de la bibliothèque de génération d'images, vidéos et audio de Hugging Face.
Aucun code amont adopté ni gain d'audience mesuré. Collecteur et générateurs
existants réemployés ; aucune dépendance ajoutée. Fenêtre de trois jours, quotas,
filtres et budget DeepSeek de 30 €/mois inchangés. La priorité départage les dates
égales, ce n'est ni un quota par source ni un filtre des préversions.

## Qualification amont

- Dépôt : [huggingface/diffusers](https://github.com/huggingface/diffusers).
- Révision consultée : `f112184d8b888456b66e2f68e2b79c698cb5de39`.
  Dernier push API observé : `2026-11-24T13:59:01Z`.
- Licence API et [LICENSE épinglé](https://github.com/huggingface/diffusers/blob/f112184d8b888456b66e2f68e2b79c698cb5de39/LICENSE) : Apache-2.0.
  Octets contrôlés contre le blob Git `038e32f6445e8f265bde482613cf0d2f43d86dbc`.
  Seule l'adresse Atom est ajoutée ; logiciel non installé ni exécuté.
- Alternative consultée : `langflow-ai/langflow`, licence API MIT, dernier push
  `2026-11-24T06:44:54Z` ; non ajoutée pour conserver une seule amélioration.
- Flux HTTPS strict le 24 novembre à **14:49 UTC** : HTTP 200,
  `application/atom+xml`, 1 312 127 octets, SHA256
  `092613b58ab3fe38b8482f79649ba4fdc2a7d5092dab10a177c2dd54fa44e8d5`.
- Vrai parseur du média exécuté sur les octets conservés : **dix entrées, aucune
  dans la fenêtre de trois jours**. Dernière date lue : 12 novembre 2026,
  `06:38:33+00:00`. Ajout prospectif : aucune date artificiellement actualisée,
  aucune fenêtre élargie et aucune nouvelle brève Diffusers revendiquée.

## Validation locale

Base : `830ad1684160bbf55cc94ecff0c3fc21158807ef`.
Le pull demandé au Bureau échoue avec `Resource deadlock avoided`. Le clone
partagé est en rebase avec conflits : index, données et preuves conservés.
Worktree neuf sur `origin/main`, puis pull fast-forward réussi dans ce seul arbre.
Dernier rapport/manifeste de la vague du 23 lus ; aucun candidat de cette vague importé.

`tests/test_source_diffusers.py` échoue avant l'ajout puis réussit : source unique,
projection exacte du catalogue dans l'OPML, compteur cohérent. **434 tests Python
réussis** dans une copie séparée. Vrai `engine/run.py --essai --sans-redaction`
réussi : **2 638 pages**, zéro rédaction payante, transfert ou publication sociale.
La clé n'est utilisée que pour lire le solde, jamais affichée. Les erreurs tierces
LocalLLaMA (404), L'Usine Digitale (403) et Reddit Claude (429) sont conservées.

Les 63 fichiers de preuves/publications contrôlés restent identiques, le préfixe
du journal intact. Aucune donnée de recette importée dans le dépôt. OPML candidat :
SHA256 `665248e72c42b6c0e6be0dd255fcdc85f6b5dcec2d7c378894a858876e66d757`.
Pièces privées : `crabe-chantiers/croissance/2026-11-24-1548/preuves/`.

## Livraison vérifiée, clôture cloud distincte

Deux pushs ont été refusés pour avancées voisines. Le seul commit de cette mission
a été rebasé dans son worktree : nouvelle suite combinée **438 tests réussis**
après le premier rebase ; le second n'ajoutait que des documents presse. Aucun
reset, force-push ou changement du clone partagé. Code livré :
**`2a585945e8c8d2e47f5b5c3c7cbd9b8f5c7c8426`** ; les trois fichiers relus sur
`main` par l'API GitHub sont identiques aux octets locaux.

Dispatch unique `45420138152`, ensuite annulé sans job en file d'attente.
Successeur `45421309006`, SHA `c18eb8fb256399262a00e177c6e49a29b7a61b78` :
ascendance et identité des trois fichiers vérifiées. Aucun nouveau dispatch ni
annulation d'un run actif par cette mission.

Le run antérieur `45417959509` s'est terminé **cancelled**, pipeline annulé et
sauvegarde sautée. Le délai du watcher n'est pas utilisé comme diagnostic de
cause. Le transfert ciblé a attendu sa terminaison. Préflight à **15:33 UTC** :
inventaire paginé des cinq statuts actifs, seul le successeur avec 42 sources
actif ; aucun éditeur local `engine/run.py` détecté. Contrôle ponctuel,
pas verrou transactionnel.

Clé hôte SFTP vérifiée avant secret, deux cibles exactes sauvegardées et base
OPML identique au catalogue parent de 41 sources. Seuls `veille/sources.opml`
et le compteur **41 → 42** de `transparence/index.html` ont été transférés,
par fichiers intermédiaires exclusifs puis renommage. Tous les autres octets de
Transparence sont préservés, ainsi que les témoins `.htaccess` racine, veille et
CORS Skool. Relecture SFTP exacte à **15:33:23 UTC**.

La première réponse HTTPS de l'OPML renvoyait encore les octets précédents ;
échec et corps conservés, **aucune réécriture** pour le masquer. Les relectures
suivantes sont exactes. À **15:34:15 UTC**, deux passages SFTP + HTTPS strict
confirment les mêmes octets : OPML de **5 209 octets / 42 couples nom-URL**,
compteur 42 ; témoins toujours inchangés. Une lecture ultérieure réussie ne
prouve pas la cause de l'écart initial. Preuve privée :
`crabe-chantiers/croissance/2026-11-24-1548/recontrole-01/result.json`.

La publication ciblée est acquise et les contrats cloud du successeur ont réussi ;
son pipeline est encore en cours au dernier contrôle. Cela ne clôt ni sa sauvegarde
cloud, ni les conflits du clone partagé, ni les interruptions d'exploitation.
Aucun gain d'audience n'est déduit de cet ajout.
