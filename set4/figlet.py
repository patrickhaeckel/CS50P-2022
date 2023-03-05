from pyfiglet import Figlet
from random import shuffle
import sys
text = input()
if len(sys.argv) == 3 and (sys.argv[1]) == "--f" and (sys.argv[1]) == "--font":
    font = Figlet(font=sys.argv[2])
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 1:
    fonts = ["slant", "rectangles", "alphabet"]
    shuffle(fonts)
    font = Figlet(fonts[1])
    print(font.renderText(f"{text}"))
else:
    sys.exit()


