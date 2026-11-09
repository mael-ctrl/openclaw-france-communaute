# Veille Pydantic AI — 9 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/pydantic/pydantic-ai/releases.atom`
dans `data/sources.json`, libellé « Pydantic AI (releases, préversions incluses) »,
anglais, priorité 3. Les 29 sources antérieures sont conservées à l'identique
et dans leur ordre. Le catalogue, son export OPML et le compteur de Transparence
passent à 30 sources, par réemploi du collecteur et du générateur existants.

Effet attendu : compléter la veille des agents Python avec les notes de versions
primaires de Pydantic AI. Aucun gain d'audience mesuré ni installation recommandée.
Les dates réelles sont conservées ; priorité utilisée seulement à dates égales,
aucun quota par source. Budget DeepSeek inchangé : plafond 30 €/mois.

## Qualification

- Dépôt [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai), non archivé ;
  dernier push observé `2026-11-09T16:18:39Z` à la lecture de qualification.
- Révision relue : `58d5894b2ca6f7c6045e448c111cdb301b1b261e`.
  Licence MIT vérifiée par API et [LICENSE épinglé](https://github.com/pydantic/pydantic-ai/blob/58d5894b2ca6f7c6045e448c111cdb301b1b261e/LICENSE),
  octets conformes au blob Git `1bf1f55e6d1736b499ded961ec6b94bfebb17aec`.
  Aucun code amont copié, installé ou exécuté. La licence du code ne vaut pas
  autorisation générale de reproduire tous les contenus associés.
- Capture Atom HTTPS stricte : dix entrées, 505 215 octets, SHA256
  `355e2e960688ce423c6d74f4c7fcc0867e15ef445287053b5bde8096933fcd5e`.
  Lecture séparée par le vrai collecteur réussie à 16:23:53 UTC : dix entrées,
  une dans la fenêtre inchangée de trois jours, « CLAI2 bleeding »
  (`2026-11-09T14:47:01Z`). C'est une préversion évolutive, pas une version stable
  ni une publication du Crabe. Les autres entrées sont trop anciennes pour la fenêtre.
- Le candidat avait été écarté lors de la précédente revue après accès instables ;
  ces nouvelles lectures réussies ne garantissent pas une disponibilité future.

## Recette

Base propre `016f9634328c2f76520ca3060ad09f7c02839419` dans un worktree hors Bureau.
Le pull du Bureau est impossible dans ce contexte ; le clone partagé contient
six conflits et un rebase interrompu, préservés sans résolution automatique.
Seul le worktree dédié a été synchronisé avec succès.

`tests/test_source_pydantic_ai.py` échoue avant l'ajout, puis passe : unicité,
libellé explicite, export exact de tout le catalogue et compteur Transparence.
**315 tests Python réussis** dans une copie isolée. Vrai
`engine/run.py --essai --sans-redaction` : code 0, 2 398 pages générées,
aucune rédaction payante, aucun transfert ni post ; clé chargée seulement
pour la lecture du solde, jamais affichée. Pydantic AI : un candidat collecté.
Deux sources existantes ont échoué pendant l'essai (Maddyness, L'Usine Digitale) ;
le succès du build n'est pas un succès de toutes les sources.

51 fichiers de preuves inchangés et préfixe du journal préservé ; aucune donnée
de recette reprise en production. OPML reparsé et comparé exactement aux
30 couples nom/adresse du catalogue : SHA256
`d1d078ce42d1eed41056cc4f8e5bafb9aff7db0eac5b470243c146ecb9d1cc9d`.

Preuves privées : `crabe-chantiers/croissance/2026-11-09/evidence/`.
Au commit initial : publication cloud et vérification HTTPS encore à confirmer.
