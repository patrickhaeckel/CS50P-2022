def main():
    q = input("whos god? ").strip().upper().lower.replace("-"," ")
    match q:
        case "42" | "forty two" | "FORTY TWO":
            print("Yes")
        case _:
            print("No")
main()