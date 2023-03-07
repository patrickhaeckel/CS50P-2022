import random
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 10:
                otra(level)
        except ValueError:
            main()
def otra(level):
    if level >= 1 and level <= 10:
            n = random.randint(1, level)
            guess = int(input("Guess: "))
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")

main()