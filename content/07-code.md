---
id: s-code
nav: Coding
label:
title: Building toward line following
---

Four short activities that build up the skills needed for a line following robot. Each one adds a piece: display, input, motors, sensors. By the end you have everything working and the facilitator will show you how to put it together into a complete line follow.

> **Adding your MakeCode project to this page:** open your project at [makecode.microbit.org](https://makecode.microbit.org), click **Share**, copy the URL (looks like `https://makecode.microbit.org/S12345-abcde`), then paste it as `makecode_url:` in the matching block in `content/07-code.md` and rebuild.

### Setup: extensions you need

1. Go to [makecode.microbit.org](https://makecode.microbit.org) and click **New Project**.
2. Click the **gear icon** (top right) then **Extensions**.
3. Search for `motorbit` and add it (motor control blocks).
4. Search for `sonarbit` and add it (ultrasonic sensor block).

<!-- SLIDE_BREAK -->

### Wiring reference

| Connection | Port | Notes |
|---|---|---|
| Left motor | `M1` | TT motor, left wheel |
| Right motor | `M2` | TT motor, right wheel |
| Left IR sensor | `P4` | 0 = black, 1 = white |
| Right IR sensor | `P3` | 0 = black, 1 = white |
| Ultrasonic sensor | Free GVS port | Match pin in MakeCode |

> **Sensor logic:** the IR sensors return 0 on black and 1 on white. Set a pull-up on P3 and P4 inside your *on start* block.

<!-- SLIDE_BREAK -->

### Activity 1: LED display

Board and browser only. Get comfortable with MakeCode and confirm your setup works before touching the robot.

**Goal:** on start, show a heart icon. When button A is pressed, scroll the text "READY". When button B is pressed, show a tick icon.

<!-- MAKECODE_EMBED
title: Activity 1 - LED display
makecode_url:
hint: Create your Activity 1 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 2: Button events

Introduces event-driven programming. The robot will need to start from a button press in competition, so this is directly useful.

**Goal:** button A shows an arrow (forward). Button B shows a square (stop). Both buttons together show a cross (emergency stop). On start, show a dot.

<!-- MAKECODE_EMBED
title: Activity 2 - Button events
makecode_url:
hint: Create your Activity 2 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 3: Motor control

Assembled robot required (motor:bit + motors + battery). Confirms the robot is wired correctly before adding sensors.

**Goal:** button A drives both motors forward for 1 second then stops. Button B spins on the spot (one motor forward, one back). On start, show a ready icon.

<!-- MAKECODE_EMBED
title: Activity 3 - Motor control
makecode_url:
hint: Create your Activity 3 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 4: Reading IR sensors

IR sensors must be connected (P3 and P4). No track needed. This confirms the sensors are working and you understand what the values mean.

**Goal:** in the forever loop, read P3 and P4. If both return 1 (white), show a blank display. If either returns 0 (black detected), show a dot.

<!-- MAKECODE_EMBED
title: Activity 4 - Reading sensors
makecode_url:
hint: Create your Activity 4 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Live demo: line following

Once activities 1 to 4 are done, you have all the pieces. The facilitator will now show how to combine motor control and sensor readings into a working line follower.

The logic is straightforward: read both sensors in a forever loop, steer toward whichever sensor sees the line, drive forward when both see white.

> **Want to try it yourself?** Use a 5 cm strip of black electrical tape on white paper. You do not need a full track to test the steering logic.
