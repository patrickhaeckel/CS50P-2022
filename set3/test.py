while True:
    try:
        x = int(input("whats x? "))
        print(f"x is {x}")
    except ValueError:
        print("x is not an integer")



