def main():
    message = input("Your text here ")
    print(shorten(message))

def shorten(word):
    vocals = ["a", "e", "i", "o", "u"]
    for i in vocals:
        word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()