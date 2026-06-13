#!/usr/bin/env python3
"""
Build script: reads content/*.md + code/*.py -> microbit-workshop.html

Usage:
    python build.py              # writes microbit-workshop.html
    python build.py --watch      # rebuild on file change (requires watchdog: pip install watchdog)
"""

import re
import sys
import html
from glob import glob
from pathlib import Path

try:
    import markdown as _markdown  # type: ignore[import-untyped]
    HAS_MARKDOWN = True
except ImportError:
    _markdown = None  # type: ignore[assignment]
    HAS_MARKDOWN = False

ROOT     = Path(__file__).parent
CONTENT  = ROOT / 'content'
CODE_DIR = ROOT / 'code'
TEMPLATE = ROOT / 'template' / 'shell.html'
OUTPUT   = ROOT / 'microbit-workshop.html'


# ── Front matter parser ───────────────────────────────────────────────────────

def parse_frontmatter(text):
    """Returns (meta dict, body string). Front matter is YAML-lite between --- lines."""
    meta = {}
    if not text.startswith('---'):
        return meta, text
    end = text.index('---', 3)
    fm_block = text[3:end].strip()
    body = text[end + 3:].strip()
    for line in fm_block.splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip().strip('"\'')
    return meta, body


# ── Markdown -> HTML ──────────────────────────────────────────────────────────

def md_to_html(text):
    """Convert markdown to HTML. Falls back to passthrough if markdown not installed."""
    if not text.strip():
        return ''
    if HAS_MARKDOWN and _markdown is not None:
        return _markdown.markdown(
            text,
            extensions=['tables', 'fenced_code', 'attr_list'],
            output_format='html',
        )
    # Minimal fallback: wrap paragraphs, pass HTML blocks through
    lines = text.split('\n')
    out = []
    buf = []
    def flush():
        p = ' '.join(buf).strip()
        if p:
            out.append(f'<p>{p}</p>')
        buf.clear()
    in_html = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('<') and not in_html:
            flush()
            in_html = True
        if in_html:
            out.append(line)
            if stripped == '' and out and not out[-1].strip().startswith('<'):
                in_html = False
        elif stripped == '':
            flush()
        else:
            buf.append(stripped)
    flush()
    return '\n'.join(out)


# ── Code file embedder ────────────────────────────────────────────────────────

def code_block(path):
    """Return a styled <pre><code> block for a .py file."""
    rel = path.relative_to(ROOT)
    try:
        src = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return f'<p class="code-missing">File not found: {rel}</p>'
    escaped = simple_highlight(src)
    return (
        f'<div class="code-filename">{rel}</div>'
        f'<pre class="code-block">{escaped}</pre>'
    )


def simple_highlight(src):
    """Very basic Python syntax colouring using spans."""
    KEYWORDS = {'from', 'import', 'def', 'class', 'if', 'elif', 'else',
                'while', 'for', 'in', 'return', 'True', 'False', 'None',
                'and', 'or', 'not', 'pass', 'break', 'continue', 'with',
                'as', 'try', 'except', 'finally', 'raise', 'lambda',
                'global', 'nonlocal', 'yield', 'del', 'assert', 'is'}
    result = []
    for line in src.splitlines(keepends=True):
        # Comment
        if line.lstrip().startswith('#'):
            result.append(f'<span class="cm">{html.escape(line)}</span>')
            continue
        # Tokenise roughly: strings, keywords, numbers, rest
        esc_line = html.escape(line)
        # Just escape and do word-level keyword highlight
        words = re.split(r'(\b\w+\b)', esc_line)
        out = ''
        for w in words:
            if w in KEYWORDS:
                out += f'<span class="kw">{w}</span>'
            elif re.fullmatch(r'\d+(\.\d+)?', w):
                out += f'<span class="nm">{w}</span>'
            else:
                out += w
        result.append(out)
    return ''.join(result)


# ── Section builder ───────────────────────────────────────────────────────────

def build_section(meta, body_html):
    """Wrap body HTML in the right section element."""
    sid   = meta.get('id', '')
    label = meta.get('label', '')
    title = meta.get('title', '')
    kind  = meta.get('type', 'section')

    if kind == 'hero':
        return f'<section id="hero" aria-label="Introduction">\n<div class="hero-inner">\n{body_html}\n</div>\n</section>'

    if kind == 'fullwidth':
        return f'<section id="{sid}">\n{body_html}\n</section>'

    intro_match = re.match(r'^<p>(.*?)</p>', body_html, re.DOTALL)
    intro_html = ''
    rest_html = body_html
    if intro_match:
        intro_html = f'<p class="section-intro">{intro_match.group(1)}</p>\n'
        rest_html = body_html[intro_match.end():].lstrip()

    label_html = f'<p class="section-label">{html.escape(label)}</p>\n' if label else ''
    title_html = f'<h2 class="section-title">{html.escape(title)}</h2>\n' if title else ''

    return (
        f'<section class="section" id="{sid}">\n'
        f'{label_html}'
        f'{title_html}'
        f'{intro_html}'
        f'{rest_html}\n'
        f'</section>'
    )


# ── Main build ────────────────────────────────────────────────────────────────

def build():
    files = sorted(glob(str(CONTENT / '*.md')))
    if not files:
        print('ERROR: no files found in content/')
        sys.exit(1)

    nav_tabs   = []
    hero_html  = ''
    page_secs  = []
    fw_secs    = []

    for fpath in files:
        raw = Path(fpath).read_text(encoding='utf-8')
        meta, body = parse_frontmatter(raw)
        body_html = md_to_html(body)
        section_html = build_section(meta, body_html)

        kind = meta.get('type', 'section')
        nav  = meta.get('nav', '')
        sid  = meta.get('id', '')

        if kind == 'hero':
            hero_html = section_html
        elif kind == 'fullwidth':
            fw_secs.append(section_html)
            if nav and sid:
                nav_tabs.append((sid, nav))
        else:
            page_secs.append(section_html)
            if nav and sid:
                nav_tabs.append((sid, nav))

    # Build nav HTML (first tab gets .active)
    nav_html_parts = []
    for i, (sid, label) in enumerate(nav_tabs):
        active = ' active' if i == 0 else ''
        nav_html_parts.append(
            f'<button class="nav-tab{active}" data-target="{sid}">{html.escape(label)}</button>'
        )
    nav_html = '\n    '.join(nav_html_parts)

    # Read template
    shell = TEMPLATE.read_text(encoding='utf-8')

    # Inject
    shell = shell.replace('<!-- NAV_TABS -->', nav_html)
    shell = shell.replace('<!-- HERO -->', hero_html)
    shell = shell.replace('<!-- SECTIONS_BEFORE_PAGE -->', '')
    shell = shell.replace('<!-- SECTIONS_IN_PAGE -->', '\n\n'.join(page_secs))
    shell = shell.replace('<!-- SECTIONS_FULLWIDTH -->', '\n\n'.join(fw_secs))

    OUTPUT.write_text(shell, encoding='utf-8')
    print(f'Built: {OUTPUT}')
    if not HAS_MARKDOWN:
        print('  Tip: pip install markdown  for proper markdown parsing')


# ── Watch mode ────────────────────────────────────────────────────────────────

def watch():
    try:
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler
    except ImportError:
        print('watchdog not installed. Run: pip install watchdog')
        sys.exit(1)
    import time

    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            if not event.is_directory:
                print(f'Changed: {event.src_path}')
                build()

    observer = Observer()
    for path in [str(CONTENT), str(CODE_DIR), str(ROOT / 'template')]:
        observer.schedule(Handler(), path, recursive=False)
    observer.start()
    print('Watching for changes. Ctrl+C to stop.')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    if '--watch' in sys.argv:
        build()
        watch()
    else:
        build()
