import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(".+@.+", ip):
        print(ip)
    else:
        print("false")






if __name__ == "__main__":
    main()