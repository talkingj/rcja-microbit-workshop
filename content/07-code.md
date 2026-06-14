---
id: s-code
nav: Coding
label:
title: "Activities: simple to complex"
---

Five activities in order of complexity. Activities 1 and 2 need only the micro:bit and a browser. Activity 3 needs the assembled robot. Activities 4 and 5 need the IR sensors attached. No rescue line track is required.

<div class="callout">
  <strong>Adding your MakeCode project to this page:</strong> open your project at <a href="https://makecode.microbit.org" target="_blank" rel="noopener">makecode.microbit.org</a>, click <strong>Share</strong>, copy the URL (looks like <code>https://makecode.microbit.org/S12345-abcde</code>), then paste it as <code>makecode_url:</code> in the matching block in <code>content/07-code.md</code> and rebuild.
</div>

<div class="code-ref">
<div class="code-ref-section">
<h3>Setup: extensions you need</h3>
<ol class="setup-steps">
  <li>Go to <a href="https://makecode.microbit.org" target="_blank" rel="noopener">makecode.microbit.org</a> and click <strong>New Project</strong>.</li>
  <li>Click the <strong>gear icon</strong> (top right) then <strong>Extensions</strong>.</li>
  <li>Search for <code>motorbit</code> and add it (motor control blocks).</li>
  <li>Search for <code>sonarbit</code> and add it (ultrasonic sensor block).</li>
</ol>
</div>
</div>

<!-- SLIDE_BREAK -->

<div class="code-ref">
<div class="code-ref-section">
<h3>Wiring reference</h3>
<table class="pin-table">
  <thead>
    <tr><th>Connection</th><th>Port</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td>Left motor</td><td><code>M1</code></td><td>TT motor, left wheel</td></tr>
    <tr><td>Right motor</td><td><code>M2</code></td><td>TT motor, right wheel</td></tr>
    <tr><td>Left IR sensor</td><td><code>P4</code></td><td>0 = black, 1 = white</td></tr>
    <tr><td>Right IR sensor</td><td><code>P3</code></td><td>0 = black, 1 = white</td></tr>
    <tr><td>Ultrasonic sensor</td><td>Free GVS port</td><td>Match pin in MakeCode</td></tr>
  </tbody>
</table>
<div class="callout">
  <strong>Sensor logic:</strong> the IR sensors return 0 on black and 1 on white. Set a pull-up on P3 and P4 inside your <em>on start</em> block.
</div>
</div>
</div>

<!-- SLIDE_BREAK -->

<!-- Activity 1 -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Activity 1: LED display</h3>
<p>Board and browser only. No hardware needed beyond the micro:bit. Write a program that shows text and icons on the 5x5 LED display. Test it in the simulator before downloading.</p>
<p><strong>Goal:</strong> on start, show a heart icon. When button A is pressed, scroll the text "READY". When button B is pressed, show a tick icon.</p>

<!-- MAKECODE_EMBED
title: Activity 1 - LED display
makecode_url:
hint: Create your Activity 1 MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>

<!-- SLIDE_BREAK -->

<!-- Activity 2 -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Activity 2: Button events</h3>
<p>Board only. Introduces event-driven programming. Each button does something different, and the program waits for input rather than running continuously.</p>
<p><strong>Goal:</strong> button A shows an arrow pointing forward. Button B shows a square (stop). Both buttons together show a cross (emergency stop). On start, show a dot to indicate the program is running.</p>

<!-- MAKECODE_EMBED
title: Activity 2 - Button events
makecode_url:
hint: Create your Activity 2 MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>

<!-- SLIDE_BREAK -->

<!-- Activity 3 -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Activity 3: Motor control</h3>
<p>Assembled robot required (motor:bit + motors + battery). No sensors needed. Button presses drive the wheels directly. This confirms the robot is wired correctly before adding sensors.</p>
<p><strong>Goal:</strong> button A drives both motors forward for 1 second then stops. Button B drives one motor forward and one backward (spin on the spot). On start, show a ready icon.</p>

<!-- MAKECODE_EMBED
title: Activity 3 - Motor control
makecode_url:
hint: Create your Activity 3 MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>

<!-- SLIDE_BREAK -->

<!-- Activity 4 -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Activity 4: Reading sensors</h3>
<p>IR sensors must be connected (P3 and P4). No track needed. Read the sensor values and show them on the LED display. Hold the sensor over white paper, then over a dark surface, and watch the display change.</p>
<p><strong>Goal:</strong> in the forever loop, read P3 and P4. If both return 1 (white), show a blank display. If either returns 0 (black detected), show a dot. This confirms the sensors are working before any driving logic is added.</p>

<!-- MAKECODE_EMBED
title: Activity 4 - Reading sensors
makecode_url:
hint: Create your Activity 4 MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>

<!-- SLIDE_BREAK -->

<!-- Activity 5 -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Activity 5: Simple decisions (stretch)</h3>
<p>Full robot required. A strip of black electrical tape on white paper is enough to test with. Write an if/else block that steers based on sensor readings. This is the foundation of line following.</p>
<p><strong>Goal:</strong> in the forever loop: if both sensors read white, drive forward. If the left sensor reads black (0), steer left. If the right sensor reads black (0), steer right. Start the program with button A.</p>
<div class="callout">
  <strong>No track?</strong> Use a 5 cm wide strip of black electrical tape on an A3 sheet of white paper. Students can hold it by hand and move it under the sensor while the robot is stationary, watching the steering change in the motor output.
</div>

<!-- MAKECODE_EMBED
title: Activity 5 - Simple decisions
makecode_url:
hint: Create your Activity 5 MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>
