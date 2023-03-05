from pyfiglet import Figlet
from random import shuffle
import sys
fonts = ["-f slant", "-f rectangles", "-f alphabet"]
text = input("Text here ")
font = Figlet(font="doh")
if len(sys.argv) == 2:
    font = Figlet(font="doh")
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 1:
    shuffle(fonts)
    font = fonts[1]
    print(font.renderText(f"{text}"))


