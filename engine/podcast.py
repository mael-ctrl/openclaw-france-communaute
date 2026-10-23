"""Podcast statique : index éditorial + pilote, stdlib, sans réseau ni audio généré."""
import xml.etree.ElementTree as ET
import hashlib
import json
import math
import re
from pathlib import Path
from html import escape
from datetime import datetime, timezone
from email.utils import format_datetime
from urllib.parse import urlsplit

ATOM = 'http://www.w3.org/2005/Atom'
ITUNES = 'http://www.itunes.com/dtds/podcast-1.0.dtd'
ET.register_namespace('atom', ATOM)
ET.register_namespace('itunes', ITUNES)


def valider_metadonnees(pilote):
    """Refuse les valeurs ambiguës et les caractères interdits en XML 1.0."""
    for cle in ('titre', 'description', 'guid', 'fichier', 'mime'):
        valeur = pilote.get(cle)
        if not isinstance(valeur, str) or not valeur.strip():
            raise ValueError(f'Champ texte obligatoire : {cle}')
        if any(not (c in '\t\n\r' or 0x20 <= ord(c) <= 0xD7FF or
                    0xE000 <= ord(c) <= 0xFFFD or 0x10000 <= ord(c) <= 0x10FFFF)
               for c in valeur):
            raise ValueError(f'Caractère interdit en XML : {cle}')
    if not re.fullmatch(r'[A-Za-z0-9_-]+\.mp3', pilote['fichier']):
        raise ValueError('Le nom du MP3 doit être un fichier local simple')
    if pilote['mime'] != 'audio/mpeg':
        raise ValueError('Le pilote doit déclarer audio/mpeg')
    if type(pilote.get('octets')) is not int or pilote['octets'] <= 0:
        raise ValueError('Taille entière positive obligatoire')
    duree = pilote.get('duree_secondes')
    if type(duree) not in (float, int) or not math.isfinite(duree) or duree <= 0:
        raise ValueError('Durée positive finie obligatoire')
    date_publication(pilote.get('publie_le'))


def origine_https(url_site):
    """Le site statique est à la racine d'une origine HTTPS sans identifiants."""
    label = r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?'
    if not isinstance(url_site, str) or not re.fullmatch(
            rf'https://{label}(?:\.{label})*(?::[0-9]+)?/?', url_site):
        raise ValueError('Origine HTTPS mal formée')
    url = urlsplit(url_site)
    if url.port == 0:
        raise ValueError('Port HTTPS invalide')
    if (url.scheme != 'https' or not url.hostname or url.username is not None or
            url.password is not None or url.query or url.fragment or url.path not in ('', '/') or
            any(c.isspace() for c in url_site)):
        raise ValueError('URL_SITE doit être une origine HTTPS sans chemin ni identifiants')
    return url_site.rstrip('/')


def charger_pilote(dossier_assets):
    """Échoue si les métadonnées ne désignent plus les octets vérifiés."""
    dossier = Path(dossier_assets) / 'podcast'
    pilote = json.loads((dossier / 'pilote.json').read_text(encoding='utf-8'))
    valider_metadonnees(pilote)
    donnees = (dossier / pilote['fichier']).read_bytes()
    if len(donnees) != pilote['octets'] or len(donnees) == 0:
        raise ValueError('Taille du MP3 différente des métadonnées vérifiées')
    if hashlib.sha256(donnees).hexdigest() != pilote['sha256']:
        raise ValueError('Empreinte du MP3 différente des métadonnées vérifiées')
    return pilote


def date_publication(iso):
    """Date RSS en UTC ; aucune déduction à partir d'une date de build."""
    if iso is None:
        return None
    if not isinstance(iso, str):
        raise ValueError('La date de publication doit être une chaîne ISO avec fuseau')
    dt = datetime.fromisoformat(iso)
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError('La date de publication exige une heure et un fuseau explicites')
    return dt.astimezone(timezone.utc)


def charger_episodes(racine):
    """Adapte l'index éditorial existant sans convertir son jour en pubDate."""
    racine = Path(racine).resolve()
    index = json.loads((racine / 'contenus/podcast/episodes.json').read_text(encoding='utf-8'))
    if not isinstance(index, list):
        raise ValueError('L’index podcast doit être une liste')
    pilote = charger_pilote(racine / 'assets')
    ids, fichiers = {'pilote'}, {'assets/podcast/' + pilote['fichier']}
    episodes = []
    for entree in index:
        if not isinstance(entree, dict) or not {'id', 'date', 'titre', 'fichier', 'durée'} <= entree.keys():
            raise ValueError('Épisode incomplet : id/date/titre/fichier/durée requis')
        identifiant, jour, chemin = entree['id'], entree['date'], entree['fichier']
        if not isinstance(identifiant, str) or not re.fullmatch(r'[A-Za-z0-9_-]+', identifiant):
            raise ValueError('Identifiant stable invalide (ne pas le normaliser)')
        if not isinstance(chemin, str):
            raise ValueError('Le chemin MP3 doit être du texte')
        if identifiant in ids or chemin in fichiers:
            raise ValueError('Identifiant ou fichier podcast dupliqué')
        if not isinstance(jour, str) or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', jour):
            raise ValueError('Date éditoriale attendue au format AAAA-MM-JJ')
        datetime.strptime(jour, '%Y-%m-%d')
        if not isinstance(chemin, str) or not re.fullmatch(r'assets/podcast/[A-Za-z0-9_-]+\.mp3', chemin):
            raise ValueError('Chemin MP3 attendu sous assets/podcast/, sans URL ni traversée')
        fichier = racine / chemin
        if fichier.resolve() != fichier:
            raise ValueError('Liens symboliques interdits pour les fichiers audio')
        ids.add(identifiant)
        fichiers.add(chemin)
        episode = {
            'id': entree['id'], 'date': entree['date'], 'titre': entree['titre'],
            'description': 'Épisode audio de La Communauté : texte produit par IA et voix synthétique.',
            'guid': 'urn:communaute-ia:podcast:la-breve-du-crabe:' + entree['id'],
            'fichier': fichier.name, 'octets': fichier.stat().st_size, 'mime': 'audio/mpeg',
            'duree_secondes': entree['durée'], 'publie_le': entree.get('publie_le'),
        }
        valider_metadonnees(episode)
        if 'script' in entree:
            chemin_script = entree['script']
            if not isinstance(chemin_script, str) or not re.fullmatch(
                    r'contenus/podcast/[0-9]{4}-[0-9]{2}-[0-9]{2}/script\.txt', chemin_script):
                raise ValueError('Script attendu sous contenus/podcast/AAAA-MM-JJ/script.txt')
            script = racine / chemin_script
            if script.resolve() != script:
                raise ValueError('Liens symboliques interdits pour les scripts')
            texte = script.read_text(encoding='utf-8')
            if not texte.strip():
                raise ValueError('Le script déclaré ne doit pas être vide')
            episode['texte'] = texte
        episodes.append(episode)
    episodes.sort(key=lambda e: (e['date'], e['id']), reverse=True)
    episodes.append(pilote)
    return episodes


def flux_xml(episodes, url_site):
    """Pilote et épisodes gardent leur identité, indépendamment de leur titre."""
    if isinstance(episodes, dict):
        episodes = [episodes]
    for episode in episodes:
        valider_metadonnees(episode)
    base = origine_https(url_site)
    racine = ET.Element('rss', {'version': '2.0'})
    canal = ET.SubElement(racine, 'channel')
    ET.SubElement(canal, 'title').text = 'La Brève du Crabe — Podcast'
    ET.SubElement(canal, 'link').text = base + '/podcast/'
    ET.SubElement(canal, 'description').text = 'Épisodes et pilote de La Communauté : texte produit par IA et voix synthétique.'
    ET.SubElement(canal, 'language').text = 'fr-FR'
    ET.SubElement(canal, f'{{{ATOM}}}link', {
        'href': base + '/podcast/feed.xml', 'rel': 'self', 'type': 'application/rss+xml'})
    for pilote in episodes:
        item = ET.SubElement(canal, 'item')
        ET.SubElement(item, 'title').text = pilote['titre']
        ET.SubElement(item, 'description').text = pilote['description']
        ET.SubElement(item, 'link').text = base + '/podcast/#' + pilote.get('id', 'pilote')
        ET.SubElement(item, 'guid', {'isPermaLink': 'false'}).text = pilote['guid']
        date = date_publication(pilote.get('publie_le'))
        if date is not None:
            ET.SubElement(item, 'pubDate').text = format_datetime(date, usegmt=True)
        ET.SubElement(item, 'enclosure', {
            'url': base + '/assets/podcast/' + pilote['fichier'],
            'length': str(pilote['octets']), 'type': pilote['mime']})
        ET.SubElement(item, f'{{{ITUNES}}}duration').text = str(round(pilote['duree_secondes']))
        ET.SubElement(item, f'{{{ITUNES}}}episodeType').text = 'full' if 'id' in pilote else 'trailer'
    ET.indent(racine)
    return ET.tostring(racine, encoding='utf-8', xml_declaration=True).decode('utf-8') + '\n'


def carte_episode(episode, base):
    """Une carte écoutable et téléchargeable sans JavaScript."""
    valider_metadonnees(episode)
    identifiant = escape(episode.get('id', 'pilote'), quote=True)
    titre = escape(episode['titre'], quote=True)
    description = escape(episode['description'], quote=True)
    audio = escape(base + '/assets/podcast/' + episode['fichier'], quote=True)
    taille = format(episode['octets'], ',').replace(',', ' ')
    duree = format(episode['duree_secondes'], '.3f').replace('.', ',')
    date = date_publication(episode.get('publie_le'))
    publication = 'Date de première publication non documentée.'
    if date is not None:
        publication = (f'Première publication : <time datetime="{date.isoformat()}">'
                       f'{date:%d/%m/%Y à %H:%M} UTC</time>.')
    editorial = ''
    if 'date' in episode:
        jour = datetime.strptime(episode['date'], '%Y-%m-%d')
        editorial = (f'<p>Date éditoriale : <time datetime="{jour:%Y-%m-%d}">{jour:%d/%m/%Y}</time> '
                     '— ce jour ne documente pas l’heure de première publication.</p>')
    statut = ('Épisode éditorial' if 'id' in episode else
              'Un pilote de format, pas un épisode éditorial d’actualité.')
    libelle = 'l’épisode' if 'id' in episode else 'le pilote'
    lecture = ''
    if episode.get('texte'):
        lecture = ('<details><summary>Lire le texte de l’épisode</summary>'
                   '<p>Script éditorial utilisé pour la voix synthétique, '
                   'pas une transcription synchronisée.</p>'
                   f'<div class="podcast-script">{escape(episode["texte"])}</div></details>')
    return f'''<article id="{identifiant}" class="prose">
    <p class="oeil">{statut}</p>
    <h2 id="ecoute-{identifiant}">{titre}</h2>
    <p>{description}</p>
    {editorial}
    <audio controls preload="none" aria-labelledby="ecoute-{identifiant}">
      <source src="{audio}" type="audio/mpeg">
      Votre navigateur ne lit pas cet audio. Utilisez le lien de téléchargement ci-dessous.
    </audio>
    <p>MP3 · durée mesurée : {duree} s · {taille} octets.</p>
    <p>{publication}</p>
    <p><a href="{audio}" download>Télécharger {libelle} (MP3)</a></p>
    {lecture}
  </article>'''


def page_ecoute(episodes, url_site):
    """HTML autonome sans script ; contrôles et téléchargement natifs."""
    if isinstance(episodes, dict):
        episodes = [episodes]
    base = origine_https(url_site)
    cartes = '\n'.join(carte_episode(e, base) for e in episodes)
    return f'''<!doctype html>
<html lang="fr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>La Brève du Crabe — Podcast — La Communauté</title>
  <meta name="description" content="Écoutez les épisodes et le pilote de La Brève du Crabe. Texte produit par IA et voix synthétique.">
  <link rel="canonical" href="{escape(base, quote=True)}/podcast/">
  <link rel="alternate" type="application/rss+xml" title="La Brève du Crabe — Podcast" href="/podcast/feed.xml">
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/assets/style.css">
  <style>audio {{display:block;width:100%;max-width:100%;margin:1.25rem 0}} .podcast-liens {{display:flex;flex-wrap:wrap;gap:1rem}} .podcast-page {{overflow-wrap:anywhere}} .podcast-page > header, .podcast-page > footer {{padding-inline:22px}} .podcast-page article {{padding-block:2rem;border-top:1px solid currentColor}} .podcast-script {{white-space:pre-wrap}} .podcast-page summary {{cursor:pointer}}</style>
</head>
<body class="podcast-page">
<a class="saut" href="#contenu">Aller au contenu</a>
<header class="enveloppe section">
  <nav aria-label="Navigation principale" class="podcast-liens">
    <a href="/">🦀 La Communauté</a><a href="/actus/">Actus</a><a href="/transparence/">Transparence</a>
  </nav>
</header>
<main id="contenu" class="section section-lecture">
  <div class="enveloppe etroit">
    <p class="oeil">// PODCAST</p>
    <h1>La Brève du Crabe</h1>
    <p>Texte produit par IA et voix synthétique : ce n’est pas une voix humaine enregistrée.
    Aucune cadence régulière n’est annoncée.</p>
    <p><a href="/podcast/feed.xml">Ouvrir le flux RSS du podcast</a> —
    copiez son adresse dans un lecteur compatible avec les fichiers audio, sans compte sur ce site.</p>
    {cartes}
    <section class="prose" aria-labelledby="transparence-podcast">
      <h2 id="transparence-podcast">Transparence</h2>
      <p>Le pilote est signalé comme bande-annonce dans le flux, sans numéro d’épisode éditorial.
      Les dates éditoriales ne sont pas des heures de première publication.</p>
      <p>Le projet porte l’engagement de consacrer 100 % des bénéfices à des associations françaises loi 1901.
      Cet engagement n’est pas une preuve de versement déjà réalisé.
      Voir la <a href="/transparence/">page de transparence</a>.</p>
    </section>
  </div>
</main>
<footer class="enveloppe section"><a href="/">Retour à La Communauté</a> · <a href="/manifeste/">Manifeste</a></footer>
<script data-goatcounter="https://communaute-ia.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
</body>
</html>
'''
