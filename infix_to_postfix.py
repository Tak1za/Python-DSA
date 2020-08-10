from pythonds import Stack

prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

def toPostfix(infixString):
    s = Stack()
    output = []
    infixString = infixString.split()

    for i in infixString:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789":
            output.append(i)
        elif i == '(':
           s.push(i)
        elif i == ')':
            top = s.pop()
            while top != '(':
                output.append(top)
                top = s.pop()
        else:
            while (not s.isEmpty()) and (prec[s.peek()] > prec[i]):
                output.append(s.pop())
            s.push(i)
    
    while not s.isEmpty():
        output.append(s.pop())
    return " ".join(output)

print(toPostfix("A * B + C * D"))
print(toPostfix("( A + B ) * C - ( D - E ) * ( F + G )"))