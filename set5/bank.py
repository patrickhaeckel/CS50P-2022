def main():
    greeting = input("say hello ").replace(" ", "").casefold()
    print(value(greeting))


def value(word):
    if word.startswith("hello"):
        return("$0")
    elif word.startswith("h"):
        return("$20")


if __name__ == "__main__":
    main()



