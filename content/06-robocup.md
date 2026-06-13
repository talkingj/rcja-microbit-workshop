---
id: s-robocup
nav: RoboCup
label: Real-world context
title: "RoboCup Junior Rescue Line"
---

The skills covered in this workshop apply directly to RoboCup Junior Rescue Line. The competition gives students a concrete goal that uses line following, sensor reading, and motor control together in a timed autonomous run.

<div class="rcja-banner">
  <div>
    <div class="rcja-title">RoboCup Junior Australia: Rescue Line</div>
    <div class="rcja-sub">An autonomous robot navigates a black line, avoids obstacles, climbs ramps, and rescues a victim from a chemical spill. 120 seconds. Scored on every element it completes.</div>
  </div>
  <div class="rcja-badge">
    <div class="rcja-badge-val">120</div>
    <div class="rcja-badge-label">seconds per run</div>
  </div>
</div>

<table class="map-table">
  <thead>
    <tr>
      <th>micro:bit capability</th>
      <th>What it does in the competition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IR tracking sensors (via carrier board)</td>
      <td>Reads the black line on the white tile; the robot follows it autonomously</td>
    </tr>
    <tr>
      <td>Ultrasonic sensor (via carrier board)</td>
      <td>Detects obstacles ahead; triggers avoidance and locates the rescue capsule inside the spill</td>
    </tr>
    <tr>
      <td>DC motors (via carrier board)</td>
      <td>Drives two wheels independently for straight lines, turns, and ramp climbs up to 20°</td>
    </tr>
    <tr>
      <td>Button A + downloaded program</td>
      <td>The Robot Handler presses a button to start the run. Competition rules require this; no laptops at the field</td>
    </tr>
    <tr>
      <td>LED display</td>
      <td>Shows the robot's current state during the run; referees and coaches can see what the robot is "thinking"</td>
    </tr>
  </tbody>
</table>

<div class="photo-row">
  <div class="diagram-slot" id="photo-motorbit-kit">
    <!-- Replace with a real photo: <img src="assets/photos/motorbit-kit.jpg" alt="Elecfreaks motor:bit kit parts"> -->
    <img src="assets/motorbit-parts.svg" alt="motor:bit kit parts — diagram showing micro:bit, motor:bit carrier board, TT motors, IR tracking sensor, ultrasonic sensor, battery pack, wheels, and castor">
  </div>
  <div class="diagram-slot" id="photo-motorbit-assembled">
    <!-- Replace with a real photo: <img src="assets/photos/motorbit-assembled.jpg" alt="Assembled motor:bit robot"> -->
    <img src="assets/motorbit-robot.svg" alt="assembled motor:bit robot — top-down diagram showing ultrasonic sensor at front, IR sensors, micro:bit, motor:bit board, battery pack, and two drive wheels">
  </div>
</div>

<div class="callout">
  <strong>The kit:</strong> Individual components — a micro:bit, an Elecfreaks motor:bit carrier board, two TT motors, a 2-channel IR tracking module, an ultrasonic sensor, and a 4×AA battery pack. The carrier board plugs directly onto the micro:bit edge connector.
</div>
