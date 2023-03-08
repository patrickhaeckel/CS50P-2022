import random
import sys
def main():
    level = get_level()
    score = sim_game(level)
    print(f"Score: {score}/10")




def sim_round(x, y):
    eeecounter = 1
    while eeecounter <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                eeecounter += 1
                print("EEE")
        except:
            eeecounter += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False

def get_level():
    while True:
        try:
            level = int(input("level "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(level):
    while True:
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)

        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)

        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        return x,y

def sim_game(level):
    counter = 1
    score = 0
    while counter <= 10:
        x, y = generate_integer(level)
        response = sim_round(x, y)
        if response == True:
            score +=1
            counter +=1
        else:
            counter += 1
    return score

if __name__ == "__main__":
    main()