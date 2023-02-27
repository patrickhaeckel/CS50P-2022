def main():
    try:
        x = int(input("type x "))
        y = int(input("type y "))
        if x > y:
            print("yes")
    except(EOFError):
        print(end = "\n")
main()


