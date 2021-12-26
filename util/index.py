import pyfiglet
import os

fig = pyfiglet 

black = "\x1b[30m"
red = "\x1b[31m"
green = "\x1b[32m"
yellow = "\x1b[33m"
blue = "\x1b[34m"
magenta = "\x1b[35m"
cyan = "\x1b[36m"
white = "\x1b[37m"
end = "\x1b[0m"

def formatedText(color, txt):
    if color == "black":
        return print(f"{black} {fig.figlet_format(txt, font='larry3d')}")
    elif color == "red":
        return print(f"{red} {fig.figlet_format(txt, font='larry3d')}")
    elif color == "green":
        return print(f"{green} {fig.figlet_format(txt, font='larry3d')}")
    elif color == "cyan":
        return print(f"{cyan} {fig.figlet_format(txt, font='larry3d')}")\
        


# by default python doesnt support multiline inputs
# so with this function, we can get multi-line input from users
 

def Input(question):
    print(question)
    print("")
    lines = []
    result = "\n"
    
    while True:
        inp = input("")
        
        if inp:
            lines.append(inp)
        else:
            break
    return result.join(lines)    