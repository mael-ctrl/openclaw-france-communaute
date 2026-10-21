# Export des sources de veille en OPML — 21 octobre 2026

## Une amélioration

`/skills/` propose le téléchargement gratuit et sans inscription de
`/veille/sources.opml`, avec trois étapes d'import dans un lecteur compatible.
L'export OPML 2.0 est construit depuis `data/sources.json` : noms et URL exacts,
RSS et Atom, sans copier les articles ni les règles de filtrage du moteur.
Le lien figure aussi dans `llms.txt`. Aucune nouvelle source ni dépendance de
production, aucun formulaire, traceur ou changement commercial.

La liste configurée comprend **22 URL distinctes** à la base de recette
`4aafaecd66799d86ef16c998714b681306f251ba`. Ce nombre n'est pas codé en dur.
La disponibilité de chaque flux n'est pas garantie : l'essai du jour a relevé
un 502 sur HN OpenClaw, un 403 sur Siècle Digital et un 429 sur Reddit Claude.
L'export conserve fidèlement le catalogue, il ne prétend pas certifier sa santé.

## Recherche de réemploi avant implémentation

Métadonnées GitHub et code lus le 21/10/2026 :

| Dépôt | Licence API | Dernier push API | Code examiné / décision |
|---|---|---|---|
| [lemon24/reader](https://github.com/lemon24/reader) | BSD-3-Clause | 15/10/2026 19:37:08 UTC | `src/reader/opml.py`, SHA `f0fa044da4fa47bac51d68bf5c4ea429b116c102` : parsing/export via ElementTree. Pas de lecteur complet à installer dans le média. |
| [kurtmckee/listparser](https://github.com/kurtmckee/listparser) | MIT | 06/10/2026 00:52:48 UTC | `src/listparser/opml.py`, SHA `61270aae1103c325145280427a2be923aa0f318c` : test d'interopérabilité avec la release **0.20**, uniquement en environnement QA isolé. |

Implémentation indépendante via `xml.etree.ElementTree` (stdlib), sans code tiers
copié. Réemploi de la chaîne existante des fichiers annexes. Référence de format :
[spécification OPML 2.0](https://opml.org/spec2.opml), éléments `head/body`,
`outline` avec `text`, et abonnements `type="rss"` / `xmlUrl` (y compris Atom).
Pas de date de publication inventée ni de titre/URL de site tiers déduit.

## Recette exécutée avant push

- Deux cycles rouge/vert : fichier absent, puis lien de téléchargement absent.
- **179 tests Python + 4 Node réussis** ; cinq contrats dans
  `tests/test_sources_opml.py` : fidélité/échappement XML, téléchargement natif,
  build réel, catalogue vide déterministe, refus d'un JSON corrompu.
- Deux builds à horloge commune : **2 963 sorties identiques**, deux modifications
  attendues (`skills/index.html`, `llms.txt`) et un seul ajout (`veille/sources.opml`).
  Les flux du média, podcast/GUID, démonstration B2B, fichiers gratuits et
  livrables du pack restent inchangés.
- **375 fichiers de données de production inchangés**. Vrai
  `engine/run.py --essai --sans-redaction` dans une copie isolée : sortie 0,
  aucune rédaction payante, aucun transfert ni post ; préfixe du journal
  conservé, 26 fichiers de preuves inchangés. Les erreurs de collecte ci-dessus
  sont conservées, pas maquillées en réussite de toutes les sources.
- `listparser 0.20` lit **22 abonnements**, noms et URL identiques au JSON.
  Cela ne constitue pas une importation dans le compte d'un lecteur commercial.
- Chromium sans JavaScript à **360/390/1 440 px** : six téléchargements réels
  souris/Entrée, **2 443 octets identiques**, nom `sources-du-crabe.opml`, sans
  débordement. Captures mobile/desktop relues. Le header mobile reste haut et
  un défilement est nécessaire ; aucun changement de navigation globale.
- SHA-256 OPML : `026987a715b4732222bb4b77a67d529307f5a932b78e06e4eab8a975172dd00f`.

Preuves privées : `crabe-chantiers/croissance/2026-10-21-opml/` — `recette.json`,
logs, copies isolées, `qa-local.json`, téléchargements et captures. Le premier
échec de ciblage du clic est conservé : le défilement CSS animé et le header
exigeaient un placement dans la zone visible ; la production n'a pas été
modifiée pour le masquer.

## Effet attendu et limites

Offrir une ressource utile et partageable pour commencer sa veille, plutôt que
faire recopier les adresses une par une. Aucun gain de trafic, d'abonnement,
de vente ou de rétention mesuré par cette livraison.

## Production vérifiée — 12:48 UTC

- Code **`68fa49797dd46c32a392d762e70e08b1e1288001`**, quatre blobs relus sur
  `main` après push. [Run `39597609143`](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/39597609143)
  **réussi**, 179 tests Python cloud, **1 529 fichiers envoyés**. Sauvegarde cloud
  `0cc5fd5`, intégrée à `0a4456f` après changements concurrents ; ces changements
  n'altèrent pas les fichiers du présent lot.
- `/skills/`, `/veille/sources.opml` et `/llms.txt` répondent **200 en HTTPS strict**,
  sans redirection et avec des octets identiques aux sorties de recette.
  OPML : **2 443 octets**, MIME `text/x-opml`, empreinte indiquée plus haut.
  Les sources de la sauvegarde distante sont identiques au catalogue testé.
- Les **six téléchargements publics souris/Entrée**, sans JavaScript aux trois
  largeurs, donnent le même fichier et le bon nom. Captures de production
  relues ; le bloc ajouté n'a pas de débordement. La navigation préexistante
  reste haute et « Transparence » est tronqué à 360 px : cette mission ne
  revendique pas une correction générale du header.
- Relevés : `cloud-result.json`, `cloud.log`, `https-verification.json`, corps
  HTTPS, `qa-production.json`, téléchargements et captures dans le dossier
  privé cité ci-dessus. Le 404 intermédiaire à 12:47:14 UTC est antérieur à
  l'envoi du fichier à 12:47:35 ; il n'a pas été traité comme un échec final.

Aucune autre amélioration intégrée par cette mission ; aucun contact ni
promotion ajouté. Le téléchargement est livré, pas un résultat de croissance
mesuré ni une garantie de disponibilité des 22 flux tiers.
