def main():
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    word = input("Your text here ")
    print(shorten(word))

def shorten(word):
    for i in vocals:
        word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()