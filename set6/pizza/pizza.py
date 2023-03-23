import sys
import csv

while True
    try:
        if len(sys.argv) == 2:
            with open(sys.argv[1], "r") as file:
                    table = csv.reader(file)
                    for row in reader