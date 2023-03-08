import random
def main():
    level = get_level()
    x = 0
    y = 0
    generate_integer(level, x, y)
    counter = 0
    answer = 0
    eeecounter = 0
    if counter < 11:
        answer = int(input(f"{x} + {y} = "))
        if answer == (x + y):
            counter += 1
        elif answer != (x + y):
            eeecounter += 1
    if eeecounter == 3:
        print({x}+{y})

def gen_round()

def get_level():
    while True:
        try:
            level = int(input("level "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level

def generate_integer(level, x, y):
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
        return level, x, y

main()