# RTPS-wifi-camera-
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
- 🏠 Perfect for Raspberry Pi and home server dashboards

---

## 📷 Screenshot

> *(Add a screenshot here after your first release.)*

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

- Python 3.9+
- OpenCV
- NumPy

Install dependencies:

```bash
pip install opencv-python numpy
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/security-overwatch.git

cd security-overwatch
```

Configure your camera URLs inside `main.py`:

```python
rtsp_cam1 = "rtsp://username:password@192.168.1.2:554/stream1"
rtsp_cam2 = "rtsp://username:password@192.168.1.12:554/stream1"
```

> **Tapo Camera Users**
>
> Enable RTSP by creating a **Camera Account** inside the Tapo app:
>
> Settings → Advanced Settings → Camera Account

Run:

```bash
python main.py
```

Press **Q** to exit.

---

# Project Structure

```
security-overwatch/
│
├── main.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

# Performance

The application minimizes latency by:

- Disabling FFmpeg buffering
- Using TCP transport
- Running each camera in its own thread
- Continuously reading the newest frame
- Automatically reconnecting when streams fail

This keeps the display as close to real time as possible.

---

# Customization

### Change Grid Size

The display uses:

```python
np.hstack()
np.vstack()
```

You can modify these to support:

- 2 Cameras
- 4 Cameras
- 6 Cameras
- 8 Cameras
- 16 Cameras

---

### Reduce CPU Usage

If running on older hardware:

- Reduce tile resolution
- Use camera substreams (`stream2`)
- Lower the camera FPS

---

# Troubleshooting

## Stream is delayed

Use the substream:

```
stream1 → Full Resolution
stream2 → Low Resolution
```

Substreams greatly reduce CPU decoding load.

---

## Camera Offline

Security Overwatch automatically:

- Detects disconnects
- Displays a placeholder
- Reconnects automatically

No restart required.

---

# Roadmap

- [ ] Motion detection
- [ ] Snapshot capture
- [ ] Recording support
- [ ] Web dashboard
- [ ] Hardware acceleration
- [ ] Docker image
- [ ] ONVIF camera discovery

---

# Contributing

Contributions are welcome.

Feel free to open an Issue or submit a Pull Request.

---

# License

Released under the MIT License.

---

Made with ❤️ for DIY home labs, Raspberry Pi enthusiasts, and self-hosted security systems.