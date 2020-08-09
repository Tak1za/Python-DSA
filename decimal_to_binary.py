from pythonds.basic import Stack

def toBinary(num):
    s = Stack()
    while num > 0 :
        s.push(str(num%2))
        num = num // 2

    dataList = [s.pop() for x in range(s.size())]
    return "".join(dataList)

print(toBinary(42))