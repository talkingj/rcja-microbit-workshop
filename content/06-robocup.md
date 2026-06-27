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
  cap: "Sensors \xB7 Motors \xB7 Decisions"
  desc: An autonomous robot follows a black line on white tiles, avoids obstacles, climbs ramps, and rescues a victim from a marked zone. IR sensors detect the line; the micro:bit decides when to steer, avoid, and stop.
- title: Rescue Maze
  cap: "Sensors \xB7 Motors \xB7 Navigation"
  desc: The robot navigates a maze of black walls to find and rescue victims. No line to follow; the robot uses distance sensors and dead-reckoning to map and traverse the maze autonomously.
- title: OnStage
  cap: "LED \xB7 Sound \xB7 Choreography"
  desc: "A robot or robotic creation performs a 2-minute choreographed routine on a stage. The micro:bit's speaker, LED matrix, and radio make it useful for coordinated multi-robot or prop-based performances."
- title: Soccer
  cap: "IR ball sensing \xB7 Motors \xB7 Strategy"
  desc: Two robots per team play autonomous soccer. They must detect the infrared ball, navigate the field, and score goals. Motor control, sensor reading, and game-state logic are all needed.
-->

This workshop uses Rescue Line as the worked example because the kit maps directly to it: IR sensors for line detection, DC motors for driving, and the micro:bit making all decisions. Students who complete this workshop have the core skills to enter any competition.

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
  cap: "IR tracking sensors \xB7 P3 and P4"
  desc: Two IR sensors read the black line on the white tile. When one sensor leaves the line the robot steers back. This is the core loop that runs for the whole course.
- title: Obstacle avoidance
  num: Core skill 2
  cap: Ultrasonic sensor via carrier board
  desc: The ultrasonic sensor measures distance ahead. When an obstacle is detected the robot drives around it and reacquires the line within 30 cm.
- title: Victim rescue
  num: Core skill 3
  cap: "Ultrasonic sensor \xB7 DC motors"
  desc: The robot detects the victim inside the rescue zone using the ultrasonic sensor, then drives forward to push it clear. Worth 50 points, the highest single scoring action in a run.
- title: Autonomous start
  num: Core skill 4
  cap: "Button A \xB7 downloaded program"
  desc: Competition rules require the robot to start from a button press on the board. The Robot Handler presses Button A to begin. No laptops, phones, or remote controls at the field.
- title: Status display
  num: Core skill 5
  cap: 5x5 LED display
  desc: "The LED display shows the robot's current state during the run: following, avoiding, rescuing. Referees and coaches can see what mode it is in without stopping the robot."
- title: Ramp detection
  num: Core skill 6
  cap: Accelerometer
  desc: The accelerometer reads the board's tilt angle. Teams use this to detect when the robot is on a ramp and switch to a different motor speed or control strategy for the climb.
-->
