"""! New: offline tests for file deployment and conflict protection, not AI quality."""
import hashlib
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ['kit-brief', 'kit-data', 'kit-verify', 'kit-debug', 'kit-explain']


def snapshot(root):
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in root.rglob('*') if p.is_file() and not p.is_symlink()
    }


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.kit = self.base / 'kit-source'
        shutil.copytree(ROOT, self.kit, ignore=shutil.ignore_patterns('__pycache__'))
        self.project = self.base / 'work space'
        self.project.mkdir()
        (self.project / 'AGENTS.md').write_text('existing instructions\n')
        (self.project / 'app.txt').write_text('existing application\n')

    def run_install(self, target=None):
        return subprocess.run(['bash', str(self.kit / 'install.sh'), str(target or self.project)],
                              text=True, capture_output=True, timeout=10)

    def test_fresh_install_preserves_existing_files(self):
        before = snapshot(self.project)
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name, digest in before.items():
            self.assertEqual(snapshot(self.project)[name], digest)
        for name in NAMES:
            self.assertTrue((self.project / '.agents/skills' / name / 'SKILL.md').is_file())
        self.assertTrue((self.project / 'KIT.md').is_file())
        self.assertFalse((self.project / '.codex').exists())

    def test_identical_install_is_idempotent(self):
        self.assertEqual(self.run_install().returncode, 0)
        before = snapshot(self.project)
        self.assertEqual(self.run_install().returncode, 0)
        self.assertEqual(snapshot(self.project), before)

    def test_conflict_is_detected_before_writing(self):
        conflict = self.project / '.agents/skills/kit-explain'
        conflict.mkdir(parents=True)
        (conflict / 'SKILL.md').write_text('different instructions')
        before = snapshot(self.project)
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(snapshot(self.project), before)
        self.assertFalse((self.project / 'KIT.md').exists())
        self.assertFalse((self.project / '.agents/skills/kit-brief').exists())

    def test_conflicting_kit_md_preserved(self):
        (self.project / 'KIT.md').write_text('keep this')
        before = snapshot(self.project)
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(snapshot(self.project), before)
        self.assertFalse((self.project / '.agents').exists())

    def test_agents_symlink_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        (self.project / '.agents').symlink_to(outside, target_is_directory=True)
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(list(outside.iterdir()), [])

    def test_missing_source_leaves_target_unchanged(self):
        (self.kit / 'skills/kit-verify/SKILL.md').unlink()
        before = snapshot(self.project)
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual(snapshot(self.project), before)
        self.assertFalse((self.project / '.agents').exists())

    def test_source_link_rejected(self):
        (self.kit / 'skills/kit-data/ref-link').symlink_to(self.kit / 'README.md')
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertFalse((self.project / '.agents').exists())

    def test_non_directory_agents_rejected(self):
        (self.project / '.agents').write_text('keep file')
        self.assertNotEqual(self.run_install().returncode, 0)
        self.assertEqual((self.project / '.agents').read_text(), 'keep file')

    def test_install_into_source_rejected(self):
        self.assertNotEqual(self.run_install(self.kit).returncode, 0)
        self.assertFalse((self.kit / '.agents').exists())

    def test_missing_target_rejected(self):
        target = self.base / 'missing'
        self.assertNotEqual(self.run_install(target).returncode, 0)
        self.assertFalse(target.exists())

    def test_skill_metadata_and_names(self):
        self.assertEqual(sorted(p.name for p in (self.kit / 'skills').iterdir()), sorted(NAMES))
        for name in NAMES:
            text = (self.kit / 'skills' / name / 'SKILL.md').read_text()
            self.assertTrue(text.startswith('---\n'))
            meta = text.split('---', 2)[1]
            self.assertIn('name: ' + name, meta)
            self.assertRegex(meta, r'description: ".+"')
            self.assertLess(len(meta), 1024)

    def test_forbidden_side_effects_absent_from_installer(self):
        script = (self.kit / 'install.sh').read_text()
        for pattern in (r'\bcurl\b', r'\bwget\b', r'\bgit\b', r'\bpip\b', r'\bnpm\b',
                        r'\bsudo\b', r'\bchmod\b', r'\beval\b', r'\bexec codex\b'):
            self.assertNotRegex(script, pattern)


if __name__ == '__main__':
    unittest.main()
