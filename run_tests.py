import apikeys
import requests
import json
import test_api
import parse_data

#odds_json is a list of events

odds_json = test_api.test_response5()

parse_data.parse_data(odds_json)
