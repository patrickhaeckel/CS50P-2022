k = 0
v = 0
dict = {k}
while True:
    try:
        k = input("key ")
        v = input("value ")
        dict = dict, {k:v}
        print(dict)
    except:
        break


