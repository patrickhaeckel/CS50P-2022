import sys

n = 0
with open("linestxt.py", "r") as file:
    lines = file.readlines()
for line in lines:
    if line[0] == "#":
        break
    n += 1
print(n)

