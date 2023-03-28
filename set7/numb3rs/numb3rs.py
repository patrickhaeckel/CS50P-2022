import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\.", ip):
        print("valid")
    else:
        print("invalid")






if __name__ == "__main__":
    main()