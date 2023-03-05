from pyfiglet import Figlet
inp = input()
font = Figlet(font="doh")
print(font.renderText(f"{inp}"))
