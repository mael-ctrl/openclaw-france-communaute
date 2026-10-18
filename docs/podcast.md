# Podcast : rendre les audios existants découvrables et abonnables

## Amélioration de croissance du 17 octobre 2026

Une seule fonctionnalité : une [page d'écoute](https://communaute-ia.fr/podcast/), liée depuis le pied du média, et son [flux RSS audio](https://communaute-ia.fr/podcast/feed.xml). Elle reprend les épisodes déjà publiés les 15 et 16 octobre et le pilote, sans générer de nouvel audio ni ajouter de service externe. Le lecteur et le téléchargement fonctionnent sans JavaScript ; le flux s'ajoute dans un lecteur compatible.

Le lot podcast préparé le matin a été réemployé : sept fichiers ciblés, dont seulement cinq lignes d'intégration dans les deux modules existants. Les fichiers de démonstration B2B restent dans les annexes. Base de recette : `c98b0516388cdf58662f5cf00e8eeaea9954988a` ; empreinte SHA-256 du patch préparé : `7c73e0e30deed0309fe688aa9c89f7754f5beeb8443198d18dffc6b8563fe4f0`.

## Recette locale réellement exécutée

- Les 57 artefacts du lot ont été vérifiés par empreinte avant intégration. Le contrat `test_podcast_courant.py` échoue sur la base : « RSS des épisodes indexés absent ». Après application du patch : **123 tests Python et 4 tests Node réussis**.
- Builds avant/après : **661 puis 662 sorties comptées par le moteur**, plus assets et flux annexe. **654 HTML existants** identiques après retrait du seul lien podcast ajouté au pied ; **640 couvertures** identiques en octets et mtime. RSS général, RSS articles et news-sitemap identiques à horloge de test commune. Données, journal et preuves inchangés par tests/builds.
- Vrai CLI `engine/run.py --essai --sans-redaction` en copie indépendante : retour 0, trois items collectés, aucune rédaction payante, aucun envoi FTP/social ; journal initial préservé en préfixe et manifestes/registre inchangés. Collecte partielle : Siècle Digital 403, Reddit Claude 429 ; ces limites ne sont pas présentées comme résolues.
- Les trois MP3 ont été mesurés avec `afinfo`, identifiés `audio/mpeg` et intégralement décodés par FFmpeg. Durées : 130,224 s (16/10), 127,584 s (15/10), 61,128 s (pilote). Octets identiques entre sources et build.
- Chrome sans JavaScript, largeurs 390 et 1440 px : lien depuis l'accueil, démarrage effectif des trois lecteurs natifs, six téléchargements identiques et ouverture du RSS. Aucun débordement horizontal ni erreur console ; captures examinées.
- Première invocation de la recette déplacée : rejet de son ancien chemin fixe de confinement dans le vérificateur navigateur. Chemin adapté dans la seule copie de recette ; suite complète rejouée avec succès, sans affaiblir le confinement ni changer le patch.

## Identité, dates et limites

Les GUID proviennent des IDs stables de `contenus/podcast/episodes.json` ; le pilote conserve `urn:communaute-ia:podcast:la-breve-du-crabe:pilote`. Une correction de titre ou un déplacement de MP3 ne doit pas changer ces identités. Tailles d'enclosure calculées depuis les fichiers ; chemin local strict et doublons rejetés.

Le jour éditorial ne prouve pas la première heure de mise en ligne. Aucun `pubDate` ni `lastBuildDate` inventé ; une éventuelle date `publie_le` future exige une preuve distincte et un fuseau. Le pilote est signalé comme bande-annonce, pas comme épisode d'actualité. Texte IA et voix synthétique sont déclarés.

Cette livraison ne constitue ni une soumission ni une acceptation Apple/Spotify, ni une chaîne YouTube. Elle ne garantit pas la compatibilité de tous les annuaires. Les bénéfices destinés aux associations sont distingués de versements effectivement réalisés. Effet attendu : faciliter l'écoute, le partage et le retour des auditeurs ; aucun gain d'audience mesuré.

## Recherche de réemploi et licences

Métadonnées GitHub reconsultées le 17/10/2026 ; code et provenance relus dans le lot préparé, aucune dépendance ni fragment tiers incorporés :

| Dépôt | Licence API | Dernier push API | Décision |
|---|---|---|---|
| [lkiesow/python-feedgen](https://github.com/lkiesow/python-feedgen) | BSD-2-Clause | 2024-07-04T10:19:12Z | Concepts enclosure/GUID déjà couverts. En-tête du module podcast mentionnant aussi LGPL : ne pas copier aveuglément. |
| [svpino/rfeed](https://github.com/svpino/rfeed) | MIT | 2023-11-22T12:20:17Z | Concepts longueur en octets et `isPermaLink` explicite ; hiérarchie de classes inutile ici. |

Choix : module interne stdlib préparé, pas de nouvelle bibliothèque. Codes relus à `97260abb1793eb164c458c10b493690beb413f6d` et `a4ccbcb40eb86d5a4bda26b4f49c3921b39be26e` respectivement.

## Production

**Livraison confirmée le 17/10/2026 à 14:18 CEST.** Commit fonctionnel `5a0bfa43724d9c9e7dffc8800efdf62120c2ec23` ; [run cloud 39031238936](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39031238936) réussi, **123 tests Python sur Linux**, **689 fichiers envoyés**, sauvegarde d'état `5adfaa1`. Les logs attestent l'envoi de `podcast/index.html` et `podcast/feed.xml` ; huit blobs du commit relus sur GitHub, identiques.

Contrôle TLS strict : **9 URL distinctes, 12 requêtes** avec trois lectures Range supplémentaires. Page et RSS identiques octet pour octet au rendu testé ; trois GUID distincts. Les trois MP3 sont identiques aux fichiers sources, servis en `audio/mpeg`, et les plages 0–1023 répondent 206 avec tailles exactes. Lien d'accueil et entrée unique du sitemap présents ; téléchargements B2B préservés.

Chrome sur la **production HTTPS réelle**, sans substitution des réponses et sans JavaScript : clic depuis l'accueil, démarrage des trois lecteurs et six téléchargements identiques à 390/1440 px, ouverture du RSS ; aucune erreur console ni débordement. Page et flux sont livrés, pas seulement préparés. Aucune nouvelle génération audio, soumission à un annuaire, chaîne YouTube ou mesure de gain d'audience dans cette mission.

## Croissance du 18 octobre — lire les épisodes sans audio

Une seule amélioration : les trois épisodes des 15–17 octobre proposent « Lire le texte de l’épisode » sur `/podcast/`, avec un accordéon HTML natif. Le texte provient exactement du `script.txt` déjà utilisé pour la synthèse vocale ; ce n’est ni une transcription synchronisée ni une nouvelle rédaction. Aucun texte, MP3, GUID, date éditoriale ou flux RSS n’est réécrit.

Le champ optionnel `script` de l’index lie explicitement chaque épisode à son fichier sous `contenus/podcast/AAAA-MM-JJ/script.txt`. Aucun rapprochement par date n’est deviné. Sans champ, aucun bloc n’est affiché ; un chemin déclaré invalide, lié symboliquement, vide ou absent fait échouer le build. Le contenu est échappé, ses retours à la ligne conservés, sans nouveau JavaScript ni dépendance de production.

**Réemploi examiné le 18/10 :** [shipshapecode/starpod](https://github.com/shipshapecode/starpod), MIT, dernier push API `2026-09-02T18:33:16Z`, code `c9601ca128507c4fd19910714095425007bfbe45`, module `packages/starpod/src/lib/transcript.ts`. Son parseur multi-format et ses repères temporels dépassent notre besoin de texte brut local. Aucun code copié ; extension du module interne existant. Pelican (AGPL-3.0, push `2026-10-13T10:31:16Z`) également repéré mais non adopté.

**Recette locale :** base `53a7894ab5dde44d167e7d7124703645c89c1844` dans une copie isolée hors Bureau, celui-ci illisible en cron. Contrats rouge/vert puis **134 tests Python + 4 Node réussis**. Première suite complète : trois erreurs de fixture, car l’index test copié ne contenait pas les nouveaux fichiers explicitement référencés ; dépendances de fixture ajoutées sans affaiblir le contrôle des fichiers absents. Build réel, RSS podcast identique au module précédent, **312 fichiers de données/audio/contenus préservés**. Essai isolé `--essai --sans-redaction` réussi : aucun transfert, rédaction ou annonce ; journal conservé en préfixe et sceaux inchangés. Collecte partielle préexistante : Siècle Digital 403, Reddit Claude 429.

**Navigateur local :** Chrome éphémère dédié, JavaScript désactivé, 390 et 1440 px : ouverture/fermeture des trois textes, contenu exact, contrôle clavier, aucun débordement. Captures relues. Aucun accès au profil Chrome personnel verrouillé ; aucune configuration navigateur partagée modifiée.

**Production vérifiée le 18/10 à 14:30 CEST :** commit `3b8b6215b132d03bbe046bf3127877d4c42ea829`, [run 39126125145 réussi](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39126125145), **134 tests cloud, 721 fichiers envoyés**, sauvegarde `63d5fab` intégrée dans `2fa53c2`. Les logs attestent l’envoi de la page et du flux podcast ; cinq blobs de la livraison vérifiés sur GitHub. **Huit URL HTTPS contrôlées** : page, RSS et quatre MP3 identiques aux octets attendus ; lien d’accueil et entrée sitemap présents. Chrome sur la production réelle, sans JavaScript : six ouvertures/fermetures de scripts à 390/1440 px, textes exacts, contrôle clavier et captures conformes, aucun débordement. Les attentes bornées du suivi n’étaient pas des échecs CI.

Effet attendu : permettre la lecture sans son et rendre le contenu textuel accessible sur la page. Aucune hausse de trafic ni indexation effective démontrée.

## Épisode quotidien du 17 octobre — publié à la suite

Épisode `breve-2026-10-17`, commit `9a6f300bbc9b357ac363aa07b6719052da329efb` : quatre sujets (Meta, Nvidia Dory, llama.cpp, BYD), sélectionnés parmi les huit brèves les plus récemment rédigées au SHA `1156f5d2bed9130cd995fab01434b1d2d1c98c6f`. [Script](../contenus/podcast/2026-10-17/script.txt), [sources et recette](../contenus/podcast/2026-10-17/sources.md) conservés. Sortie de Dory le 16 octobre distinguée de son relais du 17 ; objectif de CA distinct du reversement des bénéfices.

Voix Denise, débit +8 %, sans repli : **125,280 s**, **751 680 octets**, MP3 intégralement décodé et mesuré. **129 tests réussis localement et dans le cloud** ; cinq fichiers du commit relus sur GitHub, identiques.

[Run 39050026731](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39050026731) **réussi**, terminé à 16:57:50 UTC ; 695 fichiers envoyés, dont le MP3 et les deux sorties podcast. Sauvegarde d’état `06e1509`, intégrée dans `00eba4b`. Les attentes bornées du suivi et la disponibilité partielle pendant l’envoi n’étaient pas des échecs du pipeline.

**Contrôle HTTPS strict à 16:58:35 UTC** : MP3 identique au fichier source (`audio/mpeg`, SHA-256 `b704b4e272682e0f92990358ed430ea1818990c96c6e154306a599f6457fb378`) ; plage 0–1023 servie en 206 avec taille exacte. Épisode présent dans `/podcast/` et en tête de `/podcast/feed.xml`, quatre GUID distincts (trois épisodes + pilote), enclosure correcte, sans `pubDate` fabriqué. La recette navigateur de la fonctionnalité reste celle de la section précédente ; cette livraison de contenu n’a pas refait les clics navigateur ni soumis le flux à un annuaire.
