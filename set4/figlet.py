from pyfiglet import Figlet
import sys
font = Figlet(font="doh")
if len(sys.argv) >2 or len(sys.argv) = 0
text = input("Text here ")
print(font.renderText(f"{text}"))
