class Empleados():
    def __init__(self, nombre, sueldo) -> None:
        self._nombre = nombre
        self._sueldo = sueldo
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def sueldo(self):
        return self._sueldo
    # Hacemos que los atributos solo sean de lectura, es decir, no podremos modificarlos
    
    def __str__(self) -> str:
        return f'Empleado: [{self._nombre} {self._sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()