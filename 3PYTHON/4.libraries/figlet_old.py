from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) > 1:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")
    if sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")


text = input("Input: ")
if len(sys.argv) < 2:
    font_choice = random.choice(fonts)
    figlet.setFont(font=font_choice)
    print(f"Output: \n{figlet.renderText(text)}")
else:
    figlet.setFont(font=sys.argv[2])
    print(f"Output: \n{figlet.renderText(text)}")
