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

### Calibrate the sensors first

**Do this before writing any line-following logic; it is the single most important step.** IR tracking modules don't all read the same way: some return **1** on black, others **1** on white. If you assume the wrong one, *every* branch of your program is inverted and no amount of speed-tuning will fix it.

Find out what *your* sensors actually do:

1. In a `forever` loop, add `show number` and drop `digital read pin P13` inside it.
2. Download it, then hold the left sensor over the **black** line and read the number. Move it over **white** and read again.
3. Note which surface gives **1** and which gives **0**. Repeat for `P14` (the right sensor).

<div class="callout">
<strong>Which way did yours read?</strong> The wiring reference and code below are written for <b>1 = black, 0 = white</b> (as shown in the video). If your module is the other way round (black reads <b>0</b>), that's fine and common: just swap every <code>0</code> and <code>1</code> in the comparisons below. The logic is identical; only the numbers flip.
</div>

<!-- SLIDE_BREAK -->

### Wiring reference

| Connection | Port | Notes |
|---|---|---|
| Left IR sensor | `P13` | black = 1, white = 0 *(confirm by calibration)* |
| Right IR sensor | `P14` | black = 1, white = 0 *(confirm by calibration)* |
| Ultrasonic trig | `P15` | trigger pin |
| Ultrasonic echo | `P16` | echo pin |
| Left motor | `M1` | TT motor, left wheel |
| Right motor | `M2` | TT motor, right wheel |

> **Sensor logic:** read the sensors with `digital read pin P13` and `digital read pin P14`. The values below assume your calibration matched the video (black = 1). If it didn't, swap the 0s and 1s throughout.

<!-- SLIDE_BREAK -->

### Part 1: Line following

The two sensors sit on either side of the line, so the line runs **between** them. Build this as an **if / else if / else** chain inside the forever loop, using `digital read pin` on P13 and P14:

- **Turn left:** if `P13 = 1` (left sees black) **and** `P14 = 0` (right sees white). Use *turn left* at speed 50.
- **Turn right:** if `P13 = 0` **and** `P14 = 1` (right sees black). Use *turn right* at speed 50.
- **Go straight:** if `P13 = 0` **and** `P14 = 0` (both on white, line running between the sensors). Use *move forward* at speed 50.
- **Else:** stop.

<div class="callout">
<strong>Known limitation: both sensors on black.</strong> The one case left over is <b>both sensors see black at once</b>, which lands in the <em>else</em> and stops the robot. That happens on a thick line, a sharp corner, or an intersection, so this two-sensor design follows a clean line well but stalls at junctions. That's a property of the design, not a student mistake. Handling intersections is a later step (see <b>Extend it</b> below and the RoboCup section).
</div>

Load it, then tune. Two different problems have two different fixes:

- **It steers the *wrong way* on every turn** (turns away from the line): a sensor or motor pair is plugged in mirrored. Swap *turn left* / *turn right* in the code.
- **It does the *opposite* action everywhere** (drives off instead of correcting, "straight" and "stop" swapped): the polarity is inverted, so go back and swap the 0s and 1s. This is what the calibration step catches.

<!-- SLIDE_BREAK -->

### Part 2: Obstacle avoidance (ultrasonic)

In RoboCup Rescue Line the robot must drive **around** an obstacle. Add the ultrasonic sensor on top of the line follower:

- Read the distance every loop with the **sonar** block (trig `P15`, echo `P16`, units **cm**).
- If the distance is **less than 12 cm**, run an avoidance manoeuvre: break out of line following, pause briefly, then step through *turn right → pause → forward → pause → turn left → forward → …* until the robot has cleared the object and is back on the line.
- Nest the whole line-following if/else inside the ultrasonic if/else so both run together: the ultrasonic is checked every loop, and line following runs whenever nothing is in range.

<div class="callout">
<strong>Expect a lot of tuning; it may not work first time.</strong> This manoeuvre is <em>open-loop</em>: it runs fixed turn and drive times and hopes the robot ends up back on the line. Battery level, floor friction, and small motor differences all change how far each timed step travels, so the pause lengths from the video may need adjusting, and the robot won't always rejoin the line cleanly. Treat it as a starting point to tune, not a finished solution.
</div>

> **Facilitator note:** this final program is built live in the video. Participants can follow along in MakeCode or just watch; no track is required to test the logic.

<!-- SLIDE_BREAK -->

### Troubleshooting

Robotics with a class guarantees a few of these. Work down the table.

| Symptom | Likely cause | Fix |
|---|---|---|
| Spins on the spot / does the opposite everywhere | Sensor polarity is inverted (black actually reads 0) | Re-run the calibration step; swap every 0 and 1 in the comparisons |
| Turns the wrong way on every turn | Left/right sensors or motors are mirrored | Swap *turn left* / *turn right* in the code (don't rewire) |
| One motor runs backwards | That motor's two wires are in the terminal the wrong way round | Swap the red and black wires on that M1/M2 terminal |
| Doesn't move at all | No power, flat batteries, or extensions not added | Check the battery switch and cells; confirm LEDs light; re-check `motorbit`/`sonarbit` are added |
| Drives straight off the line | Speed too high to react, or sensors too high off the surface | Lower the speed (try 35–40); mount the IR sensors closer to the floor |
| Stops dead on a corner or thick line | Both sensors see black → the *else* branch (known limitation) | Expected for this design; slow down before corners, or add intersection handling later |

<!-- SLIDE_BREAK -->

### Extend it

For groups that finish early, or to stretch stronger students:

- **Tune for speed:** find the fastest speed the robot can still follow the line reliably.
- **Show its state:** use the LED display or the V2 speaker to signal what the robot "thinks": an arrow for each turn, a tone when it sees an obstacle. Great for debugging, too.
- **Add a third state:** handle *both sensors on black* (a corner or junction) deliberately instead of stopping; for example, keep turning until one sensor comes off the black.
- **Struggling groups:** focus on getting calibration and Part 1 working: a robot that follows a line is a complete result. Flash the finished program below and let them read and tweak it rather than build from scratch.

<!-- SLIDE_BREAK -->

### The finished program

Here is the complete line-following and obstacle-avoidance program from the video. Click **Edit** to open it in MakeCode, or **Download** to send it straight to a connected micro:bit.

<!-- MAKECODE_EMBED
title: Line following + obstacle avoidance
makecode_url: https://makecode.microbit.org/S61778-52603-41373-17881
-->
