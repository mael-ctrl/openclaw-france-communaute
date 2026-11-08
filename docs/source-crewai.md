# Veille CrewAI — passage du 7 novembre, exécuté le 8 novembre 2026

## Une amélioration

Ajout du flux officiel `https://github.com/crewAIInc/crewAI/releases.atom`
dans `data/sources.json`, libellé « CrewAI (releases, préversions incluses) »,
anglais, priorité 3. Les 28 sources antérieures sont conservées à l'identique
et dans leur ordre ; le catalogue et son export OPML passent à 29 sources.
Réemploi du collecteur et du générateur OPML existants, aucun nouveau moteur.

Effet attendu : compléter la veille des agents par les notes de versions de
CrewAI, sans dépendre d'une reprise par un média tiers. Aucun gain d'audience
mesuré ni installation recommandée. La priorité départage les dates égales,
pas les sources par quota ; préversions possibles, dates réelles conservées.
Aucun changement du plafond DeepSeek de 30 €/mois ni des quotas de rédaction.

## Qualification et limites de disponibilité

- Dépôt officiel : [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI),
  non archivé, dernier push observé `2026-11-08T08:33:48Z`.
- Révision relue : `2fba413623a60d7a2f24a7d21685bbcd8dd45a4f` ; licence MIT
  vérifiée par API et [LICENSE épinglé](https://github.com/crewAIInc/crewAI/blob/2fba413623a60d7a2f24a7d21685bbcd8dd45a4f/LICENSE),
  conforme au blob Git `a6ee25527ec07201e4373fcbf89f128f304a6f2e`.
  Aucun code amont copié, installé ou exécuté ; cette licence du code n'est
  pas une autorisation générale de reproduire tous les contenus associés.
- Le vrai collecteur a lu dix entrées à 10:39 UTC le 8 novembre. Capture HTTPS
  stricte indépendante par curl : 39 947 octets, dix entrées, empreinte
  `22b22816f6c50aa341763f64dd94c6f4affb2f2268018640b2b3562e46899ddd`.
- À 10:55 UTC, deux entrées de cette capture sont dans la fenêtre inchangée
  de trois jours : `1.15.37` (7 novembre) et `1.15.36` (6 novembre).
  Ce sont des candidats, pas des publications du Crabe.
- **Disponibilité intermittente** : d'autres lectures ont répondu timeout,
  502 ou 504. L'essai complet a également rencontré ces erreurs sur CrewAI
  et plusieurs flux GitHub existants. Le succès du build ne signifie pas
  succès de chaque source ; aucune garantie de collecte immédiate.
- Pydantic AI et Google ADK examinés mais non ajoutés après lectures instables.

## Validation

Base propre `e04a96e28217bc1341788ad0ffb12068f1d9863c`, dans un worktree
hors Bureau. Le clone partagé est en conflit/rebase et reste intact ;
synchronisation réussie seulement dans le worktree de cette mission.

`tests/test_source_crewai.py` échoue avant l'ajout puis réussit : unicité,
libellé explicite, export exact de tout le catalogue et compteur Transparence.
**305 tests Python réussis** dans une copie isolée. Vrai
`engine/run.py --essai --sans-redaction` : code 0, 2 377 pages générées,
aucune rédaction payante, aucun transfert ni post. La clé est chargée seulement
pour la lecture du solde et n'est pas affichée. Les erreurs de sources restent
consignées dans le journal de recette.

50 fichiers de preuves inchangés et préfixe du journal préservé ; aucune donnée
de recette reprise en production. OPML reconstruit, reparsé et comparé aux
29 couples nom/adresse du catalogue : SHA-256
`2f5a178e20ded382698d1d42875e58498d0de18638b899647ecc1ee2728417b8`.

Preuves privées : `crabe-chantiers/croissance/2026-11-07/evidence/`.
Au commit initial, publication cloud et recette HTTPS encore à confirmer.

## Publication ciblée vérifiée le 8 novembre à 11:15 UTC

Configuration, test et document initial : **`e09b21c202207b0f721cfe39ed8db76829811735`**,
avec trois blobs relus identiques sur `main` distant. Dispatch `42473537205`
sur ce commit ; aucun changement de cadence, workflow ou secrets.

Avant le SFTP, attente de la fin du run sur l'ancien catalogue `42471488727` :
annulé pendant le pipeline après environ 45 minutes, sauvegarde ignorée.
Son état et ses logs sont conservés ; aucune annulation manuelle.

Préflight : OPML distant exactement conforme au catalogue parent ; sauvegarde
des deux cibles et identité HTTPS/SFTP vérifiées. Clé hôte épinglée avant
authentification. Envoi `.part`, renommage puis relecture SFTP exacte :
seuls `/veille/sources.opml` et le compteur **28 → 29** de Transparence changent,
tous les autres octets de cette page servie sont préservés.

La première comparaison HTTPS après SFTP a différé ; échec conservé, aucun
renvoi ni réécriture pour le masquer. **Deux nouvelles lectures canoniques
TLS strictes à 11:15:05 UTC : 200 et octets exacts**, 29 flux uniques,
CrewAI présent une fois. La cause de l'écart initial n'est pas établie.
Preuves : `livraison-ciblee/` et `evidence/https-20261108T111505Z/`.

Contrats du nouveau run cloud **réussis à 11:15:26 UTC**. Au contrôle de
11:15:29, son pipeline est en cours et sa sauvegarde en attente : la publication
ciblée est acquise, pas la clôture globale du cloud ni une collecte CrewAI
réussie dans ce run. Le conflit du clone partagé reste ouvert et préservé.
