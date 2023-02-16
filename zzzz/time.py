def main():
    time = input("what time is it? ").strip().split(":")
    output = convert(time)

def convert(time):
    hours, minutes = time
main()
print(output)


