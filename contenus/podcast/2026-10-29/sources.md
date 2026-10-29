# La Brève du Crabe — 29 octobre 2026

Édition du jour réel d'exécution ; aucun épisode rétrodaté au 28 octobre.
Sélection : les **8 brèves les plus récentes par `date_redac` décroissante**, au commit `d5f2d085e0e3d3c84cc7f5e294f7f11d7f99677a`. L'instantané joint est comparé au blob Git exact. Trois sujets retenus ; le script corrige les raccourcis non démontrés de leurs résumés, sans modifier les données historiques.

## 1. Gemini 4 Carbon — accès initial restreint

- Brève `2568456569b56073`, rédigée le 29/10 à 06:36:41 UTC : [Latent Space](https://latent.space/p/ainews-gemini-4-carbon/), billet affiché le 29 octobre couvrant les 27–28 octobre.
- Source primaire : [Google, Introducing Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/), datée du **28 octobre 2026**, consultée le 29.
- Recoupement : annonces [Google DeepMind](https://x.com/GoogleDeepMind/status/2115489356437651654) et [Google AI](https://x.com/GoogleAI/status/2115489593818816591), 28 octobre.
- Le premier accès vise un sous-ensemble de spécialistes de cyberdéfense via Fairwind. L'accès plus large est futur, sans date ferme. La première place rapportée concerne l'Artificial Analysis Intelligence Index v5, **pas tous les classements** ; le relais mentionne des positions différentes en code et sur Vals. Scores de cybersécurité et fiabilité interne non transformés en essais indépendants ou en garanties.

## 2. Microsoft et OpenAI — dix milliards de revenus trimestriels

- Brève `28ecc21919a277b2`, rédigée le 28/10 à 23:29:09 UTC : [TechCrunch, Rebecca Bellan](https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/), 28 octobre.
- Source primaire consultée le 29 : [Microsoft, Form 10-Q](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526436133/msft-20260930.htm), déposé le **28 octobre 2026**.
- Passage vérifié : « For the three months ended September 30, 2026, we recorded revenue from commercial arrangements with OpenAI, inclusive of revenue-sharing payments, of $10.0 billion. »
- Périmètre conservé : revenus de Microsoft liés aux accords commerciaux, trois mois clos le 30 septembre, partage de revenus inclus. Ce n'est ni un bénéfice ni un chiffre annuel. Ventilation cloud/partage non précisée selon TechCrunch. Aucune extrapolation annuelle ajoutée.

## 3. Qwen4 — une valeur logicielle, pas une capacité confirmée

- Brève `1ee6baefe3558c03`, rédigée le 29/10 à 02:45:54 UTC : [fil r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1xi7390/qwen4_1m_context_window/).
- **Accès Reddit refusé** par l'extracteur et par la lecture HTTPS directe : le fil n'a pas été lu. Le lien primaire exact a été retrouvé dans le récapitulatif Latent Space, puis vérifié directement par l'API GitHub.
- Source primaire : [QwenLM/qwen-code, PR #15762](https://github.com/QwenLM/qwen-code/pull/15762), « fix(core): size the qwen4 generation at 1M », fusionnée le **28/10 à 05:26:35 UTC** ; tête examinée `3a393098b4e6f774099b325ba71b5082d6a571db`.
- [Diff de tokenLimits.ts](https://github.com/QwenLM/qwen-code/blob/3a393098b4e6f774099b325ba71b5082d6a571db/packages/core/src/core/tokenLimits.ts) et tests lus via l'API. La règle attribue un défaut 1M aux identifiants qwen4 lorsque le catalogue n'apporte pas de valeur prioritaire.
- Réserve explicite du producteur : « the CLI path was exercised against a fake endpoint, not a real qwen4 one, so the model's actual window is still unconfirmed ». Les tests du contributeur sont rapportés, pas rejoués par ce podcast. **Ni capacité de toute la gamme, ni disponibilité, ni calendrier de lancement ne sont établis par cette PR.** Le script ne reprend pas la date spéculative du 1er novembre.

## Autres candidates non retenues

Les brèves `82cc04de9aeb5617`, `fd8eb594e36a2330`, `34c5f501057042b5`, `eb5ead38de04bc4e`, `9f227232b7f50ab9` sont conservées dans l'instantané, mais leurs fils Reddit ont refusé les lectures. Leurs performances ne sont pas reprises dans l'audio faute de recoupement suffisant pendant cette édition.

## Transparence et production

Texte produit par IA et voix synthétique annoncés dans l'intro. L'objectif est **1 M€ de chiffre d'affaires en douze mois**, distinct de l'engagement de reverser **100 % des bénéfices** à des associations françaises loi 1901. Aucun don accompli revendiqué. Le jour éditorial ne devient pas une heure de première publication ; aucun `pubDate` fabriqué.

Réemploi : CLI existante [rany2/edge-tts](https://github.com/rany2/edge-tts), version locale 7.3.1. Métadonnées GitHub consultées le 29 octobre : dernier push `2026-10-14T09:30:53Z`, licence API `NOASSERTION` ; fichier LICENSE relu : LGPLv3 pour l'ensemble sauf `srt_composer.py` sous MIT. Utilisation du programme installé sans copier de code dans le média ; aucune nouvelle dépendance moteur.

Le pull du clone partagé a échoué à cause de conflits Git déjà présents dans les données. Travail réalisé dans un worktree isolé sur `origin/main`, dont le pull fast-forward a réussi ; aucun conflit, journal ou sceau du clone partagé n'a été résolu ou réécrit par cette édition.
