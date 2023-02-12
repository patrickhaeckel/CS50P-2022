def main():
    q = input("whos god? ").title
    match q:
        case "42" | "Forty Two" | "forty-two":
            print("Yes")
        case _:
            print("No")
main()