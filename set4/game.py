import random

while True:
    level = int(input("Level: "))
    n = random.randint(1, level)
    if level >= 1 and level <= 10:
        guess = int(input("Guess: "))
        if guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            print("Just right!")
            break


