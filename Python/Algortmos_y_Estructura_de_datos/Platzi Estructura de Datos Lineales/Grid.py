# Ahora creemos una clase para crear matrizes:
from Arrays import Array

class Grid(object):

    # Creamos nuestro constructor y creamos la matriz. aqui podeos usar la clase Array  que creamos anteriormente. creamos un array dentro de 
    # ese array creamos mas arrays, asi creamos un array bidimensional.
    def __init__(self, rows, columns, fill_value = None):
        self.data = Array(rows)
        print(self.data)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)
    # Creacion de metodos:

    # Para obtener el alto de la matriz dicimensional, es lo mismo que la cantidad de filas/rows
    def __getHeight__(self):
        return len(self.data)

    # Para obtener el ancho de la matriz bidimensional, es la misma cantidad de las columnas/columns yeste valor es igaulñ en el ancho de las
    # filas asi que en vez del 0 tambien podremos usar otro numero simepre y cuando este entre 0 y el total de rows a la altura.
    def __getWidth__(self):
        return len(self.data[0])


    # Para acomodar e imprimrir la matriz
    def __str__(self) -> str:
        imprimir = ""
        for row in self.data:
            imprimir += '|'
            for value in row:
                imprimir += str(value) + "|" + " "

            imprimir += "\n"
        return imprimir

    # Para Obtener un item
    def __getItem__(self, fila, columna):
        return self.data[fila][columna]


    # Para insertan o intercambiar un elemento
    def __insertItem__(self, fila, columna, value):
        self.data[fila][columna] = value

arra_1 = Grid(3, 3)
print(arra_1)
# >>> |None| None| None| 
# >>> |None| None| None|
# >>> |None| None| None|
arra_1.__insertItem__(2,2,3)
arra_1.__insertItem__(2,1,5)
arra_1.__insertItem__(0,2,100)
print(arra_1)
# >>> |None| None| 100|
# >>> |None| None| None|
# >>> |None| 5| 3|
print(arra_1.__getItem__(2, 1))
# 5