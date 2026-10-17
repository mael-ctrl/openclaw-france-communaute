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

Les validations ci-dessus sont locales. Le run cloud et les lectures HTTPS de la page, du flux et des audios doivent être consignés ici après leur réussite ; un commit ou un dispatch seul ne prouve pas la mise en ligne.
