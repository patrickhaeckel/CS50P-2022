def main():
    value(greeting)


def value(greeting):
    greeting = input("say hello ").replace(" ", "").casefold()
    if greeting.startswith("hello"):
        return("$0")
    elif greeting.startswith("h"):
        return("$20")


if __name__ == "__main__":
    main()



