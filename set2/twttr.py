def main():
    vocals = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    text = input("Your text here ").split()
    for text in vocals:
        print(text).replace(vocals, "")

main()


