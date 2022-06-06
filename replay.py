from datetime import datetime, timedelta
import time 
import requests

def save_every_hour():
    while True:

        # requests.get('http://71.255.58.230/save_frame')
        requests.get('http://localhost:80/save_frame')

        dt = datetime.now() + timedelta(minutes=15)

        while datetime.now() < dt:
            time.sleep(1)

if __name__ == "__main__":
    save_every_hour()