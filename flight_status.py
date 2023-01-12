import json
import requests
from dotenv import load_dotenv
import os
from pprint import pprint
load_dotenv()

FLIGHT_TRACKING = os.getenv("FLIGHT_TRACKING")

# r = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_TRACKING}")
# pprint(r.text)

api_result = requests.get(f"http://api.aviationstack.com/v1/flights?access_key={FLIGHT_TRACKING}")

api_response = api_result.json()

with open("response.json","w")as f:
    f.write(json.dumps(api_response))

flight_info = api_response.get ("data") [0]
flight_date = flight_info.get("flight_date")
flight_status = flight_info.get("flight_status")
departure = flight_info.get("departure")
arrival = flight_info.get("arrival")
airline = flight_info.get("airline")

pprint(f"Flight date {flight_date}")
pprint(f"Flight status {flight_status}")
pprint(f"Departure {departure}")
pprint(f"Arrival {arrival}")
pprint(f"Airline {airline}")
