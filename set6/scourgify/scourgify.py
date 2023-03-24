import sys
import csv

info = {}
if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            students = dict.reader(file)
            for row in students:
                info.append(row)
    print(info)


