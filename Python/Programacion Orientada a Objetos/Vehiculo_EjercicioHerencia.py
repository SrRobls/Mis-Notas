class Vehiculo(object):
    def __init__(self, color, ruedas) -> None:
        self._color = color
        self._ruedas = ruedas
    
    @property
    def color(self):
        return self._color

    @property
    def ruedas(self):
        return self._ruedas
    
    @color.setter
    def color(self, nuevo_color):
        self._color = nuevo_color

    @ruedas.setter
    def ruedas(self, nuevas_ruedas):
        self._ruedas = nuevas_ruedas

    def __str__(self) -> str:
        return f'Color: {self._color}, Ruedas: {self._ruedas}'

if __name__ == '__main__':
    moto = Vehiculo('Negro', 2)
    print(moto.color)
    # Negro
    print(moto.ruedas)
    # 2
    moto.color = 'Rojo'
    moto.ruedas = 4
    print(moto.color)
    # Rojo
    print(moto.ruedas)
    # 4
    print(moto)
    # Color: Rojo, Ruedas: 4