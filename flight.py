import http.client, urllib.parse
import json
import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()

FLIGHT_TRACKING = os.getenv("FLIGHT_TRACKING")

api_result = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_TRACKING}")

conn = http.client.HTTPConnection('api.positionstack.com')

params = urllib.parse.urlencode({
    'access_key': api_result,
    'query': 'Warsaw',
    'region': 'Europe',
    'limit': 1,
    })

conn.request('GET', '/v1/forward?{}'.format(params))

res = conn.getresponse()
data = res.read()

print(data.decode('utf-8'))