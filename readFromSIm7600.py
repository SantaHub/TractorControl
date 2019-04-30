# Reading GPS data from 7600

## Setup
# sudo pip install --upgrade RPi.GPIO

import RPi.GPIO as GPIO

def readGPS():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    gps_read = GPIO.input(4)
    ## Handle more Read errors
    if gps_read == -1:
        return {'latitude':None, 'longitude':None, 'ts':None}
    return gps_read


def read(retries=15, delay_seconds=2):
    for i in range(retries):
        gps = readGPS
        ## Process the gps into lat and long
        latitude = 0
        longitude =0
        if latitude is not None and longitude is not None:
            return (latitude, longitude)
        time.sleep(delay_seconds)
    return (None, None)

## GPS would need to be processed
