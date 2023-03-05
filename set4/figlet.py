from pyfiglet import Figlet
from random import shuffle
import sys
fonts = ["slant", "rectangles", "alphabet"]
text = input("Text here ")
if len(sys.argv) == 3:
    font = Figlet(font=sys.argv[2])
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 1:
    shuffle(fonts)
    font = Figlet(fonts[1])
    print(font.renderText(f"{text}"))


