def main():
    time = input("what time is it? ").strip().split(":")
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)
def convert(time):
    output = (minutes/60) + (hours)
    print(output)
main()
