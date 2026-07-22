---
id: s-kit
nav: Assembling
label: Build the robot
title: Assembling your robot
---

Your kit arrives as individual components: no soldering, and every connection is push-fit or screw terminal. Watch the assembly video, then use the step list and kit reference below to build along.

<!-- VIDEO_EMBED
title: Assembling your micro:bit robot
drive_url: https://drive.google.com/file/d/10NKOaa0V-621W8AjKQY3cZ_uS2OXyHd0/view
caption: "Full walkthrough: sensors, motors, battery, and mounting the board on a base."
-->

<!-- SLIDE_BREAK -->

### Assembly steps

Every connector is labelled. The one rule that keeps you out of trouble: **black always goes to ground (G)**.

1. **IR tracking sensors.** Clip each sensor and its two cables into the case. On the back, the pins are labelled **G / V / S**. Line the **black** cable up with **G** (ground). Plug the first sensor into **pin set 13** and the second into **pin set 14**, keeping black on the ground row.
2. **Ultrasonic sensor.** Plug the four cables into **VCC, Trig, Echo, GND** on the sensor. Run the **ground** cable to the ground pin at **pin set 15** and **VCC** to the VCC pin just above it. Then plug the two signal cables in: **Trig → P15**, **Echo → P16**.
3. **Motors.** Screw each motor's wires into the M1 / M2 terminals: **red → +**, **black → −**. Left motor on **M1**, right motor on **M2**. If a motor pin snaps off (it happens with students), strip the wire end and screw the bare wire straight into the terminal.
4. **Battery pack.** **Black → GND**, **red → VIN**, both screwed into the power terminal.
5. **micro:bit.** Slot it into the edge connector at the top of the board. Switch on the batteries and the LEDs light up when everything is powered.
6. **Chassis.** Hot-glue the assembled board onto a base. Laser-cut and 3D-printable chassis files are on the **Resources** page.

> **Sensor and motor mirroring:** if the robot later steers the wrong way, a sensor or motor pair is simply plugged in mirrored. Swap the left/right values in code rather than rewiring.

<!-- SLIDE_BREAK -->

### What's in your kit

> **What is in your kit:** one micro:bit V2, one Elecfreaks motor:bit carrier board, two TT DC gear motors with wheels, one 2-channel IR tracking sensor module, one HC-SR04 ultrasonic sensor, one 4xAA battery holder with JST connector, and jumper wires.

<!-- PHOTO_ROW
- url: "https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/6zRKrvw.jpg"
  alt: Elecfreaks motor:bit carrier board
  id: photo-motorbit-kit
- url: "https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/5ayGCgd.png"
  alt: micro:bit inserted into the motor:bit carrier board
  id: photo-motorbit-assembled
-->

<!-- HW_CARDS
- name: micro:bit V2
  icon: microbit
  desc: The brain. Has the 5x5 LED display, buttons, sensors, and radio. Plugs into the top of the carrier board.
- name: motor:bit carrier board
  icon: motorbit
  desc: Connects to the micro:bit edge connector. Has motor driver circuits, power regulation, and labelled ports for motors and sensors.
- name: TT gear motors x2
  icon: motor
  desc: One for each wheel. Wired to M1 and M2 on the carrier board using the screw terminals.
- name: IR tracking sensor
  icon: ir-sensor
  desc: Two sensors on one board. Detects black vs. white surfaces. Connects to P13 and P14. Mount at the front, facing down.
- name: Ultrasonic sensor
  icon: ultrasonic
  desc: "Two round transducers: one transmits, one receives. Measures distance up to 4 m. Trig to P15 and echo to P16 (match the pins in MakeCode)."
- name: 4xAA battery pack
  icon: battery
  desc: Plugs into the JST connector on the carrier board. Use alkaline AA batteries. Rechargeable AA batteries are too low-voltage for reliable motor operation.
-->
