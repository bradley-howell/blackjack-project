def read_money():
    try:
        with open("money.txt", "r") as file:
            money = float(file.readline())
    except FileNotFoundError:
        return 0

def write_money(money):
    with open("money.txt", "w") as file:
        file.write(str(money))

def main():
    money = read_money()
    write_money(money)
    
if __name__ == "__main__":
    main()
