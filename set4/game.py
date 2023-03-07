import random
leveltest = 0
while True:
        try:
            level = int(input("Level: "))
            leveltest = level
            if leveltest >= 1 and leveltest <= 10:
                n = random.randint(1, leveltest)
        except ValueError:
            break

        if level >= 1 and level <= 10:
            guess = int(input("Guess: "))
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")
                break

