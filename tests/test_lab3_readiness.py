"""Local synthetic readiness tests; does not build or certify a release."""
import importlib.util,json,hashlib,tempfile,shutil,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HELPER=ROOT/'plugins/wf-lab-guide/skills/lab-guide/scripts/prepare_workspace.py'
spec=importlib.util.spec_from_file_location('prepare',HELPER);helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
class Lab3Readiness(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.skill=self.root/'skill';(self.skill/'assets').mkdir(parents=True);self.work=self.root/'AI-Labs';self.work.mkdir();helper.SKILL=self.skill
  self.contents={'KIT-Lab3-Reporting-Adversarial-Pass.md':b'# Synthetic Lab 3 kit\nKeep both draft and sources.\n','MOCK-Mess-Pack.md':b'# Fictional source\nCount: 12.\n'}
  files=[]
  for name,data in self.contents.items():
   (self.skill/'assets'/name).write_bytes(data);files.append({'asset':'assets/'+name,'destination':'Kits/'+name,'sha256':hashlib.sha256(data).hexdigest()})
  (self.skill/'assets/manifest.json').write_text(json.dumps({'files':files}))
 def tearDown(self):self.tmp.cleanup()
 def test_read_only_reports_missing(self):
  result=helper.run(self.work);self.assertFalse(result['lab3_materials_ready']);self.assertEqual(len(result['lab3_missing']),2);self.assertEqual(list(self.work.iterdir()),[])
 def test_prepare_copies_then_reopens_without_inventing_profile(self):
  result=helper.run(self.work,True);self.assertTrue(result['lab3_materials_ready']);self.assertEqual(result['instructions'],'missing');self.assertFalse((self.work/'AGENTS.md').exists())
  for name,data in self.contents.items():self.assertEqual((self.work/'Kits'/name).read_bytes(),data)
 def test_existing_different_copy_is_preserved_and_not_current(self):
  helper.run(self.work,True);p=self.work/'Kits/KIT-Lab3-Reporting-Adversarial-Pass.md';p.write_text('Earlier work: keep me.')
  result=helper.run(self.work,True);self.assertFalse(result['lab3_materials_ready']);self.assertIn('Kits/'+p.name,result['lab3_preserved_different']);self.assertEqual(p.read_text(),'Earlier work: keep me.')
 def test_old_lab12_only_manifest_cannot_claim_lab3_ready(self):
  (self.skill/'assets/manifest.json').write_text('{"files": []}');result=helper.run(self.work,True);self.assertTrue(result['lab_files_ready']);self.assertFalse(result['lab3_materials_ready']);self.assertIn('Bundled files only',result['readiness_scope'])
 def test_profile_presence_is_not_completion(self):
  (self.work/'AGENTS.md').write_text('# Instructions\nAsk before changes.\n');result=helper.run(self.work,True);self.assertEqual(result['instructions'],'present; rules need readback')
 def test_bad_asset_hash_changes_nothing(self):
  (self.skill/'assets/MOCK-Mess-Pack.md').write_text('altered');self.assertRaises(ValueError,helper.run,self.work,True);self.assertEqual(list(self.work.iterdir()),[])
 def test_builder_and_guide_have_lab3_contract(self):
  builder=(ROOT/'build/build_guide.py').read_text();guide=(ROOT/'build/SKILL.template.md').read_text()
  for name in self.contents:self.assertIn('"'+name+'":',builder)
  for text in ['Check my Lab 3 access','How Claude runs Lab 3','draft AND sources','second-chair.md','one question/action at a time']:self.assertIn(text,guide)
if __name__=='__main__':unittest.main()
