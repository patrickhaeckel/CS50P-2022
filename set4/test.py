import random
import sys
while True:
        try:
            level = int(input("Level: "))
            n = random.randint(1, level)
            otra(level, n)
        except ValueError:
            main()

def otra(level, n):
    while True:
        if level >= 1 and level <= 10:
                guess = int(input("Guess: "))
                if guess > n:
                    print("Too large!")
                    otra(level, n)
                elif guess < n:
                    print("Too small!")
                    otra(level, n)
                else:
                    sys.exit("just right!")

main()