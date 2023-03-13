def main():
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]


def shorten(word):

    word = input("Your text here ")
    for i in vocals:
        word = word.replace(i, "")
    print(word)


if __name__ == "__main__":
    main()