# Restructure Plan — multi-workshop site + landing page

**Goal:** Turn this single-workshop generator into a multi-workshop site. The site
root (`index.html`) becomes a **landing page** with a card for each workshop, and each
workshop builds to its own page. Also tidy up the file layout so adding a new workshop
is a copy-paste-and-edit job.

**Audience for this doc:** an implementer (possibly a cheaper model) who has NOT seen
this repo before. Follow the steps in order. Do not skip the "Key facts" section.

---

## Key facts you MUST understand before touching anything

1. **`index.html` is generated. Never edit it by hand — it gets overwritten.**
   The real source is:
   - `content/*.md` — the workshop content (frontmatter + markdown + HTML + shortcodes)
   - `template/shell.html` — the CSS/JS page shell with placeholder comments
   - `build.py` — reads content, fills the shell, writes `index.html`

2. **How the build works today (`build.py` → `build()`):**
   - Globs `content/*.md` (sorted by filename — that's why files are numbered `00-`, `01-`…).
   - For each file: parse frontmatter → markdown-to-HTML → expand shortcodes
     (`<!-- HW_CARDS -->`, `<!-- EMBED: code/x.py -->`, `<!-- MAKECODE_EMBED -->`, etc.)
     → wrap in a `<section>`.
   - The file with `type: hero` becomes the hero; the rest become body sections and
     nav tabs.
   - Loads `template/shell.html`, string-replaces these placeholders, writes `index.html`:
     - `<!-- NAV_TABS -->`
     - `<!-- HERO -->`
     - `<!-- SECTIONS_IN_PAGE -->`
     - (`<!-- SECTIONS_BEFORE_PAGE -->` and `<!-- SECTIONS_FULLWIDTH -->` are set to `''`)

3. **The shell has three hard-coded strings that must become per-workshop** (in
   `template/shell.html`): the `<title>` (line ~6), the top-bar `<h1>micro:bit</h1>`
   (~line 1153), and the pill `<span class="top-pill">Getting Started</span>` (~line 1162).

4. **Asset paths in content and shell are root-relative-ish** (`resources/...`,
   `assets/photos/...`, `./resources/vendor/...`, `code/*.py`). They resolve because
   `index.html` sits at the repo root. **This is the #1 thing that can break.** The plan
   below keeps every generated page AT THE REPO ROOT (`microbit.html`, not
   `microbit/index.html`) precisely so these paths keep working with zero rewriting.

5. **Deploy:** `.github/workflows/build.yml` runs `python build.py` and publishes the
   whole repo dir to GitHub Pages on push to `main`. **No workflow change is needed** —
   as long as `build.py` still produces all the HTML at the repo root.

---

## Target layout

```
workshops.yml            ← NEW. The registry: one entry per workshop. Single source of
                            truth for both the landing page and the build loop.
content/
  microbit/              ← NEW subdir. MOVE the existing content/*.md files in here.
    00-hero.md
    00b-session.md
    ... (unchanged)
    08-resources.md
  <future-slug>/         ← each new workshop = a new folder of numbered .md files
template/
  shell.html             ← workshop shell. Add placeholder tokens (see Step 4).
  landing.html           ← NEW. The landing-page shell.
build.py                 ← refactor into build_workshop() + build_landing() (Step 5).
code/  assets/  resources/  ← unchanged, stay at repo root, shared across workshops.
index.html               ← now the LANDING page (generated).
microbit.html            ← the micro:bit workshop (generated).
```

**URL result:** `/<repo>/` → landing; `/<repo>/microbit.html` → the workshop.
(Flat `.html` files at root are deliberate — see Key fact #4. Do NOT use
`microbit/index.html` subfolders; that would break every `resources/` and `assets/`
path in the content.)

---

## Step 1 — Create the registry `workshops.yml`

Create `workshops.yml` at the repo root. This drives everything.

```yaml
- slug: microbit
  title: "The micro:bit"
  subtitle: "What it is and why it works"
  blurb: "A hands-on intro to the BBC micro:bit and how it powers a RoboCup Rescue Line robot. Covers the hardware, MakeCode, and live robot coding."
  level: "Beginner"
  duration: "2 hours"
  audience: "Teachers & students"
  accent: "#3db166"
  pill: "Getting Started"
  content: "content/microbit"
```

Field meaning:
- `slug` — output filename (`microbit` → `microbit.html`) and card link target.
- `title` / `subtitle` — used for the browser `<title>` and can be shown on the card.
- `blurb`, `level`, `duration`, `audience` — shown on the landing card.
- `accent` — the card's top-stripe colour (reuse the existing green `#3db166`).
- `pill` — text for the workshop's top-bar pill.
- `content` — path to that workshop's markdown folder.

To add a workshop later: add a folder under `content/` and one entry here. Nothing else.

---

## Step 2 — Move existing content

```
mkdir content/microbit
git mv content/*.md content/microbit/
```

(Use `git mv` so history is preserved.) After this, `content/` contains only the
`microbit/` folder. The `.md` files themselves need **no changes** — their asset paths
(`resources/...`, `assets/...`) still point at repo root, and the pages still build at
root.

---

## Step 3 — Refactor `build.py`: constants + workshop loading

At the top of `build.py`, the constants currently are:

```python
CONTENT  = ROOT / 'content'
TEMPLATE = ROOT / 'template' / 'shell.html'
OUTPUT   = ROOT / 'index.html'
```

Replace `OUTPUT`/`CONTENT` usage with per-workshop values and add:

```python
WORKSHOPS_YML  = ROOT / 'workshops.yml'
SHELL_TEMPLATE = ROOT / 'template' / 'shell.html'
LANDING_TEMPLATE = ROOT / 'template' / 'landing.html'

def load_workshops():
    """Read workshops.yml -> list of dicts. Requires pyyaml."""
    text = WORKSHOPS_YML.read_text(encoding='utf-8')
    data = _parse_yaml(text)          # _parse_yaml already exists in build.py
    return data if isinstance(data, list) else []
```

(`_parse_yaml` already exists and returns `{}` on failure — but for a top-level YAML
*list* you may want `_yaml.safe_load` directly. Simplest: reuse `parse_frontmatter`'s
yaml path or call `_yaml.safe_load(text)` guarded by `HAS_YAML`.)

---

## Step 4 — Tokenise `template/shell.html`

Make the three hard-coded strings into placeholders so each workshop fills them.

- Line ~6: `<title>micro:bit: What it is and why it works</title>`
  → `<title><!-- PAGE_TITLE --></title>`
- Line ~1153: `<h1>micro:bit</h1>`
  → `<h1><!-- WORKSHOP_NAME --></h1>`
- Line ~1162: `<span class="top-pill">Getting Started</span>`
  → `<span class="top-pill"><!-- TOP_PILL --></span>`

**Add a "back to all workshops" link** so users can get from a workshop back to the
landing page. Put it in the top bar, right after the `<h1>`. Insert:

```html
<a href="index.html" class="home-link">← All workshops</a>
```

And add this CSS near the top-bar styles (around line 61 in the shell's `<style>`):

```css
.home-link {
  font-size: 11px; font-weight: 700; color: rgba(255,255,255,0.65);
  text-decoration: none; text-transform: uppercase; letter-spacing: 0.05em;
  white-space: nowrap; flex-shrink: 0;
}
.home-link:hover { color: #fff; }
```

Note the `#top-bar h1` rule has `flex: 1` — the home link and pill sit to its right, so
layout stays intact.

---

## Step 5 — Refactor `build.py`: `build_workshop()` and `build_landing()`

Rename the existing `build()` to `build_workshop(workshop)` and parameterise it. The
body is almost identical — only the content directory, the output path, and the three
new template tokens change. Concretely:

```python
def build_workshop(workshop):
    slug        = workshop['slug']
    content_dir = ROOT / workshop['content']
    out_path    = ROOT / f'{slug}.html'

    files = sorted(glob(str(content_dir / '*.md')))
    if not files:
        print(f'WARNING: no content for workshop {slug!r}')
        return

    nav_tabs, hero_html, page_secs = [], '', []
    for fpath in files:
        raw = Path(fpath).read_text(encoding='utf-8')
        meta, body = parse_frontmatter(raw)
        body_html  = resolve_embeds(md_to_html(body), fpath)
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

    nav_html = '\n    '.join(
        f'<button class="nav-tab{" active" if i == 0 else ""}" data-target="{sid}">'
        f'{html.escape(label)}</button>'
        for i, (sid, label) in enumerate(nav_tabs)
    )

    title    = workshop.get('title', slug)
    subtitle = workshop.get('subtitle', '')
    page_title = f'{title}: {subtitle}' if subtitle else title

    shell = SHELL_TEMPLATE.read_text(encoding='utf-8')
    shell = shell.replace('<!-- PAGE_TITLE -->',    html.escape(page_title))
    shell = shell.replace('<!-- WORKSHOP_NAME -->',  html.escape(title))
    shell = shell.replace('<!-- TOP_PILL -->',       html.escape(workshop.get('pill', '')))
    shell = shell.replace('<!-- NAV_TABS -->',       nav_html)
    shell = shell.replace('<!-- HERO -->',           hero_html)
    shell = shell.replace('<!-- SECTIONS_BEFORE_PAGE -->', '')
    shell = shell.replace('<!-- SECTIONS_IN_PAGE -->', '\n\n'.join(page_secs))
    shell = shell.replace('<!-- SECTIONS_FULLWIDTH -->', '')

    out_path.write_text(shell, encoding='utf-8')
    print(f'Built workshop: {out_path.name}')
```

Then the landing builder:

```python
def render_workshop_card(w):
    slug   = html.escape(str(w.get('slug', '')))
    title  = html.escape(str(w.get('title', '')))
    sub    = html.escape(str(w.get('subtitle', '')))
    blurb  = html.escape(str(w.get('blurb', '')))
    accent = html.escape(str(w.get('accent', '#3db166')))
    metas  = []
    for key in ('level', 'duration', 'audience'):
        if w.get(key):
            metas.append(f'<span class="wc-meta">{html.escape(str(w[key]))}</span>')
    meta_html = ''.join(metas)
    return (
        f'<a class="workshop-card" href="{slug}.html">'
        f'<div class="wc-stripe" style="background:{accent}"></div>'
        f'<div class="wc-body">'
        f'<div class="wc-title">{title}</div>'
        f'<div class="wc-sub">{sub}</div>'
        f'<div class="wc-blurb">{blurb}</div>'
        f'<div class="wc-metas">{meta_html}</div>'
        f'<span class="wc-cta">Open workshop →</span>'
        f'</div></a>'
    )

def build_landing(workshops):
    cards = ''.join(render_workshop_card(w) for w in workshops)
    shell = LANDING_TEMPLATE.read_text(encoding='utf-8')
    shell = shell.replace('<!-- WORKSHOP_CARDS -->', cards)
    (ROOT / 'index.html').write_text(shell, encoding='utf-8')
    print('Built landing: index.html')
```

And the entry point (`if __name__ == '__main__':` / `build()`):

```python
def build():
    workshops = load_workshops()
    if not workshops:
        print('ERROR: no workshops found in workshops.yml'); sys.exit(1)
    for w in workshops:
        build_workshop(w)
    build_landing(workshops)
```

Keep `--watch` working: it already calls `build()`, and the watch paths should be
widened to include the whole `content/` tree and `workshops.yml`. Change the watched
paths to `[str(CONTENT), str(CODE_DIR), str(ROOT / 'template'), str(ROOT)]` (or just
re-run `build()` on any change under `content/`).

---

## Step 6 — Create `template/landing.html`

A standalone page (its own `<style>`, no dependency on the workshop shell). Reuse the
existing design language: navy `#1b2945`, green `#3db166`, system font, square corners.
It needs exactly one placeholder: `<!-- WORKSHOP_CARDS -->`.

Skeleton (the implementer can refine the visual polish):

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RCJA Workshops</title>
<style>
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
  :root{--navy:#1b2945;--navy-mid:#263a5e;--green:#3db166;--border:#d0d7e3;
        --surface:#f4f6fa;--muted:#666;--label:#3a3a3a}
  body{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;color:#0a0a0a;
       background:#fff;line-height:1.6}
  .lp-hero{background:var(--navy);padding:64px 24px}
  .lp-hero-inner{max-width:1000px;margin:0 auto}
  .lp-kicker{font-size:11px;font-weight:700;text-transform:uppercase;
             letter-spacing:.1em;color:var(--green);margin-bottom:14px}
  .lp-hero h1{font-size:clamp(30px,5vw,52px);font-weight:700;letter-spacing:-0.035em;
              color:#fff;line-height:1.1;margin-bottom:16px}
  .lp-hero p{font-size:16px;color:rgba(255,255,255,.6);max-width:60ch}
  .lp-main{max-width:1000px;margin:0 auto;padding:48px 24px}
  .workshop-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));
                 gap:20px}
  .workshop-card{display:block;border:1.5px solid var(--border);text-decoration:none;
                 color:inherit;background:#fff;transition:border-color .15s,transform .15s}
  .workshop-card:hover{border-color:var(--green);transform:translateY(-2px)}
  .wc-stripe{height:6px}
  .wc-body{padding:24px}
  .wc-title{font-size:20px;font-weight:700;color:var(--navy);letter-spacing:-0.02em}
  .wc-sub{font-size:13px;color:var(--muted);margin:2px 0 12px}
  .wc-blurb{font-size:14px;color:var(--label);line-height:1.6}
  .wc-metas{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0}
  .wc-meta{font-size:11px;font-weight:600;background:var(--surface);
           border:1px solid var(--border);color:var(--muted);padding:3px 9px}
  .wc-cta{font-size:12px;font-weight:700;color:var(--green);text-transform:uppercase;
          letter-spacing:.05em}
  .lp-footer{max-width:1000px;margin:0 auto;padding:0 24px 64px;
             font-size:13px;color:var(--muted)}
  @media(max-width:640px){.lp-hero{padding:44px 16px}.lp-main{padding:32px 16px}}
</style>
</head>
<body>
  <section class="lp-hero">
    <div class="lp-hero-inner">
      <div class="lp-kicker">RoboCup Junior Australia</div>
      <h1>Teacher Workshops</h1>
      <p>Self-contained, hands-on workshops you can run in your classroom. Pick one to
         get started — each includes everything you need: hardware tour, code, and a
         presentation mode for the projector.</p>
    </div>
  </section>
  <main class="lp-main">
    <div class="workshop-grid">
      <!-- WORKSHOP_CARDS -->
    </div>
  </main>
  <footer class="lp-footer">RoboCup Junior Australia · built for classroom use</footer>
</body>
</html>
```

---

## Step 7 — Update `README.md`

Update the "How it works" section to describe the new layout:
- Content per workshop lives in `content/<slug>/*.md`.
- `workshops.yml` registers each workshop and drives the landing page.
- `python build.py` now builds `index.html` (landing) + one `<slug>.html` per workshop.
- To add a workshop: create `content/<new-slug>/` with numbered `.md` files (copy the
  `microbit` set as a starting point) and add an entry to `workshops.yml`.

---

## Step 8 — Verify

Run locally (deps already used by CI: `markdown`, `pyyaml`, plus `ezdxf`, `Pillow` for
the resources section):

```bash
pip install markdown pyyaml ezdxf Pillow
python build.py
```

Expect console output:
```
Built workshop: microbit.html
Built landing: index.html
```

Then check, by opening the files in a browser:
1. `index.html` shows the landing page with a **micro:bit** card that links to
   `microbit.html`.
2. `microbit.html` looks **identical to the current site**, with a working
   "← All workshops" link in the top bar back to `index.html`.
3. On `microbit.html`: images/diagrams load, the 3D STL viewer and DXF preview render,
   the code embeds show, **Present** mode works, **Save PDF** works, nav tabs scroll.
   (These all depend on the `resources/`, `assets/`, `code/` paths still resolving —
   confirming the flat-file-at-root decision held.)

If anything in #3 is broken, it's almost certainly a path issue from accidentally
putting the workshop in a subfolder — it must be `microbit.html` at the repo root.

---

## Explicitly out of scope (do not do these)

- Do **not** edit `index.html` or `microbit.html` directly — they are build outputs.
- Do **not** move `code/`, `assets/`, or `resources/` — they stay at the repo root and
  are shared.
- Do **not** change `.github/workflows/build.yml` — it already runs `build.py` and
  deploys the whole dir.
- Do **not** convert workshops to `<slug>/index.html` subfolders — it breaks asset paths.

---

## Summary of changes

| File | Action |
|---|---|
| `workshops.yml` | **create** — workshop registry |
| `content/microbit/*.md` | **move** existing `content/*.md` here (git mv, no content edits) |
| `template/shell.html` | **edit** — add `<!-- PAGE_TITLE -->`, `<!-- WORKSHOP_NAME -->`, `<!-- TOP_PILL -->` tokens + "All workshops" link & CSS |
| `template/landing.html` | **create** — landing-page shell with `<!-- WORKSHOP_CARDS -->` |
| `build.py` | **refactor** — `load_workshops`, `build_workshop(w)`, `render_workshop_card`, `build_landing`, new `build()` loop |
| `README.md` | **edit** — document the new multi-workshop layout |
| `index.html`, `microbit.html` | generated outputs (do not hand-edit) |
