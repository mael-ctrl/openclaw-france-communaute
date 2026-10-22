# Ressources : désactiver les listings sans bloquer les fichiers

## Chantier quotidien du 22 octobre 2026 — suite SEO #5

**Périmètre unique :** fermer les index de répertoires des ressources du média.
Les priorités #1–#4, les parents d'archives, le catalogue conservé, le compositeur
local et la confidentialité du hub sont déjà intégrés. Les autres lots de la
vague du 21/10 restent privés. La réconciliation des chemins historiques n'est
pas remplacée par cette correction ; aucun contenu n'est purgé ou restauré.

### Changement minimal

Trois fichiers source `.htaccess` contenant exactement `Options -Indexes` :

- `assets/.htaccess` → `/assets/` et ses sous-répertoires ;
- `contenus/fichiers/.htaccess` → `/fichiers/` ;
- `contenus/prive/dl/.htaccess` → le répertoire de livraison existant.

Le constructeur copie déjà ces sources, y compris les fichiers cachés. Aucun
nouveau générateur, dépendance, compte ou changement moteur n'est nécessaire.
Le contrat vérifie deux builds consécutifs : les règles survivent au nettoyage
des dossiers de sortie. Les octets des ressources restent identiques, les règles
ne figurent pas au sitemap, le robots existant et les parents d'archives restent
inchangés. Aucune règle d'authentification, de redirection ou de CORS n'est ajoutée.

**Important :** supprimer un listing ne rend pas les fichiers privés. L'accès
direct aux fichiers de livraison reste inchangé ; ce lot ne prétend pas ajouter
un contrôle de paiement. L'alias d'hébergement `/__ovh_icons/` est hors de ces
répertoires et n'est pas déclaré corrigé. Aucun gain de trafic ou d'indexation
n'est mesuré.

### État initial réellement observé

Base figée après pull : `d97d178657a878210e24529b8f18db527754e01d`.
Revue du dernier rapport/manifeste préparatoire et de la roadmap ; aucun patch
préparatoire réimporté. Le préflight HTTPS du 22/10 à 09:05 UTC conserve 28
réponses : les six dossiers `/assets/`, `/assets/podcast/`,
`/assets/couvertures/`, `/assets/skool/`, `/fichiers/` et le répertoire de
livraison répondent 200 avec listing ; leurs variantes parents sans slash
redirigent. L'alias OVH est également listable. Les fichiers sondés sont lisibles.

Lecture SFTP, clé hôte déjà épinglée vérifiée **avant** l'authentification :
les trois fichiers cibles sont absents. La racine conserve ses règles de
domaine ; `/assets/skool/.htaccess` comporte le CORS `*` dans `IfModule`.
Ces configurations sont sauvegardées hors dépôt, pas écrasées ni importées dans
une configuration globale. Les configurations des deux parents d'archives
sont aussi conservées. Aucun secret publié.

### Chasse GitHub et réemploi

Métadonnées API et code consultés le 22/10 :

| Dépôt | Licence | Dernier push API | Décision |
|---|---|---|---|
| [h5bp/server-configs-apache](https://github.com/h5bp/server-configs-apache) | MIT | 14/07/2026 13:04:51 UTC | `h5bp/security/file_access.conf` confirme la directive native ; pas de reprise des autres règles globales |
| [apache/httpd](https://github.com/apache/httpd) | Apache-2.0 | 21/10/2026 05:13:11 UTC | Documentation de `Options`, pas de dépendance embarquée |

Réemploi effectif : copie de ressources déjà implémentée par notre constructeur.
Sources : [Apache Options](https://httpd.apache.org/docs/2.4/mod/core.html#options)
et [OVH, opérations .htaccess](https://docs.ovhcloud.com/en/guides/web-cloud/web-hosting/htaccess-what-else-can-you-do).
La documentation ne remplace pas la recette du serveur après déploiement.

### Recette locale exécutée

- Rouge : six assertions d'absence échouent, trois dossiers sur deux builds ;
  vert après ajout des seules directives, sans modification du moteur.
- **183 tests Python + 4 tests Node réussis** dans une copie isolée.
- Deux builds `construction.construire()` à horloge commune et réseau interdit :
  **3 108 sorties existantes identiques**, trois ajouts seulement ; aucune
  suppression ni modification. **389 fichiers de données préservés.**
- CLI `--essai --sans-redaction` dans une troisième copie : retour 0, aucun
  transfert, rédaction ou post ; manifestes et registre identiques, préfixe du
  journal préservé. Collecte partielle (deux délais réseau, un 403, un 429),
  conservée dans les logs. Aucune donnée de test réimportée.
- Le clone partagé a avancé par sa mise à jour locale jusqu'à `f2d0bce` pendant
  la recette : aucun changement moteur/tests/assets/contenus par rapport à la
  base figée. Cette différence de données est conservée, pas annulée.

### Production

Intégration testée localement ; preuve cloud, relecture SFTP et recette HTTPS
à consigner après publication. Ne pas assimiler un push à un déploiement réussi.

Preuves privées : `crabe-chantiers/archives/2026-10-22-listings/` (préflights,
corps HTTPS, rouge/vert, suites, builds et essai) ; copies de recette sous scratch
Hermes. Livraison locale uniquement, aucun message extérieur.
