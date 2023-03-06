from pyfiglet import Figlet
from random import shuffle
import sys
text = input("Text here ")
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font":)
    font = Figlet(font=sys.argv[2])
    print(font.renderText(f"{text}"))
    else:
        sys.exit()
elif len(sys.argv) == 1:
    fonts = ["slant", "rectangles", "alphabet"]
    shuffle(fonts)
    font = Figlet(fonts[1])
    print(font.renderText(f"{text}"))
else:
    sys.exit()