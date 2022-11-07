import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        text = input("Input: ")

        f = figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid argument(s)!")
elif len(sys.argv) == 1:
    text = input("Input: ")

    f = figlet.setFont(font=choice(fonts))
    print(figlet.renderText(text))
else:
    sys.exit("Something went wrong!")