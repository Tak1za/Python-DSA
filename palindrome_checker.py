from pythonds.basic import Deque

def palChecker(inputString):
    q = Deque()

    for c in inputString:
        q.addRear(c)

    equal = True

    while q.size() > 1 and equal:
        first = q.removeFront()
        last = q.removeRear()

        if first != last:
            equal = False
        
    return equal

print(palChecker("lsdkjfskf"))
print(palChecker("radar"))