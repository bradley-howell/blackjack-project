def read_money():
    try:
        with open("money.txt", "r") as file:
            money = float(file.readline())
    except FileNotFoundError:
        return 0

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))

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

def main():
    deck = create_deck()
    for card in deck:
        print(card)
    
if __name__ == "__main__":
    main()
