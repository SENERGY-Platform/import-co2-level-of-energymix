# https://api.co2signal.com/v1/latest?countryCode=DE

import requests
from datetime import datetime

with open('credentials.json', 'r') as f:
    import json
    credentials = json.loads(f.read())

api_key = credentials['api_key']

url = 'https://api.co2signal.com/v1/latest?countryCode=DE'
headers = {'auth-token': f'{api_key}'}


def co2DataFetcher():
    dateneingang = requests.get(url, headers=headers).json()
    carbonIntensity = dateneingang['data']['carbonIntensity']
    fossilFuelPercentage = dateneingang['data']['fossilFuelPercentage']
    unit = dateneingang['units']['carbonIntensity']
    dateCo2 = datetime.strptime(dateneingang['data']['datetime'], "%Y-%m-%dT%H:%M:%S.%fz")
    dictCo2 = {
        "carbonIntensity": carbonIntensity,
        "fossilFuelPercentage": fossilFuelPercentage,
        "carbonIntensityUnit": unit
    }
    return dateCo2, dictCo2


