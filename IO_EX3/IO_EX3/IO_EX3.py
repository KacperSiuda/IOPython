import math


def newton(n,k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

def wejscie(txt):
    lista = txt.split()
    return lista

text = input()
lista1 = wejscie(text)
print(int(newton(int(lista1[0]),int(lista1[1]))))


