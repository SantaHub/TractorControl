# Main controller program
from readFromSIm7600 import read
from NetworkCheck.py import internet_check
from toThingsBoard import post
import time

INTERVAL=2

def writeData(gps_data):
    file=open('GPS_Data.txt','w')
    
    print("writing "+gps_data)
    data = "{'latitude':"+gps_data.latitude+",'longitude':"+gps.longitude+"}"
    file.write(data+"\n")
    file.close()

def getLatLong(lat,lon):
    gps_data = [{'latitude' : lat},{'longitude': lon}
    return  gps_data

def main():

    while True :
        gps_data = read()
        if(internet_check()):
            post(gps_data)
        else :
            writeData(gps_data)
        
        time.sleep(INTERVAL)