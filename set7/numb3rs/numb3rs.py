import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"[0-9].+\.[0-9].+", ip):
        print(ip)
    else:
        print("false")






if __name__ == "__main__":
    main()