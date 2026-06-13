---
id: s-code
nav: Coding
label: Coding reference
title: Setting up and writing your first programs
---

A reference to keep open during the live coding session. Setup steps, wiring, program structure, and the three programs that make up a Rescue Line robot — each with an embedded MakeCode project you can open, run, and remix directly.

<div class="code-ref">

<div class="code-ref-section">
<h3>Step 1: Open MakeCode and add extensions</h3>

<ol class="setup-steps">
  <li>Go to <a href="https://makecode.microbit.org" target="_blank" rel="noopener">makecode.microbit.org</a> and click <strong>New Project</strong>.</li>
  <li>Click the <strong>gear icon</strong> (top right) then <strong>Extensions</strong>.</li>
  <li>Search for <code>motorbit</code> and add it — this gives you motor control blocks.</li>
  <li>Search for <code>sonarbit</code> and add it — this gives you the ultrasonic sensor block.</li>
  <li>You should now see <strong>motorbit</strong> and <strong>sonarbit</strong> categories in the block palette.</li>
</ol>

<div class="callout">
  <strong>Sharing a project:</strong> once you have working blocks, click <strong>Share</strong> in the top menu. Copy the URL it gives you (looks like <code>https://makecode.microbit.org/S12345-abcde</code>). Paste that URL as <code>makecode_url:</code> in the matching section of <code>content/07-code.md</code> and it will embed live on this page.
</div>
</div>

<div class="code-ref-section">
<h3>Pin and wiring reference</h3>

<table class="pin-table">
  <thead>
    <tr><th>Connection</th><th>Pin</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td>Left motor</td><td><code>M1</code></td><td>TT yellow motor — left wheel</td></tr>
    <tr><td>Right motor</td><td><code>M2</code></td><td>TT yellow motor — right wheel</td></tr>
    <tr><td>Left IR sensor (S1)</td><td><code>P4</code></td><td>Digital. <strong>0 = on the line</strong>, 1 = white background</td></tr>
    <tr><td>Right IR sensor (S2)</td><td><code>P3</code></td><td>Digital. <strong>0 = on the line</strong>, 1 = white background</td></tr>
    <tr><td>Ultrasonic sensor</td><td>Free GVS port</td><td>Set in MakeCode to match physical wiring</td></tr>
    <tr><td>Buzzer</td><td><code>P0</code></td><td>On-board — no wiring needed</td></tr>
  </tbody>
</table>

<div class="callout">
  <strong>Sensor logic note:</strong> the IR sensors return <strong>0</strong> when they see the black line and <strong>1</strong> when they see white. This is the opposite of what you might expect. Use the <em>set pull up</em> block on P3 and P4 inside your <em>on start</em> block.
</div>
</div>

<div class="code-ref-section">
<h3>Program structure: what goes where</h3>

<table class="pin-table">
  <thead>
    <tr><th>Block</th><th>When it runs</th><th>Use it for</th></tr>
  </thead>
  <tbody>
    <tr><td><code>on start</code></td><td>Once, when the board powers on</td><td>Set pin pull-ups, show a ready icon on the LED</td></tr>
    <tr><td><code>forever</code></td><td>Continuously in a loop</td><td>Read sensors, decide direction, drive motors</td></tr>
    <tr><td><code>on button A pressed</code></td><td>When the handler presses Button A</td><td>Start the run — required by competition rules</td></tr>
    <tr><td><code>on button B pressed</code></td><td>When Button B is pressed</td><td>Emergency stop or toggle calibration mode</td></tr>
  </tbody>
</table>
</div>

<div class="code-ref-section">
<h3>The autonomy rule: two things to remember</h3>

<div class="callout">
  <strong>Rule 3.2.1 — Button start:</strong> the program must be downloaded to the robot before the run. The Robot Handler starts it by pressing a button on the board. No laptop, no remote, no phone.
</div>

<div class="callout">
  <strong>Rule 3.2.2 — No wireless:</strong> Bluetooth and radio must be off during a run. MakeCode blocks mode does not add radio by default, so you are fine as long as you do not add a radio block.
</div>
</div>

</div>

<!-- Part 1 — Line following -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Part 1: Line following</h3>
<p>Read the two IR sensors and steer the robot to stay on the black line. This is the core loop that runs for the whole course.</p>

<!-- MAKECODE_EMBED
title: Line following
makecode_url:
hint: Create your line-following MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>

<!-- Part 2 — Obstacle avoidance -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Part 2: Obstacle avoidance</h3>
<p>Use the ultrasonic sensor to detect an obstacle ahead, drive around it, and reacquire the line within 30 cm.</p>

<!-- MAKECODE_EMBED
title: Obstacle avoidance
makecode_url:
hint: Create your obstacle avoidance MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>

<!-- Part 3 — Push rescue -->
<div class="code-ref">
<div class="code-ref-section">
<h3>Part 3: Push rescue</h3>
<p>Detect the silver capsule inside the chemical spill zone and push it clear. Worth 50 points — the single highest-value action in the scoring.</p>

<!-- MAKECODE_EMBED
title: Push rescue
makecode_url:
hint: Create your push rescue MakeCode project, click Share, and paste the URL above as makecode_url:
-->
</div>
</div>
