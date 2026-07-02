import sys
import pyfiglet

if len(sys.argv) == 1:
    user_input = input("Input: ")
    print(pyfiglet.figlet_format(user_input))
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
        sys.exit("Invalid usage")
    user_input = input("Input: ")
    print(pyfiglet.figlet_format(user_input, font=sys.argv[2]))
else:
    sys.exit("Invalid usage")
