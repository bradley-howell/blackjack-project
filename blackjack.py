import random

def read_money():
    try:
        with open("money.txt", "r") as file:
            money = float(file.readline())
    except FileNotFoundError:
        money = 100
    return money

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))

def display_title():
    print("BLACKJACK!")
    print("Blacjack payout is 3:2\n")

def create_deck():
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "King", "Queen", "Jack", "10",
             "9", "8", "7", "6", "5", "4", "3", "2"]
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank == "Ace":
                value = None
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
        
def play_round(money, player_hand, dealer_hand):
    print(f"Money: {money:.2f}")
    bet_amount = float(input("Bet amount: "))
    print("\nDEALER'S SHOW CARD")
    print(f"{dealer_hand[0][1]} of {dealer_hand[0][0]}")
    print("\nYOUR CARDS:")
    for i in range(2):
        print(f"{player_hand[i][1]} of {player_hand[i][0]}")

def main():
    display_title()
    money = read_money()
    deck = create_deck()
    player_hand, dealer_hand = deal_cards(deck)
    play_round(money, player_hand, dealer_hand)
    
if __name__ == "__main__":
    main()
