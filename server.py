#!/usr/bin/env python3
"""
FPV Drone Controller Server
Receives joystick/button inputs from phone via WebSocket,
forwards them to a virtual Xbox 360 controller using ViGEm/vgamepad.
Author: HongLYe | License: MIT
"""

from flask import Flask, send_from_directory, jsonify
import socketio
import eventlet
import eventlet.wsgi
import os
import time
import logging
import sys

# Configuration
CONFIG = {
    'PORT': int(os.environ.get('PORT', 5000)),
    'HOST': '0.0.0.0',
    'LOG_LEVEL': logging.INFO,
    'JOYSTICK_SMOOTHING': 0.3,
    'DEADZONE': 0.07,
}

# Logging Setup
logging.basicConfig(
    level=CONFIG['LOG_LEVEL'],
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

# Virtual Gamepad Setup
VGAMEPAD_AVAILABLE = False
gamepad = None

try:
    import vgamepad as vg
    from vgamepad import XUSB_BUTTON
    VGAMEPAD_AVAILABLE = True
    logger.info("vgamepad library loaded")
except ImportError as e:
    logger.warning(f"vgamepad not installed: {e}")
except Exception as e:
    logger.error(f"Failed to import vgamepad: {e}")

if VGAMEPAD_AVAILABLE:
    try:
        gamepad = vg.VX360Gamepad()
        logger.info("Virtual Xbox 360 gamepad initialized")
    except Exception as e:
        logger.error(f"Failed to create virtual gamepad: {e}")
        gamepad = None
        VGAMEPAD_AVAILABLE = False

# Button Mapping - ARM uses GUIDE button to avoid conflicts
BUTTON_MAP = {
    'A': XUSB_BUTTON.XUSB_GAMEPAD_A,
    'B': XUSB_BUTTON.XUSB_GAMEPAD_B,
    'X': XUSB_BUTTON.XUSB_GAMEPAD_X,
    'Y': XUSB_BUTTON.XUSB_GAMEPAD_Y,
    'LB': XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    'RB': XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    'START': XUSB_BUTTON.XUSB_GAMEPAD_START,
    'BACK': XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    'ARM': XUSB_BUTTON.XUSB_GAMEPAD_GUIDE,
}

# Joystick State
last_values = {'left': {'x': 0.0, 'y': 0.0}, 'right': {'x': 0.0, 'y': 0.0}}

def clamp(value, min_val=-1.0, max_val=1.0):
    return max(min_val, min(max_val, value))

def apply_deadzone(value, deadzone=CONFIG['DEADZONE']):
    if abs(value) < deadzone:
        return 0.0
    sign = 1 if value > 0 else -1
    return sign * (abs(value) - deadzone) / (1.0 - deadzone)

# Flask + Socket.IO Setup
sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# HTTP Routes
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/ping')
def ping():
    return jsonify({
        'status': 'ok',
        'timestamp': time.time(),
        'server': 'FPV-Drone-Controller',
        'gamepad_ready': VGAMEPAD_AVAILABLE and gamepad is not None
    })

@app.route('/api/config')
def get_config():
    return jsonify({
        'deadzone': CONFIG['DEADZONE'],
        'smoothing': CONFIG['JOYSTICK_SMOOTHING'],
        'gamepad_available': VGAMEPAD_AVAILABLE
    })

# Socket.IO Events
@sio.event
def connect(sid, environ):
    client_ip = environ.get('REMOTE_ADDR', 'unknown')
    logger.info(f"Client connected: {sid} from {client_ip}")
    sio.emit('server_info', {
        'gamepad_ready': VGAMEPAD_AVAILABLE and gamepad is not None,
        'config': {'deadzone': CONFIG['DEADZONE']}
    }, room=sid)

@sio.event
def disconnect(sid):
    logger.info(f"Client disconnected: {sid}")

@sio.on('joystick')
def on_joystick(sid, data):
    try:
        stick = data.get('stick')
        if stick not in ['left', 'right']:
            return
        x = clamp(float(data.get('x', 0.0)))
        y = clamp(float(data.get('y', 0.0)))
        x = apply_deadzone(x)
        y = apply_deadzone(y)
        alpha = CONFIG['JOYSTICK_SMOOTHING']
        lv = last_values[stick]
        smoothed_x = (1 - alpha) * x + alpha * lv['x']
        smoothed_y = (1 - alpha) * y + alpha * lv['y']
        last_values[stick] = {'x': smoothed_x, 'y': smoothed_y}
        if gamepad is not None:
            if stick == 'left':
                gamepad.left_joystick_float(x_value_float=smoothed_x, y_value_float=smoothed_y)
            else:
                gamepad.right_joystick_float(x_value_float=smoothed_x, y_value_float=smoothed_y)
            gamepad.update()
    except Exception as e:
        logger.error(f"Joystick error: {e}")

@sio.on('button')
def on_button(sid, data):
    try:
        btn = data.get('btn')
        state = data.get('state')
        if btn not in BUTTON_MAP:
            return
        if gamepad is None:
            return
        button_code = BUTTON_MAP[btn]
        if state == 'down':
            gamepad.press_button(button=button_code)
        elif state == 'up':
            gamepad.release_button(button=button_code)
        gamepad.update()
    except Exception as e:
        logger.error(f"Button error: {e}")

@sio.on('calibrate')
def on_calibrate(sid, data):
    logger.info(f"Calibration request from {sid}")
    last_values['left'] = {'x': 0.0, 'y': 0.0}
    last_values['right'] = {'x': 0.0, 'y': 0.0}
    sio.emit('calibration_complete', {'success': True}, room=sid)

# Server Entry Point
if __name__ == '__main__':
    logger.info("Starting FPV Drone Controller Server")
    logger.info(f"Port: {CONFIG['PORT']}")
    logger.info(f"Gamepad: {'Ready' if (VGAMEPAD_AVAILABLE and gamepad) else 'Not available'}")
    
    if not VGAMEPAD_AVAILABLE:
        logger.warning("Running without virtual gamepad")
    
    try:
        eventlet.wsgi.server(
            eventlet.listen((CONFIG['HOST'], CONFIG['PORT'])),
            app,
            log_output=(CONFIG['LOG_LEVEL'] <= logging.INFO)
        )
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
    except Exception as e:
        logger.critical(f"Server crashed: {e}")
        sys.exit(1)
