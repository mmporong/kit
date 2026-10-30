"""! New: reference deployment and synthetic runner cases; not AI-quality tests."""
import hashlib
import re
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def snapshot(root: Path) -> dict:
    """! Record file bytes only; temporary test data never leaves this process."""
    return {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in root.rglob('*') if p.is_file() and not p.is_symlink()
    }


class GuidanceTests(unittest.TestCase):
    def test_new_references_are_installed_byte_for_byte(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            result = subprocess.run(
                ['bash', str(ROOT / 'install.sh'), str(project)],
                capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            for relative in (
                'kit-data/references/model-evaluation.md',
                'kit-verify/references/evidence-log.md',
            ):
                self.assertEqual(
                    (ROOT / 'skills' / relative).read_bytes(),
                    (project / '.agents/skills' / relative).read_bytes())

    def test_changed_reference_conflict_preserves_existing_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            command = ['bash', str(ROOT / 'install.sh'), str(project)]
            first = subprocess.run(command, capture_output=True, text=True, timeout=10)
            self.assertEqual(first.returncode, 0, first.stderr)
            reference = project / '.agents/skills/kit-data/references/model-evaluation.md'
            reference.write_text('existing project-specific guidance\n', encoding='utf-8')
            before = snapshot(project)
            second = subprocess.run(command, capture_output=True, text=True, timeout=10)
            self.assertNotEqual(second.returncode, 0)
            self.assertEqual(snapshot(project), before)

    def test_skill_reference_paths_exist_and_remain_inside_skill(self):
        checked = []
        for skill in sorted((ROOT / 'skills').glob('*/SKILL.md')):
            text = skill.read_text(encoding='utf-8')
            references = set(re.findall(r'references/[a-z0-9-]+\.md', text))
            for reference in references:
                target = (skill.parent / reference).resolve()
                self.assertIn(skill.parent.resolve(), target.parents)
                self.assertTrue(target.is_file(), str(target))
                self.assertGreater(target.stat().st_size, 0)
                checked.append(reference)
        self.assertIn('references/model-evaluation.md', checked)
        self.assertIn('references/evidence-log.md', checked)

    def run_synthetic_unittest(self, case_source=None):
        """! Inspect actual exit codes; do not implement a production log classifier."""
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp)
            if case_source is not None:
                (work / 'test_case.py').write_text(textwrap.dedent(case_source), encoding='utf-8')
            return subprocess.run(
                [sys.executable, '-m', 'unittest', 'discover', '-s', str(work), '-v'],
                cwd=work, capture_output=True, text=True, timeout=10)

    def test_zero_tests_wrapper_can_have_zero_exit_code(self):
        # ! Use an explicit wrapper; unittest CLI behavior differs by Python version.
        code = 'import unittest; unittest.TextTestRunner().run(unittest.TestSuite())'
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, '-c', code], cwd=tmp,
                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Ran 0 tests', result.stderr)

    def test_all_skipped_can_have_zero_exit_code(self):
        result = self.run_synthetic_unittest('''
            import unittest
            class SyntheticCase(unittest.TestCase):
                @unittest.skip('synthetic skip example')
                def test_never_executed(self):
                    raise AssertionError('This assertion is not executed')
        ''')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Ran 1 test', result.stderr)
        self.assertIn('OK (skipped=1)', result.stderr)

    def test_wrapper_can_mask_failed_test_exit_code(self):
        code = textwrap.dedent('''
            import unittest
            class SyntheticFailure(unittest.TestCase):
                def test_failure(self):
                    self.assertEqual(1, 2)
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(SyntheticFailure)
            unittest.TextTestRunner(verbosity=2).run(suite)
            # ! Synthetic anti-pattern: the wrapper ignores the failed result.
        ''')
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, '-c', code], cwd=tmp,
                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertIn('FAILED (failures=1)', result.stderr)


if __name__ == '__main__':
    unittest.main()
