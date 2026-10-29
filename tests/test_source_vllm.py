"""Le flux primaire vLLM alimente la veille et son export public."""
import json
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import config


class SourceVLLMTest(unittest.TestCase):
    def test_source_officielle_unique_et_exportee_sans_intermediaire(self):
        sources = json.loads(config.FICHIER_SOURCES.read_text(encoding="utf-8"))
        url = "https://vllm.ai/blog/rss.xml"
        cible = [s for s in sources if s["url"] == url]
        self.assertEqual(cible, [{"nom": "vLLM (blog officiel)", "url": url,
                                 "langue": "en", "priorite": 4}])
        self.assertEqual(len({s["url"] for s in sources}), len(sources))
        opml = ET.fromstring(annexes.sources_opml())
        exports = [s for s in opml.findall(".//outline[@type='rss']")
                   if s.get("xmlUrl") == url]
        self.assertEqual(len(exports), 1)
        self.assertEqual(exports[0].get("text"), cible[0]["nom"])
        page = annexes.page_transparence([], [], {}, [])
        self.assertIn(f"<strong>Collecte.</strong> {len(sources)} flux RSS et Atom", page)


if __name__ == "__main__":
    unittest.main()
