#!/usr/bin/env python3
"""
Build script: reads content/*.md + code/*.py -> microbit-workshop.html

Usage:
    python build.py              # writes microbit-workshop.html
    python build.py --watch      # rebuild on file change (requires watchdog: pip install watchdog)

Dependencies:
    pip install markdown pyyaml
"""

import re
import sys
import html
from glob import glob
from pathlib import Path

try:
    import yaml as _yaml          # type: ignore[import-untyped]
    HAS_YAML = True
except ImportError:
    _yaml = None                  # type: ignore[assignment]
    HAS_YAML = False

try:
    import markdown as _markdown  # type: ignore[import-untyped]
    HAS_MARKDOWN = True
except ImportError:
    _markdown = None              # type: ignore[assignment]
    HAS_MARKDOWN = False

ROOT     = Path(__file__).parent
CONTENT  = ROOT / 'content'
CODE_DIR = ROOT / 'code'
TEMPLATE = ROOT / 'template' / 'shell.html'
OUTPUT   = ROOT / 'microbit-workshop.html'


# ── Front matter parser ───────────────────────────────────────────────────────

def parse_frontmatter(text):
    """Returns (meta dict, body string). Uses PyYAML if available, else key:value fallback."""
    meta = {}
    if not text.startswith('---'):
        return meta, text
    try:
        end = text.index('---', 3)
    except ValueError:
        return meta, text
    fm_block = text[3:end].strip()
    body = text[end + 3:].strip()

    if HAS_YAML and _yaml is not None:
        try:
            meta = _yaml.safe_load(fm_block) or {}
        except Exception:
            pass
    else:
        # Minimal fallback: top-level key: value only
        for line in fm_block.splitlines():
            if ':' in line:
                k, _, v = line.partition(':')
                meta[k.strip()] = v.strip().strip('"\'')

    return meta, body


# ── Markdown -> HTML ──────────────────────────────────────────────────────────

def md_to_html(text):
    """Convert markdown to HTML."""
    if not text.strip():
        return ''
    if HAS_MARKDOWN and _markdown is not None:
        result = _markdown.markdown(
            text,
            extensions=['tables', 'fenced_code', 'attr_list'],
            output_format='html',
        )
        # Auto-apply pin-table class to all tables (plain <table> first)
        result = result.replace('<table>', '<table class="pin-table">')
        # Tables already given a class via attr_list (e.g. timing-table) get pin-table prepended
        result = re.sub(
            r'<table class="([^"]+)">',
            lambda m: f'<table class="pin-table {m.group(1)}">',
            result,
        )
        # Auto-apply setup-steps class to all ordered lists
        result = result.replace('<ol>', '<ol class="setup-steps">')
        # Convert blockquotes to callout divs
        result = re.sub(
            r'<blockquote>\s*<p>(.*?)</p>\s*</blockquote>',
            r'<div class="callout">\1</div>',
            result,
            flags=re.DOTALL,
        )
        return result
    # Minimal fallback
    lines = text.split('\n')
    out, buf = [], []
    def flush():
        p = ' '.join(buf).strip()
        if p:
            out.append(f'<p>{p}</p>')
        buf.clear()
    in_html = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('<') and not in_html:
            flush(); in_html = True
        if in_html:
            out.append(line)
            if not stripped:
                in_html = False
        elif not stripped:
            flush()
        else:
            buf.append(stripped)
    flush()
    return '\n'.join(out)


# ── SVG icon lookup ───────────────────────────────────────────────────────────

ICONS = {
    'led-matrix':     ('<rect x="3" y="3" width="18" height="18"/>'
                       '<circle cx="8.5" cy="8.5" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="12" cy="8.5" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="15.5" cy="8.5" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="8.5" cy="12" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="12" cy="12" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="15.5" cy="12" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="8.5" cy="15.5" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="12" cy="15.5" r="1.5" fill="#3db166" stroke="none"/>'
                       '<circle cx="15.5" cy="15.5" r="1.5" fill="#3db166" stroke="none"/>'),
    'buttons':         '<circle cx="7" cy="12" r="3"/><circle cx="17" cy="12" r="3"/>',
    'accelerometer':   ('<path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83'
                        'M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/>'
                        '<circle cx="12" cy="12" r="3"/>'),
    'compass':         ('<circle cx="12" cy="12" r="3"/>'
                        '<path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42'
                        'M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/>'),
    'temperature':     '<path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/>',
    'radio':           '<path d="M1 6l5 6-5 6M23 6l-5 6 5 6M8 12h8"/>',
    'microphone':      ('<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>'
                        '<path d="M19 10v2a7 7 0 0 1-14 0v-2"/>'
                        '<line x1="12" y1="19" x2="12" y2="23"/>'
                        '<line x1="8" y1="23" x2="16" y2="23"/>'),
    'speaker':         ('<polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>'
                        '<path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/>'),
    'edge-connector':  ('<rect x="2" y="14" width="20" height="6" rx="0"/>'
                        '<path d="M6 14V8M12 14V4M18 14V10"/>'),
    'microbit':        '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 9h18"/>',
    'motorbit':        '<rect x="2" y="7" width="20" height="10" rx="1"/><path d="M6 7V5M10 7V5M14 7V5M18 7V5"/>',
    'motor':           '<circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>',
    'ir-sensor':       '<rect x="4" y="8" width="16" height="8" rx="1"/><circle cx="9" cy="12" r="2"/><circle cx="15" cy="12" r="2"/>',
    'ultrasonic':      '<rect x="3" y="8" width="18" height="8" rx="1"/><circle cx="8" cy="12" r="2"/><circle cx="16" cy="12" r="2"/>',
    'battery':         '<rect x="3" y="9" width="18" height="10" rx="1"/><path d="M7 9V7a2 2 0 0 1 4 0v2M13 9V7a2 2 0 0 1 4 0v2"/>',
}


def _icon_svg(key):
    paths = ICONS.get(key, '')
    if not paths:
        return ''
    return (
        f'<svg viewBox="0 0 24 24" width="20" height="20" fill="none" '
        f'stroke="#3db166" stroke-width="2" stroke-linecap="round">'
        f'{paths}</svg>'
    )


def _parse_yaml(text):
    """Parse YAML text; return dict or list. Falls back to empty dict on error."""
    if HAS_YAML and _yaml is not None:
        try:
            return _yaml.safe_load(text) or {}
        except Exception:
            return {}
    return {}


# ── Shortcode renderers ───────────────────────────────────────────────────────

def render_hw_cards(yaml_text):
    """Render <!-- HW_CARDS --> shortcode: YAML list of {name, icon, desc, tag?}."""
    items = _parse_yaml(yaml_text)
    if not isinstance(items, list):
        return ''
    cards = []
    for item in items:
        name = html.escape(str(item.get('name', '')))
        desc = html.escape(str(item.get('desc', '')))
        tag  = item.get('tag', '')
        icon = _icon_svg(str(item.get('icon', '')))
        tag_html = f'<span class="hw-tag">{html.escape(str(tag))}</span>' if tag else ''
        cards.append(
            f'<div class="hw-card">'
            f'<div class="hw-icon">{icon}</div>'
            f'<div class="hw-name">{name}</div>'
            f'<div class="hw-desc">{desc}</div>'
            f'{tag_html}'
            f'</div>'
        )
    return f'<div class="hw-grid">{"".join(cards)}</div>'


def render_activity_cards(yaml_text):
    """Render <!-- ACTIVITY_CARDS --> shortcode: YAML list of {title, cap, desc, num?}."""
    items = _parse_yaml(yaml_text)
    if not isinstance(items, list):
        return ''
    cards = []
    for item in items:
        title = html.escape(str(item.get('title', '')))
        cap   = html.escape(str(item.get('cap', '')))
        desc  = html.escape(str(item.get('desc', '')))
        num   = item.get('num', '')
        num_html = f'<div class="activity-num">{html.escape(str(num))}</div>' if num else ''
        cards.append(
            f'<div class="activity-card">'
            f'{num_html}'
            f'<div class="activity-title">{title}</div>'
            f'<div class="activity-cap">{cap}</div>'
            f'<div class="activity-desc">{desc}</div>'
            f'</div>'
        )
    return f'<div class="activity-grid">{"".join(cards)}</div>'


def render_rcja_banner(yaml_text):
    """Render <!-- RCJA_BANNER --> shortcode."""
    data = _parse_yaml(yaml_text)
    if not isinstance(data, dict):
        data = {}
    title       = html.escape(str(data.get('title', 'RoboCup Junior Australia')))
    sub         = html.escape(str(data.get('sub', '')))
    count       = html.escape(str(data.get('count', '')))
    count_label = html.escape(str(data.get('count_label', '')))
    return (
        f'<div class="rcja-banner">'
        f'<div>'
        f'<div class="rcja-title">{title}</div>'
        f'<div class="rcja-sub">{sub}</div>'
        f'</div>'
        f'<div class="rcja-badge">'
        f'<div class="rcja-badge-val">{count}</div>'
        f'<div class="rcja-badge-label">{count_label}</div>'
        f'</div>'
        f'</div>'
    )


def render_photo_row(yaml_text):
    """Render <!-- PHOTO_ROW --> shortcode: YAML list of {url, alt, id?}."""
    items = _parse_yaml(yaml_text)
    if not isinstance(items, list):
        return ''
    slots = []
    for item in items:
        url     = html.escape(str(item.get('url', '')))
        alt     = html.escape(str(item.get('alt', '')))
        slot_id = item.get('id', '')
        id_attr = f' id="{html.escape(str(slot_id))}"' if slot_id else ''
        slots.append(
            f'<div class="diagram-slot"{id_attr}>'
            f'<img src="{url}" alt="{alt}" loading="lazy">'
            f'</div>'
        )
    return f'<div class="photo-row">{"".join(slots)}</div>'


# ── Card / grid renderers (called when YAML data is present) ──────────────────

def render_projects(projects):
    """Render a list of project dicts as a .project-grid."""
    cards = []
    for p in projects:
        name   = html.escape(str(p.get('name', '')))
        domain = html.escape(str(p.get('domain', '')))
        desc   = html.escape(str(p.get('desc', '')))
        color  = html.escape(str(p.get('color', '#3db166')))
        img    = str(p.get('img', ''))
        tags   = p.get('tags', [])
        tag_html = ''.join(f'<span class="tag">{html.escape(str(t))}</span>' for t in tags)
        img_html = (f'<div class="project-img"><img src="{html.escape(img)}" alt="{name}" loading="lazy"></div>'
                    if img else '')
        cards.append(
            f'<div class="project-card">'
            f'<div class="project-stripe" style="background:{color}"></div>'
            f'{img_html}'
            f'<div class="project-body">'
            f'<div class="project-domain">{domain}</div>'
            f'<div class="project-name">{name}</div>'
            f'<div class="project-desc">{desc}</div>'
            f'<div class="project-tags">{tag_html}</div>'
            f'</div></div>'
        )
    return f'<div class="project-grid">{"".join(cards)}</div>'


def render_pitch(points):
    """Render a list of pitch/why dicts as a .pitch-grid."""
    cards = []
    for i, p in enumerate(points, 1):
        title = html.escape(str(p.get('title', '')))
        body  = html.escape(str(p.get('body', '')))
        cards.append(
            f'<div class="pitch-card">'
            f'<div class="pitch-num">{i:02d}</div>'
            f'<div class="pitch-title">{title}</div>'
            f'<div class="pitch-body">{body}</div>'
            f'</div>'
        )
    return f'<div class="pitch-grid">{"".join(cards)}</div>'


def render_makecode_embed(url, title=''):
    """Render a MakeCode project embed, or a placeholder if no URL."""
    if not url:
        hint = title or 'MakeCode project'
        return (
            f'<div class="makecode-placeholder">'
            f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.4"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>'
            f'<div class="mcp-label">MakeCode embed</div>'
            f'<div class="mcp-hint">Share your MakeCode project and add the URL as<br>'
            f'<code>makecode_url: https://makecode.microbit.org/S...</code><br>'
            f'in this section\'s front matter</div>'
            f'</div>'
        )
    # Extract share ID from various URL forms
    # e.g. https://makecode.microbit.org/S12345-abcde or #pub:XXXXX
    embed_src = url
    if 'makecode.microbit.org' in url and '---' not in url and '--docs' not in url:
        # Convert share URL to embed URL
        embed_src = url.replace('makecode.microbit.org/', 'makecode.microbit.org/---run#pub:').replace('/#', '#')
        if 'makecode.microbit.org/S' in url:
            share_id = url.split('/S')[-1].split('/')[0].split('#')[0]
            embed_src = f'https://makecode.microbit.org/---run#pub:S{share_id}'
    label = html.escape(title or 'MakeCode project')
    return (
        f'<div class="makecode-embed">'
        f'<div class="makecode-header">'
        f'<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>'
        f'{label}'
        f'<a href="{html.escape(url)}" target="_blank" rel="noopener" class="makecode-open">Open in MakeCode ↗</a>'
        f'</div>'
        f'<iframe src="{html.escape(embed_src)}" '
        f'frameborder="0" '
        f'sandbox="allow-popups allow-forms allow-scripts allow-same-origin" '
        f'allowfullscreen></iframe>'
        f'</div>'
    )


# ── Code file embedder ────────────────────────────────────────────────────────

def is_placeholder(src):
    """True if a code file contains only comments and whitespace."""
    for line in src.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith('#'):
            return False
    return True


def code_block(path):
    """Return a styled code block, or a placeholder if the file is empty/not written."""
    rel = path.relative_to(ROOT)
    try:
        src = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        return (
            f'<div class="code-filename">{rel}</div>'
            f'<div class="code-placeholder-block">'
            f'<span>File not found: {html.escape(str(rel))}</span>'
            f'</div>'
        )
    if is_placeholder(src):
        hint_lines = [l for l in src.splitlines() if l.strip().startswith('#')]
        hint = html.escape('\n'.join(hint_lines)) if hint_lines else 'Code coming soon.'
        return (
            f'<div class="code-filename">{rel}</div>'
            f'<div class="code-placeholder-block">'
            f'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.4"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>'
            f'<span>Facilitator adds code here</span>'
            f'<pre class="code-hint">{hint}</pre>'
            f'</div>'
        )
    return (
        f'<div class="code-filename">{rel}</div>'
        f'<pre class="code-block">{simple_highlight(src)}</pre>'
    )


def simple_highlight(src):
    """Very basic Python/JS syntax colouring."""
    KEYWORDS = {'from', 'import', 'def', 'class', 'if', 'elif', 'else',
                'while', 'for', 'in', 'return', 'True', 'False', 'None',
                'and', 'or', 'not', 'pass', 'break', 'continue', 'with',
                'as', 'try', 'except', 'finally', 'raise', 'lambda',
                'global', 'nonlocal', 'yield', 'del', 'assert', 'is',
                'let', 'const', 'var', 'function', 'true', 'false', 'null'}
    result = []
    for line in src.splitlines(keepends=True):
        if line.lstrip().startswith('#') or line.lstrip().startswith('//'):
            result.append(f'<span class="cm">{html.escape(line)}</span>')
            continue
        esc_line = html.escape(line)
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


def resolve_embeds(body, _source_file=''):
    """Replace EMBED and MAKECODE_EMBED comment markers with rendered HTML."""
    # <!-- HW_CARDS\n...yaml...\n-->
    body = re.sub(
        r'<!--\s*HW_CARDS\s*\n(.*?)\n-->',
        lambda m: render_hw_cards(m.group(1).strip()),
        body, flags=re.DOTALL,
    )
    # <!-- ACTIVITY_CARDS\n...yaml...\n-->
    body = re.sub(
        r'<!--\s*ACTIVITY_CARDS\s*\n(.*?)\n-->',
        lambda m: render_activity_cards(m.group(1).strip()),
        body, flags=re.DOTALL,
    )
    # <!-- RCJA_BANNER\n...yaml...\n-->
    body = re.sub(
        r'<!--\s*RCJA_BANNER\s*\n(.*?)\n-->',
        lambda m: render_rcja_banner(m.group(1).strip()),
        body, flags=re.DOTALL,
    )
    # <!-- PHOTO_ROW\n...yaml...\n-->
    body = re.sub(
        r'<!--\s*PHOTO_ROW\s*\n(.*?)\n-->',
        lambda m: render_photo_row(m.group(1).strip()),
        body, flags=re.DOTALL,
    )

    # <!-- EMBED: code/foo.py -->
    def replace_embed(match):
        ref = match.group(1).strip()
        return code_block(ROOT / ref)
    body = re.sub(r'<!--\s*EMBED:\s*([\w/.\-]+)\s*-->', replace_embed, body)

    # <!-- MAKECODE_EMBED\ntitle: ...\nmakecode_url: ...\nhint: ...\n-->
    def replace_makecode(match):
        block = match.group(1)
        data = {}
        for line in block.splitlines():
            if ':' in line:
                k, _, v = line.partition(':')
                data[k.strip()] = v.strip()
        url   = data.get('makecode_url', '').strip()
        title = data.get('title', '').strip()
        hint  = data.get('hint', '').strip()
        if not url:
            return (
                f'<div class="makecode-placeholder">'
                f'<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" opacity="0.4"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>'
                f'<div class="mcp-label">MakeCode project: {html.escape(title)}</div>'
                f'<div class="mcp-hint">{html.escape(hint) if hint else "Share a MakeCode project and add the URL as <code>makecode_url: https://makecode.microbit.org/S...</code>"}</div>'
                f'</div>'
            )
        return render_makecode_embed(url, title)
    body = re.sub(r'<!--\s*MAKECODE_EMBED\s*\n(.*?)\n-->', replace_makecode, body, flags=re.DOTALL)

    return body


# ── Section builder ───────────────────────────────────────────────────────────

def build_section(meta, body_html):
    """Wrap body HTML in the right section element, injecting YAML-driven components."""
    sid   = meta.get('id', '')
    label = meta.get('label', '')
    title = meta.get('title', '')
    kind  = meta.get('type', 'section')

    # Inject YAML-driven components at the end of body_html
    extras = ''

    if 'projects' in meta:
        extras += render_projects(meta['projects'])

    if 'points' in meta:
        extras += render_pitch(meta['points'])

    # MakeCode embed at section level (for coding sections with one embed)
    if 'makecode_url' in meta or meta.get('makecode_embed'):
        url = meta.get('makecode_url', '')
        embed_title = meta.get('makecode_title', title or label)
        extras += render_makecode_embed(url, embed_title)

    body_html = body_html + extras

    if kind == 'hero':
        return (
            f'<section id="hero" aria-label="Introduction">\n'
            f'<div class="hero-inner">\n{body_html}\n</div>\n</section>'
        )

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
        f'{label_html}{title_html}{intro_html}{rest_html}\n'
        f'</section>'
    )


# ── Main build ────────────────────────────────────────────────────────────────

def build():
    files = sorted(glob(str(CONTENT / '*.md')))
    if not files:
        print('ERROR: no files found in content/')
        sys.exit(1)

    nav_tabs  = []
    hero_html = ''
    page_secs = []

    for fpath in files:
        raw = Path(fpath).read_text(encoding='utf-8')
        meta, body = parse_frontmatter(raw)
        body_html = md_to_html(body)
        body_html = resolve_embeds(body_html, fpath)
        section_html = build_section(meta, body_html)

        kind = meta.get('type', 'section')
        nav  = meta.get('nav', '')
        sid  = meta.get('id', '')

        if kind == 'hero':
            hero_html = section_html
        else:
            page_secs.append(section_html)
            if nav and sid:
                nav_tabs.append((sid, nav))

    # Nav tabs (first gets .active)
    nav_html = '\n    '.join(
        f'<button class="nav-tab{" active" if i == 0 else ""}" data-target="{sid}">'
        f'{html.escape(label)}</button>'
        for i, (sid, label) in enumerate(nav_tabs)
    )

    shell = TEMPLATE.read_text(encoding='utf-8')
    shell = shell.replace('<!-- NAV_TABS -->', nav_html)
    shell = shell.replace('<!-- HERO -->', hero_html)
    shell = shell.replace('<!-- SECTIONS_BEFORE_PAGE -->', '')
    shell = shell.replace('<!-- SECTIONS_IN_PAGE -->', '\n\n'.join(page_secs))
    shell = shell.replace('<!-- SECTIONS_FULLWIDTH -->', '')

    OUTPUT.write_text(shell, encoding='utf-8')
    print(f'Built: {OUTPUT}')
    if not HAS_YAML:
        print('  Tip: pip install pyyaml  for YAML front matter support')
    if not HAS_MARKDOWN:
        print('  Tip: pip install markdown  for proper markdown parsing')


# ── Watch mode ────────────────────────────────────────────────────────────────

def watch():
    try:
        from watchdog.observers import Observer      # type: ignore[import-untyped]
        from watchdog.events import FileSystemEventHandler  # type: ignore[import-untyped]
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
