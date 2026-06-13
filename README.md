# RCJA micro:bit Workshop

A self-contained workshop resource for RoboCup Junior Australia. Covers what the micro:bit is, what it can do, and why it suits Rescue Line — then hands off to a live coding demo.

**Live site:** https://talkingj.github.io/rcja-microbit-workshop/

---

## How it works

Content lives in `content/*.md`. Push to `main` and GitHub Actions rebuilds the site automatically.

```
content/        ← edit these to change the page
code/           ← drop your .py robot code files here
assets/photos/  ← drop kit photos here
build.py        ← assembles everything into index.html
template/       ← CSS + JS shell (rarely needs editing)
```

## Editing content

Open any file in `content/` in a text editor. Prose is plain markdown. The HTML blocks (cards, tables, grids) can have their text edited directly — just don't change the class names.

## Adding photos

Drop your photo into `assets/photos/`, then find the matching `photo-slot` div in the relevant content file and replace the `<!-- Replace with: -->` comment:

```html
<img src="assets/photos/your-photo.jpg" alt="description">
```

## Adding robot code

Paste your MicroPython into the relevant file in `code/`. It will appear as a syntax-highlighted code block on the page once you reference it from `content/07-code.md`.

## Local preview

```bash
pip install markdown
python build.py
# open microbit-workshop.html in a browser
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
| Left tracking sensor | P4 |
| Right tracking sensor | P3 |
| Buzzer | P0 (on-board) |

Tracking sensors return `0` on the black line, `1` on white. Set pull-ups on P3 and P4.
