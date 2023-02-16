def main():
    time = input("what time is it? ").strip().split(":")
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)
    output = (minutes/60) + (hours)
    print(output)
    if output >= 4 and output <= 5:
        print("breakfast time")
main()

def main()
    

