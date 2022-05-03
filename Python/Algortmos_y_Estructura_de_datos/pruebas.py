cube = lambda x: x**3
def aux(n):
    if n == 1 or n == 0:
        return n
    else:
        return aux(n-1) + aux(n-2)
def fibonacci(n):
    lista = []
    for i in range(n):
        lista.append(aux(i))
    return lista
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))