import sys
import csv

if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            students = csv.DictReader(file)
            with open(sys.argv[2], "w") as file2:
                writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])



