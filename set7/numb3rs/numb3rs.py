import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("[0-255].+\.[0-75].+", ip):
        print(ip)
    else:
        print("invalid")






if __name__ == "__main__":
    main()