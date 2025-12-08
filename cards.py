import random
import printing as p

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
        # Execute twice
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
    return player_hand, dealer_hand

def calculate_points(hand):
    # Index 2 corresponds to card value
    return sum([card[2] for card in hand])

def set_ace_value(card, points):
    if points > 21:
        card[2] = 1
    else:
        # Exception handling is not necessary here since the while loop condition forces ace_value to be either "1" or "11"
        while (ace_value := input("Choose a value for the ace (1/11): ")) not in ["1", "11"]:
            p.print_invalid_input()
        card[2] = int(ace_value)
        print()
    return card
