def main():
    fraction = input("type your fraction ")
    percentage = convert(fraction)
    output = gauge(percentage)
    print(output)

def convert(fraction):
    while True:
        try:
            fraction = fraction.split("/")
            x = int(fraction[0])
            y = int(fraction[1])
            fraction = (x/y)
            percentage = round(fraction*100)
            return(percentage)
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(f"{percentage}%")




if __name__ == "__main__":
    main()
