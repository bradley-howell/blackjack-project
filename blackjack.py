import random
import db

def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")

def create_deck():
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "King", "Queen", "Jack", "10",
             "9", "8", "7", "6", "5", "4", "3", "2"]
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = 11
            elif rank in ["King", "Queen", "Jack"]:
                value = 10
            else:
                value = int(rank)
            card = [suit, rank, value]
            deck.append(card)
    return deck

def deal_cards(deck):
    random.shuffle(deck)
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    return player_hand, dealer_hand

def calculate_points(hand):
    return sum([card[2] for card in hand])

def set_ace_value(hand):
    for card in hand:
        if card[1] == "Ace":
            points = calculate_points(hand)
            if points > 21:
                card[2] = 1
            else:
                while (ace_value := input("Choose a value for the ace (1/11): ")) not in ["1", "11"]:
                    print("Invalid value.")
                card[2] = int(ace_value)
    return hand

def print_show_card(hand):
    print("\nDEALER'S SHOW CARD")
    print(f"{hand[0][1]} of {hand[0][0]}")

def print_cards(hand):
    for card in hand:
        print(f"{card[1]} of {card[0]}")
    print()

def get_valid_choice():
    while True:
        player_choice = input("Hit or stand (hit/stand): ").lower()
        if player_choice in ["hit", "stand"]:
            return player_choice
        else:
            print("Invalid choice.")
            
def play_round(money, deck):
    print(f"Money: {money:.2f}")
    bet_amount = float(input("Bet amount: "))
    player_hand, dealer_hand = deal_cards(deck)
    print_show_card(dealer_hand)
    print("\nYOUR CARDS:")
    print_cards(player_hand)
    player_hand = set_ace_value(player_hand)
    dealer_hand = set_ace_value(dealer_hand)
    player_points = calculate_points(player_hand)
    dealer_points = calculate_points(dealer_hand)
    
    while player_points <= 21:
        player_choice = get_valid_choice()
        if player_choice == "hit":
            player_hand.append(deck.pop())
            print("\nYOUR CARDS:")
            print_cards(player_hand)
            player_hand = set_ace_value(player_hand)
            player_points = calculate_points(player_hand)
            if player_points > 21:
                print("\nSorry. You lose.")
                money -= bet_amount
        else:
            break

    if player_points == 21:
        if dealer_points != 21:
            print("\nBlackjack!")
            money += 1.5 * bet
        elif dealer_points == 21:
            print("\nIt's a tie.")
        
    if player_points < 21:
        print("\nDEALER'S CARDS:")
        print_cards(dealer_hand)
        
        print(f"YOUR POINTS:     {player_points}")
        print(f"DEALER'S POINTS: {dealer_points}")
        if dealer_points < player_points or dealer_points > 21:
            print("\nYou win!")
            money += bet_amount
        elif dealer_points == player_points:
            print("\nIt's a tie.")
        else:
            print("\nSorry. You lose.")
            money -= bet_amount

    db.write_money(money)
    print(f"Money: {money:.2f}")
        
def main():
    display_title()
    
    #money = db.read_money()
    #deck = create_deck()
    #play_round(money, deck)

    hand = set_ace_value([["Spades", "Ace", 11]])
    print(hand)
    
if __name__ == "__main__":
    main()
