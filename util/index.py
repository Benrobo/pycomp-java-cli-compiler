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