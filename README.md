# plantcam

Running a webcam feed to public IP on raspberry pi using OpenCV and Flask

First, you must attached a webcam to your computer. If you have multiple cameras attached, you can change the index of the camera that openCV uses on Line 2 of `plantcam.py` (from `0` to `1`, or to something else).

Then:
```
git clone https://github.com/mbennett12/plantcam
cd plantcam
pip install opencv-python
pip install Flask

python plantcam.py
```

Now your server should be running, and it can be accessed by going to:
`localhost:80` in a web browser.

You can also set up port-forwarding through your wifi admin settings to access the webcam from your wifi's public IP, and furthermore, you can use this public IP as the endpoint of an A Record if you'd like to have it accessible via a domain name.
