# RTSP-wifi-camera

# 🛡️ Security Overwatch 1.0

> Lightweight, low-latency multi-camera RTSP viewer built with Python and OpenCV.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Raspberry%20Pi-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

Security Overwatch is a lightweight DIY security camera viewer that displays multiple RTSP camera feeds in a single window with minimal latency.

Designed for Raspberry Pi, home servers, and always-on monitoring stations, it avoids the delays commonly experienced when viewing RTSP streams through OpenCV.

---

## ✨ Features

- 🚀 Low-latency RTSP streaming using custom FFmpeg flags
- 🧵 Dedicated thread per camera
- 🔄 Automatic reconnect when a camera goes offline
- 📺 Live 2×2 camera grid
- 💻 Lightweight OpenCV rendering
- 🏠 Optimized for Raspberry Pi and home server dashboards
- 📡 Supports any RTSP-compatible IP camera (Tapo, Hikvision, Dahua, Reolink, etc.)

---

## 📷 Screenshot

> *Add a screenshot or GIF of the application after your first release.*

```
+----------------------+----------------------+
| Camera 1             | Camera 2             |
|                      |                      |
+----------------------+----------------------+
| Camera 3             | Camera 4             |
|                      |                      |
+----------------------+----------------------+
```

---

# Requirements

- Python 3.9 or newer
- OpenCV
- NumPy

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install opencv-python numpy
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/kalu47/RTSP-wifi-camera.git

cd RTSP-wifi-camera
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configure your cameras

Open `main.py` and replace the example RTSP URLs with your own.

Example:

```python
rtsp_cam1 = "rtsp://username:password@192.168.1.2:554/stream1"
rtsp_cam2 = "rtsp://username:password@192.168.1.12:554/stream1"
```

### Tapo Camera Users

To enable RTSP on Tapo cameras:

1. Open the **Tapo** app.
2. Select your camera.
3. Go to **Settings → Advanced Settings → Camera Account**.
4. Create a camera username and password.
5. Use those credentials in your RTSP URL.

---

## Running the application

```bash
python main.py
```

Press **Q** while the window is focused to exit safely.

---

# Project Structure

```
RTSP-wifi-camera/
│
├── main.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# Performance

Security Overwatch minimizes RTSP latency by:

- Disabling FFmpeg buffering
- Forcing TCP transport for stable streaming
- Running every camera on its own dedicated thread
- Continuously reading only the newest available frame
- Automatically reconnecting if a camera disconnects

This keeps camera feeds as close to real-time as possible while remaining lightweight enough for Raspberry Pi and low-power home servers.

---

# Customization

## Change Grid Size

The display grid is generated using:

```python
np.hstack()
np.vstack()
```

You can easily modify the layout to display:

- 2 Cameras
- 4 Cameras
- 6 Cameras
- 8 Cameras
- 16 Cameras

---

## Reduce CPU Usage

If you're using older hardware:

- Reduce the tile resolution.
- Switch from `stream1` to the lower-resolution `stream2`.
- Lower the camera FPS.
- Reduce the number of simultaneously displayed cameras.

---

# Troubleshooting

## Stream is delayed

If your stream falls behind real time, switch to your camera's substream.

```
stream1 → Full Resolution
stream2 → Lower Resolution (Recommended)
```

Substreams require significantly less decoding power and help maintain smooth, low-latency playback.

---

## Camera Offline

If a camera disconnects, Security Overwatch will:

- Detect the connection loss
- Display a placeholder frame
- Continuously attempt to reconnect

No application restart is required.

---

# Roadmap

- [ ] Motion detection
- [ ] Snapshot capture
- [ ] Video recording
- [ ] Hardware-accelerated decoding
- [ ] Web dashboard
- [ ] ONVIF camera discovery
- [ ] Docker support
- [ ] Full-screen kiosk mode
- [ ] Configuration file support (JSON/YAML)

---

# Contributing

Contributions are always welcome!

If you find a bug, have a feature request, or would like to improve the project, feel free to open an Issue or submit a Pull Request.

---

# License

This project is released under the **MIT License**.

---

Made with ❤️ for DIY home labs, Raspberry Pi enthusiasts, and self-hosted security systems.