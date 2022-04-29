from Vehiculo_EjercicioHerencia import Vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad) -> None:
        super().__init__(color, ruedas)
        self._velocidad = velocidad
    
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        self._velocidad = nueva_velocidad
    
    def __str__(self) -> str:
        return f'{super().__str__()}, Velocidad: {self._velocidad} km/h'


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo) -> None:
        super().__init__(color, ruedas)
        self._tipo = tipo
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo

    def __str__(self) -> str:
        return f'{super().__str__()}, Tipo: {self._tipo}'

if __name__ == '__main__':
    mazda = Coche('Azul', 4, 240)
    print(mazda)
    # Color: Azul, Ruedas: 4, Velocidad: 240 km/h
    print(mazda.color)
    # Azul
    print(mazda.velocidad)
    # 240
    print(mazda.ruedas)
    # 4

    mazda.color = 'Rojo'
    print(mazda)
    # Color: Rojo, Ruedas: 4, Velocidad: 240 km/h


    bmx = Bicicleta('Blanco', 2, 'Montaña')
    print(bmx)
    # Color: Blanco, Ruedas: 2, Tipo: Montaña
    print(bmx.color)
    # Blanco
    print(bmx.ruedas)
    # 2
    print(bmx.tipo)
    # Montaña

    bmx.tipo = 'Carreras'
    print(bmx)
    # Color: Blanco, Ruedas: 2, Tipo: Carreras