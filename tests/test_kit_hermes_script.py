# Tests du wrapper uniquement : OS et téléchargement simulés, aucune installation réelle.
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile
import unittest

SITE = Path(__file__).resolve().parents[1] / "sites" / "openclaw-france"
SCRIPT = SITE / "dl/kit-hermes/scripts/install.sh"
DOCS = "https://hermes-agent.nousresearch.com/docs/getting-started/"


class KitHermesScriptTest(unittest.TestCase):
    def run_wrapper(self, system="Darwin", machine="x86_64", args=(), uid="1000",
                    download="ok", official_exit="0"):
        with tempfile.TemporaryDirectory(prefix="hermes-wrapper-test-") as tmp:
            root = Path(tmp)
            binaries = root / "bin"
            binaries.mkdir()
            (root / "home").mkdir()
            fixture = "#!/bin/bash\nprintf \"%s\\n\" \"$@\" > \"$TEST_ARGS\"\nexit \"${TEST_OFFICIAL_EXIT:-0}\"\n"
            stubs = {
                "id": "import os\nprint(os.environ[\"TEST_UID\"])\n",
                "uname": "import os, sys\nprint(os.environ[\"TEST_SYSTEM\"] if sys.argv[1] == \"-s\" else os.environ[\"TEST_MACHINE\"])\n",
                "curl": "import os, sys, json\nfrom pathlib import Path\n"
                        "Path(os.environ[\"TEST_CURL\"]).write_text(json.dumps(sys.argv[1:]))\n"
                        "if os.environ[\"TEST_DOWNLOAD\"] != \"ok\": sys.exit(22)\n"
                        "target = Path(sys.argv[sys.argv.index(\"-o\") + 1])\n"
                        "target.write_text(" + repr(fixture) + ")\n",
            }
            for name, body in stubs.items():
                p = binaries / name
                p.write_text("#!" + sys.executable + "\n" + body)
                p.chmod(0o700)
            env = {
                "PATH": str(binaries) + os.pathsep + os.defpath,
                "HOME": str(root / "home"), "TMPDIR": str(root),
                "TEST_SYSTEM": system, "TEST_MACHINE": machine, "TEST_UID": uid,
                "TEST_DOWNLOAD": download, "TEST_OFFICIAL_EXIT": official_exit,
                "TEST_CURL": str(root / "curl.json"), "TEST_ARGS": str(root / "args.txt"),
            }
            result = subprocess.run(["/bin/bash", str(SCRIPT), *args], cwd=root,
                                    env=env, capture_output=True, text=True, timeout=15)
            curl = json.loads((root / "curl.json").read_text()) if (root / "curl.json").exists() else None
            forwarded = (root / "args.txt").read_text().splitlines() if (root / "args.txt").exists() else None
            return result, curl, forwarded

    def test_intel_reserve_et_sources_avant_telechargement(self):
        result, curl, _ = self.run_wrapper(args=("--non-interactive",))
        self.assertEqual(result.returncode, 0, result.stderr)
        for text in ("compatibilité non garantie", "divergent", "ne valide pas", "2026-10-17",
                     DOCS + "installation", DOCS + "platform-support"):
            self.assertIn(text, result.stdout)
        self.assertLess(result.stdout.index("compatibilité non garantie"),
                        result.stdout.index("Téléchargement de"))
        self.assertNotIn("celle-ci, justement", result.stdout)
        self.assertIn("https://hermes-agent.nousresearch.com/install.sh", curl)

    def test_help_sans_telechargement_ni_controle_root(self):
        result, curl, forwarded = self.run_wrapper(args=("--help",), uid="0")
        self.assertEqual(result.returncode, 0)
        self.assertIn("compatibilité non garantie", result.stdout)
        self.assertIn(DOCS + "platform-support", result.stdout)
        self.assertIsNone(curl)
        self.assertIsNone(forwarded)

    def test_apple_silicon_et_linux_options_inchangees(self):
        args = ("--non-interactive", "--skip-browser", "--dir", "chemin avec espaces")
        for system, machine in (("Darwin", "arm64"), ("Linux", "x86_64"), ("Linux", "aarch64")):
            with self.subTest(system=system, machine=machine):
                result, curl, forwarded = self.run_wrapper(system, machine, args)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("Mac Intel", result.stdout)
                self.assertEqual(forwarded, list(args))
                self.assertEqual(curl[:2], ["-fsSL", "https://hermes-agent.nousresearch.com/install.sh"])

    def test_autre_architecture_macos_sans_fausse_identification_intel(self):
        result, _, _ = self.run_wrapper(machine="unknown-arch")
        self.assertIn("compatibilité non garantie", result.stdout)
        self.assertNotIn("Intel détecté", result.stdout)
        self.assertIn(DOCS + "platform-support", result.stdout)

    def test_refus_root_et_systeme_non_pris_en_charge(self):
        for options in ({"uid": "0"}, {"system": "FreeBSD"}):
            with self.subTest(options=options):
                result, curl, forwarded = self.run_wrapper(**options)
                self.assertEqual(result.returncode, 1)
                self.assertIsNone(curl)
                self.assertIsNone(forwarded)

    def test_erreurs_telechargement_et_installateur_propagees(self):
        result, curl, forwarded = self.run_wrapper(download="fail")
        self.assertEqual(result.returncode, 1)
        self.assertIn("Le téléchargement a échoué", result.stderr)
        self.assertIsNotNone(curl)
        self.assertIsNone(forwarded)
        result, _, _ = self.run_wrapper(official_exit="7")
        self.assertEqual(result.returncode, 1)
        self.assertIn("une erreur", result.stderr)


if __name__ == "__main__":
    unittest.main()
