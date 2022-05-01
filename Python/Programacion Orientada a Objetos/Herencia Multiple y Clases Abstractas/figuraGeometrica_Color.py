# ABC -> Abstract Base Classes
'''
Este concepto de las clases abstractas se aplica a las clases padres para que estas no puedadn ser instanciadas, mas bien cuando tienen metodos 
abstractos, estas clases se vuelven abstarcatas y por tanto no pueden ser instanciadas (no se pueden crear objetos con estas) y obligar que
las clases hijas a definir, implrmentar o expandir un metodo abstracto de la clase padre.
'''
# importamos el modulo de clases abstracta para pasarsela como padre a las clases padres y tambien importamos abstractmethod para generar metodos
# abstractos. 
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, ancho, alto) -> None:
        # Agregamos algunas validaciones
        if self._validar(ancho):
            self._ancho = ancho
        else:
            print(f'Valor invalido: {ancho}')
            self._ancho = 0

        if self._validar(ancho):
            self._alto = alto
        else:
            print(f'Valor invalido: {alto}')
            self._alto = 0

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        if self._validar(nuevo_ancho):
            self._ancho = nuevo_ancho
        else:
            print(f'Valor invalido: {nuevo_ancho}')
            self._alto = 0

    @alto.setter
    def alto(self, nuevo_alto):
        if self._validar(nuevo_alto):
            self._alto = nuevo_alto
        else:
            print(f'Valor invalido: {nuevo_alto}')
            self._alto = 0
    
    def __str__(self) -> str:
        return f'Ancho: {self._ancho}, Alto: {self._alto}'
    
    # Tambien podemos crear metodos encapsulados
    def _validar(self, valor):
        return True if 0 < valor <= 10 else False

    # Nuestro metodo abstracto sere el como se calculara el area segun el tipo de figura, esto tiene sentido ya que el area de las figuras se calcula
    # diferente segun el tipo de la figura. por tanto para cada clase hija (cuadrado y rectangulo) las obligamos a que implementen este metodo 
    # segun la figura.
    @abstractmethod
    def Area(self):
        pass



class Color(object):
    def __init__(self, color) -> None:
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color

    def __str__(self) -> str:
        return f'Color: {self._color}'

if __name__ == '__main__':
    # si intentamos instanciar la clase abstracta Figura no maracaria error.
    figura = Figura(5, 5)
    # TypeError: Can't instantiate abstract class Figura with abstract method Area