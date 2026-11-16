# Veille MCP TypeScript SDK — reprise du 16 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/modelcontextprotocol/typescript-sdk/releases.atom`
dans `data/sources.json` : « MCP TypeScript SDK (releases, préversions incluses) »,
anglais, priorité 3. Les **33 sources antérieures** sont inchangées, valeurs et
ordre compris. Le collecteur et l'export OPML existants sont réemployés :
**34 sources**, compteur de Transparence dérivé du même catalogue.
Aucun nouveau moteur, paquet installé ou code amont copié.

Effet attendu : compléter la veille MCP Python par les évolutions des clients et
serveurs TypeScript/Node. Aucun gain d'audience mesuré ni recommandation d'installation.
La fenêtre de trois jours, les dates, les quotas et le plafond DeepSeek de
**30 €/mois** restent inchangés. La priorité départage seulement les dates égales.

## Qualification préalable

- Dépôt [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk),
  non archivé ; push observé `2026-11-10T14:38:41Z`, consultation le 16/11 à 10:49 UTC.
- Révision `919bb8ea88b6e10e72c2f8b6218fad4cfdc40b2c` ; API licence **NOASSERTION**.
  Lecture du [LICENSE épinglé](https://github.com/modelcontextprotocol/typescript-sdk/blob/919bb8ea88b6e10e72c2f8b6218fad4cfdc40b2c/LICENSE),
  octets vérifiés contre le blob Git `4a93985763241755401a10678395303de4e720ba` :
  transition MIT → Apache-2.0, anciennes contributions sans consentement restant
  sous MIT, documentation hors spécifications sous CC-BY-4.0. Ne pas réduire
  cette situation à « tout Apache ». Seul le flux est référencé ; aucune exécution
  ni réutilisation de code amont. La licence ne valide pas les faits des releases.
- HTTPS strict, HTTP 200, MIME `application/atom+xml`, **53 978 octets** ;
  SHA256 `1bce24fdef0043c450a5cbdafd4b737428739ecd16d238cd2f11451c1a25b29b`.
- XML : **10 entrées**, toutes lues par le vrai parseur du collecteur sur le corps
  capturé. **Zéro candidat dans les trois derniers jours** au 16/11 à 10:49 UTC ;
  dernière date lue `2026-10-23T18:32:25+00:00`. Ajout prospectif : aucun contenu
  redaté, aucune fenêtre élargie. Le flux inclut aussi des releases par paquet,
  pas seulement des annonces globales ; les quotas habituels restent applicables.

## Validation locale

Mission initialement ouverte le 14/11, reprise et vérifications le **16/11**,
sans antidater les relevés. Bureau inaccessible depuis le cron ; clone opérationnel
avec conflits préexistants laissé intact. Worktree dédié hors Bureau, pull réussi ;
base de validation `3eae07371f9a05a7d43e41807cac84f6ed5a8525`.
Dernier rapport d'orchestration et manifeste consultés ; aucun de leurs patches importé.

`tests/test_source_mcp_typescript.py` : rouge observé avant ajout, vert après ajout
(source unique, libellé explicite, export exact du catalogue, compteur cohérent).
**356 tests Python réussis** dans une copie isolée, puis
`engine/run.py --essai --sans-redaction` : code 0, **2 588 pages**, zéro rédaction,
transfert ou publication sociale. Clé chargée uniquement pour le contrôle du solde,
jamais affichée. L'Usine Digitale répond 403 pendant cet essai : un build réussi
ne prouve pas la disponibilité de tous les flux tiers.

**59 fichiers de preuves/publications inchangés**, préfixe du journal conservé.
Aucune donnée d'essai reprise. OPML reparsé : 34 couples nom/adresse exactement
conformes au catalogue ; SHA256
`5e48612e63c3ab5d2db3069dc1fab9c301e29bad14bc99903cf8652bcb2f1687`.
Pièces privées : `crabe-chantiers/croissance/2026-11-14-mcp-ts/evidence/`.

Au commit initial, livraison cloud et relecture HTTPS restent à confirmer.
La reprise du chantier ne répare pas le clone opérationnel conflictuel.
