from pythonds import Stack

prec = {"**": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

def toPostfix(infixString):
    s = Stack()
    output = []
    infixString = infixString.split()

    for i in infixString:
        if i.isalnum():
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
print(toPostfix("10 + 3 * 5 / ( 16 - 4 )"))
print(toPostfix("5 * 3 ** ( 4 - 2 )"))