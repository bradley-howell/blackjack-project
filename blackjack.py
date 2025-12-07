import sys
import db
import cards
import printing as p

def exit_progam():
    print("Exiting program. Bye!")
    sys.exit()

def get_valid_choice():
    while True:
        player_choice = input("Hit or stand (hit/stand): ").lower()
        if player_choice in ["hit", "stand"]:
            return player_choice
        else:
            p.print_invalid_input()

def buy_chips():
    choice = input("Would you like to buy more chips? (y/n): ").lower()
    if choice == "y":
        while True:
            try:
                money = int(input("Enter the number of chips you would like to buy: "))
                if money < 5:
                    p.print_chips_message()
                    continue
                else:
                    print()
                    db.write_money(money)
                    return money
            except ValueError:
                p.print_invalid_input()
    else:
        exit_progam()

def get_bet_amount(money):
    while True:
        try:
            bet_amount = float(input("Bet amount: "))
            if 5 <= bet_amount <= min(1000, money):
                return bet_amount
            else:
                p.print_bet_message()
        except ValueError:
            p.print_invalid_input()
            
def play_round(money, deck):
    p.print_money(money)
    bet_amount = get_bet_amount(money)
    player_hand, dealer_hand = cards.deal_cards(deck)
    p.print_show_card(dealer_hand)
    p.print_cards(player_hand, player = True)

    player_points = cards.calculate_points(player_hand)
    for card in player_hand:
        # Index 1 corresponds to card rank
        if card[1] == "Ace":
            card = cards.set_ace_value(card, player_points)
            # Recalculate points after setting ace value
            player_points = cards.calculate_points(player_hand)
    
    while player_points <= 21:
        player_choice = get_valid_choice()
        if player_choice == "hit":
            draw = deck.pop()
            player_hand.append(draw)
            p.print_cards(player_hand, player = True)
            player_points = cards.calculate_points(player_hand)
            if draw[1] == "Ace":
                # Updating the draw variable also updates player_hand
                draw = cards.set_ace_value(draw, player_points)
                # Recalculate points after setting ace value
                player_points = cards.calculate_points(player_hand)
            if player_points > 21:
                p.print_points(player_points, player = True)
                print("Bust.")
                money -= bet_amount
                db.write_money(money)
                p.print_money(money)
                # Remaining code is not executed because round is over
                return
        else:
            # Remaining code is executed because choice is "stand"
            break

    # Dealer's turn
    while (dealer_points := cards.calculate_points(dealer_hand)) < 17:
        # Continue drawing cards until dealer_points >= 17
        dealer_hand.append(deck.pop())

    p.print_cards(dealer_hand, dealer = True)
    p.print_points(player_points, dealer_points, player = True, dealer = True)

    if player_points == dealer_points:
        print("It's a tie.")      
    elif player_points == 21:
        # Already checked that it's not a tie
        print("Blackjack!")
        money += 1.5 * bet_amount   
    elif dealer_points < player_points or dealer_points > 21:
        print("You win!")
        money += bet_amount
    else:
        # Only remaining case is player_points < dealer_points <= 21
        print("Sorry. You lose.")
        money -= bet_amount

    db.write_money(money)
    p.print_money(money)
        
def main():
    p.print_title()

    while True:
        money = db.read_money()
        if money < 5:
            money = buy_chips()
        # New deck is initialized for every round
        deck = cards.create_deck()
        play_round(money, deck)
        if (again := input("\nPlay again? (y/n): ").lower()) != "y":
            break
        else:
            print()
        
    p.print_bye()
    
if __name__ == "__main__":
    main()
