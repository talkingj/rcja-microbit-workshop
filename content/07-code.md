---
id: s-code
nav: Coding
label:
title: "Activities: simple to complex"
---

Five activities in order of complexity. Activities 1 and 2 need only the micro:bit and a browser. Activity 3 needs the assembled robot. Activities 4 and 5 need the IR sensors attached. No rescue line track is required.

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

Board and browser only. No hardware needed beyond the micro:bit. Write a program that shows text and icons on the 5x5 LED display. Test it in the simulator before downloading.

**Goal:** on start, show a heart icon. When button A is pressed, scroll the text "READY". When button B is pressed, show a tick icon.

<!-- MAKECODE_EMBED
title: Activity 1 - LED display
makecode_url:
hint: Create your Activity 1 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 2: Button events

Board only. Introduces event-driven programming. Each button does something different, and the program waits for input rather than running continuously.

**Goal:** button A shows an arrow pointing forward. Button B shows a square (stop). Both buttons together show a cross (emergency stop). On start, show a dot to indicate the program is running.

<!-- MAKECODE_EMBED
title: Activity 2 - Button events
makecode_url:
hint: Create your Activity 2 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 3: Motor control

Assembled robot required (motor:bit + motors + battery). No sensors needed. Button presses drive the wheels directly. This confirms the robot is wired correctly before adding sensors.

**Goal:** button A drives both motors forward for 1 second then stops. Button B drives one motor forward and one backward (spin on the spot). On start, show a ready icon.

<!-- MAKECODE_EMBED
title: Activity 3 - Motor control
makecode_url:
hint: Create your Activity 3 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 4: Reading sensors

IR sensors must be connected (P3 and P4). No track needed. Read the sensor values and show them on the LED display. Hold the sensor over white paper, then over a dark surface, and watch the display change.

**Goal:** in the forever loop, read P3 and P4. If both return 1 (white), show a blank display. If either returns 0 (black detected), show a dot. This confirms the sensors are working before any driving logic is added.

<!-- MAKECODE_EMBED
title: Activity 4 - Reading sensors
makecode_url:
hint: Create your Activity 4 MakeCode project, click Share, and paste the URL above as makecode_url:
-->

<!-- SLIDE_BREAK -->

### Activity 5: Simple decisions (stretch)

Full robot required. A strip of black electrical tape on white paper is enough to test with. Write an if/else block that steers based on sensor readings. This is the foundation of line following.

**Goal:** in the forever loop: if both sensors read white, drive forward. If the left sensor reads black (0), steer left. If the right sensor reads black (0), steer right. Start the program with button A.

> **No track?** Use a 5 cm wide strip of black electrical tape on an A3 sheet of white paper. Students can hold it by hand and move it under the sensor while the robot is stationary, watching the steering change in the motor output.

<!-- MAKECODE_EMBED
title: Activity 5 - Simple decisions
makecode_url:
hint: Create your Activity 5 MakeCode project, click Share, and paste the URL above as makecode_url:
-->
