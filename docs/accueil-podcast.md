# Accueil → podcast — croissance du 19 octobre 2026

## Une seule amélioration

Le bouton natif « Écouter le podcast » mène de l’introduction de l’accueil à `/podcast/`. Jusqu’ici, l’accès à cette page depuis l’accueil se trouvait seulement dans le pied. Les deux actions existantes (actus/manifeste), les extraits du pack et les kits gratuits sont conservés.

Une ligne de production dans `engine/construction.py`, styles existants réemployés, aucun lecteur audio, script, traceur, service ou dépendance ajouté à l’accueil. MP3, textes, GUID, RSS, dates et prix ne changent pas. La page d’écoute existante déclare le texte IA et la voix synthétique.

## Réemploi examiné

Consultation GitHub du 19/10/2026 : [shipshapecode/starpod](https://github.com/shipshapecode/starpod), licence MIT, dernier push API `2026-09-02T18:33:16Z`, SHA `c9601ca128507c4fd19910714095425007bfbe45`. Le code `packages/starpod/src/pages/index.astro` met une liste d’épisodes sur son accueil. Un catalogue dynamique ou une migration Astro seraient disproportionnés ici : aucune copie ni dépendance adoptée, lien HTML vers le catalogue déjà construit.

## Recette exécutée

- Base `84cc9ec6e1ae0439bf26e23eeec1b9fc53f789cc`, copie Git isolée hors Bureau (illisible depuis ce cron), pull effectué. Sources, statistiques et 40 dernières lignes de journal consultées ; dépenses mensuelles consignées 4,01 USD, mode normal. Aucun réglage budgétaire modifié.
- Contrat `tests/test_accueil_podcast.py` : échec attendu avant le changement (aucun lien podcast dans le hero), réussite après. **144 tests Python + 4 Node réussis**. Premier lancement complet en échec d’environnement : `TMPDIR` pointait vers `/var`, symlink refusé par le garde-fou des couvertures. Suite intégralement rejouée sous le scratch Hermes, garde-fou inchangé.
- Accueil avant/après identique après retrait de l’unique ligne ajoutée, sur les données réelles. Build de **1 221 sorties comptées par le moteur**, puis essai réel `--essai --sans-redaction` dans une seconde copie : retour 0, aucune rédaction, aucun transfert ni annonce. Les **319 fichiers de données** de la copie Git restent identiques ; les **24 manifestes**, le registre et le préfixe du journal de l’essai sont préservés. Collecte partielle préexistante : Siècle Digital 403, Reddit Claude 429.
- Chromium éphémère, sans JavaScript, **390 et 1 440 px** : clic et activation clavier du nouveau lien, page d’écoute atteinte, script déplié, pas de débordement horizontal ni requête MP3 sur l’accueil. Quatre captures relues. L’en-tête mobile existant reste haut ; le lien est accessible après défilement, pas annoncé comme visible sans défilement.

## Production

**Production confirmée le 19/10 à 14:27 CEST.** Commit fonctionnel `06c06bfd1c7871460375c795407141e972a50f93` ; [run cloud 39249559960](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39249559960) réussi, **144 tests Python cloud**, **1 256 fichiers envoyés**, sauvegarde `7cdd48d906150d1836fa62b8838a6af378f58b82`. Les logs attestent l’envoi de l’accueil et des deux sorties podcast ; les trois blobs du commit ont été relus sur GitHub.

**Quatre URL HTTPS en TLS strict** : accueil identique au rendu du commit cloud sauvegardé ; page podcast, flux et CSS identiques aux octets attendus. Chromium sur la production réelle, sans substitution des réponses ni JavaScript : clic et Entrée depuis l’accueil à 390/1 440 px, destination correcte et texte dépliable ; aucun débordement horizontal. Quatre captures de production relues. Le suivi borné a attendu le pipeline complet, sans confondre délai de transfert et échec.

Effet attendu : rendre les épisodes plus faciles à découvrir depuis l’accueil. Aucun gain d’écoute, d’abonnement ou d’audience mesuré.
