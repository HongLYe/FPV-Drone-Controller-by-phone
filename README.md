I can't directly send downloadable files through this chat, but here's a **Python script** that will automatically generate `README.md` for you in your project folder. Just run it and you're done!

```python
# save this as: create_readme.py
# run it in your project folder: python create_readme.py

import os

content = """# 🚁 FPV Drone Controller by Phone

> Use your phone as a wireless controller for FPV drone simulators (Liftoff, DRL, Velocidrone).

---

## ⚙️ How to Set Up

### ✅ Prerequisites
- Windows PC (required for virtual controller)
- Python 3.10 or higher
- Phone + PC on the **same Wi-Fi network**

---

### 🔹 Step 1: Install ViGEmBus Driver (Windows Only)

This driver lets your PC emulate an Xbox 360 controller.

1. Download latest release:  
   🔗 https://github.com/ViGEm/ViGEmBus/releases
2. Run `ViGEmBus_Setup_x.x.x.exe`
3. **Reboot your PC** after installation

> ⚠️ Without this driver, the simulator won't detect any controller input.

---

### 🔹 Step 2: Clone the Repository

```bash
git clone https://github.com/HongLYe/FPV-Drone-Controller-by-phone.git
cd FPV-Drone-Controller-by-phone
```

---

### 🔹 Step 3: Create Virtual Environment & Install Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows Command Prompt:
venv\\Scripts\\activate
# Windows PowerShell:
.\\venv\\Scripts\\Activate.ps1
# Linux/Mac:
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

---

### 🔹 Step 4: Run the Server

```bash
python server.py
```

✅ You should see output like:
```
[INFO] Starting FPV Drone Controller Server
[INFO]    Port: 5000
[INFO]    Gamepad: ✓ Ready
```

> 🔒 Keep this terminal window open while using the controller.

---

### 🔹 Step 5: Find Your PC's IP Address

Your phone needs to connect to your PC over Wi-Fi.

**On Windows:**
1. Press `Win + R`, type `cmd`, press Enter
2. Type `ipconfig` and press Enter
3. Look for **IPv4 Address** under your active network adapter  
   Example: `192.168.1.100`

---

### 🔹 Step 6: Connect Your Phone

1. Open your phone's browser (Chrome/Safari)
2. Go to:  
   ```
   http://YOUR_PC_IP:5000
   ```
   Example: `http://192.168.1.100:5000`

3. ✅ You should see the controller interface with joysticks

4. (Optional) Tap **Share → Add to Home Screen** to install as a PWA app

> ⚠️ Must use `http://` not `https://`.  
> ⚠️ If it won't load, check your PC firewall allows port 5000.

---

### 🔹 Step 7: Test in Your Simulator

1. Launch your FPV simulator (Liftoff / DRL / Velocidrone)
2. Go to **Settings → Controller / Input**
3. Select **"Xbox 360 Controller"** as the input device
4. Move the joysticks on your phone → the drone should respond 🎉

---

### 🔹 Step 8: Verify Connection (Optional)

Open this URL in any browser to check server status:
```
http://YOUR_PC_IP:5000/ping
```

✅ Expected response:
```json
{"status": "ok", "timestamp": 1234567890.123, "gamepad_ready": true}
```

---

## 🔘 Button Layout

| Phone Button | Virtual Controller | Typical Simulator Use |
|--------------|------------------|----------------------|
| 🕹️ Left Stick | Throttle + Yaw | Mode 2 default |
| 🕹️ Right Stick | Pitch + Roll | Mode 2 default |
| A / B / X / Y | A / B / X / Y | Camera, reset, actions |
| LB / RB | Left/Right Bumper | View toggle, OSD |
| START / BACK | Start / Back | Pause, menu |
| 🔴 ARM | Xbox GUIDE button (🏠) | Arm/disarm motors* |

> *ARM uses the Xbox "Guide" button by default to avoid conflicts.  
> If your simulator doesn't respond to ARM, edit `server.py` line ~45 and change `XUSB_GAMEPAD_GUIDE` to `XUSB_GAMEPAD_X`.

---

## 🛠️ Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| ❌ Phone can't load page | • Check PC IP is correct<br>• Disable firewall temporarily<br>• Ensure both devices on same Wi-Fi |
| ❌ Simulator doesn't see controller | • Reboot after installing ViGEmBus<br>• Run simulator as Administrator<br>• Check `server.py` output shows "Gamepad: ✓ Ready" |
| ❌ Inputs feel laggy | • Move closer to Wi-Fi router<br>• Reduce network traffic (pause downloads)<br>• Use 5GHz Wi-Fi if available |
| ❌ ARM button doesn't work | • Your sim may ignore GUIDE button → change mapping in `server.py` |

---

## 📁 Project Files Overview

```
FPV-Drone-Controller-by-phone/
├─ server.py              # Backend: Flask + Socket.IO + virtual gamepad
├─ requirements.txt       # Python dependencies
├─ README.md              # This file
├─ .gitignore             # Git ignore rules
│
└─ static/                # Frontend (PWA)
   ├─ index.html          # Controller UI
   ├─ manifest.json       # PWA install config
   ├─ sw.js               # Offline caching
   └─ icons/              # App icons
```

---

## 🔄 Updating the Project

```bash
# Pull latest changes
git pull origin main

# Reinstall dependencies (if requirements.txt changed)
pip install -r requirements.txt

# Restart server
python server.py
```

> 💡 **Tip**: Keep this repo updated — new features and bug fixes are added regularly!
"""

# Write to file
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("✅ README.md created successfully in current folder!")
```

### 🚀 How to use:
1. Save the code above as `create_readme.py` inside your `FPV-Drone-Controller-by-phone` folder
2. Open terminal/command prompt in that folder
3. Run: `python create_readme.py`
4. Done! `README.md` is automatically created with the exact content.
