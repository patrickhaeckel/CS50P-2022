import sys
import csv

output = []
if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith("csv"):
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_name = row["name"].split(",")
                output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": split_name[2]})





