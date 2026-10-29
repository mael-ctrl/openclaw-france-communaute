# Une source primaire supplémentaire : le blog officiel vLLM

## Périmètre — 29 octobre 2026

Une seule évolution : ajouter `https://vllm.ai/blog/rss.xml` à `data/sources.json`,
en anglais, priorité 4. Le collecteur existant et l'export public OPML sont réemployés,
sans nouvelle bibliothèque ni changement de rédaction, cadence ou plafond de 30 €/mois.
Les 22 sources précédentes sont conservées : le catalogue en contient désormais 23.

Effet attendu : suivre directement les annonces techniques d'inférence et de prise en
charge des modèles, plutôt que dépendre seulement de leurs reprises. Une annonce du
projet reste une source intéressée : ses performances ne deviennent pas des mesures
indépendantes. Aucun gain d'audience ou nouvelle publication éditoriale n'est déduit.

## Recherche et provenance

- Page officielle consultée : `https://vllm.ai/blog`, qui lie le flux ci-dessus.
  L'ancienne piste `https://blog.vllm.ai/feed.xml` renvoie une page 404 : elle n'est pas ajoutée.
- Dépôt inspecté via GitHub : `vllm-project/vllm-project.github.io`, révision
  `153a69ffbbb65832dc5d16053cf140d5fd01ad5a`, dernier push annoncé le 28/10/2026 à 14:28:29 UTC.
  L'API ne déclare pas de licence et l'arbre ne contient pas de LICENSE/COPYING.
  **Aucun code ni contenu intégral de ce dépôt n'est adopté** : seul le lien du flux public est configuré.
- Capture HTTPS du 29/10 à 08:46:12 UTC : 200, XML, 37 391 octets,
  SHA-256 `6691242038a865d262f7341a159c1e93df5c039fa0c301994a41ffba02dfad0b`.

## Recette effectuée

`tests/test_source_vllm.py` échoue avant l'ajout, puis passe : source unique,
export OPML exact et compteur de sources raccordé à Transparence. Une assertion
initiale erronée attendait les URL individuelles dans Transparence, qui n'affiche
qu'un total ; elle a été rectifiée sans modifier ce gabarit. Les deux refus sont conservés.

**251 tests Python réussis.** Transport HTTPS réel et vrai parseur : 25 entrées lues,
25 dates reconnues ; la plus récente est du 23/10. Aucune n'entre dans la fenêtre de
fraîcheur de trois jours le 29/10 : zéro nouvelle entrée vLLM est donc attendu,
sans republier d'archives ni antidater les sources.

`engine/run.py --essai --sans-redaction` exécuté dans une copie isolée : code 0,
2 049 pages construites, zéro rédaction, transfert ou publication sociale.
Les refus tiers Siècle Digital 403 et Reddit Claude 429 restent visibles dans le log,
sans être confondus avec un échec du nouveau flux. Manifestes inchangés, préfixe du
journal préservé et données du worktree non modifiées par l'essai. OPML construit
reparsé : les 23 noms/adresses correspondent exactement au catalogue.

Preuves privées : `crabe-chantiers/croissance/2026-10-29/` (capture, métadonnées,
logs rouge/vert/suite/essai, recette et résultat JSON). Aucun de ces jeux de données
de test n'est intégré à la production. Clone partagé en conflit laissé intact ;
worktree propre fondé sur `aba7a548b2a90ed2fb92bf885bbfd01e5a161e4f`.

## Publication

Ajout publié dans Git sous **`f8acc1d`**, trois blobs relus sur `main`.
Après rebase sur les évolutions voisines : **253 tests locaux et 253 tests cloud réussis**.
Le run `40845273333` a effectivement collecté vLLM (`0 neuf(s)`, attendu), mais a
été annulé par la limite de **45 minutes**, après 2 025 lignes de transfert.
L'étape de sauvegarde d'état a été ignorée. Cela n'est pas un pipeline réussi.

Les deux sorties publiques restaient anciennes. Repli SFTP ciblé à 10:20 UTC :
clé hôte Ed25519 épinglée avant authentification, sauvegardes privées, contrôle
anti-écrasement, upload temporaire et renommage, relecture des octets distants.
- `/veille/sources.opml` : rendu exact du catalogue Git, **23 sources**, 2 538 octets ;
  SHA-256 `1c143fa45b5c126559d5c02ab5418b086745dc6878d972b1c5116f6caec97c15`.
- `/transparence/` : **seul le compteur 22 → 23** remplacé dans la capture publique,
  sans reprendre les statistiques, dates ou journaux de la recette.

La première relecture HTTPS immédiatement après écriture n'était pas encore identique ;
ce refus est conservé. Deux relectures canoniques ultérieures à 10:20:37–38 et 10:21:13 UTC
sont exactes pour les deux cibles ; `/skills/` répond 200 et conserve le téléchargement.
Aucune nouvelle écriture distante n'a été nécessaire après le premier envoi.
Preuves : `repli-cible/` dans le dossier privé du chantier (avant/après, préflight,
relevés HTTP et `result-final.json`).

**L'ajout et son export public sont livrés ; le timeout cloud et la sauvegarde d'état
restent non réparés.** Le successeur automatique `40853475177` contient l'ajout,
a passé les contrats et est encore en cours au contrôle de 10:17 UTC ; il n'a pas
été redéclenché ni annulé. Une source configurée et collectée ne prouve ni nouvelle
brève rédigée ni hausse d'audience.
