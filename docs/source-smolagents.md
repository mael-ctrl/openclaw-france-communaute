# Veille officielle smolagents — 4 novembre 2026

## Une amélioration bornée

Ajout de `https://github.com/huggingface/smolagents/releases.atom` dans
`data/sources.json` : anglais, priorité 3, libellé **« smolagents (releases,
préversions incluses) »**. Les 27 sources précédentes sont conservées à
l'identique et dans leur ordre ; le catalogue et son export OPML passent à
28 adresses uniques. Réemploi du collecteur et du générateur OPML existants :
aucun changement de moteur, de quota ni du plafond DeepSeek de 30 €/mois.

Effet attendu : compléter le blog général Hugging Face par les notes officielles
de sa bibliothèque d'agents Python. Ce n'est pas une mesure de croissance ni
une recommandation d'installation. Le flux peut inclure des préversions ; la
priorité ne départage que les dates égales, ce n'est pas un quota par source.

## Qualification de la source

- Recherche GitHub : dépôt officiel [huggingface/smolagents](https://github.com/huggingface/smolagents).
- API observée le 04/11/2026 à 13:02 UTC : dépôt non archivé, dernier push
  `2026-11-03T18:36:41Z`, révision `96f33faaf028479119ec8d34507b47694cf14e34`.
- Licence Apache-2.0 vérifiée via API et [LICENSE épinglé](https://github.com/huggingface/smolagents/blob/96f33faaf028479119ec8d34507b47694cf14e34/LICENSE),
  octets conformes au blob Git `261eeb9e9f8b2b4b0d119366dda99c6fd7d35c64`.
  Aucun code amont copié, installé ou exécuté. Cette licence du code ne constitue
  pas une licence générale sur tous les contenus associés.
- Lecture HTTPS stricte du flux : 200, `application/atom+xml`, 252 175 octets.
  Collecteur réel : dix entrées datées et liées aux releases ; **aucune dans sa
  fenêtre inchangée de trois jours**. La plus récente lue, `v1.26.0`, est datée
  du 29 mai 2026 dans le flux. Le push récent du dépôt ne rend pas ses releases
  récentes : ajout prospectif, sans redatation ni publication immédiate promise.

## Validation réelle

Base propre `d428f212edb90a1faa29c66cfd9ab1035dfdc97d` dans un worktree séparé.
Le pull demandé sur le Bureau a échoué, puis celui du clone partagé a refusé
ses fichiers non fusionnés. Ces deux états restent intacts ; seul le nouveau
worktree a été synchronisé. Aucune fusion de données ni réparation de sceaux.

`tests/test_source_smolagents.py` a échoué avant l'ajout puis réussi : source
unique, libellé explicite, export OPML et compteur de Transparence.
**300 tests Python réussis** dans une copie isolée, puis vrai
`engine/run.py --essai --sans-redaction` : code 0, 2 285 pages construites,
aucune rédaction payante, aucun transfert ni post. La clé n'a servi qu'à la
lecture du solde. Le 429 de Reddit Claude est conservé comme limite indépendante.

Les 46 fichiers de preuves de la copie sont inchangés et le préfixe du journal
est intact. Aucune donnée de recette n'est reprise dans la production.
OPML reconstruit et reparsé : 28 couples nom/adresse conformes au catalogue ;
SHA-256 `f6ef671b88f929b380a5f5b8cc6d726e030fd5ee569ef3310b49e8a5b6e587bb`.

Preuves privées : `crabe-chantiers/croissance/2026-11-04-smolagents/evidence/`
(provenance, licence, Atom, collecteur, rouge/vert, suite et essai).
Les contrôles locaux ne prouvent pas à eux seuls la mise en ligne ; celle-ci
est vérifiée séparément après le push et le déclenchement cloud.
