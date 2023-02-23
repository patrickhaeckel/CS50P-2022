def main():
    list = [25, 10, 5]
    amountdue = 50
    while amountdue > 0:
        print("Amount Due:", amountdue)
        coin = int(input("Insert a coin "))
        if coin in list:
            amountdue = amountdue - coin
    if amountdue < 0:
        print("Change Owed:", (amountdue *(-1)))
    elif amountdue == 0:
        print("Amount Due:", amountdue)

main()
