# creareos una clase persona que tendra una variable de clase que aumentara su valor por cada objeto instanciado
class Persona():
    
    id = 0
    def __init__(self, nombre, edad) -> None:
        # Aumentamos el contador por cada objeto creado
        
        self.id = Persona._aumentar_contador()
        self.edad = edad
        self.nombre = nombre
    
    def __str__(self) -> str:
        return f'{self.id}:[{self.nombre} {self.edad}]'

    # definamos un metodo de clase para aumentar el contador cuando se instancie un metodo
    @classmethod
    def _aumentar_contador(cls):
        cls.id += 1
        return cls.id

    def aumentar_id(self):
        self.id += 1
if __name__ == '__main__':
    persona1 = Persona('Juan', 20)
    print(persona1)
    # 1:[Juan 20]
    persona2 = Persona('Pepe', 15)
    print(persona2)
    # 2:[Pepe 15]
    persona3 = Persona('Daniela', 19)
    print(persona3)
    # 3:[Daniela 19]
    print(persona1.id)
    # 1:[Juan 20]

    persona1.aumentar_id()
    print(persona1)
    # 2:[Juan 20]