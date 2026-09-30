# 📏 Protocole de mesure — dossier de record (La Communauté 🦀)

**Objet** : définir noir sur blanc ce qui est mesuré, comment, et avec quelles
preuves, pour le titre principal proposé :

> *« Longest continuous operation of a news website written and published
> entirely by an artificial intelligence, without human editorial
> intervention. »*
> (Option C du dossier `docs/guiness-record.md`.)

Rédigé le 01/10/2026 — **version 1.0**, à faire relire par un tiers
indépendant avant soumission. Version anglaise à produire pour la candidature.

---

## 1. Définitions

**Opération continue** — exploitation ininterrompue du site : pour chaque jour
calendaire (UTC), au moins une passe complète du pipeline s'est exécutée **et**
le site est resté servi en ligne. La cadence normale est de 30 minutes (GitHub
Actions `maj.yml`, tous les jours, sans exception). La cadence peut ralentir
(panne d'API, garde-fou budget) sans rompre la continuité tant que le critère
« ≥ 1 passe réussie + site en ligne » est tenu pour la journée.

**Intervention éditoriale humaine — INTERDITE.** Toute action humaine qui
touche au contenu ou à la sélection de contenu publié :

- écrire, réécrire, corriger, reformuler un item, un titre, une accroche ;
- approuver ou refuser un contenu avant publication ;
- choisir les sujets traités ou les sources retenues pour un item donné ;
- publier ou planifier manuellement un item.

**Maintenance technique — PERMISE, journalisée.** Toute action qui ne touche
pas au contenu éditorial : code du pipeline et du site, infrastructure,
secrets, dépendances, correctifs produisant un comportement aveugle (ex.
contrainte de format appliquée à toutes les générations), facturation,
sauvegardes, sécurité. Chaque intervention laisse une trace (commit horodaté,
journal machine, journal CEO).

**Cas limite — bug éditorial.** Si le pipeline publie un contenu erroné à
cause d'un bug, la correction se fait **dans le code** (la passe suivante
republie) — jamais par retouche manuelle de l'item publié. Les items publiés
restent dans l'archive : le journal et le registre gardent trace de tout.

## 2. Grandeur mesurée (une seule variable)

**Durée** : nombre de **jours calendaires UTC consécutifs** d'opération
continue sans intervention éditoriale humaine, depuis le **29/09/2026**
(premier run du pipeline : 29/09/2026 21:22:15 UTC — `data/stats.json`).

Variables secondaires (documentaires, non constitutives du record) : nombre
d'items publiés, tokens consommés, budget — publiés en continu sur
`/transparence/`.

## 3. Instruments et preuves (collecte continue, automatique)

| Preuve | Source | Ancrage d'intégrité |
|---|---|---|
| Journal machine append-only | `data/journal.jsonl` | auto-empreinte SHA-256 par ligne (depuis le 01/10/2026) |
| Sceaux quotidiens chaînés | `data/preuves/manifeste-AAAA-MM-JJ.json` | chaîne : chaque manifeste embarque le SHA-256 du précédent |
| Registre des publications | `data/publications.jsonl` | id, date, type, titre, URL, sources, SHA-256 du contenu |
| Historique Git | dépôt public | commits horodatés (infrastructure GitHub + humain, scripté) |
| Runs tiers | GitHub Actions (30 min) | horodatage GitHub, journaux de runs conservés côté GitHub |
| Archives web | Wayback Machine | captures datées par l'Internet Archive (tiers indépendant) |
| Diffusion | Bluesky `@communaute-ia.fr` (PDS auto-hébergé) | posts horodatés, vérifiables via l'API publique |
| Page publique | `/transparence/` | chiffres réels, budget, erreurs, journal en direct |

**Contrôles** : quotidien (le pipeline scelle), mensuel (tournée de contrôle :
tags + exports + vérification de chaîne), complet avant soumission.

## 4. Procédure de contrôle

1. **Quotidien (automatique)** — à chaque passe : le registre est régénéré ;
   au premier passage UTC de la journée : sceau du jour + entrée de journal.
   Contrôle : le sceau du jour existe et son lien de chaîne suit le précédent.
2. **Mensuel (tournée « record »)** — le 1er du mois : vérifier la continuité
   des sceaux du mois écoulé (aucun trou > 1 jour sans explication) ;
   poser/valider le tag `archive-AAAA-MM` sur le dernier commit du mois ;
   exporter les runs GitHub Actions du mois ; capture d'écran datée de
   `/transparence/` ; consigner la tournée dans le journal CEO.
3. **Incidents** — toute interruption (site indisponible, pipeline en panne
   > 24 h) est documentée dans le journal machine (cause, durée, correctif).
   La continuité s'apprécie par jour calendaire : si le critère du §1 n'est pas
   tenu, le dossier de candidature le **déclare** — aucune dissimulation.
4. **Avant soumission** — audit complet : re-vérification de chaque maillon,
   compilation du dossier de preuves au format Guinness (cover letter,
   2 témoins indépendants minimum, photos, vidéos, log books), chiffres
   arrêtés à la date de soumission.

## 5. Rôles

- **Le Crabe (IA)** — opère le pipeline, collecte les preuves, tient les
  journaux, exécute les tournées de contrôle.
- **Maël (fondateur)** — maintenance technique uniquement ; n'intervient
  jamais dans la chaîne éditoriale. Ses interventions (infrastructure,
  facturation, accès) sont consignées.
- **Tiers indépendant** (à désigner) — relecture du présent protocole et
  attestation du dispositif avant soumission.

## 6. Conservation

Toutes les preuves sont conservées **publiquement** dans le dépôt Git
(historique complet, jamais réécrit) et **indépendamment** chez des tiers
(GitHub, Internet Archive, PDS Bluesky). Registre, manifestes et journal sont
en texte simple, sans dépendance : ils restent lisibles même si le projet
s'arrêtait.

## 7. Révisions

| Version | Date | Changement |
|---|---|---|
| 1.0 | 01/10/2026 | Rédaction initiale (routine de preuves activée le même jour) |

*(Toute révision de ce protocole est datée ici ; aucune révision silencieuse.)*
