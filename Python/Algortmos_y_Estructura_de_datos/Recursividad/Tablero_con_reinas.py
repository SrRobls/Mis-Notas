'''
Ejercicios de las reinas. hallar la cantidad de formas diferentes de las posiciones de las reinas
en un tablero nxn
'''

class Array(object):
    def __init__(self, size) -> None:
        self.items = []
        for _ in range(size):
            self.items.append(None)
    
    def retornar(self):
        return self.items


def reinas(n, array_uni_dimensional, i = 0):
    if i == n:
        print(array_uni_dimensional)
    else:
        for k in range(n):
            if comprobarColumnas(array_uni_dimensional, k) and comprobarDiagonales( array_uni_dimensional, i, k):
                array_uni_dimensional[i] = k
                reinas(n, array_uni_dimensional, i+1)
        array_uni_dimensional[i] = None

def comprobarColumnas(array, k):
    if k in array:
        return False
    else:
        return True

def comprobarDiagonales(array, i,  k):
    iter = 0
    while array[iter] != None:
        diferencia_ind = abs(i - iter)
        diferencia_valor = abs(k - array[iter])
        if diferencia_ind == diferencia_valor:
            return False
        iter += 1
    return True

n = int(input('Dame la dimension del tablero (nxn): '))
reinas(n, Array(n).retornar())