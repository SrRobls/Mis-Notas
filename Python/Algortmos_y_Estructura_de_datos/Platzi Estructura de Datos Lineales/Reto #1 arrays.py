# Acontinuacion crearemos un objeto array y probaremos sus metodos.
from Arrays import Array


'''
Crear una clase de array que incorpore un metodo para rellenarla de numeros secuenciales y que tambien tenga un metodo para sumar esos valores
'''

class RetoArray:

    def __init__(self, capacidad, valor = None) -> None:
        self.items = list()
        for _ in range(capacidad):
            self.items.append(valor)

    def __rellenar__(self): 
        i = 0
        while i <= len(self.items)-1:
            self.items[i] = i+1
            i += 1
    
    def __str__(self):
        return str(self.items)

    def __suma__(self):
        sum = 0
        for value in self.items:
            sum += value
        return sum



reto_array = RetoArray(5)
reto_array.__rellenar__()
print(reto_array)
# >>> [1, 2, 3, 4, 5]
print(reto_array.__suma__())
# >>> 15