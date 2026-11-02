# Veille officielle Codex — 2 novembre 2026

## Une seule amélioration

Ajout de `https://github.com/openai/codex/releases.atom` dans `data/sources.json` :
anglais, priorité **3**, libellé **« Codex (releases, préversions incluses) »**.
Les 25 entrées précédentes sont conservées à l'identique et dans leur ordre ;
le catalogue et son export OPML contiennent désormais 26 URL distinctes.
Aucun moteur, quota, filtre de fraîcheur, budget (30 €/mois), journal ou sceau
historique n'est modifié par ce lot.

Effet attendu : compléter la veille des agents de programmation par les notes
publiées directement dans le dépôt officiel de Codex, sans intermédiaire.
Le flux inclut des versions alpha : le libellé l'explicite et la priorité reste
inférieure à celle des flux OpenClaw/Hermes/Claude Code. Une préversion n'est
pas une version stable ni une recommandation d'installation. Les affirmations
de l'éditeur ne sont pas une validation indépendante des performances.
Aucun gain de trafic ni nouvelle brève publiée n'est déduit de l'ajout.

## Recherche GitHub et source réelle

- Dépôt : [openai/codex](https://github.com/openai/codex), révision observée
  `ba0d0e1f74ee0f41c27ef24b37ed5fc030b487e7`, dernier push API
  `2026-11-02T12:24:56Z`.
- Licence Apache-2.0 vérifiée dans l'API et le fichier `LICENSE` épinglé ;
  contenu comparé au blob Git `4606e72e042564097e8780d66c1d4dcb611869bd`.
  **Aucun code tiers copié, installé ou exécuté** : réemploi du collecteur
  stdlib et de l'export OPML déjà présents. La licence du code n'est pas
  étendue implicitement aux autres contenus de l'éditeur.
- Atom obtenu en HTTPS strict : HTTP 200 sans redirection,
  `application/atom+xml`, dix entrées. Capture du 02/11 à 13:13:19 UTC :
  239 328 octets, SHA-256
  `c99f3af5326ce9a301623688884256d39a9f4cee9e348a2b9ecb1432aee33011`.
- Le vrai collecteur a relu dix entrées avec dates/liens reconnus, dont trois
  dans sa fenêtre inchangée de trois jours à 13:18 UTC. Ce sont des candidats,
  pas trois publications. Le flux majoritairement alpha est qualifié comme tel.

## Recette exécutée

Base propre `4f958639dbc3b84872121b70e352da9c828d2492`, worktree distinct :
Bureau inaccessible depuis le cron ; clone partagé en rebase/conflict laissé
intact. Pull réussi dans le nouveau worktree, sans importer les données sales.

`tests/test_source_codex.py` : échec attendu avant ajout, succès ensuite ;
source unique, projection OPML et compteur Transparence contrôlés.
**274 tests Python réussis** dans une copie isolée, puis vrai
`engine/run.py --essai --sans-redaction` : code 0, 2 188 pages construites,
aucune rédaction payante, aucun transfert et aucun post. Le 429 de Reddit
Claude reste consigné séparément.

44 fichiers du dossier de preuves inchangés, préfixe du journal conservé ;
données du worktree inchangées par la recette, aucune donnée de test intégrée.
OPML construit reparsé : 26 noms/adresses conformes au catalogue, SHA-256
`469fa1779eb428d976ff558e9e9469dbe1f531cd218cf51a599d51d2f6a58c20`.

Preuves privées : `crabe-chantiers/croissance/2026-11-02-codex/preuves/`
(captures, provenance GitHub, logs ciblé/suite/essai et résultats JSON).
La validation locale ne constitue pas encore une preuve de publication ;
la clôture Git/cloud/HTTPS est consignée séparément après lecture réelle.
