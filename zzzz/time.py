def main():
    time = input("what time is it? ").strip().split(":")
    output = convert(time)
    print(output)

def convert(time):
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)
    output = (hours) + (minutes/60)
    return output


main()



