def main():
    q = input("whos god? ").replace("-", " ").strip().upper().lower()
    print (q)
    match q:
        case "42" | "forty two" | "FORTY TWO":
            print("Yes")
        case _:
            print("No")
main()
