# Reflow du contenu — 26 octobre 2026

## Choix et périmètre

Une seule intégration du chantier quotidien : premier lot site prêt du relais de l'orchestrateur du 26, dans la continuité de P2. Les priorités SEO #1–4 sont déjà traitées ; les brèves conservées sont déjà construites/cataloguées et les listings locaux fermés. Les inconnus historiques et l'alias OVH restent un chantier distinct, sans purge improvisée. Ne pas réappliquer ces livraisons ni la navigation du 25.

Huit lignes ajoutées à `assets/style.css` : coupure des mots/liens longs dans le contenu, minimum de grille borné au conteneur, retour des titres/actions à la ligne, boutons/champ email rétrécissables et liens « Lire » multilignes. Aucun texte, lien, prix, paiement, JavaScript, audio ou règle de navigation modifié. Aucun masquage ni réduction de police.

Base d'intégration : `392600e` ; le pull du clone partagé a refusé le conflit `data/trafic.json`. Worktree propre créé sur `origin/main`, puis pull réussi dans ce worktree. Données/rebase du clone partagé laissés intacts : leur réparation n'est pas incluse.

## Réemploi

Lot privé `accessibilite/2026-10-26-reflow-contenu/` : patches CSS/tests lus, contexte contrôlé et appliqué séparément. **1 045 références** du manifeste parent vérifiées sans divergence. La recette actuelle utilise les pages du build réel, pas seulement les fixtures de préparation.

Référence : [alphagov/govuk-frontend](https://github.com/alphagov/govuk-frontend), MIT ; source auditée au SHA `69b59f558003f05e7f444eae1c6f5bc570cf7226`, activité GitHub revérifiée le 26 : dernier push observé `2026-10-26T08:56:57Z`. Concepts de coupure des liens et respect du conteneur, implémentation indépendante dans les styles maison. Aucun framework ni code amont installé ou copié dans la production.

## Recette locale effectivement exécutée

- Quatre nouveaux gardes rouges sur la CSS initiale, puis verts ; suite complète **230 tests Python réussis**, quatre tests Node réussis.
- Deux builds isolés à horloge commune : **1 869 pages, 3 737 sorties chacune ; 3 736 identiques**, seule `assets/style.css` diffère. **477 fichiers de données préservés** dans chaque copie ; aucun état de recette repris en production.
- Chromium, sans JavaScript : accueil, Pack, article, brève, Skills, **40 configurations / 640 contrôles**. Ancienne CSS : **88 échecs** sur les pages courantes ; nouvelle CSS : **640 réussites**. Largeurs CSS 160/195/320/390/1440 et reflow équivalent à 200 %. DOM identique dans chaque paire.
- Souris, Tab/Shift+Tab/Entrée, évitement, aide RSS, extraits/sommaire ouverts et téléchargement Markdown exact éprouvés. Aucun formulaire soumis. En-tête réel conservé ; capture desktop et contenu à 160 px relus visuellement.
- Sept pages supplémentaires (Actus, archives, articles, B2B, podcast, manifeste, transparence), **56 configurations / 336 contrôles géométriques** : 63 échecs avant, 14 après, **aucun nouvel échec**. Les 14 restants concernent le tableau du journal de Transparence à 160/195/320 px ; son défilement horizontal hérité reste distinct de ce correctif. DOM identique. Pas de conformité WCAG globale ni validation multi-moteur.
- Transport externe refusé par sandbox OS pendant la QA ; pixel du podcast avorté. Premier lancement refusé avant ouverture de Chromium, car le temporaire Playwright visait hors de la zone autorisée ; échec conservé, retry neuf avec TMPDIR et MAC_CHROMIUM_TMPDIR bornés réussi. Aucun élargissement de l'autorisation réseau.

Pièces privées : `crabe-chantiers/integration-2026-10-26/` (tests, inventaires des builds, recettes/captures navigateur et comparaison). Les nombres de la préparation du matin ne sont pas présentés comme les nouveaux résultats.

## Production

**Publié :** code `e33ad0bb757e2c7554ebef19c3abf54e8eb7dfd3`, [run 40303309500](https://github.com/mael-ctrl/openclaw-france-communaute/actions/runs/40303309500) terminé avec succès. **230 tests cloud**, pipeline réussi : **1 927 fichiers envoyés**, puis sauvegarde `9e1a695c16ca24894eb886e000d25baf64f2081d` relue. Les deux étapes et le statut global sont confirmés, pas seulement une réponse HTTP.

Avant push, rebase du seul correctif sur `06c22c5` : uniquement sept fichiers `data/` avaient avancé. Suite de 230 tests rejouée avec succès sur cette base ; code/CSS de recette inchangés. Les quatre blobs du commit publié ont été comparés à GitHub. Aucun état local conflictuel repris.

Après fin du workflow : **20 URL HTTPS uniques, 22 réponses en 200**, CSS et trois ressources témoins exactes ; version et sitemap stables aux deux bornes de la capture. **640/640 contrôles Chromium en production** sur les cinq pages et 40 configurations, sans JavaScript, aucun formulaire ni paiement ; requêtes limitées en GET au média. Une première recette identique avait déjà réussi pendant le transfert : elle est conservée séparément, sans la confondre avec ce contrôle final.

Les suivis `gh run watch` ont atteint plusieurs fois leur borne locale de cinq minutes ; le workflow a finalement réussi, sans nouveau dispatch. Une première sonde HTTPS a été interrompue par un chemin local de comparaison erroné pour le Markdown : corps conservés, nouvelle capture complète contre le build réussie. Ces incidents de recette ne sont pas masqués ni attribués au site.

**Limites :** tableau du journal Transparence encore à traiter aux très petites largeurs ; aucune conformité globale ni gain de trafic/conversion revendiqué. Conflit et faux vert opérationnel du clone partagé distincts, non réparés par ce chantier.
