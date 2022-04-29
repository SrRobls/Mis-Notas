# Veremos como heredar de dos o mas clases padres
# importamos nuestras clases padres
from figuraGeometrica_Color import Figura, Color

class Cuadrado(Figura, Color):
    def __init__(self, lado, color) -> None:
        # La forma de heredar atributos y metodos de las clases padres es NO usando super (pues este es factible usarlo cuando solo se tiene una
        # clase padre) si no, llamando los metodods constructores, pero como los estamos llamado, es necesario llamarlos con el parametro self, 
        # es decir, lo llalamos como si fueran metodos de esta clase
        Figura.__init__(self, lado, lado) # Recordar que la clase padre recibe como parametro el alto y el ancho, pero como esta clase es para
        # crear una clase cuadrado, entonces eso valores son iguales, le pasamos el valor lado a los dos.
        Color.__init__(self, color)
    
    def calcular_area(self):
        # OJO, recordar que estos atributos son heredados de las clases padres (mas en congreto, la clase Figura), asi que esos valores de alto
        # y ancho son heredados de la clase figura. lo mismo pasa con self.color, ese atributo es heredado de la clase Color
        return self.alto * self.ancho
    
    def __str__(self) -> str:
        return f'Figura: Cuadrado, Lado: {self.alto}, Color: {self.color}, Area: {self.calcular_area()}'

cuadrado = Cuadrado(5, 'Rojo')
print(cuadrado)
# Figura: Cuadrado, Lado: 5, Color: Rojo, Area: 25

# MRO = Metod Resolucion Order, esto lo usamos para saber que clases estan siendo llamada y en que orden. esto puede ser muy importante a la hora de
# manipular clases que tienen muchas clases padres.
print(Cuadrado.mro())
# [<class '__main__.Cuadrado'>, <class 'figuraGeometrica_Color.Figura'>, <class 'figuraGeometrica_Color.Color'>, <class 'object'>]
# Como podemos ver, primero se llama la clase hija, luego las dos padres en orden de como los lee el codigo y por ultimo el Object
# recordar que este ultimo siempre se heredan a todas las clases.

class Rectangulo(Figura, Color):
    def __init__(self, ancho, alto, color) -> None:
        Figura.__init__(self, ancho, alto)
        Color.__init__(self, color)
    
    def Area(self):
        return self._ancho * self._alto
    
    def __str__(self) -> str:
        return f'{Figura.__str__(self)}, {Color.__str__(self)}, Area: {self.Area()}'

rectangulo = Rectangulo(10, 5, 'Azul')
print(rectangulo)
# Ancho: 10, Alto: 5, Color: Azul, Area: 50
print(rectangulo.alto)
# 5
print(rectangulo.ancho)
# 10
print(rectangulo.color)
# Azul
rectangulo.alto = 2
rectangulo.ancho = 8
rectangulo.color = 'Amarillo'
print(rectangulo)
# Ancho: 8, Alto: 2, Color: Amarillo, Area: 16