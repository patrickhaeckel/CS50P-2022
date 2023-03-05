from pyfiglet import Figlet
from random import shuffle
import sys
fonts = {}
text = input("Text here ")
if len(sys.argv) == 2:
    font = Figlet(font="doh")
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 0:
    font = shuffle.Figlet(font="doh")
    print(font.renderText(f"{text}"))


