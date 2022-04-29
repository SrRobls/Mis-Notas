class Figura(object):
    def __init__(self, ancho, alto) -> None:
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @property
    def alto(self):
        return self._alto
    
    @ancho.setter
    def ancho(self, nuevo_ancho):
        self._ancho = nuevo_ancho

    @alto.setter
    def alto(self, nuevo_alto):
        self._alto = nuevo_alto
    
    def __str__(self) -> str:
        return f'Ancho: {self._ancho}, Alto: {self._alto}'

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