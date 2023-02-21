def main():
    camelCase = input("camelCase: ")
    print("snake_case: ", end="")
    snake_case(camelCase)


def snake_case(camelCase):
    for letter in camelCase:
        if letter.isupper():
            print("_" + letter.lower(), end="")
        else:
            print(letter, end="")
    print()
main()