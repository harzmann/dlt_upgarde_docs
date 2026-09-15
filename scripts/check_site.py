"""Check both language builds, local assets and public download metadata."""
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'site'
release = json.loads((ROOT / 'release.json').read_text(encoding='utf-8'))


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.lang = None

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == 'html':
            self.lang = attrs.get('lang')
        for name in ('href', 'src'):
            if name in attrs:
                self.links.append(attrs[name])


errors = []
for code in ('de', 'en'):
    for page in ('', 'guide', 'download', 'troubleshooting', 'changelog', 'image-changelog'):
        path = SITE / code / page / 'index.html'
        if not path.is_file():
            errors.append(str(path))
            continue
        text = path.read_text(encoding='utf-8')
        parsed = Links()
        parsed.feed(text)
        if parsed.lang != code:
            errors.append(f'Wrong HTML language: {path}')
        if '@@' in text:
            errors.append(f'Unresolved release placeholder: {path}')
        if page == 'download' and (release['download_url'] not in text or release['sha256'] not in text):
            errors.append(f'Missing release evidence: {path}')
        for link in parsed.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (path.parent / unquote(parts.path)).resolve()
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'Broken local link: {path.relative_to(SITE)} -> {link}')
if errors:
    raise SystemExit('\n'.join(errors))
print('Verified 12 DE/EN pages, HTML language, local links and download metadata.')
