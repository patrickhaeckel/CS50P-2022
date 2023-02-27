#  Program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer
#  and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank

def main():
    while True:
        try:
            f = input("type your fraction ").split("/")
            x = int(f[0])
            y = int(f[1])
            z = round((x/y)*100)
            if x < y:
                if tooless(z):
                    print("E")
                elif toomuch(z):
                    print("F")
                else:
                    print(f"{z}%")
                break
        except (ValueError, ZeroDivisionError):
            _ = "."


#  If, though, 1% or less remains, output E instead And if 99% or more remains, output F instead

def tooless(n):
    if n <= 1:
        return True
def toomuch(n):
    if n >= 99:
        return True

#  If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
#  (It is not necessary for Y to be 4.)




main()