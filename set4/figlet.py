from pyfiglet import Figlet
from random import shuffle
import sys
figlet = Figlet()
fonts = figlet.getFonts()
if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
    print(font.renderText(f"{text}"))
elif len(sys.argv) == 1:
    shuffle(fonts)
    figlet.setFont(font=fonts[1])
    print(font.renderText(f"{text}"))
else:
     sys.exit(print("Invalid usage"))

