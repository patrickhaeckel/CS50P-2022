k = input("key ")
v = input("value ")
dict = {k:v}
while True:
    try:
        dict = dict, {k:v}
        print(dict)
    except:
        break


