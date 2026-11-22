# Veille Agno — 22 novembre 2026

## Une amélioration

Ajout du flux primaire `https://github.com/agno-agi/agno/releases.atom`,
libellé « Agno (releases, préversions incluses) », anglais, priorité 3.
Les **39 sources précédentes** restent identiques et dans le même ordre ;
le catalogue, l'OPML et le compteur de Transparence passent à **40**.
Le collecteur et les générateurs existants sont réemployés, sans dépendance ajoutée.

Effet attendu : compléter la veille des outils de création et d'exploitation
d'agents par les prochaines versions d'Agno. Cet ajout n'est ni une recommandation
de sécurité ni une adoption de son logiciel ; aucun gain d'audience mesuré.
Fenêtre de trois jours, filtres, quotas et budget de 30 €/mois inchangés.
La priorité départage seulement les dates égales ; les préversions sont signalées.

## Qualification GitHub et flux

- Dépôt : [agno-agi/agno](https://github.com/agno-agi/agno).
- Révision consultée : `e59ca576219e589136e53b6cff8d6677899cf95f`.
  Dernier push observé à 13:01 UTC : `2026-11-20T20:41:13Z`.
- Licence API et [LICENSE épinglé](https://github.com/agno-agi/agno/blob/e59ca576219e589136e53b6cff8d6677899cf95f/LICENSE) : Apache-2.0.
  Octets vérifiés contre le blob Git `51032f045aafc8732c072ed31aa96f2994f29081`.
  Aucun code amont copié, installé ou exécuté : seule l'adresse Atom est ajoutée.
- Flux HTTPS strict : HTTP 200, `application/atom+xml`, 269 088 octets,
  SHA256 `cd1dbd6b512316802ab3c3c74633fb08e7ae418223819b00e12d2a3b6aa551c7`.
- Vrai parseur exécuté sur les octets conservés : dix entrées liées au dépôt,
  **aucune dans la fenêtre de trois jours** au relevé du 22 novembre à 13:01 UTC.
  Date maximale lue : `2026-11-17T17:05:45+00:00`.
  Ajout prospectif : aucune redatation, aucun élargissement de fenêtre.

## Recette locale

Base : `aba300c0484589c6a44e368a18675dbc1506129a`.
Le clone partagé reste dans un rebase interrompu, avec six fichiers en conflit.
Son index, ses variantes et ses preuves ne sont pas modifiés par cette mission.
Un worktree neuf sur `origin/main` a réussi `pull --ff-only origin main` ;
aucun rebase ou merge des données du clone partagé n'a été tenté.
Dernier rapport et manifeste de préparation du 22 novembre lus ; aucun de leurs
patches préparatoires n'est importé dans cette amélioration de source.

`tests/test_source_agno.py` échoue avant l'ajout puis réussit : source unique,
projection OPML exacte du catalogue et compteur cohérent.
**425 tests Python réussis** dans une copie séparée, puis vrai
`engine/run.py --essai --sans-redaction` réussi : **2 638 pages**,
zéro rédaction payante, transfert ou publication sociale.
La clé est utilisée seulement pour la lecture du solde, jamais affichée.
Les échecs tiers HN (timeout/502), LocalLLaMA (404), L'Usine Digitale (403)
et Reddit Claude (429) ne sont pas des échecs du nouveau flux.

Les 63 fichiers de preuves/publications contrôlés sont inchangés ; le préfixe du
journal est intact. Aucune donnée de recette importée dans le dépôt.
Export construit : SHA256 `67c1daceb6765991034f827ef314ce3da1dc0857214ec7d233d7b59d701f9070`.
Pièces privées : `crabe-chantiers/croissance/2026-11-22-agno/evidence/`.
La recette ne prouve pas la publication : celle-ci exige une relecture distante
Git et HTTPS séparée. La pression disque et le rebase interrompu restent des
dettes d'exploitation distinctes, non réparées par cet ajout.
