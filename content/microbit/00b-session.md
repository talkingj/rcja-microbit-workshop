---
id: s-session
nav: About this session
label: Session overview
title: About this session
---

A 2-hour hands-on activity. The first half covers what the micro:bit is and what it can do. The second half follows two videos: assembling the robot, then coding it to follow a line and avoid obstacles. No rescue line track is required.

<div class="callout">
<strong>At a glance.</strong> <b>Audience:</b> students around 10 and up; screw terminals and if/else logic suit upper primary and lower secondary. <b>Group size:</b> 2–3 students per robot, so everyone gets hands on. <b>Duration:</b> about 2 hours. <b>You provide:</b> one robot kit and one USB laptop or Chromebook per group, plus something to test on: a black line on white (electrical tape on paper or a whiteboard works).
</div>

<!-- SLIDE_BREAK -->

### What students will be able to do

By the end of the session, students can:

- Read a digital sensor and explain what its 0 / 1 output means.
- Write an if / else if / else chain that makes a robot act on sensor readings.
- Explain a control loop: sense → decide → act, repeated every cycle.
- Calibrate a sensor and debug a robot that misbehaves.

<!-- SLIDE_BREAK -->

### Before the session

- **Devices:** any laptop or Chromebook with a USB port and a modern browser. All coding runs in the browser at makecode.microbit.org, with nothing to install.
- **Flashing:** students click **Download** to get a `.hex` file and drag it onto the MICROBIT USB drive. Direct flashing over WebUSB also works in Chrome and Edge if the school allows it.
- **School networks:** check ahead of time that makecode.microbit.org and the two video links actually open on the school network; some filters block unfamiliar sites or Google Drive.
- **Batteries:** use fresh alkaline AA cells. Rechargeable AAs (1.2 V each) are too low-voltage for reliable motors.

<div class="callout">
<strong>Safety.</strong> <b>Hot glue guns</b> run at around 200 °C, so an adult should do the gluing or supervise closely, and keep cold water nearby for burns. <b>Small parts</b> (screws, wheels) are a choking and loss hazard, so work over trays. <b>Batteries:</b> don't let the bare leads touch; a short circuit gets hot fast. <b>Moving robot:</b> keep fingers, hair, and loose clothing clear of the wheels and gears when it's powered, and test on the floor or a large table where it can't drive off an edge.
</div>

<!-- SLIDE_BREAK -->

| Topic | Time | Notes |
|---|---|---|
| Introduction | 10 min | What is the micro:bit, where it is used, cost and availability |
| Hardware tour | 10 min | Walk through the built-in sensors and what the edge connector gives access to |
| Assembling the robot | 30 min | Follow the assembly video: sensors, motors, battery, and mounting the board on a base |
| Coding: line following | 25 min | Follow the coding video: add the extensions, calibrate the sensors, then build the if/else line-follow program |
| Coding: obstacle avoidance | 20 min | Add the ultrasonic sensor logic on top so the robot drives around an obstacle |
| RoboCup Junior context | 15 min | Show how the sensor readings connect to a real competition. Demo or video of a Rescue Line run |
| Questions & buffer | 10 min | Also your buffer if assembly or coding overran |

<div class="callout">
<strong>Running short on time?</strong> Assembly and coding are the blocks most likely to overrun, and the times above leave little slack. If you fall behind: hand out pre-assembled robots (or at least pre-fit the fiddly ultrasonic wiring) to protect the coding time; and since line-following can't be tested in the simulator, build the program along with the video on one shared robot at the front rather than having every group tune their own. If a group runs out of time, the finished MakeCode program on the Coding page flashes straight to their board.
</div>
