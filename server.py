# server.py
from flask import Flask, send_from_directory, request
import socketio
import eventlet
import eventlet.wsgi
import os
import time

# virtual gamepad libs (Windows: vgamepad + ViGEm)
try:
    import vgamepad as vg
    from vgamepad import XUSB_BUTTON
    VGAMEPAD_AVAILABLE = True
except Exception as e:
    print("vgamepad not available:", e)
    VGAMEPAD_AVAILABLE = False

# Flask + python-socketio (eventlet mode)
sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')
app = Flask(__name__, static_folder='static', static_url_path='/static')
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# create virtual gamepad if available
gamepad = None
if VGAMEPAD_AVAILABLE:
    try:
        gamepad = vg.VX360Gamepad()
        print("Virtual X360 gamepad created.")
    except Exception as e:
        print("Failed to create virtual gamepad:", e)
        gamepad = None

# helper: clamp
def clamp(x, a=-1.0, b=1.0):
    return max(a, min(b, x))

# mapping buttons to vgamepad enum
BUTTON_MAP = {
    'A': XUSB_BUTTON.XUSB_GAMEPAD_A,
    'B': XUSB_BUTTON.XUSB_GAMEPAD_B,
    'X': XUSB_BUTTON.XUSB_GAMEPAD_X,
    'Y': XUSB_BUTTON.XUSB_GAMEPAD_Y,
    'LB': XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    'RB': XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    'START': XUSB_BUTTON.XUSB_GAMEPAD_START,
    'BACK': XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    # ARM is not XInput standard; map to a spare button (e.g. X)
    'ARM': XUSB_BUTTON.XUSB_GAMEPAD_X
}

# Keep last values (simple smoothing optional)
last_values = {'left': {'x':0.0,'y':0.0}, 'right': {'x':0.0,'y':0.0}}

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# serve other static automatically via Flask static folder
# socket handlers
@sio.event
def connect(sid, environ):
    print('Client connected', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected', sid)

@sio.on('joystick')
def on_joystick(sid, data):
    """
    data: {stick:'left'|'right', x:float, y:float}
    x,y expected floats in [-1,1], with y: up positive
    """
    stick = data.get('stick')
    x = float(data.get('x',0.0))
    y = float(data.get('y',0.0))
    x = clamp(x,-1.0,1.0)
    y = clamp(y,-1.0,1.0)
    # simple smoothing (exponential)
    alpha = 0.3
    lv = last_values.get(stick, {'x':0.0,'y':0.0})
    nx = (1-alpha)*x + alpha*lv['x']
    ny = (1-alpha)*y + alpha*lv['y']
    last_values[stick]['x'] = nx
    last_values[stick]['y'] = ny

    # send to virtual pad if available
    if gamepad is not None:
        try:
            if stick == 'left':
                # left stick: map directly
                gamepad.left_joystick_float(x_value_float=nx, y_value_float=ny)
            else:
                gamepad.right_joystick_float(x_value_float=nx, y_value_float=ny)
            gamepad.update()
        except Exception as e:
            print("Error updating gamepad:", e)

@sio.on('button')
def on_button(sid, data):
    """
    data: {btn:'A'|'B'|..., state:'down'|'up'}
    """
    btn = data.get('btn')
    state = data.get('state')
    print("button", btn, state)
    if gamepad is not None and btn in BUTTON_MAP:
        try:
            b = BUTTON_MAP[btn]
            if state == 'down':
                gamepad.press_button(button=b)
            else:
                gamepad.release_button(button=b)
            gamepad.update()
        except Exception as e:
            print("button mapping error:", e)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("Starting server on port", port)
    # eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', port)), app)
