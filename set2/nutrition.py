d = {
    "Apple" : 130,
    "Avocado" : 50,
    "SweetCherries" : 100,
    "Kiwifruit" : 90,
    "Pear" : 100
    }
i = input("type your fruit here ").title().replace(" ", "")
if i in d:
    print (d[i])
