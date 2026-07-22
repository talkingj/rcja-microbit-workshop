---
id: s-code
nav: Coding
label: Program the robot
title: "Coding your robot"
---

Watch the video, then build the program in MakeCode. It has two parts: following the line, then driving around an obstacle with the ultrasonic sensor. No rescue line track is needed to test the logic.

<!-- VIDEO_EMBED
title: Coding the line-following robot
drive_url: https://drive.google.com/file/d/1auG9TSjEIdfi6OtP2WDCCmV0zuniTodb/view
caption: Adds the motorbit and sonar extensions, then builds the line-follow logic and ultrasonic obstacle avoidance in MakeCode.
-->

<!-- SLIDE_BREAK -->

### Setup: extensions you need

1. Go to [makecode.microbit.org](https://makecode.microbit.org) and click **New Project**.
2. Click the **gear icon** (top right) then **Extensions**.
3. Search for `motorbit` and add it (motor control blocks).
4. Search for `sonarbit` and add it (ultrasonic sensor block).

<!-- SLIDE_BREAK -->

### Wiring reference

| Connection | Port | Notes |
|---|---|---|
| Left IR sensor | `P13` | 1 = black, 0 = white |
| Right IR sensor | `P14` | 1 = black, 0 = white |
| Ultrasonic trig | `P15` | trigger pin |
| Ultrasonic echo | `P16` | echo pin |
| Left motor | `M1` | TT motor, left wheel |
| Right motor | `M2` | TT motor, right wheel |

> **Sensor logic:** as shown in the video, the IR sensors read **1 on black** and **0 on white**. Read them with `digital read pin P13` and `digital read pin P14`. (If your module reads the other way round, just swap the 0s and 1s in the comparisons.)

<!-- SLIDE_BREAK -->

### Part 1: Line following

Build this as an **if / else if / else** chain inside the forever loop, using `digital read pin` on P13 and P14:

- **Turn left:** if `P13 = 1` (left sees black) **and** `P14 = 0` (right sees white). Use *turn left* at speed 50.
- **Turn right:** if `P13 = 0` **and** `P14 = 1` (right sees black). Use *turn right* at speed 50.
- **Go straight:** if `P13 = 0` **and** `P14 = 0` (both on white, line running between the sensors). Use *move forward* at speed 50.
- **Else:** stop. Anything else means an unexpected reading you can problem-solve later.

Load it, then tune: raise or lower the speed, and if it steers the wrong way, swap *turn left* / *turn right* (your motors or sensors are mirrored).

<!-- SLIDE_BREAK -->

### Part 2: Obstacle avoidance (ultrasonic)

In RoboCup Rescue Line the robot must drive **around** an obstacle. Add the ultrasonic sensor on top of the line follower:

- Read distance with the **sonar** block: trig `P15`, echo `P16`, units **cm**.
- If the distance is **less than 12 cm**, run an avoidance manoeuvre: *break* out of line following, *pause* briefly, then step through **turn right → pause → forward → pause → turn left → forward → …** until the robot has cleared the object and is back on the line.
- **Nest the whole line-following if/else inside the ultrasonic if/else** so both run together: the ultrasonic is checked every loop, and line following runs whenever nothing is in range.

> **Facilitator note:** this final program is built live in the video. Participants can follow along in MakeCode or just watch, no track is required to test the logic.

<!-- SLIDE_BREAK -->

### The finished program

Here is the complete line-following and obstacle-avoidance program from the video. Click **Edit** to open it in MakeCode, or **Download** to send it straight to a connected micro:bit.

<!-- MAKECODE_EMBED
title: Line following + obstacle avoidance
makecode_url: https://makecode.microbit.org/S61778-52603-41373-17881
-->

