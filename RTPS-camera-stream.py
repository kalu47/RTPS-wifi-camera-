# RTSP streams
rtsp_cam1 = "rtsp://username:pass@192.168.1.2:554/stream1"
rtsp_cam2 = "rtsp://username:pass@192.168.1.12:554/stream1"
rtsp_cam3 = "rtsp://username:pass@192.168.1.19:554/stream1"
rtsp_cam4 = "rtsp://username:pass@192.168.1.22:554/stream1"

import cv2
import numpy as np
import threading
import time

# ==========================
# RTSP URLs
# ==========================

tile_w = 640
tile_h = 360


def placeholder(text):
    img = np.zeros((tile_h, tile_w, 3), dtype=np.uint8)
    cv2.putText(
        img,
        text,
        (40, tile_h // 2),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2,
    )
    return img


class RTSPCamera:
    def __init__(self, url, name):
        self.url = url
        self.name = name

        self.frame = placeholder(f"{name} Connecting...")
        self.lock = threading.Lock()

        self.running = True
        self.cap = None

        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def connect(self):
        """Connect to the RTSP stream."""
        if self.cap is not None:
            self.cap.release()

        print(f"[{self.name}] Connecting...")

        self.cap = cv2.VideoCapture(self.url, cv2.CAP_FFMPEG)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

        if self.cap.isOpened():
            print(f"[{self.name}] Connected.")
        else:
            print(f"[{self.name}] Connection failed.")

    def update(self):
        """Continuously read frames and reconnect if needed."""
        while self.running:

            if self.cap is None or not self.cap.isOpened():
                self.connect()
                time.sleep(1)
                continue

            ret, frame = self.cap.read()

            if not ret or frame is None:
                print(f"[{self.name}] Lost stream. Reconnecting...")
                self.connect()
                time.sleep(1)
                continue

            frame = cv2.resize(frame, (tile_w, tile_h))

            with self.lock:
                self.frame = frame

    def get_frame(self):
        with self.lock:
            return self.frame.copy()

    def stop(self):
        self.running = False
        self.thread.join(timeout=2)

        if self.cap is not None:
            self.cap.release()


# ==========================
# Start Cameras
# ==========================

cam1 = RTSPCamera(rtsp_cam1, "Camera 1")
cam2 = RTSPCamera(rtsp_cam2, "Camera 2")
cam3 = RTSPCamera(rtsp_cam3, "Camera 3")
cam4 = RTSPCamera(rtsp_cam4, "Camera 4")

# ==========================
# Window
# ==========================

window_name = "Security Overwatch 1.0"

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 1280, 720)

# ==========================
# Display Loop
# ==========================

while True:

    frame1 = cam1.get_frame()
    frame2 = cam2.get_frame()

    frame3 = cam3.get_frame()
    frame4 = cam4.get_frame()

    top = np.hstack((frame1, frame2))
    bottom = np.hstack((frame3, frame4))

    grid = np.vstack((top, bottom))

    cv2.imshow(window_name, grid)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# ==========================
# Cleanup
# ==========================

cam1.stop()
cam2.stop()
cam3.stop()
cam4.stop()

cv2.destroyAllWindows()
