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
