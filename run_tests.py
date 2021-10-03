import test_api
import parse_data

#odds_json is a list of events

odds_json = test_api.mma_1()

parse_data.parse_data(odds_json)
