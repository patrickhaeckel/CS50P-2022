k = 0
v = 0
dict = {k}
while True:
    try:
        k = input("key ")
        v = input("value ")
        dict = dict, {k}
        print(dict)
    except:
        break


