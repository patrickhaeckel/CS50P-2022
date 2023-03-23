import sys

while True:
    n = 0
    if sys.argv[1] == ".":
        print("yes")

        with open("linestxt.py", "r") as file:
            lines = file.readlines()
        for line in lines:
            if line[0] == "#" or line == "\n":
                n = n
            else:
                n += 1
    print(n)
    break


