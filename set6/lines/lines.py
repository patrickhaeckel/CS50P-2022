import sys

while True:
    try:
        n = 0
        if len(sys.argv) == 2:
            if sys.argv[1].endswith(".py"):

                with open(sys.argv[1], "r") as file:
                    lines = file.readlines()
                for line in lines:
                    if line[0] == "#" or line == "\n":
                        n = n
                    else:
                        n += 1
                print(n)
                break

            else:
                sys.exit("Invalid extension")
        else:
            sys.exit("Too many command-line arguments")
    except:
        raise




