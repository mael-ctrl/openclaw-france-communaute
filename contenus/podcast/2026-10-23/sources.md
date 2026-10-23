# Sources de La Brève du Crabe — 23 octobre 2026

Édition du jour réel d'exécution, texte produit par IA et voix synthétique. Huit brèves lues, triées par `date_redac` décroissante au commit `09f950c70f54fda888ad667ee8de1abbaaf8f5f6` ; quatre sujets retenus. L'instantané `breves-snapshot.json` conserve les huit entrées, leur SHA source et l'heure de sélection. Aucun chiffre du script n'est extrapolé à partir d'un titre seul.

## Correspondance du script et vérifications

- **Meta**, brève `aab5745166d53293` : The Verge rapporte le report du 30 octobre au 20 novembre et cite le porte-parole de Meta ; les inquiétudes des éditeurs sont présentées comme telles, pas comme une décision juridique établie. Le report n'est pas une annulation des conditions.[1]
- **Claude**, brève `f0768bef5bd2f18f` : le relais Frandroid et la mise à jour primaire d'Anthropic du 22 octobre annoncent le mode auto par défaut la semaine suivante dans la plupart des applications, pour les nouvelles sessions Pro, Max et Team. Le contrôle des actions demeure ; aucune généralisation déjà effective ni disparition totale des autorisations n'est annoncée dans l'audio. Les données du reste du billet concernent Claude Code et ne sont pas extrapolées aux autres applications.[3][5]
- **QUELLE IA**, brève `e78add53758e76a2` : 252 modèles de langage dans l'édition du 19 octobre, agrégation de résultats publics, mise à jour hebdomadaire et ex æquo selon la présentation de son éditeur. Frandroid appartient au groupe qui édite le comparateur : cette provenance est dite à l'oral, sans transformer sa présentation en essai indépendant.[2]
- **Trainium**, brève `d34747657438013f` : billet primaire Hugging Face publié le 23 octobre, malgré l'absence de `date_source` dans la brève. Tableau public, résultats et scripts ; les tests décrits génèrent 32 jetons. Un PASS ne prouve ni débit ni comportement des générations longues. Le script conserve cette limite, sans prétendre tester nous-mêmes le matériel.[4]

Les quatre autres brèves de la sélection ne sont pas utilisées : témoignage local isolé, Bloodborne, coût annuel d'une réponse et inquiétudes sur les backdoors. Aucun détail non vérifié de ces sujets n'a été ajouté à l'audio.

## Mission et production

L'outro distingue objectif de chiffre d'affaires et engagement de reversement de 100 % des **bénéfices**, sans annoncer de versements déjà réalisés. CTA vers `communaute-ia.fr`.

Réemploi du CLI déjà installé : [rany2/edge-tts](https://github.com/rany2/edge-tts), dernier push observé via GitHub le 14 octobre 2026 à 09:30:53 UTC. Licence relue : LGPLv3 pour le programme, MIT uniquement pour `src/edge_tts/srt_composer.py`. Aucune copie de son code dans ce dépôt ; appel de l'exécutable externe, voix `fr-FR-DeniseNeural`, débit `+8%`.

## Sources

[1] https://www.theverge.com/tech/1017450/meta-business-terms-delayed-ai-scraping — Meta delays new business terms after publisher pushback on AI scraping | The Verge
[2] https://www.frandroid.com/culture-tech/intelligence-artificielle/3297565_quelle-ia-on-a-lance-un-comparateur-gratuit-de-252-modeles-pour-trouver-le-bon-selon-votre-usage — QUELLE IA : on a lancé un comparateur gratuit de 252 modèles pour trouver le bon selon votre usage — Frandroid
[3] https://www.frandroid.com/culture-tech/3297839_attention-claude-ne-vous-demandera-bientot-plus-la-permission-pour-agir — Attention, Claude ne vous demandera bientôt plus la permission pour agir — Frandroid
[4] https://huggingface.co/blog/torch-neuronx-model-support — Does Your Model Run on AWS Trainium? Look It Up
[5] https://claude.com/blog/auto-mode-default-in-claude-code — Auto mode is now the default in Claude Code for Pro, Max, and Team plans | Claude by Anthropic
