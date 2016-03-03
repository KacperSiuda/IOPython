def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1: 
        return fib(n - 1) + fib(n - 2)

def addToList(n):
    l = []
    for i in range(n):
        l.append(fib(i))
    return l

def printElements(list,n):
    l = []
    for i in range (n):
        l.append((list[i]))
    return l

a = int(input())
print(printElements(addToList(a),a))