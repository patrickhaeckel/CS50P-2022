from pyfiglet import Figlet
from random import shuffle
import sys
figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 1:
    shuffle(fonts)
    font = Figlet(fonts[1])
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    font = Figlet(font=sys.argv[2])
else:
     sys.exit(print("Invalid usage"))

text = input("Text here ")
print(font.renderText(f"{text}"))

