---
id: s-robocup
nav: RoboCup Junior
label: Real-world context
title: RoboCup Junior Rescue Line
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

Each micro:bit capability from this workshop becomes a hands-on activity when building a competition robot. The activities below match what students build in the coding session.

<div class="activity-grid">

  <div class="activity-card">
    <div class="activity-num">Activity 1</div>
    <div class="activity-title">Line following</div>
    <div class="activity-cap">IR tracking sensors via carrier board · P3 and P4</div>
    <div class="activity-desc">Two IR sensors read the black line on the white tile. When one sensor leaves the line the robot steers back. This is the core loop that runs for the whole course.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Activity 2</div>
    <div class="activity-title">Obstacle avoidance</div>
    <div class="activity-cap">Ultrasonic sensor via carrier board</div>
    <div class="activity-desc">The ultrasonic sensor measures distance ahead. When an obstacle is detected the robot drives around it and reacquires the line within 30 cm.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Activity 3</div>
    <div class="activity-title">Push rescue</div>
    <div class="activity-cap">Ultrasonic sensor · DC motors via carrier board</div>
    <div class="activity-desc">The robot detects the silver capsule inside the chemical spill zone using the ultrasonic sensor, then drives forward to push it clear. Worth 50 points — the highest single scoring action.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Activity 4</div>
    <div class="activity-title">Autonomous start</div>
    <div class="activity-cap">Button A · downloaded program</div>
    <div class="activity-desc">Competition rules require the robot to start from a button press on the board. The Robot Handler presses Button A to begin the run. No laptops, phones, or remote controls at the field.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Activity 5</div>
    <div class="activity-title">Status display</div>
    <div class="activity-cap">5×5 LED display</div>
    <div class="activity-desc">The LED display shows the robot's current state during the run. Referees and coaches can see what mode the robot is in — following, avoiding, rescuing — without stopping it.</div>
  </div>

</div>

<div class="photo-row">
  <div class="diagram-slot" id="photo-motorbit-kit">
    <img src="https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/6zRKrvw.jpg" alt="Elecfreaks motor:bit carrier board">
  </div>
  <div class="diagram-slot" id="photo-motorbit-assembled">
    <img src="https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/5ayGCgd.png" alt="micro:bit inserted into the motor:bit carrier board">
  </div>
</div>

<div class="callout">
  <strong>The kit:</strong> Individual components — a micro:bit, an Elecfreaks motor:bit carrier board, two TT motors, a 2-channel IR tracking module, an ultrasonic sensor, and a 4×AA battery pack. The carrier board plugs directly onto the micro:bit edge connector.
</div>
