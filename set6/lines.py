import sys
n = 0
while True:
    try:
        if len(sys.argv) == 2:
            if sys.argv[-3:-1] == ".py":
                print ("yes")

        with open("linestxt.py", "r") as file:
            lines = file.readlines()
        for line in lines:
            if line[0] == "#" or line == "\n":
                n = n
            else:
                n += 1
        print(n)
    except:
        pass

