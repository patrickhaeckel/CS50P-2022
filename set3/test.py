def main():
    try:
        x = int(input("type x "))
        y = int(input("type y "))
        if x > y:
            print("yes")
    except(EOFError):
        pass
main()


