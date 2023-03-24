import sys
import csv

if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith("csv"):
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
          



