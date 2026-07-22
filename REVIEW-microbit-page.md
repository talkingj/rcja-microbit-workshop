# Critical review — `microbit.html` (Build-A-Bit workshop)

Review of https://talkingj.github.io/rcja-microbit-workshop/microbit.html
Written for a teacher who has to actually run this session. Prioritised for an editing agent.

---

## TL;DR — top 5 fixes, in priority order

1. **Resolve the 0-vs-1 black/white contradiction** (see below) and add a live sensor-calibration step so students confirm polarity instead of trusting the sheet.
2. **Add a troubleshooting table** (spins in place / one motor backwards / doesn't move / drives off the line).
3. **Reframe the RoboCup link** as the "first building block" of a Rescue Line robot, and name the both-sensors-black = stop limitation.
4. **Add safety notes + a realistic timing plan with a buffer / fallback** if the build runs long.
5. **State target age, group size, learning objectives, and device prerequisites** up front.

---

## 🚩 Blocking bug: black/white polarity contradicts itself

The document states opposite things about the single most important fact in the build:

- **Hardware section** ("Extending the micro:bit"): *"IR tracking sensor… reading black and white surfaces (**0 on black, 1 on white**)."*
- **Coding section** (wiring table + "Sensor logic"): *"IR sensors read **1 on black and 0 on white**."*

The entire line-following if/else is built on the "1 = black" assumption. If the real modules read 0 on black (common for reflective IR trackers), **every branch is inverted** and the robot misbehaves everywhere.

The doc's own fix — *"swap turn left/right if it steers wrong"* — will **not** fix inverted polarity; it creates new wrong behaviour.

**Fix:** pick one truth, make it consistent across the page, and add a ~2-minute calibration step: hold the sensor over black vs white and read the value on the LED display, so students *discover* the polarity.

---

## Overselling the competition link

The RoboCup Junior framing is good motivation but has a credibility gap:

- **Rescue Line** is described as "follow lines, avoid obstacles, climb ramps, and rescue victims." This kit (2 IR sensors + ultrasonic, a 4-branch if/else) can do a clean line and *attempt* an obstacle. It **cannot** do intersections, green turn-markers, gaps, ramps/seesaws, or evacuation-zone victim rescue. Say explicitly: "this is the *first building block* of a Rescue Line robot."
- The two-sensor "line runs *between* the sensors" scheme means **both-black = else = stop**. On a thick line, an intersection, or a sharp corner both sensors see black and the robot just stops. Name this as a known limitation, not a student mistake.

---

## Technical robustness the lesson glosses over

- **Obstacle avoidance is open-loop.** "Turn right → pause → forward → pause → turn left" with hardcoded timings is fragile — battery level, friction, and motor variation change the result, and it rarely returns cleanly to the line. Frame it honestly: "expect a lot of tuning; it may not work first time."
- **No troubleshooting section.** Robotics with kids guarantees problems. A short "if X, check Y" table would help the teacher more than anything else on this list. (spins on the spot / one motor backwards / doesn't move / drives off line / stops on a corner.)
- **"Rechargeable AA too low-voltage"** is a fair, correct note (4×1.2 V vs 4×1.5 V) — keep it.

---

## Pedagogy / classroom-reality gaps

- **Timing is a fantasy.** Blocks sum to exactly 120 min with **zero buffer**, and **30 min to assemble** (screw terminals, four ultrasonic wires, hot glue, mount micro:bit) with children is very optimistic. It will overrun. Add a fallback if the build eats the coding time.
- **"Just watch" undersells passivity.** Line-following can't be tested in the simulator (no IR sensor), so watchers get very little. Also, groups aren't sized — one robot per how many kids? In 3s/4s some disengage during a single-robot build.
- **No stated learning objectives / outcomes.** e.g. "By the end students can read a digital sensor, write an if/else, and explain a control loop." Helps a teacher justify and assess the session.
- **No differentiation.** Mentions Blocks vs Python but the walkthrough is effectively Blocks-only. Nothing for fast finishers (tune speed, add a third state, use the buzzer) or for strugglers.
- **Target age unspecified.** Screw terminals + boolean logic implies ~10+, but the teacher is left to guess.

---

## Safety & logistics — largely missing

- **No safety notes at all.** Hot glue guns (burns), small parts, battery/short-circuit handling, motor/wheel pinch points. A children's build resource needs these.
- **Device/setup prerequisites unstated.** Laptops vs Chromebooks, USB access, WebUSB "flash directly" vs drag-the-hex, and blocked-website caveats on school networks. All predictable friction on the day.
- **Minor accuracy nit:** MicroPython described as *"the most-used language globally"* — dubious depending on the metric. Soften it.

---

## What's genuinely good (keep)

- Clear hardware tour; specs mostly correct (radio range, ultrasonic 2–400 cm, CPU-die temperature).
- Wiring instructions are concrete and internally consistent (P13/P14/P15/P16, M1/M2); "black always to ground" is a nice memorable anchor.
- Both DXF and STL chassis files *with print settings* — thoughtful, above-and-beyond.
- The at-a-glance session table and "what's in your kit" inventory are exactly what a teacher wants.

---

# Design, theming & usability

Assessed from the actual CSS, not the rendered text. **Overall: genuinely professional and cohesive — a strength of the page.** The gaps are accessibility (contrast + small type) and classroom reliability (Drive-hosted video), not aesthetics.

## Strengths (keep)

- **Real design-token system.** A consistent CSS variable palette (`--navy #1b2945` / `--green #3fd37f` plus a full border/surface/ink/muted scale) applied everywhere. No one-off styling — every card, table header and label pulls from the same tokens. This is what makes it read as *designed*.
- **Coherent brand aesthetic.** Navy + green, sharp corners, hairline dividers (1px grid gaps), consistent 1.5px borders, tight heading letter-spacing. A deliberate editorial/technical look that holds together across ~8 different card types.
- **Good wayfinding.** Sticky top bar + sticky tab nav + scroll-progress bar; smooth-scroll with `scroll-margin-top` so anchors clear the sticky chrome; `focus-visible` outlines for keyboard users.
- **Above-and-beyond features:** a presentation/slides overlay mode, a proper **print stylesheet** (hides nav/overlays, page-breaks per section), real embedded videos, a live MakeCode embed, and an STL 3D viewer. No leftover empty placeholder boxes — all photo/video/code slots are filled. Responsive down to 520px.

## Fixes, priority order

1. **Bump up small type (biggest usability issue).** Base is 15px but card bodies run 12px and labels 10–11px. For a page that gets **projected** or read by younger kids, that's too small. Raise card/body text to 13–14px and labels to ~11px minimum.
2. **Fix contrast failures (WCAG AA).** Green section labels (`--green-dark #339655` on white ≈ 3.3:1) and dim navy-panel text (`rgba(255,255,255,0.3–0.45)`) fall below the 4.5:1 bar for small text. Darken the green for text use and lift the white opacities.
3. **Move videos off Google Drive.** Two of three iframes are `drive.google.com/.../preview`, which can require sign-in/permission, load slowly, and are sometimes blocked on locked-down school networks — exactly where this runs. Use unlisted YouTube for reliability.
4. **Modernise the mono font.** All code/pin tables use `Courier New` (dated). Swap to `ui-monospace, 'SF Mono', Menlo, Consolas, monospace` — cheap polish win.
5. **Consider dark mode.** Light-only, no `prefers-color-scheme`. Given the navy-heavy theme, a dark variant would be natural and nice for dim classrooms. Minor / optional.

## Minor notes

- The neon-ish green is slightly "tech-startup," but used sparingly so it's fine.
- Mobile tab nav scrolls with a hidden scrollbar and no visual hint that more tabs exist off-screen.
