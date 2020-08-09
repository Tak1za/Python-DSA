from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()

    for i in symbolString :
        if i == '(':
            s.push(i)
        elif i == ')':
            if s.isEmpty():
                return "Unbalanced"
            else: 
                s.pop()
        
    if s.isEmpty():
        return "Balanced"
    else:
        return "Unbalanced"


print(parChecker('((()))'))
print(parChecker('(()'))
print(parChecker('(())()()())))))'))
print(parChecker('(())()()())))))((((('))
print(parChecker('((a))(b*d)()())))))((((('))

print("-------------------------------------")

def parCheckerAll(symbolString):
    s = Stack()

    for i in symbolString :
        if i in '[{(':
            s.push(i)
        elif i in ']})':
            if s.isEmpty():
                return "Unbalanced"
            elif matches(i, s.peek()):
                s.pop()
            else:
                return "Unbalanced"
        
    if s.isEmpty():
        return "Balanced"
    else:
        return "Unbalanced"

def matches(symbol, top):
    openers = "[{("
    closers = "]})"
    return openers.index(top) == closers.index(symbol)

print(parCheckerAll('{({([][])}())}'))
print(parCheckerAll('[{()]'))