---
id: s-robocup
nav: RoboCup
label: Real-world context
title: "Where it goes next: RoboCup Junior"
---

Everything in this workshop maps directly to a real competition. RoboCup Junior Rescue Line gives students a concrete goal that exercises every micro:bit capability at once. The skills are the same; the stakes are real.

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
  <div class="photo-slot" id="photo-motorbit-kit">
    <!-- Replace with: <img src="assets/photos/motorbit-kit.jpg" alt="Elecfreaks motor:bit kit parts"> -->
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="7" width="20" height="10" rx="1"/><circle cx="6" cy="17" r="2"/><circle cx="18" cy="17" r="2"/><line x1="6" y1="7" x2="6" y2="4"/><line x1="18" y1="7" x2="18" y2="4"/></svg>
    <span>Photo: motor:bit kit (parts laid out)</span>
  </div>
  <div class="photo-slot" id="photo-motorbit-assembled">
    <!-- Replace with: <img src="assets/photos/motorbit-assembled.jpg" alt="Assembled motor:bit robot"> -->
    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="6" width="18" height="12" rx="1"/><circle cx="7" cy="18" r="2"/><circle cx="17" cy="18" r="2"/><rect x="8" y="9" width="8" height="5" rx="0"/></svg>
    <span>Photo: assembled robot (ready to run)</span>
  </div>
</div>

<div class="callout">
  <strong>The kit:</strong> Elecfreaks motor:bit smart car. Two TT motors, a 2-channel IR tracking module, an ultrasonic sensor, and a carrier board that plugs directly onto the micro:bit edge connector. Under $100 complete.
</div>
