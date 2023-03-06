from pyfiglet import Figlet
from random import shuffle
import sys
text = input("Text here ")
if len(sys.argv) == 3
    font = Figlet(font=sys.argv[2])
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 1:
    fonts = ["slant", "rectangles", "alphabet"]
    shuffle(fonts)
    font = Figlet(fonts[1])
    print(font.renderText(f"{text}"))
else:
    sys.exit()


