from pyfiglet import Figlet
import random
import sys


def main():
    figlet = Figlet()
    font = get_font(figlet)
    figlet.setFont(font=font)
    text = input("Input: ")
    print(f"Output: \n{figlet.renderText(text)}", end="")


def get_font(figlet):
    fonts = figlet.getFonts()
    if len(sys.argv) > 1:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid Usage")
        if sys.argv[2] not in fonts:
            sys.exit("Invalid Usage")
        return sys.argv[2]
    else:
        return random.choice(fonts)


if __name__ == "__main__":
    main()
