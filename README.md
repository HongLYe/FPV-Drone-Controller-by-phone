FPV Drone Controller

Use your phone as a real FPV drone controller!
This project allows you to control FPV drone simulators (like Liftoff, DRL, Velocidrone) using your phone. It emulates a real Xbox controller, works as a PWA, and supports touch joysticks + buttons.

Features

Two joysticks:

Left: throttle & yaw (throttle doesn’t snap back)

Right: pitch & roll

Buttons: A/B/X/Y, LB/RB, Start, Select, and ARM toggle

Fully touch + mouse compatible

Responsive mobile-friendly PWA (add to home screen)

Offline caching via Service Worker

Real-time communication with a Python server using Socket.IO

Emulates an Xbox 360 controller on Windows (via ViGEm + vgamepad)

Demo

Add screenshots or GIF here if you like

Requirements

PC (Windows recommended):

Python 3.10+

ViGEmBus driver (for virtual Xbox controller) – download from ViGEmBus Releases

pip packages: flask, python-socketio, eventlet, vgamepad

Phone / Browser:

Modern browser (Chrome, Edge, Safari, Firefox)

Same Wi-Fi network as your PC

Supports PWA (add to home screen)

Installation
1️⃣ Install ViGEmBus

Download and install the latest driver from ViGEmBus Releases

Reboot if required

2️⃣ Set up Python environment
# Create a virtual environment
python -m venv venv

# Activate it
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install required packages
pip install flask python-socketio eventlet vgamepad

3️⃣ Project Structure
fpv-drone-controller/

``
│
├─ server.py            # Python server
├─ static/
│   ├─ index.html       # Frontend PWA
│   ├─ manifest.json    # PWA manifest
│   ├─ sw.js            # Service Worker
│   └─ icons/
│       ├─ icon-192.png
│       └─ icon-512.png
``

4️⃣ Run the server
python server.py


By default, the server runs on http://0.0.0.0:5000/

Open this URL on your phone browser (http://<PC_IP>:5000)

Add to home screen for fullscreen PWA

5️⃣ Using the controller

Left joystick: Throttle & Yaw

Right joystick: Pitch & Roll

Buttons: tap or hold as needed

ARM toggle: click the ARM button

All controls emulate an Xbox controller visible in Steam simulators

Troubleshooting

Controller not detected:

Make sure ViGEmBus driver is installed and server is running

Buttons not responding:

Ensure your phone is connected to the same Wi-Fi as PC

Reload the PWA if connection fails

Server errors:

Check Python packages installed correctly (pip list)

Make sure Python version >= 3.10

Notes

Designed for Windows + Steam simulators. Linux / Mac support requires alternative virtual joystick solutions.

Works offline after first load thanks to Service Worker caching.

License


MIT License – feel free to use and modify.

