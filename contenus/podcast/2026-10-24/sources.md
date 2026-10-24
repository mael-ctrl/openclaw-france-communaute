# La Brève du Crabe — 24 octobre 2026

## Sélection et méthode

Huit brèves lues, triées par `date_redac` décroissante, depuis le commit `caedd44f4e48ac6035c281edfa2ade643d47f59a`. L'instantané `breves-snapshot.json` conserve les huit objets, l'heure réelle de sélection et l'empreinte du fichier source. Le clone partagé a été mis à jour par `git pull --ff-only origin main` : déjà à jour. Composition et recette dans un worktree isolé, sans modification des données ni des sceaux historiques.

Trois sujets retenus : `1015ed58ea2a4e47` (Block), `12c476ef6c418456` (OpenAI), `0cc4b0d5dbe94fa4` (Roborock). Les dates de rédaction sont celles du 24 octobre ; elles ne sont pas assimilées aux dates de lancement des produits. Script éditorial en français et voix synthétique, déclarés à l'introduction.

## Vérification éditoriale

- **Block / Dessa.** TechCrunch relaie le 24 octobre l'annonce de Block diffusée le 23 : ne pas présenter Dessa comme lancé pour la première fois le 24.[1] La page primaire affirme un entraînement sur la seule conversation humaine, sans texte, un fonctionnement full-duplex et une exécution locale sur MacBook Pro M4 Max ou mieux.[5] Ces propriétés sont attribuées à Block, sans revendication d'un essai indépendant. Le script ne reprend pas l'affirmation secondaire « un seul GPU » : la page primaire nomme un NVIDIA GB200 NVL72, pas une simple carte grand public.[1][5]
- **OpenAI / humanoïde.** Le Journal du Geek rapporte l'ambition d'OpenAI et une démonstration envisagée dès 2027, mais aucune date de vente ni aucun prix annoncés.[2] Le script présente le sujet comme une reprise du jour et un projet, pas comme une disponibilité commerciale. Le podcast original cité par le média n'a pas été réécouté dans cette mission ; l'attribution reste au Journal du Geek.
- **Roborock.** Frandroid rapporte la version **ProX avec accessoires** à 599 € chez Boulanger, contre 1 299 € auparavant ; la note 9/10 concerne le **Pro testé**.[6] Le script conserve cette distinction, le lavage des serpillières à 100 °C et la détection d'obstacles.[6] Pas de contrôle séparé du panier marchand : prix explicitement attribué à l'article, susceptible d'évoluer, sans garantie de disponibilité. Aucun lien affilié ajouté par le Crabe.

## Éléments non retenus et limites

Les fils Reddit sur Monadize et le fork d'ik_llama.cpp ont renvoyé un refus d'accès : extraction 403 puis accès HTTPS direct JSON 403. Aucun corps de fil lu ; ces sujets ne sont pas repris comme vérifiés. Kimi, motion design et Nostr n'ont pas été retenus. L'instantané conserve les résumés initiaux sans les réécrire.

L'outro distingue **objectif de chiffre d'affaires** et engagement sur **100 % des bénéfices**, sans prétendre à des dons déjà réalisés. Aucune heure de première publication n'est déduite du jour éditorial ; GUID stable et absence de `pubDate` fabriqué.

## Réemploi technique

Réemploi du CLI déjà installé `rany2/edge-tts` 7.3.1, sans copie de code tiers dans le média. Métadonnées GitHub consultées le 24 octobre : dernier push annoncé `2026-10-14T09:30:53Z`, licence API `NOASSERTION`. Le fichier LICENSE relu précise LGPLv3 pour le projet, MIT uniquement pour `src/edge_tts/srt_composer.py`. Module podcast interne existant et FFmpeg existant réutilisés ; aucun nouveau moteur ni dépendance ajoutée.

Audio effectivement généré avec `fr-FR-DeniseNeural`, débit `+8%`, sans repli : **346 mots, 130,848 secondes**, **785 088 octets**, mono 24 kHz / 48 kbit/s. Durée mesurée par `afinfo` ; décodage intégral FFmpeg réussi. SHA-256 : `8f44f8d0ad13f998c9be431f04ea1616a0a6000f257831d2cafd75293878eb39`.

Recette isolée : **207 tests Python réussis**, suivis d'un build réel (1 753 sorties), 495 fichiers de données/contenus/audio préservés. MP3 construit identique, script HTML exact, dix GUID distincts pilote compris, enclosure exacte et absence de `pubDate` inventé. Les huit brèves sélectionnées ont été recomparées au blob Git figé. Les anciens objets de l'index sont inchangés. Aucun moteur modifié, aucune nouvelle recette navigateur ni soumission aux annuaires.

Les contrôles de publication sont consignés séparément après leur exécution dans `docs/podcast.md`. Les captures de sources et logs sont conservés dans le chantier privé du jour ; ils ne constituent pas une mesure d'audience.

## Sources

[1] https://techcrunch.com/2026/10/24/blocks-new-voice-model-sounds-eerily-human
[2] https://www.journaldugeek.com/2026/10/24/openai-veut-construire-un-robot-humanoide-et-surtout-le-cerveau-qui-va-avec
[5] https://block.xyz/dessa
[6] https://www.frandroid.com/bons-plans/3296151_note-9-10-le-pro-du-menage-roborock-qrevo-curv-2-pro-perd-la-moitie-de-son-prix
