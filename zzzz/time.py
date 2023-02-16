def main():
    time = input("what time is it? ").strip().split(":")
    output = convert(time)

def convert(time):
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)
    output = (hours) + (minutes/60)
    print(output)

main()



