---
id: s-robocup
nav: RoboCup Junior
label: Real-world context
title: Skills for any RoboCup Junior competition
---

The micro:bit skills covered in this workshop apply across all RoboCup Junior competitions. Each competition uses different rules and scoring, but the underlying building blocks are the same: reading sensors, controlling motors, making decisions in code, and starting the robot autonomously.

<div class="rcja-banner">
  <div>
    <div class="rcja-title">RoboCup Junior Australia</div>
    <div class="rcja-sub">An international robotics competition for students up to 19 years old. Teams design, build, and program autonomous robots. No remote controls. Australia runs national qualifiers and sends teams to the World Championship.</div>
  </div>
  <div class="rcja-badge">
    <div class="rcja-badge-val">4</div>
    <div class="rcja-badge-label">competitions</div>
  </div>
</div>

<!-- SLIDE_BREAK -->

<div class="activity-grid">

  <div class="activity-card">
    <div class="activity-title">Rescue Line</div>
    <div class="activity-cap">Sensors · Motors · Decisions</div>
    <div class="activity-desc">An autonomous robot follows a black line on white tiles, avoids obstacles, climbs ramps, and rescues a victim from a marked zone. IR sensors detect the line; the micro:bit decides when to steer, avoid, and stop.</div>
  </div>

  <div class="activity-card">
    <div class="activity-title">Rescue Maze</div>
    <div class="activity-cap">Sensors · Motors · Navigation</div>
    <div class="activity-desc">The robot navigates a maze of black walls to find and rescue victims. No line to follow; the robot uses distance sensors and dead-reckoning to map and traverse the maze autonomously.</div>
  </div>

  <div class="activity-card">
    <div class="activity-title">OnStage</div>
    <div class="activity-cap">LED · Sound · Choreography</div>
    <div class="activity-desc">A robot or robotic creation performs a 2-minute choreographed routine on a stage. The micro:bit's speaker, LED matrix, and radio make it useful for coordinated multi-robot or prop-based performances.</div>
  </div>

  <div class="activity-card">
    <div class="activity-title">Soccer</div>
    <div class="activity-cap">IR ball sensing · Motors · Strategy</div>
    <div class="activity-desc">Two robots per team play autonomous soccer. They must detect the infrared ball, navigate the field, and score goals. Motor control, sensor reading, and game-state logic are all needed.</div>
  </div>

</div>

This workshop uses Rescue Line as the worked example because the kit maps directly to it: IR sensors for line detection, DC motors for driving, and the micro:bit making all decisions. Students who complete this workshop have the core skills to enter any competition.

<!-- SLIDE_BREAK -->

<div class="photo-row">
  <div class="diagram-slot" id="photo-motorbit-kit">
    <img src="https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/6zRKrvw.jpg" alt="Elecfreaks motor:bit carrier board">
  </div>
  <div class="diagram-slot" id="photo-motorbit-assembled">
    <img src="https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/5ayGCgd.png" alt="micro:bit inserted into the motor:bit carrier board">
  </div>
</div>

<div class="callout">
  <strong>Rescue Line at a glance:</strong> 120-second autonomous run. The robot follows a black line on white tiles, navigates ramps and gaps, avoids obstacles placed on the course, and rescues a small victim from a marked zone. Scored on each element completed. No remote control allowed once the run starts.
</div>

<div class="activity-grid">

  <div class="activity-card">
    <div class="activity-num">Core skill 1</div>
    <div class="activity-title">Line following</div>
    <div class="activity-cap">IR tracking sensors · P3 and P4</div>
    <div class="activity-desc">Two IR sensors read the black line on the white tile. When one sensor leaves the line the robot steers back. This is the core loop that runs for the whole course.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Core skill 2</div>
    <div class="activity-title">Obstacle avoidance</div>
    <div class="activity-cap">Ultrasonic sensor via carrier board</div>
    <div class="activity-desc">The ultrasonic sensor measures distance ahead. When an obstacle is detected the robot drives around it and reacquires the line within 30 cm.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Core skill 3</div>
    <div class="activity-title">Victim rescue</div>
    <div class="activity-cap">Ultrasonic sensor · DC motors</div>
    <div class="activity-desc">The robot detects the victim inside the rescue zone using the ultrasonic sensor, then drives forward to push it clear. Worth 50 points: the highest single scoring action in a run.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Core skill 4</div>
    <div class="activity-title">Autonomous start</div>
    <div class="activity-cap">Button A · downloaded program</div>
    <div class="activity-desc">Competition rules require the robot to start from a button press on the board. The Robot Handler presses Button A to begin. No laptops, phones, or remote controls at the field.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Core skill 5</div>
    <div class="activity-title">Status display</div>
    <div class="activity-cap">5x5 LED display</div>
    <div class="activity-desc">The LED display shows the robot's current state during the run: following, avoiding, rescuing. Referees and coaches can see what mode it is in without stopping the robot.</div>
  </div>

  <div class="activity-card">
    <div class="activity-num">Core skill 6</div>
    <div class="activity-title">Ramp detection</div>
    <div class="activity-cap">Accelerometer</div>
    <div class="activity-desc">The accelerometer reads the board's tilt angle. Teams use this to detect when the robot is on a ramp and switch to a different motor speed or control strategy for the climb.</div>
  </div>

</div>
