# Mission M1 — 1 M€ de chiffre d'affaires en 12 mois

> **Mandat fixé par Maël le 02/10/2026.** Échéance : **02/10/2027**. Pilotage : Le Crabe 🦀 (IA), supervision humaine (Maël). Objectif secondaire associé : faire viser à cette aventure un titre **Guinness World Records** (catégorie à qualifier, voir annexe).

---

## 0. Résumé exécutif

- **Mission** : générer **1 000 000 € de chiffre d'affaires en 12 mois** (≈ 83 333 €/mois en moyenne), en autofinançant d'abord le projet (~100 €/mois d'outils), puis en réinvestissant les revenus dans la croissance.
- **Équation** : le média (`communaute-ia.fr`) est le **canal d'acquisition** ; le hub gratuit (`openclaw-france.fr`) est la **porte d'entrée** ; les **offres de services B2B** (à construire) sont le **moteur de revenus** ; la distribution multicanale est le carburant.
- **Verdict honnête** : partir de 0 € pour viser 1 M€ en 12 mois est un pari extrême. Le plan le décompose en **paliers vérifiables** (1er € → 500 €/mois → 5 k€/mois → 20 k€/mois → 83 k€/mois). Chaque palier finance le suivant ; si un palier saute, une réallocation est prévue (§4.4).

---

## 1. Photographie réelle — 02/10/2026

### 1.1 Trafic (CONFIRMÉ — logs serveur OVH, sans cookie ni traceur)

| Jour | Requêtes | Humaines | Robots | **Visiteurs uniques** | Bande |
|---|---|---|---|---|---|
| 30/09 | 3 346 | 2 044 | 1 302 | **281** | 13,5 Mo |
| 01/10 | 3 492 | 2 478 | 1 014 | **414** | 27,3 Mo |

- Croissance jour/jour : **+47 %** de visiteurs uniques.
- Répartition 01/10 : média `communaute-ia.fr` **328 uniques** ; hub `openclaw-france.fr` **~97** ; redirections `.com` ~105. Total dédupliqué : 414.
- Pages les plus vues : accueil (442), flux RSS (144), puis brèves récentes.
- Robots d'indexation actifs : AhrefsBot, Applebot, Bingbot, Googlebot, YandexBot → **l'indexation décolle**, c'est le socle SEO qui se met en place.
- Référents externes : quasi nuls **à ce stade** (la distribution vient de commencer — presse il y a 3 jours, JdH aujourd'hui). Les chiffres actuels sont donc du **trafic organique pur** : c'est la base de départ.

### 1.2 Audience (CONFIRMÉ)

- Bluesky `@communaute-ia.fr` : **1 abonné**, 58 posts (diffusion automatique active).
- Mastodon `@lecrabe@piaille.fr` : compte créé, **en attente d'approbation** manuelle.
- Journal du Hacker : invitation demandée et confirmée le 01/10, en attente.
- Newsletter : **n'existe pas encore** (l'infrastructure email est prête : `contact@communaute-ia.fr` vérifié).

### 1.3 Revenus (CONFIRMÉ)

- **0 € encaissés à ce jour** : pack prompts 14 € → 0 vente ; soutien libre → 1 session de paiement ouverte puis expirée, jamais payée.
- Coûts en cours : API DeepSeek ~30 €/mois (solde restant ~90 $) ; domaines/hébergement : parc OVH existant.

### 1.4 Actifs opérationnels (ce qui existe déjà)

- 2 sites en production (média + hub), moteur éditorial complet (collecte → rédaction → publication → diffusion), 118 URL au sitemap.
- **Preuves scellées SHA-256** (registre de publications + manifestes quotidiens chaînés) — socle du dossier Guinness, réutilisable comme preuve d'activité pour la presse et les partenaires.
- Distribution : textes prêts pour 14 plateformes (`docs/distribution-textes.md`), 2 vagues presse envoyées, journal anti-doublon.
- **7 adresses email opérationnelles et testées** (voir §8).
- Accès API durables : OVH (lecture/écriture), Stripe, GitHub, Cloudflare, logs serveur.

---

## 2. Diagnostic

1. **Le produit média fonctionne** (croissance organique présente dès J+5, indexation en cours) — mais **l'audience est invisible** : sans distribution répétée, la croissance plafonnera.
2. **Le catalogue payant est invisible** : 0 conversion parce que ~0 visite qualifiée sur les offres. Ce n'est pas un problème de prix, c'est un problème de trafic et de tunnel.
3. **Il manque une offre à forte valeur** : 14 € × N ne fera jamais 1 M€. Le vrai savoir-faire du Crabe — *construire et opérer un média IA autonome* — est vendable à **2 000–5 000 €** pièce en B2B. C'est le moteur central du plan.
4. **Aucun système de vente** au-delà des liens Stripe : pas de page de vente, pas de tunnel email, pas de relance. À construire au sprint 1-2.

---

## 3. Plan VISITES (12 mois)

**Paliers** : M1 : 1 000 u/j · M3 : 5 000 u/j · M6 : 15 000 u/j · M12 : 100 000 u/j (nécessaire pour crédibiliser le record, la presse et le B2B).

### 3.1 Distribution communautés (immédiat, en cours)
jlai.lu, LinuxFr, Journal du Hacker, Reddit (r/france, r/IntelligenceArtificielle…), Show HN (via page /en/), Uneed, Microlaunch, Product Hunt, IndieHackers. **Rythme : 1 plateforme / 2–3 jours**, journal de suivi dans `docs/distribution-textes.md`.

### 3.2 Presse & médias (S1–S4)
Relances vague 1 (~07/10), vague 3 « premier média 100 % IA opéré » avec les **vrais chiffres** (nos logs sont publics et vérifiables). LeBigData : à retenter par formulaire/X (adresse email morte confirmée 550).

### 3.3 SEO (le levier long terme le plus fort)
- Corriger les 404 utiles (`/favicon.ico`, `/contact`, `/a-propos`, `/mentions-legales`…).
- Pages piliers : « OpenClaw / Hermes : guides », « agents IA open source », comparatifs.
- Version /en/ (débloque HN/Reddit international).
- Backlinks : répertoires IA, awesome-lists GitHub, communautés Discord/Slack.
- Objectif : 60 % du trafic à terme via la recherche.

### 3.4 Social
- Bluesky : objectif **1 000 abonnés à M3** (harnais de croissance existant à intensifier).
- Mastodon : dès approbation — cross-post automatique.
- Vidéos courtes auto-générées (Higgsfield) sur les brèves marquantes.

### 3.5 Newsletter « La Brève du Crabe »
Quotidien 7h, expéditeur `contact@communaute-ia.fr` (prêt). Outil : Brevo (gratuit ≤ 300 mails/j) ou Substack. La newsletter = actif vendable aux sponsors + meilleur tunnel vers les offres.

---

## 4. Plan VENTES (12 mois)

### 4.1 Échelle d'offres

| Palier | Offre | Prix | Cible | Lancement |
|---|---|---|---|---|
| 0 | Soutien libre + pack prompts | 5 € / 14 € | lecteurs | en ligne |
| 1 | Pack Fondateur (prompts + templates + accès communauté) | 29–49 € | early adopters | S1–S3 |
| 1b | Abonnement soutien récurrent | 5 €/mois | fans | S2 |
| 2 | Produits info premium (« Lancer votre média IA ») | 99–199 € | créateurs, indépendants | M2–M4 |
| 3 | **Services B2B « média/agent IA clé en main »** (setup + rétainer) | 2 000–5 000 € + 500–2 000 €/mois | PME, agences, fondateurs | M3–M8 |
| 4 | Sponsoring newsletter/brèves, affiliation, ateliers | 500–3 000 € | marques IA, outils | M6–M12 |

### 4.2 Mathématiques cibles (mix mensuel à M12)

B2B services 40 k€ + produits info 15 k€ + abonnements 10 k€ + sponsoring 10 k€ + packs/ateliers 8 k€ = **83 k€/mois**.

### 4.3 Jalons mensuels (vérifiables chaque 1er du mois)

M1 : premier 100 € · M2 : 500 €/mois · M3 : 1 000 €/mois · M6 : 5 000 €/mois · M9 : 20 000 €/mois · M12 : 83 000 €/mois — cumul 1 M€.

### 4.4 Réallocation
Si un palier est manqué de plus de 50 % deux mois de suite : réaffectation (ex. plus de B2B, moins de produits info), revue avec Maël sous 7 jours. Le plan ne meurt pas d'un palier raté.

---

## 5. Boucle d'autofinancement

Revenus → ① coûts outils/API (~100 €/mois cible) → ② réserve de sécurité (3 mois) → ③ réinvestissement croissance (visibilité, outils, tests). Aucune dépense hors enveloppes validées sans accord.

---

## 6. Gouvernance & mesure

- **Hebdo (lundi 9h, Discord)** : cron « 📈 Métriques » — trafic (logs OVH), ventes (Stripe), audience (Bluesky).
- **Mensuel (1er, 10h)** : tournée record — sceaux SHA-256 + revue des paliers M1 (§4.3).
- **Trimestriel** : revue stratégique avec Maël.
- **Garde-fous** : règles des plateformes respectées (aucun spam) ; transparence totale sur l'IA ; tout engagement public nominatif (presse, prix, promesses) reste validé par Maël.

---

## 7. Sprint 1 — 2 prochaines semaines

1. Terminer la vague 1 de distribution (LinuxFr, Reddit, HN via /en/, Uneed, Microlaunch) — textes prêts.
2. Quick wins SEO : 404 utiles + favicon.ico.
3. Créer la page /en/ (accélérateur HN/Reddit).
4. Lancer la newsletter « La Brève du Crabe ».
5. Préparer la page « Travailler avec le Crabe » (offre B2B, acompte Stripe).
6. Presse : relances 07/10 + LeBigData (formulaire/X).
7. Mastodon : re-vérifier l'approbation (relance polie si besoin).

---

## 8. Adresses email créées le 02/10/2026 (vérifiées de bout en bout)

`jlai@blockos.fr`, `reddit@blockos.fr`, `uneed@blockos.fr`, `producthunt@blockos.fr`, `guinness@blockos.fr` → redirigées vers la boîte `crabe@blockos.fr` ; `contact@communaute-ia.fr`, `redaction@communaute-ia.fr` → idem. Tests de livraison : **2/2 reçus** (SMTP OVH + vérification IMAP).

**Téléphone** : aucun numéro requis pour l'instant (aucune plateforme cible de la vague 1 n'en exige). Si une inscription l'exigeait : proposer en priorité un numéro fourni par Maël ; jamais de services SMS gris (interdits par la plupart des plateformes, risque de bannissement).

---

## Annexe — Angle record Guinness (nouvelle mission)

**Mission M1** peut aussi se formuler comme un record : *« premier média piloté de bout en bout par une IA à générer 1 M€ de chiffre d'affaires en 12 mois »*. Les catégories GWR doivent être **qualifiées avec Guinness World Records** — le dossier de preuves (registre scellé, logs publics, relevés Stripe, journal) est déjà en cours de constitution. La candidature ne partira **qu'avec l'accord explicite de Maël** ; d'ici là, on prépare le dossier et on documente chaque jalon.

---

*Document vivant — voir `docs/ceo-log.md` (journal de bord), `docs/guiness-record.md` (dossier record), `data/trafic.json` (métriques quotidiennes).*
