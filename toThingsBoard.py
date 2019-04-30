# Posting to ThingsBoard using HTTP POST. https://thingsboard.io/docs/reference/http-api/#attributes-api
import requests

ACCESS_TOKEN = 'DHT22_DEMO_TOKEN'
THINGSBOARD_HOST = 'demo.thingsboard.io:1883/api/vi/'+ACCESS_TOKEN+'/attributes'
HEADERS = "Content-Type:application/json"

def post(gps):
    data = {
        'latitude':gps.latitude
        'longitude':gps.longitude
        'TimeStamp':gps.ts
    }
    try:
        r = requests.post(THINGSBOARD_HOST, data=data, headers=HEADERS)
    except KeyboardInterrupt:
        pass
