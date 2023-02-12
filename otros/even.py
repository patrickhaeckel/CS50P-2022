def main():
    x = int(input("whats x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

main()
