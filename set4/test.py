import random
import sys
def main():
    while True:
        try:
            level = int(input("Level: "))
            otra(level)
        except ValueError:
            main()

def otra(level):
    n = random.randint(1, level)
    while True:
        if level >= 1 and level <= 10:
                guess = int(input("Guess: "))
                if guess > n:
                    print("Too large!")
                    otra(level)
                elif guess < n:
                    print("Too small!")
                    otra(level)
                else:
                    
                    sys.exit("just right!")

main()