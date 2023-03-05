from pyfiglet import Figlet
figlet = Figlet()
figlet.getFonts()
figlet.setFont(font=doh)
print(figlet.renderText(s))