'''
La sobrecargas de operadores (OJO es diferente a sobrescribir metodos) son las operaciones que podemos hacer entre objetos
obj1 + obj2 --> __add__ -> se aplica por defecto cuando usamos +
obj1 - obj2 --> __sub__ -> se aplica por defecto cuando usamos -
obj1 * obj2 --> __mul__ -> se aplica por defecto cuando usamos *
obj1 ** obj2 --> __pow__-> se aplica por defecto cuando usamos **
(VER IMAGENES DE LA CARPETA PARA VER TODOS)
'''

class Persona():
    def __init__(self, nombre, edad = None) -> None:
        self.edad = edad
        self.nombre = nombre
    
    # aplicaremos add para sumar los numeros
    def __add__(self, otro_objeto):
        return f'{self.nombre} {otro_objeto.nombre}'
    # aplicaremos sub para restar las edad
    def __sub__(self, otro_objeto):
        return self.edad - otro_objeto.edad

    '''
    Tener en cuanta que SI importa cual de los objetos es el que llama al metodo pues
    obj1.__add__(ob2) -> obj1 + obj2 != obj2.__add__(ob1) -> obj2 + obj1  
    '''

perosna1 = Persona('Juan', 15)
perosna2 = Persona('Pablo', 18)

perosna3 = perosna1 + perosna2
# OJO person3 NO es un objeto porque estamos haciendo add a dos objetos, persona3 es lo que retorna el metodo add de los objetos (string)
print(perosna3)
# Juan Pablo
# print(perosna3.edad)
# AttributeError: 'str' object has no attribute 'edad'

print(perosna1 - perosna2)
# -3