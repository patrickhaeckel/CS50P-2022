grocery = {}
while True:
    try:
        item = input("item ")
        if item in grocery:
            grocery[item] = "ya esta"
        else:
            grocery[item] = "es nuevo"
        print(grocery)


    except EOFError:
        print(end = "\n")
        break


