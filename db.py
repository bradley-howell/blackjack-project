import sys

def read_money():
    try:
        with open("money.txt", "r") as file:
            money = float(file.readline())
    except FileNotFoundError:
        print("Could not find the money file.")
        # The buy_chips function will be executed in the main module 
        money = 0
    except Exception as e:
        print(type(e), e)
        print("Exiting program. Bye!")
        sys.exit()
    return money

def write_money(money):
    with open("money.txt", "w") as file:
        # Money is a float value because bet_amount is a float
        file.write(str(round(money, 2)))
