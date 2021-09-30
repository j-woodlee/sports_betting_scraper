import apikeys
import requests
import json

API_KEY = apikeys.get_keys()

sports_response = requests.get('https://api.the-odds-api.com/v4/sports', params={
    'api_key': API_KEY
})

sports_response_json = sports_response.json()

if sports_response.status_code != 200:
    print("Failed to get sports: status_code {sports_response.status_code}, response body {sports_response.text}")

# print(sports_response_json)

for sport in sports_response_json:
    print(sport['key'])
    