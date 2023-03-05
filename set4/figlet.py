from pyfiglet import Figlet
font = Figlet(font="doh")
text = input("Enter your text to render here ")
print(font.renderText("f{text}"))
