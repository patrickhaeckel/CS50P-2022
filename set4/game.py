import random
level = int(input("Level: "))
n = random.randint(1, level)
while True:
    try:
        if level >= 1 and level <=10:
            guess = int(input("Guess: "))
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")
                break
    except ValueError:
        print("hubo error")
            break

