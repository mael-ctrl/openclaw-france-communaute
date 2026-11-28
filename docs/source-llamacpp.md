# Veille llama.cpp — 28 novembre 2026

## Une amélioration

Ajout de la source primaire `https://github.com/ggml-org/llama.cpp/releases.atom`,
libellée « llama.cpp (releases, préversions incluses) », anglais, priorité 3.
Les 45 sources antérieures sont conservées à l'identique et dans le même ordre ;
le catalogue et ses projections OPML/compteur passent à 46 sources.

Effet attendu : suivre directement les évolutions de l'inférence locale C/C++,
complémentaires au blog Ollama déjà suivi. Aucun gain d'audience mesuré.
Réemploi du collecteur et des projections existants : aucun code amont exécuté,
aucune dépendance ajoutée. Budget DeepSeek de 30 €/mois, quotas et fenêtre de
fraîcheur de trois jours inchangés. La priorité ne départage que les dates
égales ; elle ne garantit ni quota par source ni sélection éditoriale.
Les releases observées sont des builds numérotés `b…`, pas une certification de
stabilité. Le flux n'est pas filtré aux seules versions stables.

## Qualification

- Dépôt : [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp).
- Révision consultée : `115deee8ecfbbacb1ab8a6137b62aac1f2f0724d` ; dernier push
  observé par API : `2026-11-28T15:42:16Z`.
- Licence MIT, confirmée par API et lecture du
  [LICENSE épinglé](https://github.com/ggml-org/llama.cpp/blob/115deee8ecfbbacb1ab8a6137b62aac1f2f0724d/LICENSE),
  octets vérifiés contre le blob `e7dca554bcb802f98408383a864404e3aa4eacca`.
  Seule l'adresse du flux est ajoutée, sans adoption du logiciel.
- HTTPS strict à **16:10:26 UTC** : HTTP 200, 85 461 octets ; SHA256
  `f26597890cbf8312a41227c70ab11e22a7c5e54b7c0e620f8cdadf528f897005`.
- Vrai parseur du média sur les octets conservés : dix entrées, toutes dans la
  fenêtre de trois jours (27–28 novembre). Aucun changement de date ; ces
  candidats ne sont pas dix articles publiés.

## Recette

Base `18da2bf661e26e19c9f0c8cbb572593ae0f01e5a`. Bureau illisible depuis le cron ;
clone partagé en conflit laissé intact. Worktree neuf sur `origin/main`, pull
rebase réussi seulement dans cet arbre. Rapport et manifeste du 27 novembre
lus ; aucun candidat de reprise Git/cache/déploiement n'est intégré.

Contrat `tests/test_source_llamacpp.py` rouge avant ajout, vert ensuite : unicité,
configuration, projection OPML exacte et compteur. **482 tests Python réussis**
dans une copie isolée. Vrai `engine/run.py --essai --sans-redaction` réussi :
**2 659 pages**, zéro rédaction payante, transfert ou publication sociale.
Clé chargée seulement pour lire le solde, jamais affichée. Le nouveau flux
fournit dix candidats avant les limites globales du collecteur.

Les échecs de flux tiers sont conservés dans la recette : deux flux HN (502),
LiteLLM (connexion réinitialisée), LocalLLaMA (404), L'Usine Digitale (403),
Reddit Claude (429). Ils ne sont ni corrigés ni masqués par cet ajout.
Les 65 fichiers de preuves/publications contrôlés sont inchangés, le préfixe du
journal est intact ; aucune donnée de recette reprise dans Git.

Les conflits du clone partagé et les déploiements généraux annulés restent des
problèmes d'exploitation distincts. Pièces privées :
`crabe-chantiers/croissance/2026-11-28/`. La recette seule ne prouve pas la
publication : le commit et les relectures HTTPS sont consignés séparément.
