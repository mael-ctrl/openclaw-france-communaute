"""Contrats Bash/Git locaux : aucun vrai moteur, réseau ou secret.

Le script versionné est invoqué sans transformation, avec HOME neuf, remote Git
file:// et moteur synthétique. Les erreurs injectées complètent les états Git
réels ; ceci ne remplace ni un test du scheduler vivant ni un verrou distribué.
"""
import json
import os
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
WRAPPER = ROOT / "outils" / "communaute_maj.sh"
GIT = shutil.which("git")
GREP = shutil.which("grep")
assert GIT is not None and GREP is not None, "git et grep requis pour ces contrats"
FAKE_KEY = "SYNTHETIC_ONLY_NOT_A_SECRET"


class MajLocaleTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="maj-locale-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.home = self.root / "home"
        self.repo = self.home / ".hermes/workspaces/communaute"
        self.repo.mkdir(parents=True)
        self.remote = self.root / "remote.git"
        self.bin = self.home / ".local/bin"
        self.bin.mkdir(parents=True)
        self.env = {
            "HOME": str(self.home), "PATH": os.path.dirname(sys.executable) + ":/usr/local/bin:/usr/bin:/bin",
            "TMPDIR": str(self.root), "LANG": "C", "LC_ALL": "C",
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_ALLOW_PROTOCOL": "file", "GIT_TERMINAL_PROMPT": "0",
            "GIT_AUTHOR_NAME": "Synthetic", "GIT_AUTHOR_EMAIL": "test@example.invalid",
            "GIT_COMMITTER_NAME": "Synthetic", "GIT_COMMITTER_EMAIL": "test@example.invalid",
            "TRACE": str(self.root / "git.jsonl"), "REAL_GIT": GIT,
            "MARK": str(self.root / "engine-called"), "KEY_MARK": str(self.root / "key-read"),
        }
        self.git("init", "--bare", "-q", str(self.remote))
        self.git("init", "-q", "--initial-branch=main")
        (self.repo / "engine").mkdir()
        (self.repo / "data").mkdir()
        (self.repo / "data/value").write_text("base\n")
        (self.repo / "engine/run.py").write_text(
            "import os,pathlib,sys\n"
            "pathlib.Path(os.environ['MARK']).write_text('called')\n"
            "if os.environ.get('WRITE_DATA') == '1': pathlib.Path('data/value').write_text('new\\n')\n"
            "if os.environ.get('DEEPSEEK_API_KEY') != '" + FAKE_KEY + "': sys.exit(91)\n"
            "sys.exit(int(os.environ.get('ENGINE_RC', '0')))\n"
        )
        self.key = self.home / ".hermes/.env"
        self.key.write_text("DEEPSEEK_API_KEY=" + FAKE_KEY + "\n")
        self.git("add", "engine", "data")
        self.git("commit", "-qm", "synthetic baseline")
        self.git("remote", "add", "origin", self.remote.as_uri())
        self.git("push", "-qu", "origin", "main")
        self.base = self.git("rev-parse", "HEAD").stdout.strip()
        self.script("git", "#!" + sys.executable + "\n"
            "import json,os,sys\n"
            "from pathlib import Path\n"
            "args=sys.argv[1:]\n"
            "with open(os.environ['TRACE'],'a') as f: f.write(json.dumps(args)+'\\n')\n"
            "if args[0] == os.environ.get('FAIL_GIT'): sys.exit(int(os.environ.get('FAIL_RC','47')))\n"
            "os.execv(os.environ['REAL_GIT'], [os.environ['REAL_GIT']]+args)\n")
        self.script("grep", "#!/bin/sh\nprintf called > \"$KEY_MARK\"\nexec " + shlex.quote(GREP) + " \"$@\"\n")

    def script(self, name, text):
        target = self.bin / name
        target.write_text(text)
        target.chmod(0o755)

    def git(self, *args, check=True):
        return subprocess.run([GIT, *args], cwd=self.repo, env=self.env,
                              text=True, capture_output=True, check=check, timeout=20)

    def invoke(self, **overrides):
        result = subprocess.run(["/bin/bash", str(WRAPPER)], cwd=self.root,
                                env={**self.env, **overrides}, text=True,
                                capture_output=True, timeout=30)
        trace = self.root / "git.jsonl"
        self.commands = [json.loads(x) for x in trace.read_text().splitlines()] if trace.exists() else []
        self.assertNotIn(FAKE_KEY, result.stdout + result.stderr)
        return result

    def refused_before_engine(self, result, expected=65):
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        self.assertFalse((self.root / "engine-called").exists())
        self.assertFalse((self.root / "key-read").exists())
        self.assertFalse({"add", "diff", "commit", "push", "rebase", "reset", "stash", "merge"}
                         .intersection(c[0] for c in self.commands))

    def test_syntax(self):
        result = subprocess.run(["/bin/bash", "-n", str(WRAPPER)], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_noop_success_does_not_commit(self):
        result = self.invoke()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.root / "engine-called").exists())
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.base)
        self.assertFalse({"commit", "push"}.intersection(c[0] for c in self.commands))

    def test_engine_failure_propagated_and_not_saved(self):
        result = self.invoke(ENGINE_RC="23", WRITE_DATA="1")
        self.assertEqual(result.returncode, 23, result.stdout + result.stderr)
        self.assertEqual((self.repo / "data/value").read_text(), "new\n")
        self.assertEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.base)
        self.assertFalse({"add", "diff", "commit", "push"}.intersection(c[0] for c in self.commands))

    def test_pull_failure_stops_before_key_and_engine(self):
        self.refused_before_engine(self.invoke(FAIL_GIT="pull", FAIL_RC="29"), 29)

    def test_dirty_repository_preserved(self):
        (self.repo / "data/value").write_text("uncommitted\n")
        self.refused_before_engine(self.invoke())
        self.assertEqual((self.repo / "data/value").read_text(), "uncommitted\n")

    def test_git_operation_preserved(self):
        operation = self.repo / ".git/rebase-merge"
        operation.mkdir()
        (operation / "sentinel").write_text("preserve")
        self.refused_before_engine(self.invoke())
        self.assertEqual((operation / "sentinel").read_text(), "preserve")

    def test_unmerged_index_preserved(self):
        self.git("checkout", "-qb", "other")
        (self.repo / "data/value").write_text("other\n")
        self.git("commit", "-qam", "other")
        self.git("checkout", "-q", "main")
        (self.repo / "data/value").write_text("main\n")
        self.git("commit", "-qam", "main")
        self.assertNotEqual(self.git("merge", "other", check=False).returncode, 0)
        before = self.git("ls-files", "--unmerged").stdout
        self.assertTrue(before)
        self.refused_before_engine(self.invoke())
        self.assertEqual(self.git("ls-files", "--unmerged").stdout, before)

    def test_local_ahead_preserved(self):
        (self.repo / "data/value").write_text("local\n")
        self.git("commit", "-qam", "local only")
        local = self.git("rev-parse", "HEAD").stdout
        self.refused_before_engine(self.invoke())
        self.assertEqual(self.git("rev-parse", "HEAD").stdout, local)

    def test_wrong_branch_refused(self):
        self.git("checkout", "-qb", "not-main")
        self.refused_before_engine(self.invoke())

    def test_wrong_tracking_refused(self):
        self.git("config", "branch.main.merge", "refs/heads/other")
        self.refused_before_engine(self.invoke())

    def test_empty_key_stops_without_git_save(self):
        self.key.write_text("DEEPSEEK_API_KEY=\n")
        result = self.invoke()
        self.assertEqual(result.returncode, 65, result.stdout + result.stderr)
        self.assertTrue((self.root / "key-read").exists())
        self.assertFalse((self.root / "engine-called").exists())
        self.assertFalse({"add", "commit", "push"}.intersection(c[0] for c in self.commands))

    def test_key_reader_partial_failure_is_not_leaked(self):
        self.script("grep", "#!/bin/sh\nprintf '%s\\n' 'DEEPSEEK_API_KEY=" + FAKE_KEY + "'\n"
                    "printf '%s\\n' '" + FAKE_KEY + "' >&2\nexit 47\n")
        result = self.invoke()
        self.assertEqual(result.returncode, 47, result.stdout + result.stderr)
        self.assertFalse((self.root / "engine-called").exists())

    def test_add_error_stops_save(self):
        result = self.invoke(WRITE_DATA="1", FAIL_GIT="add", FAIL_RC="31")
        self.assertEqual(result.returncode, 31)
        self.assertFalse({"diff", "commit", "push"}.intersection(c[0] for c in self.commands))

    def test_diff_error_not_treated_as_change(self):
        result = self.invoke(WRITE_DATA="1", FAIL_GIT="diff", FAIL_RC="32")
        self.assertEqual(result.returncode, 32)
        self.assertFalse({"commit", "push"}.intersection(c[0] for c in self.commands))

    def test_commit_error_stops_push(self):
        result = self.invoke(WRITE_DATA="1", FAIL_GIT="commit", FAIL_RC="33")
        self.assertEqual(result.returncode, 33)
        self.assertFalse(any(c[0] == "push" for c in self.commands))

    def test_push_error_preserves_local_commit(self):
        result = self.invoke(WRITE_DATA="1", FAIL_GIT="push", FAIL_RC="34")
        self.assertEqual(result.returncode, 34)
        self.assertNotEqual(self.git("rev-parse", "HEAD").stdout.strip(), self.base)
        self.assertEqual(self.git("--git-dir=" + str(self.remote), "rev-parse", "main").stdout.strip(), self.base)
        self.assertEqual((self.repo / "data/value").read_text(), "new\n")

    def test_success_is_read_back_from_remote(self):
        result = self.invoke(WRITE_DATA="1")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        local = self.git("rev-parse", "HEAD").stdout.strip()
        self.assertNotEqual(local, self.base)
        self.assertEqual(self.git("--git-dir=" + str(self.remote), "rev-parse", "main").stdout.strip(), local)
        self.assertEqual(self.git("--git-dir=" + str(self.remote), "show", "main:data/value").stdout, "new\n")
        self.assertEqual([c for c in self.commands if c[0] == "add"], [["add", "data"]])
        self.assertFalse({"rebase", "reset", "stash", "merge"}.intersection(c[0] for c in self.commands))


if __name__ == "__main__":
    unittest.main()
