import random
while True:
    try:
        level = int(input("Level: "))
        guess = int(input("Guess: "))
        if level >= 1 and level <=10:
            n = random.randint(1, level)
            print(n)

    except(ValueError):
        print(level, guess)

