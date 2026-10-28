"""Les dates RSS du mardi/jeudi ne doivent pas perdre leur fraîcheur."""
import io
import json
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import collecte


class DatesCollecteTest(unittest.TestCase):
    def test_rss_mardi_et_jeudi_sont_lus_comme_rfc_et_non_iso(self):
        # Chaînes constatées dans les flux Google AI et CNIL le 27/10/2026.
        cas = [
            ("Tue, 13 Oct 2026 16:00:00 +0000", datetime(2026, 10, 13, 16, tzinfo=timezone.utc)),
            ("Thu, 22 Oct 2026 14:00:00 +0200", datetime(2026, 10, 22, 12, tzinfo=timezone.utc)),
        ]
        for brute, attendue in cas:
            with self.subTest(date=brute):
                item = ET.fromstring(f"<item><pubDate>{brute}</pubDate></item>")
                self.assertEqual(collecte._date_depuis_item(item, {}), attendue)

    def test_rfc_tous_les_jours_et_fuseaux_numeriques_ou_gmt(self):
        for jour in range(7):
            for minutes in (0, 120, -300):
                date = datetime(2026, 10, 19, 23, 45,
                                tzinfo=timezone(timedelta(minutes=minutes))) + timedelta(days=jour)
                formats = [format_datetime(date)]
                if minutes == 0:
                    formats.append(format_datetime(date, usegmt=True))
                for brute in formats:
                    with self.subTest(date=brute):
                        item = ET.fromstring(f"<item><pubDate>{brute}</pubDate></item>")
                        self.assertEqual(collecte._date_depuis_item(item, {}),
                                         date.astimezone(timezone.utc))

    def test_atom_iso_offsets_et_precision_preserves(self):
        cas = [
            ("2026-10-27T12:34:56Z", datetime(2026, 10, 27, 12, 34, 56, tzinfo=timezone.utc)),
            ("2026-10-27T01:30:00+02:00", datetime(2026, 10, 26, 23, 30, tzinfo=timezone.utc)),
            ("2026-10-26T22:30:00-05:00", datetime(2026, 10, 27, 3, 30, tzinfo=timezone.utc)),
            ("2026-10-27T12:34:56.123456Z", datetime(2026, 10, 27, 12, 34, 56, 123456, tzinfo=timezone.utc)),
            # Convention héritée du collecteur, pas une preuve du fuseau source.
            ("2026-10-27", datetime(2026, 10, 27, tzinfo=timezone.utc)),
            ("2026-10-27T12:00:00", datetime(2026, 10, 27, 12, tzinfo=timezone.utc)),
        ]
        for brute, attendue in cas:
            for balise in ("published", "updated", "date"):
                with self.subTest(date=brute, balise=balise):
                    item = ET.fromstring(
                        f'<entry xmlns="http://www.w3.org/2005/Atom"><{balise}>{brute}</{balise}></entry>')
                    self.assertEqual(collecte._date_depuis_item(item, {}), attendue)

    def test_date_invalide_ou_absente_ne_devient_pas_date_du_run(self):
        for contenu in ("", "<pubDate />", "<pubDate>inconnue</pubDate>",
                        "<pubDate>2026-02-30T12:00:00Z</pubDate>",
                        "<pubDate>Thu, 32 Oct 2026 12:00:00 GMT</pubDate>"):
            with self.subTest(contenu=contenu):
                self.assertIsNone(collecte._date_depuis_item(ET.fromstring(f"<item>{contenu}</item>"), {}))

    def test_repli_et_priorite_des_champs_restent_inchanges(self):
        item = ET.fromstring('''<item xmlns:atom="http://www.w3.org/2005/Atom">
            <pubDate>invalide</pubDate><atom:published>2026-10-27T10:00:00Z</atom:published>
            <atom:updated>2026-10-27T11:00:00Z</atom:updated></item>''')
        self.assertEqual(collecte._date_depuis_item(item, {}),
                         datetime(2026, 10, 27, 10, tzinfo=timezone.utc))
        item.find("pubDate").text = "Tue, 27 Oct 2026 09:00:00 GMT"
        self.assertEqual(collecte._date_depuis_item(item, {}),
                         datetime(2026, 10, 27, 9, tzinfo=timezone.utc))

    def test_vraie_collecte_ecarte_ancien_mardi_trie_et_deduplique(self):
        class Horloge(datetime):
            @classmethod
            def now(cls, tz=None):
                return cls(2026, 10, 27, 13, tzinfo=timezone.utc).astimezone(tz)

        # Flux synthétique : vrai téléchargement/parser/boucle de collecte,
        # seul le transport HTTP est remplacé ; aucune rédaction ni écriture prod.
        items = [
            ("ancien", "Tue, 13 Oct 2026 16:00:00 +0000"),
            ("lundi", "Mon, 26 Oct 2026 16:00:00 GMT"),
            ("mardi", "Tue, 27 Oct 2026 12:00:00 +0000"),
        ]
        xml = ("<rss><channel>" + "".join(
            f"<item><title>IA {ident}</title><link>https://example.org/{ident}</link>"
            f"<pubDate>{brute}</pubDate></item>" for ident, brute in items
        ) + "</channel></rss>").encode()
        with tempfile.TemporaryDirectory() as tmp:
            data = Path(tmp)
            sources = data / "sources.json"
            sources.write_text(json.dumps([{"nom": "Fixture", "url": "https://example.org/rss",
                                            "langue": "fr", "priorite": 4, "filtre_ia": True}]))
            with patch.multiple(collecte.config, FICHIER_SOURCES=sources,
                                FICHIER_ETAT=data / "etat.json", DOSSIER_DATA=data,
                                FENETRE_JOURS=3, MAX_ITEMS_PAR_RUN=40), \
                    patch.object(collecte, "datetime", Horloge), \
                    patch.object(collecte.urllib.request, "urlopen", side_effect=lambda *a, **kw: io.BytesIO(xml)):
                gardes, rapport = collecte.collecter(verbeux=False)
                self.assertEqual([i["lien"] for i in gardes],
                                 ["https://example.org/mardi", "https://example.org/lundi"])
                self.assertEqual(rapport, ["Fixture: 2 neuf(s)"])
                self.assertEqual(gardes[0]["date"], datetime(2026, 10, 27, 12, tzinfo=timezone.utc))
                self.assertEqual(collecte.collecter(verbeux=False)[0], [])
                self.assertEqual(len(collecte.charger_etat()["vus"]), 3)


if __name__ == "__main__":
    unittest.main()
