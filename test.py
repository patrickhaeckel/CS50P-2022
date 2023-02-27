try:
    x = int(input("whats x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


