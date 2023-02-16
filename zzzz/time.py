def main():
    time = input("what time is it? ").strip().split(":")
    output = convert(time)
    print(time)

def convert(time):
    hours, minutes = time
    hours = float(hours)
    minutes = float(minutes)
    

main()



