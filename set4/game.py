from random import randint
while True:
    try:
        level = int(input("Level: "))
        guess = int(input("Guess: "))
        if level >= 1 and level <=10:
            n = level.randint()
            print(n)

    except(ValueError):
        print(level, guess)

