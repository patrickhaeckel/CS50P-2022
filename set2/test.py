x = input("aqui ")
i = 0
while i <= len (x):
        try:

            if x[i].isdigit():
                print("es el ultimo")

            i += 1
            print(i)

        except IndexError:
             pass