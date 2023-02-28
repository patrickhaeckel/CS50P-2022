grocery = {}
while True:
    try:
        item = input("item ")
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
        print(grocery)


    except EOFError:
        print(end = "\n")
        break


