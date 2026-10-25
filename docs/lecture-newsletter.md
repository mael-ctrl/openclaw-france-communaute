# Newsletter depuis la fin de lecture — 25 octobre 2026

## Une amélioration

Le lien HTML **« La newsletter gratuite »** en fin de brève et d'article mène à `/#la-breve`, l'ancre de la section du formulaire **déjà présent** sur l'accueil. Aucun formulaire supplémentaire, script, suivi d'événement ou inscription automatique. Les flux RSS, Bluesky, podcast, aide RSS et lectures liées restent en place.

Le clic n'abonne personne : il donne accès au formulaire existant avec ses mentions de confirmation et son lien de confidentialité. Cette livraison ne valide pas à nouveau le service tiers, le double opt-in, la délivrabilité ou la désinscription ; aucun email n'est soumis ni envoyé par la recette.

## Réemploi et périmètre

- Base : `45f43896d926d2a3097c25bdb26f99b3b9825614`, travail isolé hors Bureau. Le pull demandé sur le Bureau échoue (`not a git repository`) ; le clone automatisé hors Bureau est à jour après pull `--ff-only`.
- Chasse GitHub : VuePress/VitePress/Decap CMS repérés ; `gohugoio/hugo`, Apache-2.0 selon l'API, dernier push observé le 24/10/2026. Aucun framework ni code tiers adopté : deux attributs/liens natifs dans le constructeur existant suffisent. Métadonnées conservées dans le dossier privé de recette.
- Modification de production limitée à `engine/construction.py` : une ancre et un lien. CSS, formulaire, abonnés, paiement et réglages de newsletter inchangés.

## Recette locale exécutée

- Test rouge : lien absent avant correctif (`red.log`). Correction d'une erreur d'arité dans le nouveau test, puis vert.
- **223 tests Python + 4 Node réussis** ; contrats `tests/test_lecture_newsletter.py`, `tests/test_suivre.py` et formulaire historique préservé.
- **1 355 brèves + 421 articles** comparés à horloge commune : rendus identiques après retrait du seul lien ajouté. Accueil identique après retrait du seul `id`, flux RSS identique. **521 fichiers** data/contenus/assets inchangés.
- Build réel : **1 812 pages + assets**. Essai isolé `--essai --sans-redaction`, clé non affichée, plafond 30 €/mois : retour 0, aucune rédaction/transfert/annonce ; 30 fichiers de preuves inchangés et préfixe du journal conservé. Collecte partielle : HN OpenClaw 502 et Siècle Digital 403, consignés sans les présenter comme succès.
- **32 parcours Chromium** : brève/article, clic/Tab puis Entrée, JavaScript activé/désactivé, largeurs 320/390/901/1 440 px. Titre/champ visibles sous le vrai en-tête ; Tab arrive sur le champ email après navigation clavier. Champ vide, aucun POST, requêtes externes bloquées. Captures mobile et 901 px relues.
- Premier vérificateur navigateur interrompu à 901 px : il exigeait une ancre à y=0 malgré le `scroll-padding-top: 8rem` existant. Recette corrigée pour respecter le CSS réel, sans modifier la production ni déplacer artificiellement la destination ; première trace conservée.

Preuves privées : `~/.hermes/workspaces/crabe-chantiers/croissance/2026-10-25/` (`local-result.json`, logs, `browser-local-20261025T130904Z/results.json`, captures). Aucun jeu de données de recette intégré.

## Livraison

En attente du run cloud et de la vérification HTTPS au moment de ce commit. Effet attendu : faciliter le retour des lecteurs par email. Aucun gain d'inscriptions ni d'audience mesuré.
