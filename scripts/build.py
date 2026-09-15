"""Build both languages without requiring access to the private source project."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
release = json.loads((ROOT / 'release.json').read_text(encoding='utf-8'))
if not re.fullmatch(r'[0-9a-f]{64}', release.get('sha256') or '') or release.get('size_bytes', 0) <= 0:
    raise SystemExit('Record the verified EXE in release.json before building the download site.')
for code in ('de', 'en'):
    shutil.copytree(ROOT / 'assets', ROOT / 'docs' / code / 'assets', dirs_exist_ok=True)
    subprocess.run([sys.executable, '-m', 'mkdocs', 'build', '--strict', '--clean',
                    '-f', str(ROOT / f'mkdocs.{code}.yml')], cwd=ROOT, check=True)
shutil.copyfile(ROOT / 'landing.html', ROOT / 'site/index.html')
(ROOT / 'site/.nojekyll').touch()
shutil.copyfile(ROOT / 'release.json', ROOT / 'site/release.json')
subprocess.run([sys.executable, str(ROOT / 'scripts/check_site.py')], cwd=ROOT, check=True)
