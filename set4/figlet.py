from pyfiglet import Figlet
import sys
font = Figlet(font="doh")
text = input("Text here ")

if len(sys.argv) >2 or len(sys.argv) = 0
print(font.renderText(f"{text}"))
