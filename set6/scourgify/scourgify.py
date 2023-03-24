import sys
import csv

info = []
if len(sys.argv) == 3:
    if sys.argv[1].endswith(".csv"):
        with open(sys.argv[1], "r") as file:
            students = csv.DictReader(file)
            for row in students:
                info.append(row)
    print(info)
        with open(sys.argv[2], "a") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "home"])
            writer.writerow({"name": name, "home": home})


