x = input("aqui ")
i = 1
while i <= len (x):
        if x[i].isdigit():
              if x[i:].isalpha():
                print("es el ultimo")
        i += 1
