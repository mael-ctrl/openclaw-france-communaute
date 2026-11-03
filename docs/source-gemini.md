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

## Publication ciblée vérifiée à 13:25 UTC

Configuration, test et première version de ce document poussés sous
`994f02d16cba1ae04675ed4a6f241595cde7cef4` ; les trois fichiers ont été relus
identiques sur `main` distant (repli Git après un HTTP 500 de l'API contents).
Dispatch `41641495254` sur ce SHA : **contrats cloud réussis à 13:27:38 UTC**,
pipeline encore en cours au relevé de 13:27:42 ; sauvegarde non encore acquise.

L'ancien run `41637768563`, sur le catalogue à 26 sources, a été laissé aller
jusqu'à son succès après 43 min 51 s avant le transfert ciblé, sans annulation.
Cela évite de lui laisser écraser prévisiblement le nouvel export. Ses attentes
locales de cinq minutes expirées ne constituaient pas des échecs du workflow.

À 13:25:17, préflight SFTP : ancien OPML exactement conforme au parent Git,
cibles SFTP/HTTPS identiques, clé hôte Ed25519 épinglée avant authentification,
sauvegardes privées. Seules `/veille/sources.opml` et la valeur **26 → 27** du
compteur de `/transparence/` ont été envoyées, par fichier temporaire/renommage
puis relecture SFTP exacte. Tous les autres octets de Transparence sont conservés.

À **13:25:43 UTC**, deux lectures successives de chacune des URL canoniques
en TLS strict : 200, octets exacts, **27 adresses OPML uniques**, Gemini une fois.
L'empreinte OPML est celle de la recette ci-dessus ; Transparence :
`5c63596b89b0ff5683c618609ba2872ba1761786fba17f3ede866366cc2a505d`.
Preuves : `livraison-ciblee/`, `preuves/https-20261103T132543Z/` et
`preuves/cloud-preflight-final.json` dans le chantier privé.

L'export et son compteur sont livrés ; le conflit du clone partagé reste
intact, et cette publication ciblée ne clôt pas le pipeline cloud en cours.
Collecte future, publications et effet d'audience restent distincts.
