def print_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()

def print_money(money):
    print(f"Money: {money:.2f}")
    
def print_show_card(hand):
    print()
    print("DEALER'S SHOW CARD")
    print(f"{hand[0][1]} of {hand[0][0]}")

def print_cards(hand, player = False, dealer = False):
    # This function is only ever passed one argument of True
    print()
    if player:
        print("YOUR CARDS:")
    elif dealer:
        print("DEALER'S CARDS:")
    for card in hand:
        print(f"{card[1]} of {card[0]}")
    print()

def print_points(player_points = None, dealer_points = None, player = False, dealer = False):
    # Using named arguments so that not all arguments have to be passed
    # This function is sometimes passed two arguments of True
    if player and not dealer:
        # Less space in this case
        print(f"YOUR POINTS: {player_points}")
    if player and dealer:
        print(f"YOUR POINTS:     {player_points}")
    if dealer:
        print(f"DEALER'S POINTS: {dealer_points}")
    print()

def print_chips_message():
    print("Number of chips must be higher than minimum bet (5). Please try again.")
    print()

def print_bet_message():
    print("Bet amount must be between 5 and 1000, and no more than your current money.")
    print("Please try again.")
    print()

def print_invalid_input():
    print("Invalid input. Please try again.")
    print()

def print_bye():
    print()
    print("Come back soon!")
    print("Bye!")
        
