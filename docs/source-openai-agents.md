# Veille OpenAI Agents Python — 11 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/openai/openai-agents-python/releases.atom`
dans `data/sources.json` : « OpenAI Agents Python (releases, préversions incluses) »,
anglais, priorité 3. Les 31 sources antérieures, leurs valeurs et leur ordre sont
inchangés. Réemploi du collecteur et de l'export OPML existants : **32 sources**,
compteur de Transparence dérivé du même catalogue. Aucun nouveau moteur ni dépendance.

Effet attendu : couvrir les prochaines évolutions du SDK Python d'agents OpenAI
à partir de ses notes de versions primaires, complément distinct du blog OpenAI
et de Codex. Aucun gain d'audience mesuré ni recommandation d'installation.
Fenêtre de trois jours, dates réelles, quotas et plafond DeepSeek de **30 €/mois**
conservés. La priorité départage les dates égales, sans réserver de quota au flux.

## Qualification préalable

- Dépôt [openai/openai-agents-python](https://github.com/openai/openai-agents-python),
  non archivé ; dernier push observé `2026-11-11T13:01:47Z`, consultation à 13:02 UTC.
- Révision `d68961657843c7d81dfc25834484f8aac2957eb3` ; licence MIT vérifiée par API
  et lecture du [LICENSE épinglé](https://github.com/openai/openai-agents-python/blob/d68961657843c7d81dfc25834484f8aac2957eb3/LICENSE),
  octets conformes au blob Git `e5ad2c5aa30343f143a5c418004ca1a8d2cfaff4`.
  Aucun code amont copié, installé ou exécuté. La licence du code ne valide pas
  les faits ou les droits de tous les contenus associés.
- Flux : HTTPS strict, HTTP 200, MIME `application/atom+xml`, 335 181 octets,
  SHA256 `478bc7ac2a10b2d8c5c32227810e715b6bf74944aa730d6179dd319163675bf6`.
- XML et vraie lecture du collecteur : dix entrées, dont deux titres alpha,
  toutes datées ; **zéro candidat dans les trois derniers jours** au contrôle.
  Dernière date lue : `2026-11-08T07:07:12+00:00`.
  Ajout prospectif, sans redatation ni élargissement des filtres.

## Validation locale

Base `a50848464c2435ee9c6092a23d559115eb280723`, worktree dédié hors Bureau.
Le pull du clone opérationnel a refusé ses conflits préexistants : ils sont
laissés intacts. Fetch puis pull réussis uniquement dans le worktree propre.

Le nouveau contrat `tests/test_source_openai_agents.py` échoue avant ajout, puis
passe : source unique, libellé, export exact de tout le catalogue et compteur.
**331 tests Python réussis** dans une copie isolée, puis
`engine/run.py --essai --sans-redaction` : code 0, **2 441 pages**, zéro rédaction,
zéro transfert et zéro publication sociale. Clé chargée pour lire le solde seulement,
jamais affichée ; aucune donnée d'essai reprise en production.

Deux échecs de flux préexistants pendant l'essai : L'Usine Digitale (403) et
Reddit Claude (429). La réussite du build ne prouve pas la disponibilité de tous
les flux ni la véracité éditoriale de leurs contenus.

54 fichiers de preuves/publications inchangés, préfixe du journal intact.
OPML reparsé : 32 couples nom/adresse strictement identiques au catalogue ; SHA256
`2214d0c1697e3c1196c88234ce420cb327d3e540a76974d7d899c30802246915`.
Pièces privées : `crabe-chantiers/croissance/2026-11-11/evidence/`.

Au commit initial, publication et recette HTTPS restent à confirmer.
