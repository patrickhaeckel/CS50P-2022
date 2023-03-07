import random
level = int(input("Level: "))
while True:
    try:
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

    except ValueError:
        print("hubo error")
        break

