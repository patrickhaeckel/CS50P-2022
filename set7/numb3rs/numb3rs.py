import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"[0-255]+\.[0-75]+", ip):
        print("valid")
    else:
        print("invalid")






if __name__ == "__main__":
    main()