from pyfiglet import Figlet
from random import shuffle
import sys

while True:
    text = input("Text here ")
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            sys.exit(print("Invalid usage"))
        elif sys.argv[1] != "--font":
            sys.exit(print("Invalid usage"))
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font = Figlet(font=sys.argv[2])
            print(font.renderText(f"{text}"))
    elif len(sys.argv) == 1:
            fonts = ["slant", "rectangles", "alphabet"]
            shuffle(fonts)
            font = Figlet(fonts[1])
            print(font.renderText(f"{text}"))
            sys.exit()
    else:
        sys.exit(print("invalid usage"))


