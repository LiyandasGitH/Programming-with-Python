
from pyfiglet import Figlet
import sys
import random


figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFonts(font=random.choice(fonts))
    # sys.argv ["figlet.py", "-f", "slant"]
    # indexes         [0,     1,      2]
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] =="--font") and sys.argv[2] in fonts:
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")
print(figlet.renderText(text))








'''
text = "hello, world"
figlet.setFonts(fonts="alphabet")
print(figlet.renderText(text))
'''



