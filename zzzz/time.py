def main():
    time = input("what time is it? ").strip().split(":")
    x = convert(time)
    print(x)

def convert(time):
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)


main()



