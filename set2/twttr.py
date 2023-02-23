def main():
    vocals = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U").split()
    text = input("Your text here ").replace(vocals, "")
    print(text)

main()


