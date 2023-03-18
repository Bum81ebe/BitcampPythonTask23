import sys
import random
from pyfiglet import Figlet


if len(sys.argv) == 1:
    
    figlet = Figlet(font=random.choice(Figlet().getFonts()))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in Figlet().getFonts():
    
    figlet = Figlet(font=sys.argv[2])
else:
   
    sys.exit("Invalid usage")


text = input("Enter some text: ")


print(figlet.renderText(text))
