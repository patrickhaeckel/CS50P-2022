def main():
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    text = input("Your text here ")
    for i in vocals:
        text = text.replace(i, "")
    print(text)


main()


