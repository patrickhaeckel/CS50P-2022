v = input("name of variable ")
for i in v:
       if i.isupper():
           print("_" + i.lower(), end="")
       else:
              print(i, end="")

print()

