import sys

n = 0
with open("linestxt.py", "r") as file:
    lines = file.readlines()
for line in lines:
    if line[0] == "#" or line == (""):
        n = n
    else:
        n += 1
print(n)

