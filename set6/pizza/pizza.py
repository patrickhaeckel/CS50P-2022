import sys
import csv
import tabulate

menu = []
while True:
    try:
        if len(sys.argv) == 2:
            with open(sys.argv[1], "r") as file:
                table = csv.reader(file)
                for row in table:
                    menu.append(row)

        print(tabulate(menu[1:], headers=menu[0]))
        break
    except:
        raise
