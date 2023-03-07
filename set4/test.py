import random
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level >= 1 and level <= 10:
                n = random.randint(1, level)
                otra(n)
        except ValueError:
            main()
def otra(n):
    if level >= 1 and level <= 10:
            guess = int(input("Guess: "))
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")

main()