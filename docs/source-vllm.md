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

Au commit initial, vérification cloud et HTTPS encore en attente. Ne pas confondre
la source configurée avec une brève nouvellement rédigée ou un gain de trafic.
