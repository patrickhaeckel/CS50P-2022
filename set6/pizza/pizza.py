import sys
import csv
from tabulate import tabulate

menu = []
while True:
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

        elif len(sys.argv) == 2:
            if sys.argv[1].endswith(".csv"):
                with open(sys.argv[1], "r") as file:
                    table = csv.reader(file)
                    for row in table:
                        menu.append(row)
            else:
                sys.exit("Not a Python file")
            print(tabulate(menu[1:], headers=menu[0], tablefmt="grid"))
            break

    except FileNotFoundError:
            sys.exit("File does not exist")
