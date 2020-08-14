from pythonds.basic import Queue

def hotPotato(names, num):
    q = Queue()
    for name in names:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"], 7))