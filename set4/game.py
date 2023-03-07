import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass

while True:
    try:
        if level >= 1 and level <= 10:
            guess = int(input("Guess: "))
            if guess > n:
                print("Too large!")
            elif guess < n:
                print("Too small!")
            else:
                print("Just right!")
                break
    except (ValueError, EOFError):
        break


