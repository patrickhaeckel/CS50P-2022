from pyfiglet import Figlet
from random import shuffle
import sys
fonts = [-f slant, -f rectangles, -f alphabet]
text = input("Text here ")
font = Figlet(font="doh")
if len(sys.argv) == 2:
    font = Figlet(font="doh")
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 0:
    font = shuffle(fonts)
    print(font.renderText(f"{text}"))


