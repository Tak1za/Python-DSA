from pythonds import Stack

def evaluate(postfixString):
    s = Stack()
    postfixString = postfixString.split()

    for i in postfixString:
        if i.isnumeric():
            s.push(int(i))
        else:
            op2 = s.pop()
            op1 = s.pop()
            result = calculate(op1, op2, i)
            s.push(result)
    return s.pop()

def calculate(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    if operator == "-":
        return op1 - op2
    if operator == "*":
        return op1 * op2
    if operator == "/":
        return op1 / op2
    if operator == "**":
        return op1 ** op2

print(evaluate('7 8 + 3 2 + /'))
print(evaluate('17 10 + 3 * 9 /'))
print(evaluate('5 3 4 2 - ** *'))