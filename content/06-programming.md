---
id: s-programming
nav: Programming
label: Programming concepts
title: Programming Your Robot
---

SPIKE robots can be programmed in SPIKE App blocks (drag-and-drop) or Python. This section covers the key programming concepts for soccer — the ideas your code needs to handle, regardless of which language you use.

<div class="lang-compare">
  <div class="lang-card">
    <div class="lang-hdr">
      <span class="lang-name">SPIKE App Blocks</span>
      <span class="lang-level level-beginner">Beginner</span>
    </div>
    <div class="lang-body">
      Visual drag-and-drop programming in the LEGO Education SPIKE app. Great for getting started — you can see the logic flow and test quickly.
      <ul class="lang-pros">
        <li>No syntax to memorise</li>
        <li>Built-in motor and sensor blocks</li>
        <li>Quick to prototype and iterate</li>
        <li>Works on tablets and computers</li>
      </ul>
    </div>
  </div>
  <div class="lang-card">
    <div class="lang-hdr">
      <span class="lang-name">Python</span>
      <span class="lang-level level-advanced">Step up</span>
    </div>
    <div class="lang-body">
      Text-based programming for more control and flexibility. SPIKE supports MicroPython. Better for complex logic and fine-tuned sensor handling.
      <ul class="lang-pros">
        <li>More precise control over timing</li>
        <li>Easier to handle complex conditions</li>
        <li>Transferable programming skill</li>
        <li>Better for inter-robot communication</li>
      </ul>
    </div>
  </div>
</div>

<!-- SLIDE_BREAK -->

### Core programming concepts for soccer

Your robot's program needs to handle these key tasks. The exact implementation will depend on your hardware and language choice, but every soccer robot needs to solve these problems.

<div class="pitch-grid">
  <div class="pitch-card">
    <div class="pitch-num">01</div>
    <div class="pitch-title">Sense the ball</div>
    <div class="pitch-body">Use the IR sensor to detect the ball's direction and relative distance. The ball pulses infrared light at 40 kHz — your sensor reads the strength from different angles to work out where the ball is.</div>
  </div>
  <div class="pitch-card">
    <div class="pitch-num">02</div>
    <div class="pitch-title">Drive toward it</div>
    <div class="pitch-body">Convert sensor readings into motor commands. Turn toward the strongest IR signal and drive forward. The faster your loop runs, the more responsive your robot will be.</div>
  </div>
  <div class="pitch-card">
    <div class="pitch-num">03</div>
    <div class="pitch-title">Know your heading</div>
    <div class="pitch-body">Standard League can use a gyro to maintain orientation — so the robot always knows which way is "forward". Simple Simon teams need to rely on other strategies like motor timing or colour detection.</div>
  </div>
  <div class="pitch-card">
    <div class="pitch-num">04</div>
    <div class="pitch-title">Goal awareness</div>
    <div class="pitch-body">Know which goal is yours. A colour sensor pointing forward can distinguish cyan from yellow. Without this, your robot might score own goals — which count for the opposition.</div>
  </div>
  <div class="pitch-card">
    <div class="pitch-num">05</div>
    <div class="pitch-title">Avoid penalties</div>
    <div class="pitch-body">Program a "stuck" detection: if motors are running but the robot isn't moving (e.g. stalled against a wall), reverse and turn. A robot stuck for 20+ seconds in the goal area gets deemed "damaged".</div>
  </div>
  <div class="pitch-card">
    <div class="pitch-num">06</div>
    <div class="pitch-title">Communication</div>
    <div class="pitch-body">Your two robots can communicate wirelessly (e.g. Bluetooth). Use unique message prefixes so you don't pick up signals from other teams. The referee can ask you to disable this at any time.</div>
  </div>
</div>

> **Manual start only:** Your robot must be started by pressing a button on the hub — not from a laptop, tablet, or phone. Make sure your start sequence works reliably from a physical button press, every time.

> **Annotated code:** You must submit annotated code before the competition. Judges will ask you to explain your program — make sure every team member understands how it works, not just the person who wrote it.
