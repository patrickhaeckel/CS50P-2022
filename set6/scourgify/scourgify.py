import sys
import csv
from tabulate import tabulate

info = {}
if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            students = csv.DictReader(file)
            for row in students:
                info.append
    print(info)


