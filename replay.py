import cv2 
camera = cv2.VideoCapture(1)

from datetime import datetime, timedelta
import time 

def get_camera_frame():
    success, frame = camera.read()  # read the camera frame
    if success:
        return frame
    else:
        print("unsuccessfully loaded frame")
        return

def save_every_hour():
    while True:
        dt = datetime.now() + timedelta(minutes=15)

        filename = f"images/{dt}.jpg"
        frame = get_camera_frame()
        cv2.imwrite(filename, frame)

        while datetime.now() < dt:
            time.sleep(1)

if __name__ == "__main__":
    save_every_hour()