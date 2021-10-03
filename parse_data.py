import test_api

def parse_data(events):
    for event in events:
        # get the highest prices for each team in the event
        team1highest = {"price": 0, "name": "", "bookmakers": []}
        team2highest = {"price": 0, "name": "", "bookmakers": []}
        team3highest = {"price": 0, "name": "", "bookmakers": []}

        for bookmaker in event['bookmakers']:
            if is_invalid_bookmaker(bookmaker['title']):
                continue
            for market in bookmaker['markets']:
                if market['key'] == 'h2h':
                    market_outcomes = market['outcomes']
                    priceteam1 = market_outcomes[0]['price']
                    priceteam2 = market_outcomes[1]['price']
                    
                    if team1highest['price'] < priceteam1:
                        team1highest['price'] = priceteam1
                        team1highest['name'] = market_outcomes[0]['name']
                        team1highest['bookmakers'] = [bookmaker['title']]
                    elif team1highest['price'] == priceteam1:
                        team1highest['bookmakers'].append(bookmaker['title'])

                    if team2highest['price'] < priceteam2:
                        team2highest['price'] = priceteam2
                        team2highest['name'] = market_outcomes[1]['name']
                        team2highest['bookmakers'] = [bookmaker['title']]
                    elif team2highest['price'] == priceteam2:
                        team2highest['bookmakers'].append(bookmaker['title'])

                    # if there is a draw condition
                    if len(market_outcomes) == 3:
                        priceteam3 = market_outcomes[2]['price']
                        if team3highest['price'] < priceteam3:
                            team3highest['price'] = priceteam3
                            team3highest['name'] = market_outcomes[2]['name']
                            team3highest['bookmakers'] = [bookmaker['title']]
                        elif team3highest['price'] == priceteam3:
                            team3highest['bookmakers'].append(bookmaker['title'])


        implied_prob_sum = get_implied_probability_sum(team1highest['price'], team2highest['price'], team3highest['price'])
        print(implied_prob_sum)
        if (implied_prob_sum < 1):

            implied_prob1 = 1 / team1highest['price']
            implied_prob2 = 1 / team2highest['price']
            implied_prob3 = 0


            print("Sport Key: " + event["sport_key"])
            print ("Highest for team 1 " + team1highest['name'] + " is " + str(team1highest['price']) + " or " + str(implied_prob1) + " at")
            print (team1highest['bookmakers'])

            print ("Highest for team 2 " + team2highest['name'] + " is " + str(team2highest['price']) + " or " + str(implied_prob2) + " at")
            print(team2highest['bookmakers'])

            if team3highest['price'] != 0:
                implied_prob3 = 1 / team3highest['price']
                print ("Highest for team 3 " + team3highest['name'] + " is " + str(team3highest['price']) + " or " + str(implied_prob3) + " at")
                print(team3highest['bookmakers'])
            
            
            get_bet(implied_prob1, implied_prob2, implied_prob3)

            print ("\n") 

# bet team 1 39.2857142857
# bet team 2 60.7142098443


def get_bet(prob1, prob2, prob3):
    wiggle_room = 1 - (prob1 + prob2)
    prob1 += (wiggle_room * prob1) / (prob1 + prob2 + prob3)
    prob2 += (wiggle_room * prob2) / (prob1 + prob2 + prob3)
    prob3 += (wiggle_room * prob3) / (prob1 + prob2 + prob3)

    # print prob1 + prob2

    # print("bet on away team" : prob1)
    print ("bet team 1 " + str(100 * prob1))
    print ("bet team 2 "  + str(100 * prob2))
    print ("bet team 3 " + str(100 * prob3))


def get_implied_probability_sum(highest1, highest2, highest3):
    implied_prob_sum = (1 / highest1) + (1 / highest2) 
    if highest3 != 0:
        implied_prob_sum += (1 / highest3)
    return implied_prob_sum

def is_invalid_bookmaker(bookmaker):
    list_of_invalid_bookmakers = ["BetRivers", "SugarHouse", "DraftKings", "Barstool Sportsbook"]
    return list_of_invalid_bookmakers.count(bookmaker) > 0