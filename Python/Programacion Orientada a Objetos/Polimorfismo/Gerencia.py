from Empleado import Empleados

class Gerencia(Empleados):
    def __init__(self, nombre, sueldo, gerencia) -> None:
        super().__init__(nombre, sueldo)
        self._gerencia = gerencia
    
    @property
    def gerencia(self):
        return self._gerencia
    # Hacemos que los atributos solo sean de lectura, es decir, no podremos modificarlos

    def __str__(self) -> str:
        return f'{super().__str__()} Gerencia: [{self._gerencia}]'
    
if __name__ == '__main__':
    obj1 = Gerencia('Pablo', 5000000, 'Ing. Civil')
    print(obj1)
    # Empleado: [Pablo 5000000] Gerencia: [Ing. Civil]