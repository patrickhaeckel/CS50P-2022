import sys

n = 0
with open("linestxt.py", "r") as file:
    lines = file.readlines()
for line in lines:
    n += 1
    print(line)
print(n)

