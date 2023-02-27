#  Program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer
def main():
    f = input("type your fraction ").split("/")
    x = f[0]
    y = f[1]

    print(x)


#  And then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank


#  If, though, 1% or less remains, output E instead And if 99% or more remains, output F instead


#  If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
#  (It is not necessary for Y to be 4.)


main()