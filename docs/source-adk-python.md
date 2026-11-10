# Veille Google ADK Python — 10 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/google/adk-python/releases.atom`
dans `data/sources.json`, libellé « Google ADK Python (releases, préversions incluses) »,
anglais, priorité 3. Les 30 sources antérieures et leur ordre sont inchangés.
Le collecteur et l'export OPML existants sont réemployés : 31 sources, compteur de
Transparence calculé depuis ce même catalogue. Aucun nouveau moteur ou dépendance.

Effet attendu : mieux couvrir les outils de développement d'agents Python de Google,
à partir de leurs notes de versions primaires. Aucun gain d'audience mesuré ni
recommandation d'installation. Dates réelles et fenêtre de trois jours conservées ;
la priorité départage les dates égales, ce n'est pas un quota par source.
Plafond DeepSeek inchangé : 30 €/mois.

## Qualification préalable

- Dépôt [google/adk-python](https://github.com/google/adk-python), non archivé,
  dernier push observé `2026-11-10T18:14:40Z` ; consultation à 18:18:57 UTC.
- Révision `cd8debd2e7920512783217bc81f268824a81033e` ; licence Apache-2.0
  vérifiée par API et [LICENSE épinglé](https://github.com/google/adk-python/blob/cd8debd2e7920512783217bc81f268824a81033e/LICENSE).
  Octets conformes au blob Git `d645695673349e3947e8e5ae42332d0ac3164cd7`.
  Aucun code amont copié, installé ou exécuté ; la licence du code ne vaut pas
  autorisation générale de reproduire tous les contenus associés.
- Capture HTTPS stricte : HTTP 200, 367 349 octets, SHA256
  `3a7a2842cf280879a6abdc746683fbd853e2a221d519469bd8f97352798cad05`.
  Lecture séparée avec le vrai collecteur : dix entrées, **aucune dans la fenêtre
  de trois jours**. Ajout prospectif, sans redatation ni élargissement des filtres.

## Validation locale

Base propre `8efeba80fc2fce223ca162c5169d3fccae16eea7` dans un worktree dédié hors
Bureau. Le Bureau est illisible dans ce contexte ; le clone partagé contient des
conflits préexistants, laissés intacts. Pull réussi uniquement dans le worktree dédié.

Le contrat `tests/test_source_adk.py` échoue avant l'ajout puis passe : unicité,
libellé, export exact de tout le catalogue et compteur. **322 tests Python réussis**
dans une copie isolée. `engine/run.py --essai --sans-redaction` : code 0, 2 405 pages,
zéro rédaction, transfert ou post ; clé chargée pour le solde seulement, jamais affichée.
Trois sources existantes échouent pendant cet essai : Hacker News agents (502),
L'Usine Digitale (403), Reddit Claude (429). Le build réussi ne valide pas tous les flux.

53 fichiers de preuves/publications inchangés ; préfixe du journal préservé.
Aucune donnée d'essai reprise en production. OPML reparsé, 31 couples nom/adresse
identiques au catalogue ; SHA256 `84e01691ffe4362feed0af3ae049e666f8f6570bf3f565c017cef2d6aa5e707f`.
Pièces privées : `crabe-chantiers/croissance-adk/2026-11-10/evidence/`.

Au commit initial, publication et contrôle HTTPS restaient à confirmer.

## Publication vérifiée à 21:09 UTC

Après rebase limité au correctif sur `6c1aea51b353f614fcf04831ae9e7c6730e79b4c`
(aucun delta concurrent dans moteur, tests ou catalogue), contrat ciblé rejoué.
Commit livré : `3de2d125657b93fd932e759759a2607e3b561360` ; ses trois fichiers ont
été relus identiques via l'API GitHub sur `main`.

Le run précédent `42894364849`, sur l'ancien catalogue, a été attendu jusqu'à sa
fin : annulation au plafond de 45 minutes, sauvegarde ignorée. Aucun run annulé
manuellement. Le dispatch `42900868059` du commit livré a ensuite réussi ses
contrats cloud ; son pipeline global reste **en cours** à ce relevé.

Livraison ciblée distincte : `/veille/sources.opml` et uniquement le compteur
**30 → 31** de `/transparence/`, tous ses autres octets conservés. Clé hôte SFTP
épinglée avant secret, base distante exactement comparée à l'export du parent,
sauvegardes privées, contrôle des runs actifs (catalogue nouveau), `.part` puis
renommage et relecture SFTP exacte. **Deux lectures HTTPS canoniques strictes
identiques à 21:09:22 UTC** : 31 flux et compteur cohérent.

Pièces : `livraison-ciblee/{preflight,sftp-result,https-result}.json` et corps
avant/après. Le flux public et la configuration ne prouvent ni nouvelle brève
issue d'ADK, ni croissance mesurée, ni fin du pipeline/sauvegarde cloud.
