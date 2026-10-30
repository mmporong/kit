"""Run the existing Bash installer in tests without changing user settings."""
import os
import shutil
import subprocess
from pathlib import Path


def run_install(script, target):
    if os.name == 'nt':
        # Windows' system bash may launch WSL; use the Bash shipped with Git.
        git = shutil.which('git')
        bash = Path(git).resolve().parents[1] / 'bin/bash.exe' if git else None
        if bash is None or not bash.is_file():
            raise RuntimeError('Git Bash is required to run installer tests on Windows')
    else:
        bash = 'bash'
    return subprocess.run(
        [str(bash), Path(script).as_posix(), Path(target).as_posix()],
        capture_output=True, text=True, encoding='utf-8', timeout=30)


def make_symlink_or_skip(test, link, target, *, directory=False):
    try:
        link.symlink_to(target, target_is_directory=directory)
    except OSError as error:
        if os.name == 'nt' and error.winerror == 1314:
            test.skipTest('Windows symlink creation privilege is unavailable')
        raise
