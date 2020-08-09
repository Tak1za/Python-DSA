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