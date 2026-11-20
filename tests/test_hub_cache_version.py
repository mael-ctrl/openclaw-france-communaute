"""Contrat IA : chaque consommateur local porte le SHA256 de la CSS livrée.
Test statique, pas de réseau/build/installation de kit.
"""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,urljoin,parse_qs
import hashlib,unittest
SITE=Path(__file__).resolve().parents[1]/'sites/openclaw-france'
class Styles(HTMLParser):
    def __init__(self,text):
        super().__init__();self.links=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='link' and ('stylesheet' in a.get('rel','').split() or a.get('as')=='style'):self.links.append(a['href'])
class HubCacheVersionTest(unittest.TestCase):
    def test_tous_les_consommateurs_locaux_sont_versions_par_la_css_finale(self):
        token='sha256-'+hashlib.sha256((SITE/'static/style.css').read_bytes()).hexdigest();found=[]
        for p in sorted(SITE.rglob('*.html')):
            for href in Styles(p.read_text()).links:
                u=urlsplit(href)
                if u.scheme or u.netloc:continue
                if urlsplit(urljoin('https://local.invalid/'+p.relative_to(SITE).as_posix(),href)).path!='/static/style.css':continue
                found.append(p.relative_to(SITE).as_posix())
                with self.subTest(page=str(p.relative_to(SITE))):self.assertEqual(parse_qs(u.query).get('v'),[token])
        self.assertEqual(set(found),{'404.html','cgv/index.html','index.html','openclaw/index.html','hermes/index.html','gratuit/index.html','guides/demarrer-openclaw-hermes/index.html','temoignages/index.html'})
        self.assertEqual(len(found),8)
if __name__=='__main__':unittest.main(verbosity=2)
