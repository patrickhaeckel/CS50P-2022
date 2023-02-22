def main():
    list = [25, 10, 5]
    amountdue = 50
    while amountdue > 0:
        print(f"amount due = {amountdue}")
        coin = int(input("Insert a coin "))
        if coin in list:
            amountdue = amountdue - coin
            print(amountdue)
    if amountdue < 0:
        print("change owed ", (amountdue *(-1)))

main()
