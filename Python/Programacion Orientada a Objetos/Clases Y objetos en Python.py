# Basicamente en una clase debemos colocar su caracteristicas (Atribiutos o metdos) ya una vez hecho esto. podemos crear un objeto con base a esa clase
# (Instancia de clase o Objetode clase) en la que las carecteristicas de ese objeto son los atributos/metodos de esa clase.
# En conclusion una clase es el modelo para crear objetos.

# Para crear una clase usamos:



class Objeto:
    # Le colocamos pass para declarar la clase pero no ejecutar codigo dentro de elle, los usamos ara validar la clase (Tambien funciona para funciones):
    pass
# Para comprobar de que se creo la clase
print(type(Objeto))
# >>> <class 'type'>

# Vamos a crear una clase persona
class Persona:
    # Debemos iniciar con el metodo init para poder comenzar a introducir atributos a nuestra clase. y tambien con el init inicializamos la clase
    def __init__(self, Nombre, Apellido, Edad):
        # El parametro self hace una referencia al objeto que vamos a crear
        # Para agregar atributos a nuestra clase debemos colocar parametro_del__init__.atributo = codigo
        self.nombre = Nombre
        self.apellido = Apellido
        self.edad = Edad
        # Tambien podriamos definir los valores de los atributos sin necesidad de usar parametros

# Y para crear un objeto, es basicamente crear una variable y llamar nuestra clase:

persona1 = Persona('Johan', 'Robles', 19) # Notar que llamamos la clase como si fuese una funcion y notar tambien que NO le estamos pasando el valor de la parametro self.
                     # Tengamos en cuenta que cuando llamamos la clase Persona, internamnete realmente esta llamando la funcion __init__
                     # El cual ya esta recibiendo un parametro self (lo cual ese parametro python lo pasa automaticamente y que hace referencia al objeto)
                     # que es el que le estamos agregando los atribitos. adicionalmente, notar que nostro estamos pasando el resto de parametro faltantes del __init__
                     # (Nombre, Apellido y Edad)

# Listo, ya creamos un objetos con el modelos de nuestra clase. si quermos imprimir los atributos de ese objeti, entonces:
print(persona1.nombre)
# >>> Johan
print(persona1.apellido)
# >>> Robles
print(persona1.edad)
# >>> 19

persona2 = Persona('Manuela', 'Gonzalez', 55)
print(f'{persona2.nombre} {persona2.apellido} {persona2.edad}')
# >>> Manuela Gonzales 55

# Tambien podemos cambiar 'externamente' los atributos de un objeto, por ejemplo:
persona1.nombre = 'Pablo'
persona1.apellido = 'Perez'
persona1.edad = 15
print(f'{persona1.nombre} {persona1.apellido} {persona1.edad}')
# >>> Pablo Perez 15

# METODOS DE INSTANCIA:

# Podemos crear metodos en nuestras clases, en este caso en congreto usaremos metodos de instancia, un metodo de isntancia es basicamente aquel
# en la que usamos self para referirnos al objeto en si (__init__ es un metodo de instancia). Los podemos usar para ejecutar un codigo con los 
# atributos de nuestro objeto.

class carro:
    # un detalle que hay que agregar es que el parametro self lo podemos usar con diferente nombre (Por ejemplo this), aunque no es lo usal
    # vale la pena mencionarlo  
    def __init__(self, color, tipo, caballos_de_fuerza):
        self.color = color
        self.tipo = tipo
        self.caballos_de_fuerza = caballos_de_fuerza
    # Creamos un metodo de dsiatancia para mostrar los detalles de nuestro objeto
    def mostratr_detalles_del_carro(self):
        # Como estoy DENTRO de la misma clase, para seleccionar los atributos tenemos que escrbibir self.atributo, esto puesto que estamos
        # dentro de la clase y self hace refencia al objeto al que le queremos aplicar este metodo
        print(f'Caracteristicas del carro: Color, {self.color}, Tipo: {self.tipo}, Caballos: {self.caballos_de_fuerza}')

carro1 = carro('Rojo', 'Lamborgini', 500)
# Llamamos nuestro metodo:
carro1.mostratr_detalles_del_carro()
# >>> Caracteristicas del carro: Color, Rojo Tipo: Lamborgini Caballos: 500

# Tambien podriamos llamar un metodo de diferente forma, que es llamr la clase y posteriormente llamar el metodo con nuestro objeto:
carro.mostratr_detalles_del_carro(carro1)
# >>> Caracteristicas del carro: Color, Rojo Tipo: Lamborgini Caballos: 500

# Y por ultimo tambien podemos crear atributos de forma externa a la clase, PERO hay que tener en cuenta que el atriubuto creado 
# externamente solamente se aplica al objeto al que se lo estemtos creando y no a los demas objetos diferentes ya creados.

# Ejemplo:
carro2 = carro('Negro', 'Camion', 150)
carro2.mostratr_detalles_del_carro()
# >>> Caracteristicas del carro: Color, Negro, Tipo: Camion, Caballos: 150
# Para crearle un nuevo atributo. recordar que este atributo solo se crea para este objeto en congreto y no en los demas:
carro2.marca = 'Toyota'
print(carro2.marca)
# >>> Toyota

# ____________________________________________________

class Arimetica:
    def __init__(self, valorA, valorB):
        self.operandoA = valorA
        self.operandoB = valorB
    def suma(self):
        return self.operandoA + self.operandoB
    def resta(self):
        return self.operandoA - self.operandoB
    def multiplicacion(self):
        return self.operandoA * self.operandoB
    def division(self):
        return self.operandoA / self.operandoB

arimetica1 = Arimetica(5, 3)
print(arimetica1.suma())
# >>> 8
print(arimetica1.resta())
# >>> 2
print(arimetica1.multiplicacion())
# >>> 15
print(f'{arimetica1.division():.2f}')
# >>> 1.67
# Usamos :.2f para imprimir la division con decimales

# Ejercicio: Hallar le area de un rectangulo usando clases y objetos
class Rectangulo:
    # inicializamos y creamos los atributos de la clase
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    # creamos el metodo:
    def area(self):
        return self.base * self.altura

# Creamos un objeto en la que la base y la altura sean proporcionados por el usuario
base = int(input('Dame la base: '))
altura = int(input('Dame la altura: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El Area es: {rectangulo1.area()}')

base = int(input('Dame la base: '))
altura = int(input('Dame la altura: '))
rectangulo2 = Rectangulo(base, altura)
print(f'El Area es: {rectangulo2.area()}')

# Ejercicio: Crear una clase para calcular el volumen de una cubo/objeto:
class Cubo:
    def __init__(self, ancho, alto, profundo) -> None:
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
    def Volumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input('Dame el ancho: '))
alto = int(input('Dame el alto: '))
profundo = int(input('Dame el profundo: '))
cubo1 = Cubo(ancho, alto, profundo)
print(f'El Volumen del cubo es: {cubo1.Volumen()}')