# Source primaire Ollama — 2 novembre 2026

Une seule amélioration : ajouter le blog officiel d'Ollama à `data/sources.json`
(`https://ollama.com/blog/rss.xml`, anglais, priorité 4), sans modifier le moteur,
les quotas, le budget mensuel de 30 €, les dates ni les filtres de fraîcheur.
Le catalogue passe de 24 à 25 URL distinctes ; les 24 entrées antérieures sont
conservées dans leur ordre. L'export `/veille/sources.opml` reprend cette entrée.

## Pourquoi cette source

Compléter LangChain et vLLM par les annonces de l'éditeur sur l'exécution de
modèles et les intégrations d'agents. Le blog mélange exécution locale et
services cloud : ni gratuité ni fonctionnement local de toutes ses offres ne
sont présumés. Les annonces restent des sources de l'éditeur, pas une validation
indépendante de ses performances.

Chasse GitHub du 02/11 : [ollama/ollama](https://github.com/ollama/ollama), licence
MIT vérifiée dans `LICENSE` au SHA
`c1db5f9ef203b2e946161bf4c6bd4f2ec7f123b3`, dernier push API observé
`2026-11-02T05:30:37Z`. Aucun code tiers copié, installé ou exécuté : réemploi du
collecteur RSS stdlib et de l'export OPML déjà présents. La licence du logiciel
n'est pas présumée applicable aux textes du blog.

## Vérifications avant livraison

- Base propre `68610ea7b18201859dbe2adca470c44ce663f027`, worktree isolé :
  le Bureau est illisible depuis le cron et le clone partagé est divergent et
  sale. Aucun reset, stash, conflit résolu ni données locales importées.
- Blog et RSS téléchargés en HTTPS strict, HTTP 200 sans redirection. XML réel :
  63 entrées ; le collecteur en lit 25 selon sa limite habituelle. Titres,
  dates, liens du domaine officiel, langue et priorité vérifiés.
- **Aucun candidat Ollama dans la fenêtre de trois jours** à l'heure du contrôle.
  Dernière date source : 24 octobre. Les archives ne sont pas redatées pour
  provoquer une publication ; l'ajout prépare les prochaines annonces.
- **269 tests Python réussis**. Premier appel outil interrompu à 420 secondes
  après la suite (366,743 s), sans résultat final du premier essai. Reprise
  séparée de `engine/run.py --essai --sans-redaction` : code 0 en 195 s,
  2 188 pages construites, zéro rédaction payante, zéro transfert et zéro post.
  Reddit Claude a renvoyé 429 ; ce refus tiers n'est pas masqué.
- 38 fichiers de preuves inchangés, préfixe du journal de recette conservé ;
  aucune donnée de recette reprise dans la production. OPML construit identique
  à la projection du catalogue, 25 URL distinctes ; SHA-256 :
  `dd4bab05870d4e9df99d91611bf52dcb11ee74121e1d15112a6676c21fb59e79`.

Pièces privées : `crabe-chantiers/croissance/2026-11-02/preuves/`
(corps sources, métadonnées HTTPS, licence épinglée, journaux et résultat).

Effet attendu : une veille plus directe sur les modèles et agents utilisant
Ollama, et un export de sources enrichi pour les lecteurs. Aucun gain de trafic,
publication nouvelle, abonnement ou vente mesuré par cette seule configuration.
La présente recette locale ne prouve pas encore la livraison cloud ou HTTPS.
