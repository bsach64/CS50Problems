import sys
from pyfiglet import Figlet
from random import choice

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font=choice(fonts))
    print("Output: " + figlet.renderText(input("Input: ")))

elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
            print("Output: " + figlet.renderText(input("Input: ")))
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")