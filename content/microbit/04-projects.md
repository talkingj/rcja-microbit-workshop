---
id: s-projects
nav: What you can attach
label:
title: Extending the micro:bit
projects:
  - domain: Motors
    name: Motor carrier board
    desc: The motor:bit board plugs directly onto the edge connector and adds two DC motor outputs, 12 GVS sensor ports, and a battery connector. No soldering required.
    img: "assets/photos/motorbit-board.jpg"
    tags: [DC motors, GVS ports, Robot base]

  - domain: Sensing
    name: IR tracking sensor
    desc: A two-channel sensor that reads black and white surfaces as a digital 1 or 0. Which surface reads 1 varies by module, so you calibrate it in code. Connects to GVS ports. The core sensor for line following.
    img: "assets/photos/ir-tracking-sensor.png"
    tags: [Line detection, Digital output]

  - domain: Sensing
    name: Ultrasonic distance sensor
    desc: Measures distance to an object ahead by sending and receiving a sound pulse. Range 2 cm to 400 cm. Used for obstacle detection, object location, and proximity alerts.
    img: "assets/photos/ultrasonic-sensor.jpg"
    tags: [Distance, HC-SR04 compatible]

  - domain: Sensing
    name: Soil moisture sensor
    desc: Reads moisture levels from soil via the analogue edge connector pins. Connects directly to the large gold pads with crocodile clips. Common in science and environment projects.
    tags: [Analogue input, Science]

  - domain: Output
    name: NeoPixel LED strip
    desc: Individually addressable RGB LEDs, chainable to any length. Controlled over a single GVS data line. Used in art, wearables, status indicators, and light-reactive projects.
    tags: [RGB LEDs, Chainable]

  - domain: Output
    name: OLED screen
    desc: A 128x64 pixel screen connected over I2C. Displays text, numbers, and graphics beyond the 5x5 LED matrix. Common in data logging and science projects.
    img: "assets/photos/oled-screen.png"
    tags: [I2C, 128x64 pixels]

  - domain: Control
    name: Servo motor
    desc: Precise angular movement (0 to 180 degrees) via a single GVS port. Used for steering, robotic arms, and camera mounts. Controlled with a PWM block in MakeCode.
    tags: [PWM, Precise movement]

  - domain: Gaming
    name: MakeCode Arcade shield
    desc: Adds a colour screen, directional buttons, and action buttons. Turns the micro:bit into a handheld game console. Games are written separately in MakeCode Arcade.
    img: "assets/photos/arcade-shield.jpg"
    tags: [Colour display, Game input]
---

The micro:bit's 25-pin edge connector gives access to a large ecosystem of add-ons. The accessories below connect via that connector, either directly with crocodile clips or through a carrier board. No soldering is required for any of them.
