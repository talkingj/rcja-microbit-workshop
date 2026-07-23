---
id: s-kit
nav: Assembling
label: Build the robot
title: Assembling your robot
---

Your kit arrives as individual components: no soldering, and every connection is push-fit or screw terminal. Watch the assembly video, then expand the step-by-step build below to follow along.

<!-- VIDEO_EMBED
title: Assembling your micro:bit robot
drive_url: https://drive.google.com/file/d/10NKOaa0V-621W8AjKQY3cZ_uS2OXyHd0/view
caption: "Full walkthrough: sensors, motors, battery, and mounting the board on a base."
-->

<!-- STEPS: Step-by-step build -->

Every connector is labelled. The one rule that keeps you out of trouble: **black always goes to ground (G)**.

1. **IR tracking sensors.** Clip each sensor and its two cables into the case. On the back, the pins are labelled **G / V / S**. Line the **black** cable up with **G** (ground). Plug the first sensor into **pin set 13** and the second into **pin set 14**, keeping black on the ground row.
2. **Ultrasonic sensor.** Plug the four cables into **VCC, Trig, Echo, GND** on the sensor. Run the **ground** cable to the ground pin at **pin set 15** and **VCC** to the VCC pin just above it. Then plug the two signal cables in: **Trig → P15**, **Echo → P16**.
3. **Motors.** Screw each motor's wires into the M1 / M2 terminals: **red → +**, **black → −**. Left motor on **M1**, right motor on **M2**. If a motor pin snaps off (it happens with students), strip the wire end and screw the bare wire straight into the terminal.
4. **Battery pack.** **Black → GND**, **red → VIN**, both screwed into the power terminal.
5. **micro:bit.** Slot it into the edge connector at the top of the board. Switch on the batteries and the LEDs light up when everything is powered.
6. **Chassis.** Hot-glue the assembled board onto a base. Laser-cut and 3D-printable chassis files are on the **Resources** page.

> **Sensor and motor mirroring:** if the robot later steers the wrong way, a sensor or motor pair is simply plugged in mirrored. Swap the left/right values in code rather than rewiring.

<!-- STEPS_END -->
