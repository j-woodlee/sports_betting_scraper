import test_api

def parse_data(events):
    for event in events:
        # get the highest prices for each team in the event
        highestprice_team1 = 0
        highestprice_team2 = 0
        highestbookmaker_team1 = ""
        highestbookmaker_team2 = ""
        for bookmaker in event['bookmakers']:
            for markets in bookmaker['markets']:
                if markets['key'] == 'h2h':
                    priceteam1 = markets['outcomes'][0]['price']
                    priceteam2 = markets['outcomes'][1]['price']

                    if highestprice_team1 < priceteam1:
                        highestbookmaker_team1 = bookmaker['title']
                        highestprice_team1 = priceteam1

                    if highestprice_team2 < priceteam2:
                        highestbookmaker_team2 = bookmaker['title']
                        highestprice_team2 = priceteam2

        # calculate arbitrage opportunity with highest prices
        # print(highestprice_team1)
        # print(highestprice_team2)
        # print
        implied_prob = get_implied_probability(highestprice_team1, highestprice_team2)
        print(implied_prob)
        if (implied_prob < 1):
             print("Home team: " + event["home_team"])
             print("Away team: " + event["away_team"])
             print("Sport Key: " + event["sport_key"])
             print(highestbookmaker_team1)
             print(highestbookmaker_team2)
             print(highestprice_team1)
             print(highestprice_team2)
             print




def get_implied_probability(highest1, highest2):
    implied_prob = ((1 / highest1) + (1 / highest2))
    return implied_prob