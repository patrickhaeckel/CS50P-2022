import random
level = int(input("Level: "))
while True:
    if level >= 1 and level <= 10:
        n = random.randint(1, level)
        guess = int(input("Guess: "))
        if guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            print("Just right!")
            break
    else:
        print(level)


