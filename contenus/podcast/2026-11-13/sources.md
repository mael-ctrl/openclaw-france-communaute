# La Brève du Crabe — 13 novembre 2026

Script produit par IA, voix synthétique. Sélection des huit brèves les plus récemment rédigées, triées par `date_redac` décroissante, au commit **3235af718d612a9a4e46036b406d4bd421f5d66d**. L'instantané adjacent conserve les entrées exactes de ce blob Git ; la date de rédaction n'est pas assimilée à celle des annonces. Quatre sujets retenus, sources consultées le 13 novembre avant génération à 17:42 UTC.

## 1. Google Hydrogen

- Brève `a5dfd8264c578401`, [relais du Siècle Digital du 13 novembre](https://siecledigital.fr/2026/11/13/google-deploie-une-mise-a-jour-majeure-de-son-moteur-de-recherche-grace-a-gemini-4/).
- [Annonce officielle Google datée du 12 novembre](https://blog.google/products-and-platforms/products/search/gemini-4-hydrogen-search-upgrade/).
- Le script distingue annonce du 12 et relais du 13. Capacités et disponibilité mondiale attribuées au fournisseur, sans test indépendant ni benchmark ajouté.

## 2. Bing : choix des réponses IA

- Brève `69cb7ab648d7ab34`, [Siècle Digital du 13 novembre](https://siecledigital.fr/2026/11/13/microsoft-prend-le-contre-pied-de-google-en-permettant-de-desactiver-les-reponses-ia-dans-bing/).
- [Billet Microsoft Bing](https://blogs.bing.com/search/2026/11/your-choice-turn-ai-answers-on-or-off-in-bing/) : opérateur exact `-ai`, prononcé « moins ai » dans l'audio ; extension Microsoft Bing AI Search Choice en **preview**, Chrome/Edge, qui définit aussi Bing comme moteur par défaut.
- Fonctionnalités lues dans la documentation, non essayées dans un compte utilisateur. Pas de lancement attribué arbitrairement au 13 ni d'affirmation générale sur tous les parcours Google.

## 3. Centre international d'IA de défense

- Brève `a0f81a9f77fe79cb`, [Siècle Digital du 13 novembre](https://siecledigital.fr/2026/11/13/un-centre-international-consacre-a-lintelligence-artificielle-de-defense-va-ouvrir-en-france/).
- [Publication du ministère des Armées du 13 novembre](https://www.defense.gouv.fr/actualites/intelligence-artificielle-france-annonce-lancement-dun-centre-international-defense-rennes) : projet présenté le 12, implantation Rennes, ouverture opérationnelle prévue à l'été 2027 ; coopération et référentiels partagés, pas de production directe de services IA.
- Aucun engagement ferme de pays ni accréditation OTAN déduits du relais ; projet futur distinct d'un centre déjà opérationnel.

## 4. Incident Claude, actualisé avant la voix

- Brève `c5a1b3ed9d9fe9a5`, [Numerama du 13 novembre](https://www.numerama.com/cyberguerre/2373927-panne-de-claude-lia-ne-repond-plus-chez-une-partie-des-utilisateurs-voici-ce-que-lon-sait.html).
- [Fiche officielle de l'incident nn11wk485zfn](https://status.claude.com/incidents/nn11wk485zfn) : investigation à 09:58 UTC, monitoring à 11:05 UTC, **Resolved à 11:58 UTC le 13 novembre**. La fiche liste claude.ai, Claude Console, Claude Code et Claude Cowork comme services affectés ; le dernier texte annonce spécifiquement la résolution pour claude.ai et Cowork.
- Le script dit que **l'incident est classé résolu**, sans extrapoler une garantie de santé de tous les services. Il ne répète pas au présent l'absence de rétablissement de la brève matinale et ne réécrit pas le JSON historique.

## Choix et limites

Les trois entrées relatives à Nvidia ne sont pas retenues ; leurs allégations ne sont donc pas reprises ni validées ici. L'offre commerciale Retroid n'est pas retenue. Les sources journalistiques et primaires ont été lues ; ce travail n'est pas une enquête indépendante ni une validation technique des produits.

Outro : objectif d'un million d'euros de **chiffre d'affaires** en douze mois, engagement de reverser 100 % des **bénéfices** à des associations françaises loi 1901. Aucun don déjà réalisé ni chiffre d'affaires atteint annoncé.

## Audio et réemploi

- `fr-FR-DeniseNeural`, débit `+8%`, edge-tts **7.3.1**, retour 0 ; aucun repli vocal.
- 356 mots séparés par espaces ; **135,888 secondes**, mesurées avec `afinfo` ; décodage intégral FFmpeg réussi.
- MP3 mono 24 kHz, 48 kbit/s, **815 328 octets** ; SHA-256 `0242cd7d6b28fd7bdb9d0a3550d0004012b8f600191e7afa56cfafebbc01eb40`.
- Réemploi du moteur podcast interne et de l'outil externe déjà installé [rany2/edge-tts](https://github.com/rany2/edge-tts). Métadonnées GitHub relues le 13 novembre : dernier push `2026-10-14T09:30:53Z`, licence API `NOASSERTION` ; fichier LICENSE lu : LGPLv3, sauf `srt_composer.py` sous MIT. Aucun code tiers copié, aucune nouvelle dépendance de production.
- Index augmenté sans modifier les anciennes entrées ; script lié explicitement. Le jour éditorial ne crée pas d'heure de première publication ni de `pubDate`.

## Exploitation

Le pull du clone partagé a été refusé pour conflits non résolus. Travail réalisé dans un worktree propre sur `origin/main`, avec pull fast-forward réussi ; aucune résolution, fusion, purge ou réécriture de données/sceaux du clone partagé. Cet incident reste distinct de la livraison éditoriale. Tests, commit et état cloud sont consignés séparément dans la documentation de livraison.
