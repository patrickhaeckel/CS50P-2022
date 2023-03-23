import sys
import csv

menu = []
while True:
    try:
        if len(sys.argv) == 2:
            with open(sys.argv[1], "r") as file:
                table = csv.reader(file)
                for row in reader:
                    menu.append(row)
            print(menu)
    except:
        raise
