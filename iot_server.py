from flask import Flask, send_from_directory, request, Response
import serial
import functools

# --- Setup Arduino Serial Connection ---
arduino = serial.Serial('COM5', 9600)  # ⚠️ Replace COM port

app = Flask(__name__)

# --- USERNAME & PASSWORD ---
USERNAME = "admin"
PASSWORD = "1234"

# --- BASIC AUTH DECORATOR ---
def require_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != USERNAME or auth.password != PASSWORD:
            return Response(
                'Unauthorized Access', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'}
            )
        return f(*args, **kwargs)
    return decorated

# --- Serve HTML dashboard ---
@app.route('/')
@require_auth
def serve_dashboard():
    return send_from_directory('.', 'dash.html')

# --- LED Control Endpoints ---
@app.route('/led/on')
@require_auth
def led_on():
    arduino.write(b'on\n')
    return "on"

@app.route('/led/off')
@require_auth
def led_off():
    arduino.write(b'off\n')
    return "off"

@app.route('/led/status')
@require_auth
def led_status():
    return "unknown"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
