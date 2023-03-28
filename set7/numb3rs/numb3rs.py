import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if re.search("[0-9]+\.[0-9]+\.[0-9]+\.[0-9]", ip):
        n = ip.split(".")
        if n[1] >= 0 and n[1] < 256:
            if n[2] >= 0 and n[2] < 256:
                if n[3] >= 0 and n[3] < 256:
        print("valid")
        print(n)
    else:
        print("invalid")






if __name__ == "__main__":
    main()