# Veille MCP Python SDK — 13 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/modelcontextprotocol/python-sdk/releases.atom`
dans `data/sources.json` : « MCP Python SDK (releases, préversions incluses) »,
anglais, priorité 3. Les **32 sources antérieures** sont inchangées, valeurs et ordre
compris. Réemploi du collecteur et de l'export OPML existants : **33 sources**,
compteur de Transparence dérivé du même catalogue. Aucun nouveau moteur ni dépendance.

Effet attendu : élargir la veille francophone aux évolutions du SDK Python de
Model Context Protocol, utilisé pour relier des applications IA à des outils et
ressources. Source primaire distincte des SDK d'agents déjà suivis ; aucun gain
d'audience mesuré ni recommandation d'installation.
Fenêtre de trois jours, dates réelles, quotas et plafond DeepSeek de **30 €/mois**
conservés. La priorité départage les dates égales, sans réserver de quota au flux.

## Qualification préalable

- Dépôt [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk),
  non archivé ; dernier push observé `2026-11-05T13:38:56Z`, consultation `2026-11-13T14:23:07.042111+00:00`.
- Révision `77001c96f9507be0f4d009b83210a384a5e08bda` ; licence MIT vérifiée par API et lecture du
  [LICENSE épinglé](https://github.com/modelcontextprotocol/python-sdk/blob/77001c96f9507be0f4d009b83210a384a5e08bda/LICENSE),
  octets conformes au blob Git `3d48435454b105021b4f777c11b6b07d8d2ffea3`. Aucun code amont copié,
  installé ou exécuté. La licence du code ne valide pas les faits ou les droits
  de tous les contenus associés.
- Alternative repérée : `modelcontextprotocol/typescript-sdk`, non archivé,
  push observé `2026-11-10T14:38:41Z`, API licence `NOASSERTION` ; non adoptée.
  Un seul flux ajouté, pas de multiplication des sources pendant cette mission.
- Flux : HTTPS strict, HTTP 200, MIME `application/atom+xml`, **172439 octets**,
  SHA256 `7191ae75046ab0dbda440a547ab2df2986ef6b36cc742697036b2afc0266eae7`.
- XML et vraie lecture du collecteur : **10 entrées**, toutes datées,
  dont une préversion `v2.0.0rc1` ; **zéro candidat dans les trois derniers jours**.
  Dernière date lue : `2026-10-02T22:02:27+00:00`.
  Ajout prospectif, sans redatation ni élargissement des filtres.

## Validation locale

Base `7e9b9813575a83474d69dabca5bf6f5a5303de52`, worktree dédié hors Bureau. Le pull du clone opérationnel
refuse ses conflits préexistants ; aucun reset, abort ou résolution automatique.
Fetch puis pull réussis uniquement dans le worktree propre. Le dernier rapport
d'orchestration et son manifeste ont été consultés ; aucun de leurs patches intégré.

Le contrat `tests/test_source_mcp_python.py` échoue avant ajout, puis passe :
source unique, libellé, export exact de tout le catalogue et compteur cohérent.
**352 tests Python réussis** dans une copie isolée, puis
`engine/run.py --essai --sans-redaction` : code 0, **2534 pages**,
zéro rédaction, transfert et publication sociale. Clé chargée pour lire le solde
seulement, jamais affichée ; aucune donnée d'essai reprise en production.

Quatre flux tiers échouent pendant cet essai : les deux HN RSS (502),
L'Usine Digitale (403) et Reddit Claude (429). Build réussi ne signifie pas que
tous les flux soient disponibles, ni que les contenus aient été validés factuellement.

**56 fichiers de preuves/publications inchangés**, préfixe du journal intact.
OPML reparsé : 33 couples nom/adresse strictement identiques au catalogue ; SHA256
`f73187fac94661cfab595755a8c3a3e6411c2386f348682219cf164a2475da42`. Pièces privées :
`crabe-chantiers/croissance/2026-11-13-1420/evidence/`.

Au commit initial, publication et recette HTTPS restent à confirmer.
