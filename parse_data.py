import test_api

def parse_data(events):
    for event in events:
        # get the highest prices for each team in the event
        team1highest = {"price": 0, "name": "", "bookmakers": []}
        team2highest = {"price": 0, "name": "", "bookmakers": []}

        for bookmaker in event['bookmakers']:
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    priceteam1 = market['outcomes'][0]['price']
                    priceteam2 = market['outcomes'][1]['price']
                    
                    if team1highest['price'] < priceteam1:
                        team1highest['price'] = priceteam1
                        team1highest['name'] = market['outcomes'][0]['name']
                        team1highest['bookmakers'] = [bookmaker['title']]
                    elif team1highest['price'] == priceteam1:
                        team1highest['bookmakers'].append(bookmaker['title'])

                    if team2highest['price'] < priceteam2:
                        team2highest['price'] = priceteam2
                        team2highest['name'] = market['outcomes'][1]['name']
                        team2highest['bookmakers'] = [bookmaker['title']]
                    elif team2highest['price'] == priceteam2:
                        team2highest['bookmakers'].append(bookmaker['title'])


        implied_prob_sum = get_implied_probability_sum(team1highest['price'], team2highest['price'])
        print(implied_prob_sum)
        if (implied_prob_sum < 1):
            implied_prob1 = 1 / team1highest['price']
            implied_prob2 = 1 / team2highest['price']
            print("Sport Key: " + event["sport_key"])
            print ("Highest for " + team1highest['name'] + " is " + str(team1highest['price']) + " at")
            print (team1highest['bookmakers'])

            print ("Highest for " + team2highest['name'] + " is " + str(team2highest['price']) + " at")
            print(team2highest['bookmakers'])
            # get_bet(implied_prob1, implied_prob2)
            print 


def get_bet(prob1, prob2):
    wiggle_room = 1 - (prob1 + prob2)
    prob1 += wiggle_room / 2
    prob2 += wiggle_room / 2

    # print("bet on away team" : prob1)
    print prob2


def get_implied_probability_sum(highest1, highest2):
    implied_prob = ((1 / highest1) + (1 / highest2))
    return implied_prob