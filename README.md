# RCJA Teacher Workshops

Self-contained workshop resources for RoboCup Junior Australia. The site root is a
landing page listing every workshop; each workshop builds to its own page. Covers what
the micro:bit is, what it can do, and why it suits Rescue Line — then hands off to a
live coding demo.

**Live site:** https://talkingj.github.io/rcja-microbit-workshop/

---

## How it works

Each workshop's content lives in `content/<slug>/*.md`. `workshops.yml` registers each
workshop and drives the landing page. Push to `main` and GitHub Actions rebuilds the
site automatically.

```
workshops.yml       ← registry: one entry per workshop
content/<slug>/     ← that workshop's numbered .md files
code/                ← drop your .py robot code files here (shared across workshops)
assets/photos/       ← drop kit photos here (shared across workshops)
build.py             ← builds index.html (landing) + one <slug>.html per workshop
template/shell.html  ← workshop page CSS + JS shell (rarely needs editing)
template/landing.html ← landing page shell
```

`python build.py` builds `index.html` (the landing page) plus one `<slug>.html` per
workshop listed in `workshops.yml`.

To add a workshop: create `content/<new-slug>/` with numbered `.md` files (copy the
`content/microbit/` set as a starting point) and add an entry to `workshops.yml`.

## Editing content

Open any file in `content/<slug>/` in a text editor. Prose is plain markdown. The HTML
blocks (cards, tables, grids) can have their text edited directly — just don't change
the class names.

## Adding photos

Drop your photo into `assets/photos/`, then find the matching `photo-slot` div in the relevant content file and replace the `<!-- Replace with: -->` comment:

```html
<img src="assets/photos/your-photo.jpg" alt="description">
```

## Adding robot code

Paste your MicroPython into the relevant file in `code/`. It will appear as a syntax-highlighted code block on the page once you reference it from `content/microbit/07-code.md`.

## Local preview

```bash
pip install markdown pyyaml
python build.py
# open index.html in a browser (landing page), or microbit.html directly
```

Auto-rebuild on save (requires `pip install watchdog`):

```bash
python build.py --watch
```

## Kit

Elecfreaks motor:bit smart car — two TT motors, 2-channel IR tracking module, ultrasonic sensor, carrier board that plugs directly onto the micro:bit edge connector.

| Connection | Pin |
|---|---|
| Left motor | M1 |
| Right motor | M2 |
| Left tracking sensor | P13 |
| Right tracking sensor | P14 |
| Ultrasonic trig | P15 |
| Ultrasonic echo | P16 |
| Buzzer | P0 (on-board) |

Tracking sensors return `1` on the black line, `0` on white (as demonstrated in the assembly/coding videos). If your module reads the opposite way, swap the values in the comparisons.
