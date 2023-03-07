import random

try:
    level = int(input("Level: "))
    n = random.randint(1, level)
while True:

    if level >= 1 and level <= 10:
        guess = int(input("Guess: "))
        if guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            print("Just right!")
            break


