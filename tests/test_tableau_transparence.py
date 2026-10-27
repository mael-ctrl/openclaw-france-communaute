"""Gardes ciblés du tableau : complétés par la recette Chromium privée."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'engine'))
import annexes

class Tags(HTMLParser):
    def __init__(self,html):
        super().__init__();self.tags=[];self.text=[];self.feed(html)
    def handle_starttag(self,tag,attrs):self.tags.append((tag,dict(attrs)))
    def handle_data(self,data):self.text.append(data)

class TableauTransparenceTest(unittest.TestCase):
    def test_detail_garde_largeur_lisible_sans_masquage(self):
        css=(ROOT/'assets/style.css').read_text()
        self.assertIn('.journal th:last-child, .journal td:last-child { min-width: 16rem; }',css)
        journal=css.split('/* ---------------- Pipeline / journal')[1].split('/* ----------------',1)[0]
        self.assertNotRegex(journal,r'display\s*:\s*none|text-overflow\s*:\s*ellipsis|overflow-x\s*:\s*(hidden|clip)|max-height\s*:')
    def test_focus_visible_explicite(self):
        css=(ROOT/'assets/style.css').read_text()
        self.assertIn('.journal-boite:focus-visible { outline: 2px solid var(--cyan); outline-offset: 3px; }',css)
        self.assertIn('overflow-x: auto; overscroll-behavior-x: contain;',css)
    def test_zone_nomme_tabulation_aide(self):
        doc=Tags(annexes.page_transparence([],[],{},[]))
        wrapper=next(a for t,a in doc.tags if a.get('class')=='journal-boite')
        self.assertEqual({k:wrapper.get(k) for k in ['tabindex','role','aria-label','aria-describedby']},
                         {'tabindex':'0','role':'region','aria-label':'Journal de bord','aria-describedby':'journal-defilement'})
        self.assertTrue(any(a.get('id')=='journal-defilement' for t,a in doc.tags))
    def test_entetes_scope_col_sans_remplacer_table(self):
        doc=Tags(annexes.page_transparence([],[],{},[]))
        self.assertEqual([a.get('scope') for t,a in doc.tags if t=='th'],['col']*3)
        self.assertEqual(sum(t=='table' and a.get('class')=='journal' for t,a in doc.tags),1)
    def test_cas_vide_et_entrees_echappees_sans_troncature(self):
        empty=annexes.page_transparence([],[],{},[])
        self.assertIn('<td colspan="3">Le journal s\'ouvre au premier run.</td>',empty)
        message='preuve-'+('x'*512)+'<b>&'
        html=annexes.page_transparence([],[],{},[{'ts':'2026-10-27T08:00:00+00:00','evenement':'test<svg>','details':{'message':message}}])
        self.assertIn('test&lt;svg&gt;',html)
        self.assertIn(message.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'),html)
        self.assertNotIn('test<svg>',html)

if __name__=='__main__':unittest.main()
