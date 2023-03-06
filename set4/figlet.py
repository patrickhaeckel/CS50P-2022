from pyfiglet import Figlet
from random import shuffle
import sys
text = input("Text here ")
while True:
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            sys.exit(print("Invalid usage"))
        elif sys.argv[1] != "--font":
            sys.exit(print("Invalid usage"))
        elif sys.argv[1] == "-f":
            font = Figlet(font=sys.argv[2])
            print(font.renderText(f"{text}"))
        elif sys.argv[1] == "--font":
            font = Figlet(font=sys.argv[2])
            print(font.renderText(f"{text}"))
    elif len(sys.argv) == 1:
            fonts = ["slant", "rectangles", "alphabet"]
            shuffle(fonts)
            font = Figlet(fonts[1])
            print(font.renderText(f"{text}"))
            sys.exit()


