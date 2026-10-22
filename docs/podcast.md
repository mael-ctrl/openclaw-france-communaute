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

## Épisode quotidien du 19 octobre — publication vérifiée

Épisode `breve-2026-10-19`, commit `49b98d53495e4d28ede83215899ef59e56b0ff18` : quatre sujets (robot humanoïde OpenAI, compression de Claude Code, agents Nvidia, Ming audio tiny), sélectionnés parmi les huit brèves les plus récemment rédigées au SHA `8e6bffd4836de6b503bd1bfe6890099062713079`. [Script](../contenus/podcast/2026-10-19/script.txt), [sources](../contenus/podcast/2026-10-19/sources.md) et [instantané des huit brèves](../contenus/podcast/2026-10-19/breves-snapshot.json) conservés ; instantané comparé au blob Git exact. Les dates de reprise dans la presse ne sont pas assimilées aux dates des annonces. L'outro distingue objectif de chiffre d'affaires et engagement de reversement des bénéfices.

**Audio :** 336 mots, voix `fr-FR-DeniseNeural`, débit `+8%`, sans repli ; **129,120 s**, **774 720 octets**, MP3 mono 24 kHz / 48 kbit/s mesuré avec `afinfo` et intégralement décodé par FFmpeg. SHA-256 `be3104ce84f54aa9c5d73d0f00d68003d2d909fe28c2c152df889129bbcb7fc4`. L'index conserve les anciens épisodes, ajoute la durée mesurée et lie explicitement le script ; aucune heure de première publication inventée.

**Recette isolée : 147 tests Python réussis**, puis build réel hors mocks. Les 346 fichiers de données/audio/contenus contrôlés restent identiques après tests et build ; MP3 construit identique à la source, texte HTML exact, six GUID distincts (cinq épisodes et pilote), enclosure correcte sans `pubDate` fabriqué. Les cinq fichiers de livraison ont été relus sur GitHub au commit publié, identiques par empreinte. Aucun moteur modifié ; pas de nouveau test navigateur ni de soumission à un annuaire dans cette livraison de contenu.

**Production :** [run 39286679111 réussi](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39286679111), **147 tests cloud réussis**, logs d'envoi du MP3 et des deux sorties podcast, sauvegarde d'état `c96232ae9a2cfc86f3bca05d85f921589446f5c4` confirmée sur `main`. Le suivi a rencontré un timeout de l'outil d'attente, puis plusieurs attentes bornées ; aucune n'était un échec du pipeline. À 16:52 UTC, le MP3 était déjà servi alors que page et flux étaient encore anciens : état intermédiaire du transfert, pas une publication intégrale.

**Contrôle HTTPS strict le 19/10 à 17:01:35 UTC :** page `/podcast/`, flux `/podcast/feed.xml` et MP3 identiques octet pour octet au build vérifié. MP3 servi en `audio/mpeg` ; requête Range 0–1023 répondant 206 avec `Content-Range: bytes 0-1023/774720`. L'épisode est en tête du flux, avec six GUID distincts. Preuves privées : chantier `podcast/2026-10-19-episode/` (recette, captures de sources, logs cloud et vérification de production). Aucun échec de déploiement à reporter ; aucune mesure de hausse d'écoute revendiquée.

## Épisode quotidien du 20 octobre — publication vérifiée

Épisode `breve-2026-10-20`, commit `4dd1d078e14eb020530541e382eb6ec6af5c7370` : quatre sujets (Spotify, Ornith, dossiers MDPH et Lightroom), sélectionnés parmi les huit brèves les plus récemment rédigées au SHA `add8e05c3dfa015501036f5a26460fae82ba137c`. [Script](../contenus/podcast/2026-10-20/script.txt), [sources](../contenus/podcast/2026-10-20/sources.md) et [instantané](../contenus/podcast/2026-10-20/breves-snapshot.json) conservés et comparés au blob Git. Spotify : période précise du communiqué primaire retenue plutôt que celle du relais. Ornith : méthode de la famille distinguée de la fiche d'une variante. Adobe : annonce du 19 octobre, pas invention d'un lancement le 20. L'outro distingue objectif de chiffre d'affaires et engagement sur les bénéfices, sans prétendre à des dons déjà effectués.

**Audio :** 344 mots, voix `fr-FR-DeniseNeural`, débit `+8%`, sans repli ; **125,640 secondes**, **753 840 octets**, MP3 mono 24 kHz / 48 kbit/s mesuré avec `afinfo` et intégralement décodé par FFmpeg. SHA-256 `5a03905cbc82ab84ad40c60856855a83ee709ee5ec5f77f1131456e12b98e30d`. Anciens épisodes préservés, script explicitement lié et durée mesurée dans l'index ; aucune heure de première publication déduite.

**Recette isolée : 168 tests Python réussis**, puis build réel hors mocks ; **390 fichiers de données/audio/contenus** préservés après tests et build. Audio construit identique, script HTML exact, **sept GUID distincts** (six épisodes et pilote), enclosure exacte sans `pubDate` fabriqué. Les cinq fichiers du commit de livraison ont été relus sur GitHub et comparés par empreinte. Le transport brut de `gh api` a échoué sur le MP3 (« transform: short source buffer ») ; lecture JSON/base64 réussie, sans modifier l'audio. Aucun moteur modifié, nouveau test navigateur ou envoi à un annuaire.

**Cloud :** [run 39458906879 réussi](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39458906879), **168 tests cloud réussis**, envoi du MP3 et des deux sorties podcast attesté dans les logs ; sauvegarde `5647f4e7c00c3479ebcb85b6b53d87a1d7060944` confirmée sur `main`. Plusieurs attentes bornées, dont un timeout de l'outil terminal, ne constituaient pas des échecs du workflow. À 16:51 UTC, l'audio était servi mais pas encore la page ni le flux actualisés ; ce transfert partiel n'a pas été présenté comme une publication complète.

**HTTPS strict à 17:10:34 UTC le 20/10 :** page `/podcast/`, flux `/podcast/feed.xml` et MP3 identiques octet pour octet au build vérifié. Audio servi en `audio/mpeg`, plage 0–1023 en 206 avec `Content-Range: bytes 0-1023/753840`. Nouvel épisode en tête du flux, sept GUID distincts. Preuves privées : chantier `podcast/2026-10-20-episode/`. Aucun échec de pipeline à reporter ; aucune hausse d'écoute mesurée.


## Épisode du 22 octobre — publication vérifiée

Épisode `breve-2026-10-22`, commit `6278e397448b40888e0c63170b1250debe0094b7` : trois sujets (Claude Duet, achats par agents chez Walmart, prévisions IBM Granite), parmi les huit brèves les plus récemment rédigées au SHA `f2d0bce6c522bb20cff695b34c5d5f2766edec81`. [Script](../contenus/podcast/2026-10-22/script.txt), [sources](../contenus/podcast/2026-10-22/sources.md) et [instantané](../contenus/podcast/2026-10-22/breves-snapshot.json) conservés. Jour réel d'exécution utilisé, sans édition rétrodatée au 21. Annonces du 21 distinguées du billet IBM du 22 ; préversion américaine et déploiements futurs explicités, aucune performance des fournisseurs présentée comme test indépendant.

**Audio :** 358 mots, Denise `+8%`, sans repli ; **130,224 s**, **781 344 octets**, mono 24 kHz / 48 kbit/s, mesure `afinfo` et décodage FFmpeg intégral. SHA-256 `76b52bee7bd06a74a0271972527519f62d964a8ef8c8f6b0566daa8698b5b893`. Index augmenté sans changer les anciens épisodes, script explicitement lié, aucun `pubDate` fabriqué. Objectif de chiffre d'affaires distinct du reversement des bénéfices.

**Recette locale :** 182 tests au SHA de sélection, puis **183 tests** après reprise du `main` courant dans la copie isolée ; dernier build : **1 564 sorties**, **420 fichiers de données/audio/contenus préservés**, huit GUID uniques pilote compris. Les cinq fichiers livrés ont été relus sur `main` GitHub, identiques par empreinte. Un replay intermédiaire a échoué parce que le HOME hérité pointait vers une autre recette et masquait Pillow : invocation avec le HOME attendu, canari réussi puis suite rejouée, sans réinstallation ni modification du moteur. Échec conservé hors dépôt. Les premières sondes Python HTTPS ont également refusé le réseau sous un garde « recette accessibilité offline » ; elles ne prouvaient pas une indisponibilité du site. Une nouvelle invocation sans ce garde étranger a ensuite effectué la recette réelle ci-dessous.

**Cloud :** [run 39754970334 réussi](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39754970334), terminé le 22/10 à 10:19:51 UTC ; **183 tests réussis**, **1 609 fichiers envoyés**, MP3 et deux sorties podcast présents dans les logs d'envoi. Sauvegarde `c6651f0`, intégrée dans `2f58ec9`, présence dans l'ascendance de `main` vérifiée. File d'attente puis attentes bornées, dont un timeout de l'outil de suivi : aucun de ces délais n'était un échec du pipeline.

**HTTPS strict à 13:50:28 UTC le 22/10 :** `/podcast/`, `/podcast/feed.xml` et MP3 identiques octet pour octet au build vérifié. Audio servi en `audio/mpeg`, plage 0–1023 en HTTP 206 avec `Content-Range: bytes 0-1023/781344`. Aucun échec cloud à reporter à la roadmap, aucune nouvelle recette navigateur ni soumission aux annuaires dans ce lot de contenu. Preuves privées : chantier `podcast/2026-10-22/`.
