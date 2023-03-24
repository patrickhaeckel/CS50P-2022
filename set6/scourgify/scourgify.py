import sys
import csv

info = []
if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            students = csv.DictReader(file)
            for row in students:
                info.append(row)

        with open(sys.argv[2], "a") as file2:
            writer = csv.DictWriter(file2, fieldnames=["name", "home", ])



