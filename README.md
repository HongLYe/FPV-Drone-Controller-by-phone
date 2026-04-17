[table-0da02027-9b21-4665-a277-2f4036947d5c.csv](https://github.com/user-attachments/files/26809325/table-0da02027-9b21-4665-a277-2f4036947d5c.csv)# 🚁 FPV Drone Controller by Phone

> Turn your smartphone into a wireless FPV drone controller for simulators like Liftoff, DRL Simulator, Velocidrone, and more.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PWA](https://img.shields.io/badge/PWA-Supported-orange.svg)](https://web.dev/progressive-web-apps/)

<div align="center">
  <img src="static/demo-placeholder.png" alt="Phone controller UI" width="600" onerror="this.style.display='none'">
  <p><em>📱 Phone UI with dual joysticks + button panel</em></p>
</div>

---

## ✨ Features

- 🎮 **Dual virtual joysticks**: Mode 2 layout (left: throttle/yaw, right: pitch/roll)
- 🔘 **Full button set**: A/B/X/Y, LB/RB, Start, Select, plus dedicated ARM toggle
- 📱 **Progressive Web App (PWA)**: Install to home screen, works offline after first load
- 📡 **Low-latency control**: Real-time input via Socket.IO over local Wi-Fi
- 🖥️ **Xbox 360 emulation**: Works with any simulator that supports XInput controllers
- ⚙️ **Configurable**: Deadzone, smoothing, and button mapping options built-in

---

## 🚀 Quick Start (5 Minutes)

### Prerequisites
- ✅ Windows PC (Linux/macOS support coming soon)
- ✅ Python 3.10 or higher
- ✅ Same Wi-Fi network for phone and PC

### Step 1: Install ViGEmBus Driver (Windows Only)
Download and install the virtual controller driver:
🔗 [ViGEmBus Releases → Download latest](https://github.com/ViGEm/ViGEmBus/releases)

> ⚠️ **Important**: Reboot your PC after installation for the driver to register properly.

### Step 2: Clone & Setup
```bash
# Clone the repo
git clone https://github.com/HongLYe/FPV-Drone-Controller-by-phone.git
cd FPV-Drone-Controller-by-phone

# Create virtual environment (recommended)
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Step 3: Run the Server
python server.py

You should see output like:
2024-01-15 10:30:45 [INFO] 🚀 Starting FPV Drone Controller Server
2024-01-15 10:30:45 [INFO]    Port: 5000
2024-01-15 10:30:45 [INFO]    Gamepad: ✓ Ready
2024-01-15 10:30:45 [INFO] ✓ Virtual Xbox 360 gamepad initialized
```
Step 4: Connect Your Phone
1.Find your PC's local IP address:
  Windows: Open Command Prompt → type ipconfig → look for "IPv4 Address" (e.g., 192.168.1.100)
  Mac/Linux: Open Terminal → type ifconfig or ip a
2.On your phone's browser, open:
```bash
http://192.168.1.100:5000
```
🔐 Use http:// not https:// — this is a local development server
3.(Optional) Tap "Add to Home Screen" for fullscreen PWA experience:
  Chrome Android: Menu (⋮) → "Add to Home screen"
  Safari iOS: Share button (📤) → "Add to Home Screen"

Step 5: Test in Simulator
1.Launch your FPV simulator: Liftoff / DRL / Velocidrone / Uncrashed
2.Go to Controller Settings → select "Xbox 360 Controller"
3.Move joysticks on your phone → drone should respond immediately! 🎉
4.Press the 🔴 ARM button to toggle arm/disarm (mapped to Xbox GUIDE button 🏠)

📱 Phone Interface Guide
[Uploading taControl,Function,Default Simulator Mapping
🕹️ Left Stick,Throttle (Y-axis) + Yaw (X-axis),Mode 2 (standard)
🕹️ Right Stick,Pitch (Y-axis) + Roll (X-axis),Mode 2 (standard)
🔘 A / B / X / Y,Action buttons,"Camera view, reset, aux functions"
🔘 LB / RB,Shoulder buttons,"Camera angle, OSD toggle"
🔘 START / BACK,Menu navigation,"Pause, reset model, menu"
🔴 ARM,Toggle arm/disarm,Xbox GUIDE button (🏠) ⭐ble-0da02027-9b21-4665-a277-2f4036947d5c.csv…]()

💡 ARM Button Note: The ARM toggle uses the Xbox "Guide" button (🏠) by default to avoid conflicts with normal X/Y/A/B gameplay buttons. If your simulator doesn't respond to the Guide button, edit server.py line ~52 to remap it (see Configuration section).
