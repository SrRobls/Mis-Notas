
from Arrays import Array


# Rero #2:
'''
crear una clase cube, un array tridimensional
'''

class Cube(object):
    def __init__(self, rows, colunmns, under, valor = None) -> None:
        self.tridimensional = Array(rows)
        for i in range(rows):
            self.tridimensional[i] = Array(colunmns)
            for j in range(colunmns):
                self.tridimensional[i][j] = Array(under)
    
    def __str__(self) -> str:
        imprimir = ""
        for row in self.tridimensional:
            imprimir += '|'
            for column in row:
                imprimir += '[ '
                for value in column:
                    imprimir += str(value) + ' '
                imprimir += ']'
                imprimir += '|'
            imprimir += '\n'
        return imprimir

tridimensional = Cube(3, 2, 3)
print(tridimensional)
# |[ None None None ]|[ None None None ]|
# |[ None None None ]|[ None None None ]|
# |[ None None None ]|[ None None None ]|