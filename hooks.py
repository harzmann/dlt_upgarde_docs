"""Release facts and page-preserving language links shared by both builds."""
import json
from pathlib import Path

ROOT = Path(__file__).parent


def on_page_markdown(markdown, page, config, files):
    release = json.loads((ROOT / 'release.json').read_text(encoding='utf-8'))
    values = {'VERSION': release['version'], 'SHA256': release['sha256'],
              'SIZE': f"{release['size_bytes'] / 1_000_000:.1f} MB",
              'DOWNLOAD': release['download_url'], 'RELEASE': release['release_url']}
    for name, value in values.items():
        markdown = markdown.replace('@@' + name + '@@', str(value))
    return markdown


def on_page_context(context, page, config, nav):
    config.extra['alternate'] = [
        {'name': name, 'lang': code,
         'link': f'https://harzmann.github.io/dlt_upgarde_docs/{code}/{page.url}'}
        for code, name in (('de', 'Deutsch'), ('en', 'English'))]
    return context
