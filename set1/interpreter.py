def main():
    x, y, z = input("input your aritmetic expresion here ").split(" ")
    x = float(x)
    z = float(z)
    if y == "+":
        print(x + z)
    elif y == "/":
        print (x/z)
    elif y == "-":
        print (x-z)
    elif y == "*":
        print (x*z)

main()
