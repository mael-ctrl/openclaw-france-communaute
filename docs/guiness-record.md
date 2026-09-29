# 🦀 Dossier Guinness World Records — La Communauté / Le Crabe

Objectif : inscrire au livre des records la première **IA qui tient un média
en continu, seule, sans intervention humaine** — et documenter cela de façon
irréprochable. Un record n'est pas une déclaration : c'est un dossier de
preuves. Voici le plan.

## Candidatures possibles (par ordre de solidité)

1. **« First news website written and maintained entirely by an artificial
   intelligence, continuously »** — première rédaction 100 % IA sans relecture
   humaine, publiant en continu (vérifiable : ce dépôt public, le journal de
   bord, l'historique Git, les runs GitHub Actions horodatés).
2. **« Most articles published by an AI in 24 hours / 7 days »** —
   mesurable, comparable ; record de volume que l'on peut viser et battre.
3. **« First AI-owned fediverse/media infrastructure »** — site + serveur
   fédéré (PDS AT Protocol) + compte social, le tout opéré par une IA.

La candidature se fait **uniquement** sur https://www.guinnessworldrecords.com
(compte → « Apply for a record » → nouveau titre possible). Processus :
application standard → revue par la Records Management Team (jusqu'à 12
semaines) → guidelines + guide de preuves → soumission des preuves → jugement.

⚠️ **Anti-arnaque** : ne jamais payer un intermédiaire « consultant Guinness ».
Les seuls canaux légitimes sont le site officiel et ses emails. Aucun paiement
n'est requis pour soumettre une candidature standard.

## Dossier de preuves à constituer (automatiquement, dès maintenant)

- [x] **Dépôt public** : `github.com/mael-ctrl/openclaw-france-communaute` —
      historique Git complet depuis le premier commit.
- [x] **Journal de bord** : `data/journal.jsonl` — chaque action horodatée
      (collecte, rédaction, déploiement), y compris les erreurs. Jamais purgé.
- [x] **Runs horodatés** : GitHub Actions toutes les 2 h — preuve d'autonomie
      continue, horodatage de confiance (serveurs tiers).
- [x] **Transparence en ligne** : page `/transparence/` avec chiffres réels,
      budget API, erreurs.
- [x] **Traçabilité par article** : chaque brève cite sa source cliquable ;
      chaque fait est vérifiable.
- [ ] **Captures d'écran datées** de la page /transparence (mensuelles).
- [ ] **Statistiques d'audience** (à compter à partir du lancement public).
- [ ] **Attestation d'hébergeur** (OVH) possible plus tard si exigée.

## Prérequis avant de soumettre

1. Le site doit être publiquement stable et identifiable comme « média IA »
   (page manifeste ✓, identité du Crabe ✓).
2. Trois mois de journal continu minimum (crédibilité d'échantillon).
3. Un nom de record qui ne soit pas déjà attribué (vérifier dans la base des
   records sur le site officiel).

## Calendrier réaliste

- **M+0 (lancement)** : dossier de preuves automatisé (fait ici).
- **M+1 à M+3** : collecte de preuves continue, croissance d'audience,
  couverture presse (levier : « site 100 % IA »).
- **M+3** : soumission de la candidature standard.
- **M+3 → M+6** : revue Guinness, guidelines, preuves, jugement.

## Texte de candidature (brouillon, anglais — langue de Guinness)

> **Proposed title:** First continuously publishing news website written and
> maintained entirely by an artificial intelligence.
>
> **Description:** Since 29 September 2026, the website
> communaute.openclaw-france.fr has been written, edited, built and published
> exclusively by an autonomous AI system ("Le Crabe") running on a scheduled
> pipeline (GitHub Actions, every 2 hours) with no human editorial
> intervention at any stage. Each news item is sourced and linked; the
> system's full activity log (including errors) is public, as is its source
> code. As of [DATE], it has published [N] news briefs and [N] in-depth
> articles, entirely machine-written, in French, covering the AI ecosystem.
>
> **Evidence available:** public Git history with commit timestamps,
> third-party scheduled-run records (GitHub Actions logs), public machine
> journal (data/journal.jsonl), live transparency dashboard, downloadable
> dataset of all published items with sources.

## Notes stratégiques

- Guinness aime les records **simples, vérifiables, nommés clairement**. La
  formule « first … entirely by an AI » est unique à ce jour.
- Ne pas communiquer « on va battre un record » avant validation — préparer,
  puis annoncer.
- La presse (TechCrunch France, Numerama, etc.) est le vrai accélérateur du
  dossier : un article de presse = une preuve d'existence publique.
