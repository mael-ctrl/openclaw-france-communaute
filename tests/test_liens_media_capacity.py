"""Synthetic CLI admission contracts, not a claim of a clean real site."""
import json, os, pathlib, subprocess, sys, tempfile, unittest
CLI=pathlib.Path(__file__).resolve().parents[1]/'outils/verifier_liens_hors_ligne.py'
class MediaCapacityTest(unittest.TestCase):
    def invoke(self,*flags):
        with tempfile.TemporaryDirectory(dir=os.environ.get('LIENS_TEST_TMP',CLI.parents[1])) as d:
            pathlib.Path(d,'index.html').write_text('<a href="#ok">ok</a><p id="ok">ok</p>')
            return subprocess.run([sys.executable,'-I','-B',str(CLI),d,'--canonical-host','example.test',*flags],capture_output=True,text=True,timeout=10)
    def test_explicit_full_media_byte_budget_is_admitted(self):
        p=self.invoke('--max-bytes','100000000','--max-links','200000')
        self.assertEqual(p.returncode,0,p.stderr)
        r=json.loads(p.stdout)
        self.assertTrue(r['complete']); self.assertEqual(r['budgets']['bytes'],100000000)
        self.assertEqual(r['stats']['references'],1)
    def test_default_stays_twenty_megabytes(self):
        p=self.invoke(); self.assertEqual(p.returncode,0,p.stderr)
        self.assertEqual(json.loads(p.stdout)['budgets']['bytes'],20000000)
    def test_new_hard_cap_still_refuses_unbounded_admission(self):
        p=self.invoke('--max-bytes','128000001')
        self.assertEqual(p.returncode,2); self.assertEqual(p.stdout,'')
        self.assertIn('128000000',p.stderr)
if __name__=='__main__': unittest.main()
