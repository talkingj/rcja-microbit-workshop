# RoboCup Junior Australia — Soccer Rules 2026

**Version 26.0** · Last modified 17 February 2026

> Source: *RCJA Soccer Rules 2026* (PDF). This markdown is a faithful transcription of the official document for easier searching and reference. If anything here conflicts with the official PDF, the PDF prevails.

---

## Preface notes

**Spirit.** It is expected that all participants, students and mentors will respect the aims and ideals of RoboCup Junior as set out in the mission statement. In turn, the volunteers, referees and officials will act within the spirit of the event to ensure the event is competitive, fair and most importantly fun. "It is not whether you win or lose, but how much you learn that counts."

**Sharing.** It is the overall desire of RoboCup Junior events that any technological and curricular developments will be shared with other participants after the event. Any developments, including new technology and software examples, may be published on the RoboCup Junior website after the event. Participants are strongly encouraged to ask questions of their fellow competitors to foster a culture of curiosity and exploration.

**Local Variations.** These rules will be in use for the Australian National Championships for the titled year. State and Regional events may implement minor variations with respect to age groups, divisions and judging, communicated to participants prior to the event.

**General Rules.** All RoboCup Junior challenges are governed by the General Rules, covering rules consistent across all challenges (team make-up, robot configuration and more). These can be downloaded from the Soccer Challenge Page on the RCJA website.

**Notes/Advice vs. Rules.** This document includes notes/advice plus firm rules. Advice is noted in green in the original; rule changes for the new year are noted in red.

---

## Change Log

**Revision 26.0 — Initial release for the season.** Key changes from 2025:

**General changes**

- Height requirement changed to 220 mm high above the playing field for all divisions (section 2.2.2).
- Added colour examples for the goals (section 2.3.4).
- Merged the ball-out-of-play rules for Simple Simon and Standard Leagues (section 5.9.1).
- Specified that the "forcing" rule takes priority over multiple defence (section 5.11) where a robot with the ball forces two opposing robots to do so (section 5.6.1.4).
- Clarified that the measuring cylinder is what is being rotated, not the robot itself (section 4.1.2).
- Added that cameras need to be calibrated and built to prevent interference from outside the field (section 2.5.1).
- Added that robots should not emit sounds from speakers or buzzers (section 5.7.1.7), but speakers can be used only for debugging (section 4.5.8).
- Changes to electronic submission requirements (section 7.4).

**Standard League**

- Clarified that omni wheels can be made from any material if it is only for the omniwheel; the wheel axle still needs to be a LEGO axle (section 4.5.5).

**Lightweight League**

- The ball for Lightweight will change in 2027 to the same ball internationals use (section 3.3).

---

## 1. Preface

**1.1** In Soccer, students are required to design, build and program robots to compete in a dynamic game of robot soccer against an opposing pair of robots. The robots are autonomously run during gameplay. They detect a ball and score goals on a green carpet playing field.

**1.2** There are four Soccer leagues. All leagues are open to teams of any age (primary and secondary school age).

- **Simple Simon League** — a beginner league played using a ball that emits infrared signals. Robots may weigh up to 1.0 kg and are limited to LEGO parts and an IR sensor. Teams can only participate in Simple Simon for up to 2 years.
- **Standard League** — played using a ball that emits infrared signals. Robots may weigh up to 1.0 kg and are limited to LEGO parts and a list of other third-party sensors.
- **Lightweight League** — a mid-level league played using a ball that emits infrared signals. Robots may weigh up to 1.4 kg and are not limited in components used.
- **Open League** — a high-level league played using an orange coloured ball. Robots may weigh up to 2.5 kg.

**1.3** Subject to age limitations and other criteria, teams who perform well in the National Event may qualify for the annual RoboCup Junior International Event:

- Lightweight League teams may qualify for RCJ Soccer Lightweight.
- Open League teams may qualify for RCJ Soccer Open.

Other international events may have other divisions/qualification requirements.

---

## 2. Playing Field

### 2.1 Floor

**2.1.1** The field has 50 mm thick white lines 250 mm from the walls on every side, which form the border of the out area (exclusive of the white lines). The floor is green or charcoal coloured carpet with neutral points and penalty boxes marked with 25 mm thick black lines.

**2.1.2** The field should be placed so that it is flat and level. The out areas of the field may be either flat or inclined by raising the outside of the field by 10 mm (the incline should allow the ball to roll from the top of the incline to the centre of the playing area).

**2.1.3** The field must be a carpet base. The recommended carpet is 3–5 mm thick green or charcoal coloured carpet.

> *Advice:* The Gen2 vinyl mat can be used as a practice mat.

**2.1.4** The field may be placed on a wooden or plastic table or on the floor.

**2.1.5** All dimensions of the field have a tolerance of 5%.

> *Note:* While all efforts will be made to construct the fields precisely, robots should be designed to allow for this tolerance.

### 2.2 Walls

**2.2.1** Matte black walls are placed all around the field, including behind the goals.

**2.2.2** Walls are 220 mm high above the playing field. In Simple Simon, Standard and Lightweight Leagues, the walls are at least 100 mm high above the playing field.

**2.2.3** In Open League, the walls are at least 220 mm high above the playing field.

> *Note:* The 220 mm wall height is only required for the Australian National Championships. State challenges are not required to follow this with their field construction.

### 2.3 Goals

**2.3.1** The internal width of each goal is 450 mm.

**2.3.2** The internal depth of each goal is 74 mm.

**2.3.3** Each goal will have a crossbar 140 mm above the playing surface. The depth of the crossbar is a maximum of 20 mm to avoid covering the top of the goal.

**2.3.4** The back and sides of one goal's interior, as well as the crossbar, are painted matte similar to CMYK cyan (like Dulux Striking Cyan). The back and sides of the interior of the other goal, as well as the crossbar, are painted matte similar to CMYK yellow (like Dulux Dandelion Yellow). The external sides of the goals are painted matte black.

**2.3.5** The surface within the goal area is flat and level (horizontal).

**2.3.6** The sidewalls of the goals extend to the end wall to prevent the ball from rolling behind the goals.

### 2.4 Neutral Points

**2.4.1** There are two neutral points, as shown on the field diagram in section 2.1.

**2.4.2** A neutral point is also designated in the middle of the field. This is only used for starting games and placing the ball after multiple calls of lack of progress, or if all other neutral points are occupied.

### 2.5 Lighting and Magnetic Conditions

**2.5.1** Teams must come prepared to calibrate their robots based on the lighting and magnetic conditions at the venue. It is recommended that teams design their robots to cope with variations in lighting and magnetic conditions, as these vary from venue to venue. Teams with vision systems should also be calibrated and constructed in a way to minimise interference from outside the field.

> *Note:* At the Australian Open, all fields will be raised off the floor by at least 450 mm to minimise magnetic interference.

---

## 3. Ball

### 3.1 Specification

**3.1.1** For Simple Simon, Standard and Lightweight Leagues, an infrared ball will be used. See Appendix A.

**3.1.2** For Open League, a passive orange golf ball will be used. See Appendix B. Purchasing the passive ball via the RCJA Store is recommended.

**3.1.3** If the infrared ball has a fast-flashing LED (indicating low battery power), the batteries or the ball shall be replaced prior to the start of the game or at the earliest stoppage in play. Match timing shall be paused while the issue is rectified.

### 3.2 Ball Suppliers

**3.2.1** The official infrared balls for all RCJA tournaments will be the Elekit RCJ-05 soccer ball available from Modern Teaching Aids.

> *Note:* The older, dark-grey coloured infrared ball previously sold by HiTechnic, or approved open-source alternatives, as they come available, is also acceptable.

**3.2.2** A passive orange ball that suits the requirements set out in the Ball Specification document (see Rule 3.1.2) will be used for the Open League.

### 3.3 Lightweight Ball Change 2027

Starting in 2027, Lightweight Soccer will move to a new IR ball. The key difference is the size change from 74 mm to 42 mm diameter, the same as Open League's orange passive ball. Simple Simon and Standard Leagues will continue to use the large infrared ball (3.1.1). Due to its orange colour and size, this ball can also be used for Open League. The ball is open source — anyone can produce one from the files and instructions on GitHub: <https://github.com/robocup-junior/ir-golf-ball>.

> *Note:* The new IR ball can be purchased from the RCJA website store: <https://www.robocupjunior.org.au/product/2027-lightweight-soccer-small-ir-ball/>

---

## 4. Robots

### 4.1 Dimensions

**4.1.1** A robot's dimensions and characteristics must not exceed the following limits:

| Limit | Rule | Simple Simon | Standard | Lightweight | Open |
|---|---|---|---|---|---|
| Diameter | 4.1.2 | 220 mm | 220 mm | 220 mm | 220 mm |
| Height | — | 220 mm | 220 mm | 220 mm | 220 mm |
| Weight | — | 1.0 kg | 1.0 kg | 1.4 kg | 2.5 kg |
| Ball capture zone | 4.6 | 30 mm | 30 mm | 30 mm | 15 mm |
| Voltage | 4.1.4 | Limited to the rechargeable LEGO battery | Limited to the rechargeable LEGO battery | 48 V DC / 25 V AC RMS | 48 V DC / 25 V AC RMS |

**4.1.2** A robot, as positioned in gameplay, must rotate freely within an upright 220 mm diameter cylinder and pose little or no resistance to it. Each robot, in its gameplay configuration, must fit within a vertical cylinder with a diameter of 220 mm. The cylinder must be able to rotate freely around the robot and encounter no significant resistance.

**4.1.3** While being inspected, each robot must be positioned as it will be in gameplay and at its maximum size — anything that protrudes from the robot must be fully extended. If a robot has a moving part that extends in two directions, it will be inspected with this part operating. The robot must be able to operate without touching the measuring cylinder.

> *Note:* It is recommended to design your robot to a smaller size, such as 210 mm, to allow for tolerances.

**4.1.4** In Lightweight and Open Leagues, no voltage on a robot should exceed 48 V DC or 25 V AC RMS at any point and at any time. This refers to the maximum voltage, not the nominal voltage, and includes voltage pumps used for a kicker (see kicker limitations).

### 4.2 Control

**4.2.1** Robots must be controlled autonomously.

**4.2.2** Robots must be able to be started manually. Robots cannot be started from a secondary device, such as a laptop, tablet or mobile phone. Robots must have their program downloaded to them and be able to be started/restarted manually by the Robot Handler.

**4.2.3** The use of remote control of any kind is not allowed.

**4.2.4** Robots must be able to drive in all directions.

**4.2.5** Communication between robots is acceptable as long as it does not interfere with the performance of other robots, is not detectable outside the venue, and complies with local regulations regarding frequency use and safety.

> *Advice:* Teams should perform checks on messages sent between robots. For example, prepend a unique string to a message and check that the string exists, to reduce the possibility of receiving interfering messages from other teams.

**4.2.6** Robots must have the ability to have their communication disabled at the request of the referee.

### 4.3 Marking/Colouring

**4.3.1** Competitors must mark or decorate their robots to identify them as belonging to the same team. These must not influence gameplay and will not be considered in the height restrictions.

**4.3.2** Colours of robots and/or light transmitters must not interfere with the sensor readings of other robots.

> *Advice:* In Lightweight and Open, avoid having cyan, yellow or orange visible on the outside of the robot as it may interfere with other robots using cameras.

### 4.4 Number of Robots

**4.4.1** All teams shall consist of no more than two (2) robots. Any substitution of extra robots during a tournament is forbidden, and disqualification will result. Teams cannot enter the competition venue with more than two constructed robots.

### 4.5 Construction

**4.5.1** A robot must be constructed with the following parts:

| Item | Rule | Simple Simon & Standard | Lightweight & Open |
|---|---|---|---|
| Construction | 4.5.2 | Unmodified LEGO-branded pieces, motors and sensors | Any material or building block, commercial or raw, provided the robot fits the specifications and is primarily and substantially the competitors' original work. Any number of cameras; all commercial lenses and cameras permitted |
| Third party IR sensors | 4.5.3 | Allowed if on the allowed list | — |
| Gyro and compass sensors | 4.5.4 | Not allowed (Simple Simon); allowed (Standard) | Allowed |
| Omni-wheels | 4.5.5 | Not allowed (Simple Simon); allowed with max 80 mm diameter (Standard) | Allowed |
| Other materials | 4.5.6 | No other building materials (glue, tape, screws, etc.) | — |

**4.5.2** For Simple Simon and Standard Leagues, all parts used in the robot construction (other than allowed exceptions) must be strictly LEGO-brand pieces, motors and sensors.

**4.5.3** For Simple Simon and Standard Leagues, only sensors on the official list at <https://www.robocupjunior.org.au/soccer/sensors/> are allowed.

**4.5.4** For Simple Simon League only, built-in or external compass or gyro sensors are not permitted.

**4.5.5** For Standard League only, any non-LEGO omni-directional wheels can be used. The wheels must have a maximum diameter of 80 mm and may be custom manufactured from any material; however, the structural axle connecting the wheel to the robot must be an unmodified LEGO piece.

**4.5.6** Cable ties or tape may be used as a handle or to secure wires, but must not be part of robot construction.

**4.5.7** All robots must have a stable and easily noticeable handle to hold and lift them. The handle must be easily accessible and allow the robot to be picked up from at least 50 mm above the highest structure of the robot. The handle's dimensions may exceed the robot height limit, but the part exceeding this limit cannot be used to mount components.

> *Advice:* Cable ties make a strong lightweight handle.

**4.5.8** Robots can be built with a speaker for emitting noises like music or beeps if it is only used for debugging. Any use of the speaker during gameplay will have the robot deemed "damaged" per section 5.7.1.7.

### 4.6 Ball Capturing Zones and Movement

**4.6.1** Ball Capturing Zones are defined as any internal space created when a straight edge is placed on the protruding points of a robot.

**4.6.2** The ball cannot penetrate the Ball Capturing Zone by more than the limit specified in rule 4.1.1.

**4.6.3** A robot cannot "hold" a ball. Holding means taking full control of the ball by removing all of its degrees of freedom — e.g. fixing it to the robot's body, surrounding it, encircling it, or otherwise trapping it. If a ball stops rolling while a robot is moving, or does not rebound when rolled into a robot, it is a good indication the ball is trapped.

**4.6.4** The ball cannot be held underneath a robot.

**4.6.5** In Simple Simon and Standard Leagues, the use of a dribbler is not allowed. A dribbler is a rotating drum or wheel that imparts dynamic backspin on the ball to keep it on its surface.

**4.6.6** In Lightweight and Open Leagues, a dribbler is allowed and is the only exception to rule 4.6.3. The dribbler must comply with rules 4.6.2 and 4.6.4. A robot using a dribbler must release the ball in order to score a goal.

### 4.7 Kickers (Lightweight and Open Leagues Only)

> In 2025 the General Rules were introduced. Part of this section has been relocated to the General Rules for consistency across all challenges. Please read the General Rules, available from the Soccer Challenge Page.

**4.7.1** A robot's kicker cannot exceed a certain power. Kicker power is measured by an on-field test using the tournament ball for the relevant division. The test places the robot inside the left corner of a goal and performs a kick into the opposing goal. The test is passed if the ball bounces off the opposite goal and does not leave the penalty area of the opposing goal after bouncing back.

**4.7.2** Robots that exceed the limitations must decrease the power of, or disable, the kicker.

> *Advice:* Teams should build in the ability to adjust the power of a robot's kicker during the competition.

**4.7.3** Kicker power is subject to compliance check at any time during the competition, such as during scrutineering, before a half, or when a game is about to be restarted after a goal.

---

## 5. Game Play

### 5.1 Pre-game Setup

**5.1.1** Organisers will provide access to the competition area for calibration and testing prior to the competition, according to a schedule made available at the start of the event.

**5.1.2** Organisers will make every effort to allow at least 5 minutes of setup time before each game.

**5.1.3** This time is also for teams to express any concerns about the legality of opposing robots.

### 5.2 Length of Game

**5.2.1** The game consists of two 5-minute halves. Some competitions may choose to run 10-minute halves at the discretion of the tournament organising committee.

**5.2.2** There will be a 5-minute break between the halves.

**5.2.3** The game clock runs for the duration of the game without stopping, except as noted in Referee's Timeout (section 5.10.4).

**5.2.4** Teams can be penalised one goal per minute at the referee's discretion if they are late.

**5.2.5** If a team does not report within 10 minutes of the scheduled game time, they forfeit the game and the winning team is awarded a 10–0 score line. The 10 minutes includes any break times.

**5.2.6** A game ends when there is a goal difference of 10 goals. The losing team may elect to continue playing, but the recorded score (10-goal difference) will not change.

**5.2.7** Teams may elect to end a game early; however, they forfeit the game and the winning team is awarded a 10–0 score line.

### 5.3 Start of Game

**5.3.1** At the start of the first half, the referee tosses a coin, and the team first mentioned in the draw calls the coin while it is in the air.

**5.3.2** The winner of the toss can choose either (a) which end to kick to, or (b) to kick off first.

**5.3.3** The loser of the toss decides the other option.

**5.3.4** The team not kicking off in the first half will kick off to begin the second half.

### 5.4 Kick-Offs

**5.4.1** Each half of the game begins with a kick-off.

**5.4.2** All robots must be located on their defensive side of the field. Robots must not be moving.

**5.4.3** The ball is positioned by the referee in the centre of the field.

**5.4.4** The team kicking off places their robots on the field first. Robots cannot be moved once placed.

**5.4.5** All robots on the team not kicking off must have some part of the robot in the penalty box.

**5.4.6** On the referee's command, all robots will be started immediately by human team members.

**5.4.7** The robot kicking off must make a clear strike of the ball and it must roll clear of the robot by at least 50 mm, or the robot must start at least 50 mm from the ball. An illegal kick-off will result in the opposing team being granted the kick-off.

**5.4.8** Any robots started before the referee's command will be treated as damaged.

### 5.5 Scoring

**5.5.1** A goal is scored when the ball strikes the back wall of the goal. The referee will announce the goal.

**5.5.2** A goal will be awarded if a ball deemed to be travelling into the goal strikes a defensive robot that is touching the back wall of the goal.

> *Advice:* Robots should be built so that the crossbar prevents them from going inside the goal.

**5.5.3** After a goal is scored, a kick-off occurs. The non-scoring team is awarded the ball.

**5.5.4** "Own goals" will be treated as a goal to the opposition.

### 5.6 Lack of Progress

**5.6.1** The referee will call "Lack of Progress" in the following situations:

- **5.6.1.1** If no robot has any chance of locating the ball in a reasonable amount of time.
- **5.6.1.2** If the ball is stuck between multiple robots for a reasonable amount of time.
- **5.6.1.3** When a robot is using greater power to "force" the ball past an opposition robot that is in its penalty box. If a referee is slow to remove the ball and a goal is scored as a direct result of forcing the ball through, the goal will be disallowed.
- **5.6.1.4** When a robot with the ball is using greater power to "force" two opposing robots into their penalty box, causing both to go into a multiple defence situation (see 5.11). This rule takes priority over multiple defence.

**5.6.2** When "Lack of Progress" is called, the ball is first moved to the nearest neutral point. If this occurs again, the ball is moved to the centre of the field.

**5.6.3** When Lack of Progress is called, any stuck robots will be freed using minimal movement by the referee or team captains at the referee's request. Stuck robots should not be moved at any other time.

### 5.7 Damaged Robots

**5.7.1** The referee will deem a robot "damaged" in the following situations:

- **5.7.1.1** If a robot does not respond to the ball.
- **5.7.1.2** If a robot remains in the goal area for longer than 20 seconds, or is stuck against walls or goals, and shows no indication of returning to the playing area.
  > *Advice:* A small reverse command in a program will usually free a stuck robot.
- **5.7.1.3** If a robot turns over and is unable to move. This does not apply if the referee deems the robot tipped over after a collision with an opposition robot; it can then be righted by the referee and continue playing.
- **5.7.1.4** If a robot damages a ball or the field.
- **5.7.1.5** If two colliding robots damage a ball, both robots are deemed damaged.
- **5.7.1.6** In Lightweight and Open Leagues, if the whole of a robot enters the out area (fully enters the area between the walls and white line). Robots must attempt to stay on the playing field at all times. This does not apply if the referee deems the robot was pushed out by another robot or made an attempt to stay on the field; in that case the referee may slightly push the robot back onto the field at their discretion.
- **5.7.1.7** If a robot emits a noise from a speaker or buzzer.

**5.7.2** A damaged robot must remain off the field for at least thirty seconds (or one minute for ten-minute halves), or until a goal is scored.

**5.7.3** Damaged robot removal process:

- **5.7.3.1** In Simple Simon League, a team member may remove a damaged robot from the field at any time and must inform the referee when they do so.
- **5.7.3.2** In Standard, Lightweight and Open Leagues, a team member may only request removal of a damaged robot if the robot is not significantly involved in gameplay (i.e. not near or approaching the ball). They may only remove the robot after the referee gives approval.

**5.7.4** A damaged robot must be repaired and may be returned with the referee's permission. It will be placed on an unoccupied corner of the penalty box on the robot's defending side that does not advantage the robot, e.g. facing the ball.

> *Note:* Alternatively, the referee may instruct the team to place the robot on a neutral point if the penalty box is fully occupied, or to avoid a multiple defence situation. Goalies may be returned to the area in front of the goal without advantaging the robot.

**5.7.5** Play continues during removal, repair and replacement. The referee may choose to interrupt play if robot damage occurred because of a collision with an opposition robot.

**5.7.6** When a ball or the field is damaged, a yellow warning sticker is placed on the robot and the referee records the infringement on the scorecard. If two colliding robots damage a ball and the referee considers one robot significantly more aggressive, they may remove that robot from play.

**5.7.7** Adjustments must be made to the robot(s) to prevent damage to the ball or field from recurring.

**5.7.8** If a robot damages the ball or field again during the tournament, it will be disqualified from the tournament.

> *Note:* If a robot has the power to damage an officially accepted RoboCup Junior Soccer ball, it strongly indicates the robot was built with excessive power and the intention to damage other robots. Such a robot has not been built with the ideals of RCJA and fair competition in mind, and the tournament committee has every right to remove it from the competition.

### 5.8 Goalies

**5.8.1** If a goalie is used, it cannot limit its movement to a single direction on the field. It must be programmed to move in all directions.

**5.8.2** The goalie must respond to the ball in a forward direction in an attempt to intercept the ball ahead of the goal. If required, its movement should be able to take some part of the robot outside the penalty box (300 mm from the goal).

> *Note:* The goalie cannot respond sideways, followed by a forward movement.

**5.8.3** Failure to respond to the ball with a forward movement down the field will result in the robot being classified as "damaged" (see rule 5.7).

### 5.9 Ball Out of Play

**5.9.1** A ball is considered out of play as follows:

| League | Ball is out of play when… |
|---|---|
| Lightweight & Open | The ball leaves the playing area. |
| Standard & Simple Simon | If inclines are **not** used: the ball strikes any wall (including sides of the goals). If inclines **are** used: the ball strikes the back wall or sides of goals. |
| Simple Simon | The ball strikes the wall behind either goal. |

**5.9.2** After a ball is considered out of play, it is moved to the nearest neutral point.

### 5.10 Interruption of Game Play

**5.10.1** The situations in sections 5.6–5.9 may cause play to be interrupted, usually resulting in the ball being moved to the nearest neutral point while play continues.

**5.10.2** Play may also be stopped by the referee, but the game clock is not stopped unless at the referee's discretion. All robots must be stopped immediately and restarted from their penalty box.

**5.10.3** After a stoppage, play resumes on the referee's command and all robots start simultaneously.

**5.10.4** A referee may call "Referee's Timeout" for field repair, situations such as 5.7.1.3 or 5.12.3, or if the tournament referee is called for rule clarification. The referee can elect to stop the match clock if the stoppage is lengthy.

### 5.11 Multiple Defence

**5.11.1** Multiple Defence occurs if more than one robot from the defending side enters the penalty area, takes up a defensive position, and substantially affects the game.

**5.11.2** For a Multiple Defence, the robot having the least influence on play is moved to the centre of the field. Where a goalie is involved, the other player is moved.

### 5.12 Fouls

**5.12.1** If a robot uses a device or action that continuously attacks or charges a robot not in possession of the ball, the referee will call "Foul!". The robot is deemed damaged.

**5.12.2** If the robot continues to foul, it is permanently removed from the game, a yellow warning sticker is placed on the robot(s), and the referee records the infringement on the scorecard.

**5.12.3** If a robot is damaged by a foul, the referee stops the game and the clock for up to 2 minutes while repairs are made (see Referee's Timeout, 5.10.4).

**5.12.4** If a robot is removed from two games for fouling, it is disqualified from the tournament.

### 5.13 Free Kicks, Penalty Kicks and Offside

**5.13.1** There are no free kicks, penalty kicks or offside rules.

### 5.14 Humans

**5.14.1** In general, movement of robots by humans is not acceptable.

**5.14.2** Humans can only move robots at the instruction of the referee.

**5.14.3** Before each match, teams should designate one human as "Captain", allowed to place, remove and replace robots during the game, based on the rules and as directed by the referee.

**5.14.4** Other team members may start one robot, but afterwards must not be within the vicinity of the playing field. They must remain more than one metre from the field while the ball is in play, unless otherwise directed by the referee.

**5.14.5** If requested, team members starting the robots must be able to cover up any cyan, yellow or orange on their person or equipment that interferes with the other team's robot sensors (see also 4.3.2).

### 5.15 Selections for Finals

**5.15.1** During Round Robin play, teams are allocated three points for a win, one point for a tie and 0 points for a loss.

**5.15.2** Teams are ranked on the following criteria: total points, then total goals scored, then goal difference.

### 5.16 Finals

**5.16.1** At the National Events, final play-offs for 1st, 2nd, 3rd and 4th place will be conducted.

### 5.17 Tied Games

**5.17.1** In the event of a tie at full time during a non-finals game, the tied score is recorded.

**5.17.2** In the event of a tie at full time during a finals game, the following procedure applies:

- Game play is not stopped or interrupted.
- The game continues as "golden goal" — as soon as a goal is scored, the game ends.
- If after five minutes no additional goal has been scored, only one robot from each team is allowed on the field. Any team with two robots must pick one to take off; that robot is not allowed back on for the remainder of the game. "Golden goal" then continues.
- If after a further five minutes no team has scored a golden goal, the team ranked higher in the seeding is considered to have won.

---

## 6. Conflict Resolution

### 6.1 Referee

**6.1.1** During game play, the referee's decisions are final. Any argument with a referee's decision results in a yellow warning card. If argument continues, the referee gives a red card resulting in immediate forfeit of the game.

**6.1.2** If team captains are satisfied with the result of a game, they sign the score sheet at the conclusion of play.

**6.1.3** Any protest after the game should only be if the scoring is believed incorrect, or if a game result is in doubt. After signing the score sheet, no protests can be lodged.

### 6.2 Rule Clarification

**6.2.1** Rule clarification may be made by members of the RoboCup Junior Australia Technical Committee.

**6.2.2** If a rule clarification is needed, the referee should stop the game immediately, call referee's timeout (5.10.4), stop the clock, and confirm the ruling before continuing.

### 6.3 Special Circumstances

**6.3.1** Specific modifications to the rules for special circumstances — such as unforeseen problems and/or capabilities of a team's robots — may be agreed at the time of the tournament, provided a majority of the contestants agree.

---

## 7. Inspection

### 7.1 Scrutineering

**7.1.1** All robots will be examined by a panel of referees before the start of each day of the tournament to ensure they meet all constraints in section 4.

**7.1.2** It is the responsibility of teams to have their robots re-inspected if modified at any time during the tournament, including damage or changes during game play. Any team deemed to have an illegal robot following a game will forfeit that game.

**7.1.3** Any violations of the inspection rules will prevent that robot from competing until modifications are made.

**7.1.4** Modifications must be made within the tournament schedule, and teams must not delay game play while making them.

**7.1.5** The inspection may include, but is not limited to, checking the size, weight, ball capture zone depth, maximum voltage and kicker power of each robot.

### 7.2 Team Interviews

**7.2.1** All teams will be interviewed by a panel selected by the Technical Committee over the course of the competition, preferably on the first day if the event spans multiple days, to ensure robots meet all constraints in section 7.3.

**7.2.2** Tournament organisers are expected to conduct verification interviews prior to the finals of all events.

**7.2.3** Photos of the team's robots will be taken during the interview process and added to the Official RCJA Soccer Robot Database, to ensure robots are not handed down from team to team. If robots are not substantially the original work of the team members, the team will be disqualified.

**7.2.3** *(numbering as in the source)* Teams are to submit an electronic journal, logbook or technical description paper of their journey designing, programming and testing the robots, as described in section 7.4.

### 7.3 Robot Construction

**7.3.1** Construction and programming of robots must be performed exclusively by the competitors.

**7.3.2** Competitors will be interviewed to explain the operation of their robots, to verify the construction and programming is their own work.

**7.3.3** Competitors will be asked about their preparation efforts and may be requested to answer surveys and participate in recorded interviews for research purposes.

**7.3.4** Commercial kits may be used but must be substantially modified by the competitors.

**7.3.5** Proof of a full understanding of the program must be shown.

**7.3.6** If there is excessive mentor assistance, or the work is not substantially original work by the competitors, the team will be disqualified. Referees may request Technical Committee support during the competition if there are concerns that excessive mentoring may have occurred.

### 7.4 Electronic Submission

Each team is expected to submit two (2) digital elements prior to competition, based on dates provided by the organisers: (a) Annotated Code, and (b) Digital Poster.

#### 7.4.1 Annotated Code Submission

**7.4.1.1** Teams must submit a copy of the most recent version of their competition code. The code must be clearly annotated with comments explaining the purpose and function of key sections, including (where applicable) sensor use, decision-making logic and actuator control.

> *Note:* Teams may continue updating their code after the submission deadline but must maintain an up-to-date version of their annotated code. Students may be asked to show this updated code to judges on request.

**7.4.1.2** The submitted code must accurately reflect the robot used in competition.

**7.4.1.3** Teams who fail to submit their annotated code will not be permitted to compete.

> *Note:* This can be submitted as a PowerPoint, screenshots with annotations, document, etc.

#### 7.4.2 Digital Technical Poster Submission

**7.4.2.1** Each team must submit one (1) poster communicating their team and robot design if the team wishes to be considered for special awards.

> *Note:* This poster may be shared publicly. Teams must not include information that can't be publicly shared (e.g. student personal information other than first name, photos that allow personal identification, etc.).

**7.4.2.2** The poster must be A3 size and must include all of the following: (1) Team name; (2) Team member first names and roles; (3) One interesting/innovative feature of the robot's design or engineering; (4) A challenge encountered during development and how it was overcome; (5) What the team has learned through participation.

**7.4.2.3** The poster must be clear, well-presented and suitable for display. Teams may use any software (PowerPoint, Canva, Paint, etc.) or make a physical poster and submit a photo/scan. The poster must be the team's own original work.

**7.4.2.4** Teams who fail to submit a poster will not be eligible for special awards.

> *Note:* Teams are encouraged to bring a physical copy of their poster to display at the competition, though this is not mandatory.

---

## Appendix A: Specification for Infrared Soccer Ball

*(Simple Simon, Standard and Lightweight Leagues)*

**A.1 Ball suppliers**

**A.1.1** The official infrared balls for all RCJA tournaments will be the Elekit RCJ-05 soccer ball available from Modern Teaching Aids.

> *Note:* The older, dark-grey infrared ball previously sold by HiTechnic, or approved open-source alternatives as they become available, is also acceptable.

**A.1.2** The ball will be used in pulsed and stepped-waveform mode — the Elekit RCJ-05 ball will be operated in MODE A (pulsed).

**A.2 IR light**

**A.2.1** The ball shall emit infrared (IR) light of wavelengths in the range 920–960 nm, pulsed at a square-wave carrier frequency of 40 kHz. The ball should have enough ultra-bright, wide-angle LEDs to minimise unevenness of the IR output.

**A.3 Diameter**

**A.3.1** The diameter of the ball is required to be 74 mm. A well-balanced ball shall be used.

**A.4 Durability**

**A.4.1** The ball must resist normal game play. As an indication of durability, it should survive, undamaged, a free-fall from 1500 mm onto a hardwood table or floor.

**A.5 Modulation**

**A.5.1** The 40 kHz carrier output shall be modulated with a trapezoidal (stepped) waveform of frequency 1.2 kHz. Each 833-microsecond cycle shall comprise 8 carrier pulses at full intensity, followed by 4 pulses at 1/4 intensity, 4 pulses at 1/16 intensity, and 4 pulses at 1/64 intensity, followed by a space (zero intensity) of about 346 microseconds. The peak current in the LEDs shall be 45–55 mA. The radiant intensity of each LED shall be more than 20 mW/sr.

**A.6 Battery Life**

**A.6.1** If the ball has an embedded rechargeable battery, when new and fully charged it should last more than 3 hours of continuous use before LED brightness drops to 90% of the initial value. If it uses replaceable batteries, a set of new high-quality alkaline batteries should last more than 8 hours of continuous use before brightness drops to 90%.

**A.7 Colouration**

**A.7.1** The ball shall be neutral in colour. In particular, it must not have any green, blue or yellow colouration (to avoid confusion with the colours of the field and goals).

**A.8 Weight**

**A.8.1** The ball shall have a total mass (including all batteries and parts necessary for game play) of between 0.13 kg and 0.15 kg.

---

## Appendix B: Specification for Passive Golf Ball

*(Open League)*

**B.1 Diameter**

**B.1.1** The diameter of the ball is required to be 42 ± 1 mm.

**B.2 Durability**

**B.2.1** The ball must resist normal gameplay. As an indication of durability, it should survive, undamaged, a free-fall from 1.5 metres onto a hardwood table or floor.

**B.3 Colouration**

**B.3.1** The ball shall be orange. Any colour a human would deem to be orange and substantially different from the other colours used on the field is acceptable.

**B.4 Surface**

**B.4.1** Engravings and printed labels on the ball's surface are tolerated. Teams must be prepared to play with balls as supplied by tournament organisers.

**B.5 Weight**

**B.5.1** The mass of the ball should be 46 ± 3 grams.

---

> The Soccer Ball Specifications are primarily the work of the RoboCup Junior Soccer Technical Committee and have been used with permission by RoboCup Junior Australia.
