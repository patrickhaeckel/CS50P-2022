from pyfiglet import Figlet
from random import shuffle
import sys
figlet = Figlet()
print(figlet)
text = input("Text here ")
fonts = figlet.getFonts()
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    font = Figlet(font=sys.argv[2])
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 3 and (sys.argv[1] != "-f" or sys.argv[1] != "--font"):
        sys.exit(print("Invalid usage"))
elif len(sys.argv) == 1:
    fonts = ["slant", "rectangles", "alphabet"]
    shuffle(fonts)
    font = Figlet(fonts[1])
    print(font.renderText(f"{text}"))
else:
     sys.exit(print("Invalid usage"))

