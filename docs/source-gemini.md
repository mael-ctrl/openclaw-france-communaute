# Veille officielle Gemini CLI — 3 novembre 2026

## Une seule amélioration

Ajout de `https://github.com/google-gemini/gemini-cli/releases.atom` dans
`data/sources.json` : anglais, priorité **3**, libellé
**« Gemini CLI (releases, préversions incluses) »**.
Les 26 sources précédentes sont conservées à l'identique et dans leur ordre ;
le catalogue et son export OPML comptent désormais 27 URL distinctes.
Le collecteur, les quotas et le plafond DeepSeek de 30 €/mois restent inchangés.

Effet attendu : compléter les sources primaires des agents de programmation,
aux côtés d'OpenClaw, Hermes, Claude Code et Codex. Le flux publie aussi des
versions nightly/preview : leur présence n'est ni une version stable ni une
recommandation d'installation. La priorité ne décide qu'à date égale dans le
tri actuel ; elle n'est pas un quota propre à Gemini. Les notes de l'éditeur
ne constituent pas une validation indépendante des performances.
Aucun gain de trafic ni nouvelle publication n'est déduit de cet ajout.

## Recherche GitHub et source réelle

- Dépôt officiel : [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli),
  révision observée `0ac57c029b848d109eef940afe0db4b5a0c3dad0` ; dernier push
  API `2026-11-03T01:18:35Z`.
- Licence Apache-2.0 : API et fichier `LICENSE` épinglé, octets conformes au blob
  Git `7a4a3ea2424c09fbe48d455aed1eaa94d9124835`.
  Aucun code amont copié, installé ou exécuté : réemploi du collecteur stdlib
  et de l'export OPML existants. La licence du code n'est pas étendue aux autres
  contenus de l'éditeur.
- Atom lu en HTTPS strict le 03/11 à **13:03:05 UTC** : HTTP 200 sans redirection,
  `application/atom+xml`, 95 348 octets, SHA-256
  `187c0ad4a9841e57430e818100ed22d5cf319e0f5647763939c36cc7c18d15e5`.
- Le collecteur réel relit dix entrées datées avec liens de release reconnus,
  dont trois dans sa fenêtre inchangée de trois jours à 13:05 UTC. Ce sont
  des candidats, pas trois brèves publiées. La capture inclut des nightly,
  une preview et une version sans suffixe de préversion.

## Recette exécutée

Base propre `88a1953eecbde368215cbeaf63147bbfb4eced05`, worktree distinct :
Bureau inaccessible au cron, clone partagé en conflit laissé intact.
Pull réussi dans le nouveau worktree seulement ; aucune donnée conflictuelle
ni preuve historique importée ou corrigée.

`tests/test_source_gemini.py` : refus attendu avant ajout, succès après ;
source unique, projection OPML et compteur de Transparence contrôlés.
**289 tests Python réussis**, suite originale dans une copie isolée.
Puis vrai `engine/run.py --essai --sans-redaction` : code 0, 2 233 pages,
aucune rédaction payante, aucun transfert ni post. Le 429 Reddit Claude
reste consigné séparément. La clé n'est chargée que pour la lecture du solde.

Les 45 fichiers de preuves de la copie sont inchangés, le préfixe du journal
est intact et les données du worktree n'ont pas été modifiées par la recette.
Aucune donnée de test n'est intégrée. OPML construit reparsé : 27 noms/adresses
conformes au catalogue ; SHA-256
`74eb7b369ab7e80d4245767a25fa90409bae5a7066e257ae9cd67c0ac1c28e02`.

Preuves privées : `crabe-chantiers/croissance/2026-11-03-gemini/preuves/`
(capture Atom, provenance GitHub, rouge/vert, suite, essai et résultats JSON).
La validation locale seule ne constitue pas une preuve de publication.
