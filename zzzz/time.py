def main():
    time = input("what time is it? ").strip().split(":")
    output = convert(time)
    if output >= 7 and output <= 8:
        print("breakfast time")
    elif output >= 12 and output <= 13:
        print("lunch time")
    elif output >= 18 and output <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)
    output = (hours) + (minutes/60)
    return output


main()



