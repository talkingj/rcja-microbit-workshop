---
id: s-robocup
nav: RoboCup Junior
label: Real-world context
title: Skills for any RoboCup Junior competition
---

The micro:bit skills covered in this workshop apply across all RoboCup Junior competitions. Each competition uses different rules and scoring, but the underlying building blocks are the same: reading sensors, controlling motors, making decisions in code, and starting the robot autonomously.

<!-- RCJA_BANNER
title: RoboCup Junior Australia
sub: An international robotics competition for students up to 19 years old. Teams design, build, and program autonomous robots. No remote controls. Australia runs national qualifiers and sends teams to the World Championship.
count: 4
count_label: competitions
-->

<!-- SLIDE_BREAK -->

<!-- ACTIVITY_CARDS
- title: Rescue Line
  icon: lines
  cap: "Sensors · Motors · Decisions"
  desc: Follow a black line on white tiles, avoid obstacles, climb ramps, and rescue a victim. IR sensors track the line while the micro:bit steers and decides.
- title: Rescue Maze
  icon: wall
  cap: "Sensors · Motors · Navigation"
  desc: Navigate a maze of black walls to find and rescue victims. Distance sensors and dead-reckoning replace line following.
- title: OnStage
  icon: speaker
  cap: "LED · Sound · Choreography"
  desc: Perform a 2-minute choreographed routine on stage. The micro:bit's speaker, LEDs, and radio coordinate multi-robot performances.
- title: Soccer
  icon: soccer-ball
  cap: "IR ball · Motors · Strategy"
  desc: Two robots per team play autonomous soccer — detect the IR ball, navigate the field, and score goals.
-->

This workshop uses Rescue Line as its worked example — the kit maps directly to it. Students who complete the workshop have the core skills to enter any competition.

<!-- SLIDE_BREAK -->

<!-- PHOTO_ROW
- url: "https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/6zRKrvw.jpg"
  alt: Elecfreaks motor:bit carrier board
  id: photo-motorbit-kit
- url: "https://wiki-media-ef.oss-cn-hongkong.aliyuncs.com/i18n/en/docusaurus-plugin-content-docs/current/microbit/expansion-board/images/5ayGCgd.png"
  alt: micro:bit inserted into the motor:bit carrier board
  id: photo-motorbit-assembled
-->

> **Rescue Line at a glance:** 120-second autonomous run. The robot follows a black line on white tiles, navigates ramps and gaps, avoids obstacles placed on the course, and rescues a small victim from a marked zone. Scored on each element completed. No remote control allowed once the run starts.

<!-- ACTIVITY_CARDS
- title: Line following
  num: Core skill 1
  icon: ir-sensor
  cap: "IR sensors · P3 and P4"
  desc: Two IR sensors read the black line. When one leaves the line the robot steers back. This loop runs for the whole course.
- title: Obstacle avoidance
  num: Core skill 2
  icon: ultrasonic
  cap: Ultrasonic sensor
  desc: Measures distance ahead. When an obstacle is detected, drive around it and reacquire the line within 30 cm.
- title: Victim rescue
  num: Core skill 3
  icon: goal
  cap: "Ultrasonic · DC motors"
  desc: Detect the victim in the rescue zone and push it clear. Worth 50 points — the highest single scoring action.
- title: Autonomous start
  num: Core skill 4
  icon: buttons
  cap: "Button A · downloaded program"
  desc: Rules require a button press to start. No laptops, phones, or remote controls at the field.
- title: Status display
  num: Core skill 5
  icon: led-matrix
  cap: 5×5 LED display
  desc: Show the current mode — following, avoiding, rescuing — so referees and coaches can see state without stopping the robot.
- title: Ramp detection
  num: Core skill 6
  icon: accelerometer
  cap: Accelerometer
  desc: Read the board's tilt angle to detect ramps and switch to a different motor speed for the climb.
-->
