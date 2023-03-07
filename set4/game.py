import random
while True:
    try:
        level = int(input("Level: "))
        if level >= 1 and level <=10:
            n = random.randint(1, level)
            guess = int(input("Guess: "))
            if guess > level:
                print("Too large!")
            elif guess < level:
                print("Too small!")
            else:
                print("Just right!")
                break

    except(ValueError):
        print(level, guess)

