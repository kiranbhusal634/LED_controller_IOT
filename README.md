# IoT LED Control Dashboard

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Arduino](https://img.shields.io/badge/Arduino-Compatible-orange.svg)](https://www.arduino.cc/)

A simple web-based IoT dashboard to control an LED connected to an Arduino board. The dashboard allows users to turn the LED on/off remotely via a browser. It uses a Flask backend to handle HTTP requests and communicate with the Arduino over a serial connection.

This project is ideal for beginners in IoT, web development, and embedded systems. It demonstrates full-stack integration: HTML/CSS/JS frontend, Python Flask backend, and Arduino hardware.

## Features
- **Web Dashboard**: Clean, responsive UI with real-time status updates (ON/OFF).
- **Secure Access**: Basic HTTP authentication (username: `admin`, password: `1234`—change in production).
- **LED Control**: Endpoints for `/led/on`, `/led/off`, and `/led/status`.
- **Serial Communication**: Bidirectional serial link between Flask and Arduino for commands and status queries.
- **Error Handling**: Graceful fallbacks (e.g., defaults to "off" on errors) and logging for debugging.
- **CORS Support**: Allows access from any browser or device on the network.
- **Cross-Platform**: Works on Windows, macOS, and Linux (adjust serial ports accordingly).

## Demo
- Access the dashboard at `http://localhost:5000` (or your machine's IP:5000).
- Authenticate and use the buttons to toggle the LED.
- The status updates automatically on page load and after each action.


## Prerequisites
### Hardware
- Arduino board (e.g., Uno, Nano) with an LED connected to **pin 12** (anode to pin, cathode to GND via 220Ω resistor).
- USB cable for serial connection.

### Software
- **Python 3.7+** with pip.
- **Arduino IDE** for uploading the sketch.
- Libraries:
  - Python: `flask`, `flask-cors`, `pyserial` (install via `pip install -r requirements.txt`).
  - Arduino: None (standard libraries only).

### Development Environment
- A computer with serial port access (USB).
- Text editor (e.g., VS Code) for editing files.

## Installation
1. **Clone or Download the Repository**: 
2. **Set Up Python Environment**:
- Create a virtual environment (optional but recommended):
  ```
  python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
  ```
- Install dependencies:
  ```
  pip install -r requirements.txt
  ```

3. **Prepare the HTML Dashboard**:
- The `dash.html` file is already included.

4. **Upload Arduino Sketch**:
- Open Arduino IDE.
- Paste the code from `led_control.ino` into a new sketch.
- Select your board (e.g., Arduino Uno) and port (e.g., COM5 on Windows).
- Upload the sketch.
- Close the Serial Monitor if open (to free the port).

5. **Configure Flask App**:
- Open `app.py` and update `SERIAL_PORT` (e.g., `'COM5'` on Windows, `'/dev/ttyUSB0'` on Linux, `'/dev/cu.usbserial-*'` on macOS).
- Optionally, change `USERNAME` and `PASSWORD` for security.

## Usage
1. **Run the Flask Server**:
python app.py


Run
- Output: Logs connection to Arduino and server start (e.g., "Running on http://0.0.0.0:5000").
- The server listens on all interfaces (port 5000) for network access.

2. **Access the Dashboard**:
- Open a web browser and navigate to `http://localhost:5000` (local) or `http://YOUR_IP:5000` (e.g., from phone on same WiFi).
- Enter credentials: Username `admin`, Password `1234`.
- The dashboard loads with initial LED status (fetches from Arduino).
- Click **Turn ON** or **Turn OFF** to control the LED.
- Status updates in real-time; buttons disable when active.

3. **Test Serial Commands (Optional)**:
- Open Arduino Serial Monitor (9600 baud) and send "on", "off", or "status" to test directly.

4. **Network Access**:
- Find your computer's IP (e.g., `ipconfig` on Windows, `ifconfig` on macOS/Linux).
- Access from another device: `http://192.168.1.100:5000` (replace with your IP).

## API Endpoints
All endpoints require basic auth and return plain text:
- `GET /`: Serves the dashboard HTML.
- `GET /led/on`: Turns LED on, returns "on".
- `GET /led/off`: Turns LED off, returns "off".
- `GET /led/status`: Queries and returns current state ("on" or "off").

## Troubleshooting
- **Serial Connection Errors**:
- "Failed to connect": Check port in `app.py`, ensure Arduino is plugged in, and no other app (e.g., Serial Monitor) is using it.
- Restart Arduino after upload; wait 2-3 seconds before running Flask.
- On Linux/Mac: Add user to `dialout` group (`sudo usermod -a -G dialout $USER` and reboot).

- **LED Not Responding**:
- Verify wiring: LED positive to pin 12, negative to GND via resistor.
- Check Arduino Serial Monitor for incoming commands.
- Baud rate mismatch: Ensure 9600 in both Arduino and Flask.

- **Dashboard Issues**:
- "Failed to turn on LED": Check browser console (F12) for fetch errors; ensure CORS is enabled.
- Auth fails: Clear browser cache or use incognito mode.
- Status always "off": Test `/led/status` directly in browser (with auth).

- **Port Conflicts**:
- Change Flask port in `app.run(port=XXXX)`.
- Firewall: Allow port 5000 if accessing remotely.

- **Logs**: Check Flask console for errors (e.g., "Error sending command").
  ## Contributing
1. Fork the repo.
2. Create a feature branch (:
   

#Kiran Bhusal
