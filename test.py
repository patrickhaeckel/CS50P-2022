while True:
    try:
        x = int(input("whats x? "))
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


