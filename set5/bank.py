def main():
    greeting = input("say hello ").strip().lower()
    toprint = value(greeting)
    print(f"${toprint}")


def value(greeting):
    if "hello" in greeting:
        return(0)
    elif greeting.startswith("h"):
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()



