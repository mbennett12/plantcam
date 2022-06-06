import cv2 
camera = cv2.VideoCapture(1)

from flask import Flask, render_template, Response
app = Flask(__name__)

import glob
from natsort import natsorted
import time

# livestream hosted at localhost:80/
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            print("unsuccessfully loaded frames")
            return
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# replay of images in 'images/' hosted at localhost:80/replay
def get_replay_video():
    while True:
        sorted_image_files = natsorted(glob.glob(f'images/*'))
        for img_filename in sorted_image_files:
            frame = cv2.imread(img_filename)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            time.sleep(0.5)

@app.route('/replay')
def replay():
    return render_template('replay.html')

@app.route('/replay_video_feed')
def replay_video_feed():
    return Response(get_replay_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=80)