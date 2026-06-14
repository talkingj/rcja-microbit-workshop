---
id: s-kit
nav: About your kit
label: Kit assembly
title: About your kit
---

Your kit arrives as individual components. Assembly takes around 15 minutes. No soldering is required. All connections are push-fit or screw terminal.

<div class="callout">
  <strong>What is in your kit:</strong> one micro:bit V2, one Elecfreaks motor:bit carrier board, two TT DC gear motors with wheels, one 2-channel IR tracking sensor module, one HC-SR04 ultrasonic sensor, one 4xAA battery holder with JST connector, and jumper wires.
</div>

<div class="hw-grid">

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 9h18"/></svg>
    </div>
    <div class="hw-name">micro:bit V2</div>
    <div class="hw-desc">The brain. Has the 5x5 LED display, buttons, sensors, and radio. Plugs into the top of the carrier board.</div>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><rect x="2" y="7" width="20" height="10" rx="1"/><path d="M6 7V5M10 7V5M14 7V5M18 7V5"/></svg>
    </div>
    <div class="hw-name">motor:bit carrier board</div>
    <div class="hw-desc">Connects to the micro:bit edge connector. Has motor driver circuits, power regulation, and labelled ports for motors and sensors.</div>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/></svg>
    </div>
    <div class="hw-name">TT gear motors x2</div>
    <div class="hw-desc">One for each wheel. Wired to M1 and M2 on the carrier board using the screw terminals.</div>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><rect x="4" y="8" width="16" height="8" rx="1"/><circle cx="9" cy="12" r="2"/><circle cx="15" cy="12" r="2"/></svg>
    </div>
    <div class="hw-name">IR tracking sensor</div>
    <div class="hw-desc">Two sensors on one board. Detects black vs. white surfaces. Connects to P3 and P4. Mount at the front, facing down.</div>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><rect x="3" y="8" width="18" height="8" rx="1"/><circle cx="8" cy="12" r="2"/><circle cx="16" cy="12" r="2"/></svg>
    </div>
    <div class="hw-name">Ultrasonic sensor</div>
    <div class="hw-desc">Two round transducers: one transmits, one receives. Measures distance up to 4 m. Connect to a spare GVS port and match the pin in MakeCode.</div>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><rect x="3" y="9" width="18" height="10" rx="1"/><path d="M7 9V7a2 2 0 0 1 4 0v2M13 9V7a2 2 0 0 1 4 0v2"/></svg>
    </div>
    <div class="hw-name">4xAA battery pack</div>
    <div class="hw-desc">Plugs into the JST connector on the carrier board. Use alkaline AA batteries. Do not use rechargeable AA batteries as the voltage is too low for reliable motor operation.</div>
  </div>

</div>

<!-- SLIDE_BREAK -->

<div class="code-ref">
<div class="code-ref-section">
<h3>Assembly steps</h3>
<ol class="setup-steps">
  <li><strong>Insert the micro:bit into the carrier board.</strong> Line up the gold edge connector pads on the micro:bit with the slot at the top of the motor:bit. Press firmly until it clicks in. The LED display should face outward.</li>
  <li><strong>Wire the left motor to M1.</strong> Strip 5 mm of insulation from each motor wire. Loosen the M1 screw terminals on the carrier board, insert the wires, and tighten. Polarity affects direction: if the motor runs backward you can swap the wires later.</li>
  <li><strong>Wire the right motor to M2.</strong> Same process as M1. Red to positive, black to negative is a reasonable starting point.</li>
  <li><strong>Connect the IR sensor module.</strong> The sensor has a 4-pin JST connector or individual pin headers: VCC, GND, left signal, right signal. Connect left signal to P4 and right signal to P3 on the carrier board. VCC to 3.3 V, GND to GND.</li>
  <li><strong>Connect the ultrasonic sensor.</strong> Four pins: VCC, Trig, Echo, GND. Connect Trig and Echo to a free GVS port. Note which pin you use: you will enter this in MakeCode when you add the sonarbit extension.</li>
  <li><strong>Connect the battery pack.</strong> Plug the JST connector into the power socket on the carrier board. Leave the battery pack switched off until you are ready to test.</li>
  <li><strong>Check before powering on.</strong> Confirm the micro:bit is seated fully, no wires are touching bare metal they should not, and the battery switch is off. Then switch on and look for the micro:bit LED display to light up.</li>
</ol>
</div>
</div>

<!-- SLIDE_BREAK -->

<div class="code-ref">
<div class="code-ref-section">
<h3>Wiring reference</h3>
<table class="pin-table">
  <thead>
    <tr><th>Component</th><th>Port</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td>Left motor</td><td><code>M1</code></td><td>Screw terminal on carrier board</td></tr>
    <tr><td>Right motor</td><td><code>M2</code></td><td>Screw terminal on carrier board</td></tr>
    <tr><td>IR sensor (left)</td><td><code>P4</code></td><td>0 = black line detected, 1 = white</td></tr>
    <tr><td>IR sensor (right)</td><td><code>P3</code></td><td>0 = black line detected, 1 = white</td></tr>
    <tr><td>Ultrasonic sensor</td><td>Free GVS port</td><td>Note the pin number and enter it in MakeCode</td></tr>
    <tr><td>Battery pack</td><td>JST power socket</td><td>4xAA alkaline only</td></tr>
  </tbody>
</table>
</div>
</div>
