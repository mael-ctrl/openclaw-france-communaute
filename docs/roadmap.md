# 🗺️ Roadmap — La Communauté 🦀 (média + monétisation)

**Mise à jour : 2026-10-15** · Audit : Maël · Tenue à jour : cron « 🌍 Roadmap & gouvernance » (21 h) + intégration quotidienne (10 h 45).

## Mandat
1 M€ de CA en 12 mois (échéance 02/10/2027) — **100 % des bénéfices reversés à des associations françaises loi 1901** ; tout documenté (journal public, page Transparence, manifestes chaînés).

## Phases (critère de fin = preuve vérifiable)

| # | Chantier | Critère de fin | État |
|---|---|---|---|
| P1 | Actu Google / fraîcheur | news-sitemap live + Search Console vérifiée + contenu neuf < 24 h | 🔶 news-sitemap ✅ 14/10 · GSC : action Maël |
| P2 | Revue site (perf, SEO, UX, engagement) | 1 amélioration vs testée **par jour** intégrée (cron chantier) | 🔶 15/10 : fiabilité du déploiement ✅, 72 tests OK, run 38708738646 et HTTPS vérifiés ([preuve](verification-deploiement.md)) |
| P3 | Podcast + YouTube | pilote ✅ · 1er épisode publié + chaîne créée + RSS podcast | 🔶 pilote 14/10 · chaîne : action Maël |
| P4 | Newsletter « La Brève du Crabe » | plan + 1er numéro + formulaire en ligne + 100 abonnés | ⏳ plan en cours (sous-agent) |
| P5 | Monétisation | 1er 100 € encaissés, puis paliers M2→M12 du plan | 🔶 15/10 : échantillon B2B sourcé en ligne, parcours et téléchargements vérifiés ; encaissement non démontré ([preuve](monetisation.md)) |
| P6 | Presse & distribution | vague-3 soumise + retombées mesurées | 🔶 vagues 1-2 faites · vague-3 en préparation |
| P7 | Record Guinness | dossier qualifié + preuves chaînées (routine active) | 🔶 en continu |
| P8 | Skool « La Communauté IA 🦀 » | communauté publique + 22/22 leçons + 1er membre externe | 🔶 18/22 leçons · promo à brancher |
| P9 | Organisation & process | organigramme + SOPs + orchestration multi-agents appliqués | ✅ v1 rédigée 14/10 (`crabe-chantiers/organisation/`, 25/25 crons validés) |
| P10 | Affiliation | programme Skool + pack opérationnels (divulgation partout) | 🔶 plan prêt (Skool 30 % ; produit payant à trancher) · enquête MEDVI faite |

## Actions Maël (bloquants identifiés — 1 clic chacun)
1. **Search Console + Bing Webmaster Tools** (compte Google) — le record DNS/balise sera préparé pour validation.
2. **Chaîne YouTube « La Brève du Crabe »** + projet OAuth (guide pas-à-pas prêt : `crabe-chantiers/youtube/guide-lancement.md`).
3. **PayPal de l'association loi 1901** (nom à valider) — canal de don officiel.

## Journal des jalons
- **2026-10-14** : mission associations publiée (manifeste/transparence/accueil/llms.txt) ; news-sitemap live ; pilote podcast généré (61 s) ; +6 crons ; 8 sous-agents lancés ; clone réparé ; trafic 12-13/10 publié.
- **2026-10-14 (soir)** : organisation v1 + plan d'affiliation + enquête MEDVI livrés (sous-agents) ; correctif Discover (`max-image-preview:large`) poussé ; orchestrateur de vagues et 7 crons opérationnels.
- **2026-10-15 (chantier unique, livré)** : faux succès FTP reproduit puis corrigé ; arrêt des annonces après échec, code processus 1 et sauvegarde d'état du workflow maintenue. Commit `3e79f4b`, **72 tests OK**, build isolé et essai sans rédaction validés ; **run 38708738646 réussi, 628 fichiers envoyés, 5 URL HTTPS vérifiées**, HTML brève/article identiques au rendu du commit cloud `8546b36`. [Contrat et preuves](verification-deploiement.md). Priorité donnée au prérequis de livraison fiable identifié par la vague du matin ; aucun lot podcast/B2B/newsletter intégré.

- **Jalon monétisation du 15/10** : une démonstration de veille publiée depuis `/b2b/`, avec deux téléchargements et qualification facultative ; run `38728943975` et HTTPS vérifiés. Prix, contrats et paiements inchangés ; aucun email ni promotion supplémentaire. [Compte-rendu](monetisation.md).

## Prochain chantier SEO (ordre d'impact conservé)
- Actions #1 (grands aperçus) et #2 (news-sitemap) déjà en place ; **#3 images de couverture automatiques** reste la première intégration SEO à réaliser, puis #4 JSON-LD/dates visibles et #5 autoindex/couverture des archives. Ne pas annoncer ces fonctionnalités comme livrées sur la base d'un brouillon de sous-agent.
