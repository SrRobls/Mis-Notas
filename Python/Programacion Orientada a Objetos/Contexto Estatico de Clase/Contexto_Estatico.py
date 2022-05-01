'''
En programacion orientada a objetos de python podemos crear variables de clase (todos los objetos instanciados de una clase que tenga una 
variable de clase compartiran esa variable), como tambien metodos estaticos (tiene como referencia a lo estatico de la clase, es mas bien 
como crear funciones dentro una clase, por tanto no usa el self), metodos de clase (que tienen como referencia solo a la clase en si, por 
tanto debemos darle una referncia de la clase, por lo general se usa cls. y no a las instancias/objetos, por tanto no usamos self. Este
metodo se puede usar para crear otros objetos y poder accer a a sus atributos dodos) y los metodo de instancia (que son con lo que hemos venido 
trabajando y como son de instancia necesitan la refencia de los objetos instanciados, es decir, necesitan a self). Pero hay que tener en cuenta 
dos definiciones importantes, los estatico y lo dinamico.

Lo Estatico: la parte que tiene como referencia a la clase en si, no trabaja con lo dinamico (instancias)
Lo Dinamico: Esta parte comienza o nace cuando creamos objetos de una clase, esta parte trabaja tanto con lo dinamico y lo estatico de una clase
'''


class Clase():
    variable_de_clase = 'Esto es una variable de clase'
    def __init__(self, variable_de_instancia, nombre) -> None:
        self.nombre = nombre
        self.variable_de_instancia = variable_de_instancia

    # metodo de instancia
    def metodo_de_instancia(self):
        print(f'Hola {self.nombre} soy un metodo de instancia. Necesito a self/this para poder accedr a tu nombre ya que trabajo con los objetos instanciados')
        # en los metodos de instancia podemos acceder a los metodos de clase, inclusive si son estatiicos o de clase (pero recordemos que debemos usar self, pues necesitamos refrenciar al objeto instanciado)
        # print(self.obtener_nombre())
        # print(self.metodo_estatico('juan'))
        # print(self.metodo_de_clase('pedro'))

    # recordemos que los decoradores hacen cambiar el comportamiento de una clase.
    
    # metodo estatic. para esto necesitamos al decorador @staticmethod para decirle a python que vamos a definir un metodo estatico y no uno
    # de instancia
    @staticmethod
    def metodo_estatico(name):
        print(f'Hola {name} Esto es un metodo estatico, notar que no necesita a self o la refencia de los objeto. Pero necesito referenciar a la clase si quiero acceder a sus elementos')
        print(f'Clase.variable_de_clase -> {Clase.variable_de_clase}') 
        
    
    # metodo de clase, necesitamos al decorador @classmethod y pasarle la referencia de la clase. y con podemos acceder a todos lo elemetos de la clase
    # (variable_de_clase y  metodos)
    @classmethod #y con este decorador le estamos dicentdo a python tambien que quiero usar este metodo si necesida de un objeto de instancia (sin necesidad del self), pero python necesita entonce la referencia de la clase en general, asi que se lo damos con cls
    def metodo_de_clase(cls, nombre=None):
        cls.nombre = print(nombre)
        cls.metodo = print(f'Hola {nombre} estas en un metodo de clase')
        # Desde aca podemos accer a las varaible de clase de la clase en general
        # print(cls.variable_de_clase)
        return cls('cualquier joa', nombre)
        # en si lo que estamos haciendo es retornar una instancia de la misma clase y ademas dandole mas atributos (atributos singulares).
    
    # creemos un metodo de instancia para que nuestro metodo de clase pueda accder al nombre
    def obtener_nombre(self):
        return self.nombre

print('Variable de Clase y Metodos de Instancia'.center(50, '-'))

# Para acceder en las variable de clase, tenemos que hacer la refencia a la clase
print(Clase.variable_de_clase)
# Esto es una variable de clase

# Tambien podemos acceder a la variable de clase mediante los objetos instanciados (recordar que lo dinamico puede acceder a lo estatico)
clase1 = Clase('Esta es una variable de instancia', 'Juan')
print(clase1.variable_de_instancia)
# Esta es una variable de instancia
print(clase1.variable_de_clase)
# # Esto es una variable de clase
clase1.metodo_de_instancia()
# Hola Juan soy un metodo de instancia. Necesito a self/this para poder accedr a tu nombre ya que trabajo con los objetos instanciados

clase2 = Clase('Esta es otra variable de instancia', 'Pedro')
print(clase2.variable_de_instancia)
# Esta es otra variable de instancia
print(clase2.variable_de_clase)
# Esto es una variable de clase
clase2.metodo_de_instancia()
# Hola Pedro soy un metodo de instancia. Necesito a self/this para poder accedr a tu nombre ya que trabajo con los objetos instanciados

# Notar que las varibles de instancia son diferentes segun el objeto instanciado.

# e inclusive podemos cambiar el valor de esa variable de clase, recordemos que debemos referencia a la Clase 
# a esto se le llama cambio a vuelo y OJO esto solo es posible en python ya que es dinamico
Clase.variable_de_clase = 'Cambiamos nuestra variable de clase'
print(clase1.variable_de_clase)
# Cambiamos nuestra variable de clase
print(clase2.variable_de_clase)
# Cambiamos nuestra variable de clase
Clase.variable_de_clase = 'Esto es una variable de clase'

print('Metodo Estatico'.center(50, '-'))
clase1.metodo_estatico('Sebas')
# Hola Sebas Esto es un metodo estatico, notar que no necesita a self o la refencia de los objeto. Pero necesito referenciar a la clase si quiero acceder a sus elementos
# Clase.variable_de_clase -> Esto es una variable de class

print('Metodo de Clase'.center(50, '-'))
prueba_metodo_clase = clase1.metodo_de_clase()
# por tanto podemos acceder a los atributos del metodo en si.

prueba_metodo_clase.nombre
# jhan
prueba_metodo_clase.metodo
# Hola Jhan estas en un metodo de clase
prueba_metodo_clase.variable_de_instancia
# Hola Jhan soy un metodo de instancia. Necesito a self/this para poder accedr a tu nombre ya que trabajo con los objetos instanciado 

# y tambien podemos accederr a los metodos de la clase en general y a las variables de clase

prueba_metodo_clase.metodo_de_instancia()
# Hola Jhan soy un metodo de instancia. Necesito a self/this para poder accedr a tu nombre ya que trabajo con los objetos instanciados
prueba_metodo_clase.metodo_estatico('jhan')
# Hola jhan Esto es un metodo estatico, notar que no necesita a self o la refencia de los objeto. Pero necesito referenciar a la clase si quiero acceder a sus elementos
# Clase.variable_de_clase -> Esto es una variable de clase

print(prueba_metodo_clase.variable_de_clase)
# Esto es una variable de clase