"""RSS éditoriaux : une date de source/rédaction ne prouve pas la publication."""
import copy
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from unittest.mock import patch
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import config
import construction


class DatesRssEditorialesTest(unittest.TestCase):
    def test_omet_pubdate_sans_preuve_y_compris_dates_invalides(self):
        valeurs = (
            None, "", "inconnue", "2026-02-30T12:00:00Z", "2026-10-22",
            "2026-10-22T12:00:00", "2026-10-22T12:00:00Z",
            "2026-10-22T12:00:00+00:00", "2026-10-22T00:30:00+05:30",
            "2026-10-22T23:30:00-03:00",
            "2026-03-29T01:59:59+01:00", "2026-03-29T03:00:00+02:00",
            "2026-10-25T02:30:00+02:00", "2026-10-25T02:30:00+01:00",
            'inconnue & <date> "🦀"',
        )
        for valeur in valeurs:
            for dates in ({"date_source": valeur, "date_redac": "2026-10-22T08:00:00Z"},
                          {"date_redac": valeur}, {"date_source": valeur}, {}):
                breve = {"slug": "breve", "titre": "Une brève", "resume": "Résumé.", **dates}
                article = {"slug": "article", "titre": "Analyse", "chapo": "Contexte.", "date": valeur}
                for breves in ([breve], []):
                    with self.subTest(valeur=valeur, dates=dates, general=bool(breves)):
                        original = copy.deepcopy((breves, [article]))
                        xml = construction.feed_xml(breves, [article])
                        root = ET.fromstring(xml)
                        self.assertEqual(len(root.findall("channel/item")), 1 + len(breves))
                        self.assertEqual(root.findall(".//pubDate"), [],
                                         "Les dates éditoriales ne sont pas une preuve de mise en ligne")
                        self.assertNotIn("01 Jan 1970", xml)
                        self.assertEqual((breves, [article]), original)


    def test_lastbuilddate_rfc_independant_de_la_locale(self):
        # Double d'horloge : simule strftime dans une locale non anglophone,
        # sans exiger qu'une locale système donnée soit installée en CI.
        class HorlogeLocale(datetime):
            @classmethod
            def now(cls, tz=None):
                return cls(2026, 10, 22, 9, 10, 11, tzinfo=timezone.utc).astimezone(tz)

            def strftime(self, fmt):
                if "%a" in fmt or "%b" in fmt:
                    return "jeu., 22 oct. 2026 09:10:11 +0000"
                return super().strftime(fmt)  # %z reste numérique dans toute locale.

        with patch.object(construction, "datetime", HorlogeLocale):
            canal = ET.fromstring(construction.feed_xml([], [])).find("channel")
        valeur = canal.findtext("lastBuildDate")
        self.assertEqual(valeur, "Thu, 22 Oct 2026 09:10:11 +0000")
        self.assertEqual(parsedate_to_datetime(valeur).utcoffset().total_seconds(), 0)


    def test_lastbuilddate_utc_instant_de_construction_y_compris_dst(self):
        paris = ZoneInfo("Europe/Paris")
        instants = [
            datetime.fromisoformat("2026-10-22T23:30:15.123456-03:00"),
            datetime.fromisoformat("2026-10-22T00:30:15+05:30"),
            datetime(2026, 3, 29, 1, 59, 59, tzinfo=paris),
            datetime(2026, 3, 29, 3, 0, 0, tzinfo=paris),
            datetime(2026, 10, 25, 2, 30, tzinfo=paris, fold=0),
            datetime(2026, 10, 25, 2, 30, tzinfo=paris, fold=1),
        ]
        for instant in instants:
            with self.subTest(instant=instant), patch.object(construction, "datetime") as horloge:
                horloge.now.side_effect = lambda tz: instant.astimezone(tz)
                horloge.fromisoformat.side_effect = datetime.fromisoformat
                canal = ET.fromstring(construction.feed_xml([], [])).find("channel")
                horloge.now.assert_called_once_with(timezone.utc)
                valeur = canal.findtext("lastBuildDate")
                self.assertTrue(valeur.endswith(" +0000"))
                self.assertEqual(parsedate_to_datetime(valeur),
                                 instant.astimezone(timezone.utc).replace(microsecond=0))
                self.assertEqual(canal.findall("item"), [])
                self.assertEqual(canal.findall("pubDate"), [])

    def test_xml_special_et_identite_des_items_preserves(self):
        titre = 'IA & <outils> "🦀" café'
        description = 'Résumé <sourcé> & texte ]]> « français ».'
        article = {"slug": "analyse-ia", "titre": titre, "chapo": description}
        breve = {"slug": "breve-ia", "titre": titre, "resume": description}
        for breves in ([breve], []):
            xml = construction.feed_xml(breves, [article], titre_flux=titre)
            root = ET.fromstring(xml)
            self.assertEqual(root.attrib, {"version": "2.0"})
            canal = root.find("channel")
            self.assertEqual(canal.findtext("title"), titre)
            self.assertEqual(canal.findtext("link"), config.URL_SITE + "/")
            self.assertEqual(canal.findtext("description"), config.DESCRIPTION_SITE)
            self.assertEqual(canal.findtext("language"), "fr-FR")
            chemins = ["/articles/analyse-ia/"] + (["/breves/breve-ia/"] if breves else [])
            self.assertEqual(len(canal.findall("item")), len(chemins))
            for item, chemin in zip(canal.findall("item"), chemins):
                self.assertEqual([e.tag for e in item], ["title", "link", "guid", "description"])
                self.assertEqual(item.findtext("title"), titre)
                self.assertEqual(item.findtext("description"), description)
                self.assertEqual(item.findtext("link"), config.URL_SITE + chemin)
                self.assertEqual(item.findtext("guid"), config.URL_SITE + chemin)
                self.assertEqual(item.find("guid").attrib, {"isPermaLink": "true"})
            self.assertIn("&amp;", xml)
            self.assertIn("&lt;outils&gt;", xml)

    def test_limites_20_articles_50_breves_60_total_et_egalites_stables(self):
        articles = [{"slug": f"a-{i}", "titre": f"A{i}", "chapo": "A", "date": "2026-10-22"}
                    for i in range(25)]
        breves = [{"slug": f"b-{i}", "titre": f"B{i}", "resume": "B", "date_redac": "2026-10-22"}
                  for i in range(55)]
        cas = ((breves, articles, [f"A{i}" for i in range(20)] + [f"B{i}" for i in range(40)]),
               ([], articles, [f"A{i}" for i in range(20)]),
               (breves, [], [f"B{i}" for i in range(50)]), ([], [], []))
        for b, a, attendus in cas:
            with self.subTest(breves=len(b), articles=len(a)):
                original = copy.deepcopy((b, a))
                root = ET.fromstring(construction.feed_xml(b, a))
                self.assertEqual([e.text for e in root.findall("channel/item/title")], attendus)
                self.assertEqual((b, a), original)

    def test_tri_lexical_et_priorite_source_redaction_restent_inchanges(self):
        breves = [
            {"slug": "source", "titre": "source", "resume": "", "date_source": "2026-10-21",
             "date_redac": "2026-10-30"},
            {"slug": "repli", "titre": "repli", "resume": "", "date_source": "",
             "date_redac": "2026-10-22T01:00:00+05:30"},
            {"slug": "vide", "titre": "vide", "resume": ""},
        ]
        articles = [
            {"slug": "offset", "titre": "offset", "chapo": "", "date": "2026-10-21T23:00:00-03:00"},
            {"slug": "invalide", "titre": "invalide", "chapo": "", "date": "inconnue"},
        ]
        root = ET.fromstring(construction.feed_xml(breves, articles))
        self.assertEqual([e.text for e in root.findall("channel/item/title")],
                         ["invalide", "repli", "offset", "source", "vide"])


if __name__ == "__main__":
    unittest.main()
