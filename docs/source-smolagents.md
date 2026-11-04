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

## Publication ciblée vérifiée à 13:27 UTC

Configuration, test et document initial poussés sous
`0bcc84f0cb89cf2847d31e2b5496c23f416f2789` ; les trois blobs sont identiques
sur `main` distant. Dispatch `41835188023` sur ce commit, initialement en attente.

Avant tout SFTP, attente de la fin du run précédent `41831347466` : **annulé
par GitHub à la limite de 45 minutes**, pendant le transfert FTP ; sauvegarde
d'état sautée. Ses logs montrent des transferts partiels, pas une publication
complète. Les timeouts locaux du watcher n'étaient pas des conclusions CI.
Aucune annulation manuelle, modification du workflow ou fusion de données.

Après sa fin, base OPML distante exactement conforme au catalogue parent,
identité HTTPS/SFTP contrôlée et sauvegardes privées des deux cibles.
Clé hôte SFTP épinglée avant authentification, installation par fichier
`.part` et renommage, puis relecture exacte. Seuls l'export OPML et le compteur
**27 → 28** de Transparence sont modifiés ; tous les autres octets de cette
page servie sont conservés (pas de remplacement par les statistiques de test).

À **13:27:15 UTC**, deux lectures successives de chaque URL canonique en TLS
strict : 200 et octets identiques aux cibles, 28 adresses OPML uniques dont
smolagents une fois. Empreinte OPML identique à la recette ; Transparence :
`3191a0b2d35293f9ce44926fdf0219515742011cb544578a5b2c500a5b4b5a43`.
Preuves : `livraison-ciblee/`, `evidence/https-20261104T132715Z/` et les logs
cloud dans le chantier privé. Export et compteur en production ; pipeline
cloud du nouvel état et sauvegarde finale restent distincts de cette livraison.

Contrats du nouveau run cloud **réussis à 13:28:07 UTC** ; à 13:28:23, pipeline
en cours et sauvegarde encore en attente. Le conflit du clone partagé reste
ouvert. Aucune clôture globale du cloud ni gain d'audience ne sont revendiqués.
