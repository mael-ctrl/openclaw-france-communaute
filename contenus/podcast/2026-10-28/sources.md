# La Brève du Crabe — 28 octobre 2026

Texte produit par IA, voix synthétique. Édition au jour réel d'exécution, sans antidater au jour prévu du cron. Huit brèves triées par `date_redac` décroissante au commit `953a20beac4740ae646d2701d94a0a22b8c3e70e`, sélection à 08:18:21 UTC ; instantané `breves-snapshot.json` vérifié contre le blob Git exact. Trois sujets retenus, cinq écartés. Le clone partagé a refusé le pull (conflits non résolus) : données et preuves préservées ; préparation dans un worktree isolé sur le main distant, pull fast-forward réussi.

## Sources et précautions

### Données personnelles et IA
- Brève `a2e7c198140abb31`, [01net, article du 28 octobre](https://www.01net.com/actualites/chatgpt-gemini-meta-ai-leurope-prepare-un-passe-droit-des-ia-sur-vos-donnees.html).
- Source de l'article : [noyb, communiqué du 23 octobre](https://noyb.eu/en/ai-eu-member-states-approve-digital-expropriation-europeans-ai-companies).
- Les deux textes ont été lus. La position du Conseil adoptée le 21 octobre est distinguée d'une loi finale ou d'une autorisation déjà en vigueur. La critique des garanties est attribuée à noyb, association de défense de la vie privée, pas présentée comme notre avis juridique. Aucun avis de conformité individuel.

### Agents SAP
- Brève `50ba4a9cf817274b`, [L'Usine Digitale, article du 28 octobre](https://www.usine-digitale.fr/logiciels-applications/sap/outils-agentiques-modele-dia-deploye-en-orbite-partenariats-robotiques-comment-sap-veut-passer-de-lia-qui-recommande-a-lia-qui-execute.OQEA375GARFCJCUWMGTTZ63LVY.html).
- Article intégral lu par l'outil d'extraction ; la tentative HTTPS directe de conservation a répondu 403. Le texte extrait complet est conservé hors dépôt, sans prétendre disposer d'une capture HTML directe réussie.
- Annonces TechEd du 27 distinguées du relais du 28. Joule Work/Joule Studio, ouverture aux agents tiers, contrôles d'accès, traces d'audit et validations humaines proviennent du corps de l'article. Les cas robotiques sont des démonstrations/partenariats, pas une généralisation de l'autonomie à tous les clients. Aucun gain chiffré repris.

### Indra
- Brève `c4cf20c98a2f55db`, [relais r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1xhd7vt/they_released_a_tesseract_successor_datalabtoindra/). Fil non relu directement ; vérification par la source primaire identifiée.
- [README Datalab figé au commit e20355319b5aa5705a876a8d2b40aca606d7df5f](https://github.com/datalab-to/indra/blob/e20355319b5aa5705a876a8d2b40aca606d7df5f/README.md), lu le 28 octobre. Projet déjà publié avant ce jour : pas de faux lancement du 28.
- La documentation distingue le reconnaisseur latin `rec.onnx` (environ 1,25 million de paramètres) de l'ensemble des modèles par défaut (7,3 millions, options mathématiques à part). Le résumé « tout le modèle n'aurait qu'un million » n'est donc pas repris tel quel. Le script explique la distinction sans annoncer un nombre global trompeur.
- Exécution CPU sans GPU annoncée par la documentation. Benchmarks du fournisseur, non reproduits ici ; aucun gain universel garanti et aucune installation/test d'Indra revendiqués. Code Apache-2.0, poids sous OpenRAIL-M modifiée : pas de promesse d'usage commercial sans conditions.

## Périmètre éditorial

Les autres brèves du lot (code 3D, TPU, classement Artificial Analysis, optimisations MoE et prédiction de prix GPU) ne sont pas utilisées. Les affirmations de leurs résumés ne sont pas validées par leur simple conservation. La sonde du chemin `/intelligence-index` d'Artificial Analysis a renvoyé une page 404 ; aucune conclusion sur ce classement n'est diffusée.

L'outro distingue l'objectif d'un million d'euros de chiffre d'affaires en douze mois de l'engagement de reversement de 100 % des **bénéfices** aux associations françaises loi 1901 ; elle ne prétend pas que des dons ont déjà été réalisés. CTA : `communaute-ia.fr`.

## Audio et réemploi

355 mots, `edge-tts` 7.3.1 déjà installé, voix `fr-FR-DeniseNeural`, débit `+8%`. Génération réussie sans repli. Durée `afinfo` : **129,048 secondes**, **774 288 octets**, mono 24 kHz / 48 kbit/s ; décodage intégral FFmpeg réussi. SHA-256 : `e01d023077016567a2e7d495f447240211fa45f9f4ca4a86e5458dbbbd1af903`.

Réemploi GitHub requalifié : [rany2/edge-tts](https://github.com/rany2/edge-tts), dernier push API observé `2026-10-14T09:30:53Z`, licence API `NOASSERTION` ; fichier LICENSE lu : LGPLv3, exception MIT pour `src/edge_tts/srt_composer.py`. CLI existant utilisé hors dépôt, aucun code tiers copié, aucune nouvelle dépendance du moteur. Le constructeur podcast existant est réutilisé ; GUID et anciens épisodes conservés, script explicitement lié, pas de `pubDate` inventé.

Captures, logs et résultats d'intégration conservés dans le chantier privé `podcast/2026-10-28-execution-081821Z/`. Ces vérifications ne constituent ni soumission aux annuaires ni mesure d'audience.
