---
id: s-hardware
nav: Hardware
label: On the board
title: Built-in sensors and outputs
---

The micro:bit has sensors and outputs soldered onto the board. With only the board and a USB cable, a student can detect movement, read temperature, transmit data wirelessly, and show output on the LED display — no additional components required.

<div class="photo-row">
  <div class="diagram-slot" id="photo-microbit-front">
    <!-- Replace with a real photo: <img src="assets/photos/microbit-front.jpg" alt="micro:bit V2 front"> -->
    <img src="assets/microbit-front.svg" alt="micro:bit V2 front — annotated diagram showing LED matrix, buttons, USB connector, touch logo, microphone, and edge connector pads">
  </div>
  <div class="diagram-slot" id="photo-microbit-back">
    <!-- Replace with a real photo: <img src="assets/photos/microbit-back.jpg" alt="micro:bit V2 edge connector"> -->
    <img src="assets/microbit-edge.svg" alt="micro:bit V2 edge connector — annotated diagram showing gold pads, pin labels P0 P1 P2 3V GND, and V2 notch">
  </div>
</div>

<div class="hw-grid">

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18"/><circle cx="8.5" cy="8.5" r="1.5" fill="#3db166" stroke="none"/><circle cx="12" cy="8.5" r="1.5" fill="#3db166" stroke="none"/><circle cx="15.5" cy="8.5" r="1.5" fill="#3db166" stroke="none"/><circle cx="8.5" cy="12" r="1.5" fill="#3db166" stroke="none"/><circle cx="12" cy="12" r="1.5" fill="#3db166" stroke="none"/><circle cx="15.5" cy="12" r="1.5" fill="#3db166" stroke="none"/><circle cx="8.5" cy="15.5" r="1.5" fill="#3db166" stroke="none"/><circle cx="12" cy="15.5" r="1.5" fill="#3db166" stroke="none"/><circle cx="15.5" cy="15.5" r="1.5" fill="#3db166" stroke="none"/></svg>
    </div>
    <div class="hw-name">5×5 LED display</div>
    <div class="hw-desc">25 red LEDs, each individually controllable. Shows text, numbers, icons, and animations. Also acts as a light sensor when not displaying.</div>
    <span class="hw-tag">Output + Input</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><circle cx="7" cy="12" r="3"/><circle cx="17" cy="12" r="3"/></svg>
    </div>
    <div class="hw-name">Buttons A and B</div>
    <div class="hw-desc">Physical pushbuttons on either side of the board. Detect press, release, and hold. The primary way a user interacts with a running program.</div>
    <span class="hw-tag">Input</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/><circle cx="12" cy="12" r="3"/></svg>
    </div>
    <div class="hw-name">Accelerometer</div>
    <div class="hw-desc">Measures movement and tilt across three axes. Detects gestures: shake, tilt, freefall. Reads the board's angle in any direction.</div>
    <span class="hw-tag">Input</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v2M12 20v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M2 12h2M20 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
    </div>
    <div class="hw-name">Compass</div>
    <div class="hw-desc">Measures magnetic field direction. After calibration, gives a compass bearing. Useful for navigation, detecting magnetic objects, and orientation projects.</div>
    <span class="hw-tag">Input</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0z"/></svg>
    </div>
    <div class="hw-name">Temperature sensor</div>
    <div class="hw-desc">Reads the CPU die temperature, which approximates ambient temperature. Good enough for weather logging, thermostat projects, and science experiments.</div>
    <span class="hw-tag">Input</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><path d="M1 6l5 6-5 6M23 6l-5 6 5 6M8 12h8"/></svg>
    </div>
    <div class="hw-name">Radio (2.4 GHz)</div>
    <div class="hw-desc">Send and receive short messages between micro:bits, up to 70 m in open space. Enables multi-device projects: games, remote controls, sensor networks.</div>
    <span class="hw-tag">Input + Output</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
    </div>
    <div class="hw-name">Microphone (V2)</div>
    <div class="hw-desc">Detects sound level, clap patterns, and loud/quiet events. Opens up music-reactive projects, sound-triggered automations, and noise monitoring.</div>
    <span class="hw-tag">V2 only · Input</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
    </div>
    <div class="hw-name">Speaker (V2)</div>
    <div class="hw-desc">On-board buzzer that plays tones, melodies, and effects without any extra hardware. Controlled with the music blocks in MakeCode or Python's music module.</div>
    <span class="hw-tag">V2 only · Output</span>
  </div>

  <div class="hw-card">
    <div class="hw-icon">
      <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="#3db166" stroke-width="2"><rect x="2" y="14" width="20" height="6" rx="0"/><path d="M6 14V8M12 14V4M18 14V10"/></svg>
    </div>
    <div class="hw-name">Edge connector</div>
    <div class="hw-desc">25 gold pads at the bottom: analogue, digital, I2C, SPI, and power pins. Connect motors, servos, extra sensors, and carrier boards. Crocodile clips work on the large pads.</div>
    <span class="hw-tag">Extension</span>
  </div>

</div>
