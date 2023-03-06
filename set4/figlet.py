from pyfiglet import Figlet
from random import shuffle
import sys
text = input("Text here ")
while True:
    if len(sys.argv) == 3:
        if sys.argv[1] != "-f":
            sys.exit()
        elif sys.argv[1] != "--font":
            sys.exit()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            font = Figlet(font=sys.argv[2])
            print(font.renderText(f"{text}"))
    elif len(sys.argv) == 1:
            fonts = ["slant", "rectangles", "alphabet"]
            shuffle(fonts)
            font = Figlet(fonts[1])
            print(font.renderText(f"{text}"))
    else:
        _ = "."


