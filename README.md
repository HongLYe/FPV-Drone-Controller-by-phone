# 🚁 FPV Drone Controller by Phone

> Turn your smartphone into a wireless FPV drone controller for simulators like Liftoff, DRL Simulator, Velocidrone, and more.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-Supported-orange.svg)](https://web.dev/progressive-web-apps/)

<div align="center">
  <img src="static/demo-placeholder.png" alt="Phone controller UI" width="600">
  <p><em>Phone UI with dual joysticks + button panel (demo image)</em></p>
</div>

---

## ✨ Features

- 🎮 **Dual virtual joysticks**: Mode 2 layout (left: throttle/yaw, right: pitch/roll)
- 🔘 **Full button set**: A/B/X/Y, LB/RB, Start, Select, plus dedicated ARM toggle
- 📱 **Progressive Web App (PWA)**: Install to home screen, works offline after first load
- 📡 **Low-latency control**: Real-time input via Socket.IO over local Wi-Fi
- 🖥️ **Xbox 360 emulation**: Works with any simulator that supports XInput controllers
- ⚙️ **Configurable**: Deadzone, throttle curve, and button mapping options (coming soon)

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Windows PC (Linux/macOS support coming soon)
- Python 3.10 or higher
- Same Wi-Fi network for phone and PC

### Step 1: Install ViGEmBus Driver (Windows Only)
Download and install the virtual controller driver:
🔗 [ViGEmBus Releases → Download latest](https://github.com/ViGEm/ViGEmBus/releases)

> ⚠️ Reboot your PC after installation.

### Step 2: Clone & Setup
```bash
# Clone the repo
git clone https://github.com/HongLYe/FPV-Drone-Controller-by-phone.git
cd FPV-Drone-Controller-by-phone

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt# 🚁 FPV Drone Controller by Phone

> Turn your smartphone into a wireless FPV drone controller for simulators like Liftoff, DRL Simulator, Velocidrone, and more.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-Supported-orange.svg)](https://web.dev/progressive-web-apps/)

<div align="center">
  <img src="static/demo-placeholder.png" alt="Phone controller UI" width="600">
  <p><em>Phone UI with dual joysticks + button panel (demo image)</em></p>
</div>

---

## ✨ Features

- 🎮 **Dual virtual joysticks**: Mode 2 layout (left: throttle/yaw, right: pitch/roll)
- 🔘 **Full button set**: A/B/X/Y, LB/RB, Start, Select, plus dedicated ARM toggle
- 📱 **Progressive Web App (PWA)**: Install to home screen, works offline after first load
- 📡 **Low-latency control**: Real-time input via Socket.IO over local Wi-Fi
- 🖥️ **Xbox 360 emulation**: Works with any simulator that supports XInput controllers
- ⚙️ **Configurable**: Deadzone, throttle curve, and button mapping options (coming soon)

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- Windows PC (Linux/macOS support coming soon)
- Python 3.10 or higher
- Same Wi-Fi network for phone and PC

### Step 1: Install ViGEmBus Driver (Windows Only)
Download and install the virtual controller driver:
🔗 [ViGEmBus Releases → Download latest](https://github.com/ViGEm/ViGEmBus/releases)

> ⚠️ Reboot your PC after installation.

### Step 2: Clone & Setup
```bash
# Clone the repo
git clone https://github.com/HongLYe/FPV-Drone-Controller-by-phone.git
cd FPV-Drone-Controller-by-phone

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
