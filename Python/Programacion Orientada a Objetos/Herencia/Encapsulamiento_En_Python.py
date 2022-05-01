# Los atributos encapsulado son aquellos que solo se pueden acceder para modificar dentro de nuatra clase y no afuera de esta (aunque python lo permite, no es lo
# recomendable)

class Persona():
    def __init__(self, nombre, apellido, edad) -> None:
        # colocandolo un '_' antes del nombre del altributo, creariamos un atributo encapsulado
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    # para Get usamos el decorador @propertry, que hace que se interprete un metodo como la llamada de un atributo (o eso creo yo, no he visto bien
    # que son los decoradores), por lo que se, un decorador modifica un comportamiento de nuestro metodo, en este caso caso, hace que el metodo se
    # comporte como un atributo. se usa parta obtener un atributo encapsulado
    @property
    def nombre(self):
        # print('Llamando a Get')
        return self._nombre
    
    # Y para Set usamos Nombre_Del_Atributo.setter, esto hara lo mismo que property, hacer que un metodo se interprete como un atributo, lo cual
    # usaremos para modificar un atributo encapsulado
    @nombre.setter
    def nombre(self, nuevo_nombre):
        print('Llamando a Set')
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido
    

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def __del__(self):
        print(f'El Objeto fue Eliminado: {self._nombre} {self._apellido}')
    
    def mostrar_detalles(self):
        # Podemos acceder a los atributos con _ aca ya que estamos dentro de la clase, lo ideal es NO hacerlo afuera
        print(f'Nombre: {self._nombre}, Apellido: {self._apellido}, Edad: {self._edad}.')
    
    def __str__(self) -> str:
        return f'{self._nombre} {self._apellido} {self._edad}'


if __name__ == '__main__':
    persona = Persona('Johan', 'Robles', 19)
    persona.mostrar_detalles()
    # Nombre: Johan, Apellido: Robles, Edad: 19.
    '''
    Aunque python permite accder a los atributos encapsulado, esto no es lo recomendable que lo hagamos. solo con ver un _ antes del nombre del
    atributo, eso no indica que solo podemos modificar ese atributo dentro de la clase y no afuera.
    '''
    persona._nombre ='Sebas'
    persona.mostrar_detalles()
    # Nombre: Sebas, Apellido: Robles, Edad: 19.

    '''
    La forma para que UNICAMENTE el atributo sea modificado dentro de la case pero NO afuera de esta es colocarle '__' antes del nombre del atributo
    asi, el atributo no es modificable afuera de la clase. Esta es una anotacion que no se usa tanto, por lo general solo se usa el '_'
    '''
    # persona. = 'Gallego'
    # persona.mostrar_detalles()
    # Nombre: Sebas, Apellido: Robles, Edad: 19


    # Metodos Set (Modificar atributos) y Get (obtener atributos) en python 
    # Get
    # recordar que no accedes al metodo nombre() con los () ya que property hace que este metodo se interprete como un atributo
    print(persona.nombre)
    # Llamando a Get
    # Sebas

    persona.nombre = 'Johan'
    print(persona.nombre)
    # Llamando a Set
    # Llamando a Get
    # Johan

    # Por lo que entendi, es que usamos get y set (con sus decoradroes property y setrer) para acceder y modificar ateributos encapsulados de una clase

    # VARIABLES DE SOLO LECTURA (READ-ONLY)
    '''
    Si quitamos nuestro metdo y decorador para modificar atributos encapsulados en una clase, nos marcara error 
    '''
    persona.nombre = 'Johan'
    # AttributeError: can't set attribute 'nombre
    # Aunque podemos hacerlo si usamos _nombre pero recordemao que esto es una mala practica

    # Cuando pasa esto, a ese atributo se le conoce como atributo de solo lectura

    # AGRAGAMOS GET Y SET A TODOS NUESTROS ATRIBUTOS ENCAPSULADOS   
    persona.nombre = 'Laura'
    persona.apellido = 'Rincon'
    persona.edad = 13

    print(persona.nombre)
    # Laura
    print(persona.apellido)
    # Rincon
    print(persona.edad)
    # 13

    persona.mostrar_detalles()
    # Nombre: Laura, Apellido: Robles, Edad: 13.