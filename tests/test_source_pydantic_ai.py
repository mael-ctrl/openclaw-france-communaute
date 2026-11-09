"""La source Pydantic AI officielle reste explicite et exportée."""
import json
from pathlib import Path
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "engine"))
import annexes
import config


class SourcePydanticAITest(unittest.TestCase):
    def test_source_unique_exportee_et_comptee(self):
        sources = json.loads(config.FICHIER_SOURCES.read_text(encoding="utf-8"))
        url = "https://github.com/pydantic/pydantic-ai/releases.atom"
        expected = {"nom": "Pydantic AI (releases, préversions incluses)",
                    "url": url, "langue": "en", "priorite": 3}
        self.assertEqual([s for s in sources if s["url"] == url], [expected])
        self.assertEqual(len({s["url"] for s in sources}), len(sources))
        exported = ET.fromstring(annexes.sources_opml()).findall(".//outline[@type='rss']")
        self.assertEqual([(e.get("text"), e.get("xmlUrl")) for e in exported],
                         [(s["nom"], s["url"]) for s in sources])
        page = annexes.page_transparence([], [], {}, [])
        self.assertIn(f"<strong>Collecte.</strong> {len(sources)} flux RSS et Atom", page)


if __name__ == "__main__":
    unittest.main()
