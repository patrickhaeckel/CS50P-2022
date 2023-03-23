import sys

while True:
    n = 0
    x = sys.argv[1]
    if x[-1:-3] == "yp.":
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


