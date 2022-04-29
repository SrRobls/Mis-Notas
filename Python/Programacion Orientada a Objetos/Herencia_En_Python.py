# Importamos un modulo (aunque tambien podemos crearla aca, pero esta vez vamos a importarla)
from Encapsulamiento_En_Python import Persona

# Cramos nuestra clase que recibira como clase padre Persona (la clase del modulo que importamos), cabe destacar que TODAS las clases en python
# tenen como clase padre el metodo Object, asi que no hace falta llamarla dentro de los () pues esta ya viene por defecto en las clases 
class Empleado(Persona):
    # Definimos los atributos de la clase Empleado, pero los atributos Nombre, apellido y edad los herdara de su la clase Persona
    def __init__(self, nombre, apellido, edad, sueldo) -> None:
        # con super podemos heredar los atribtos de la clase pafre, para esto tambien debemos pedir como parametr los valores
        # de nombre, apellido y edad y luego pasarselo como parametro a la clase padre con super. recordemos que __init__ es donde damos
        # los valores de los atributos (o bien, crearlo).
        super().__init__(nombre, apellido, edad)
        # y creamos los atributos idependientes que en este caso sere el sueldo,  este atributo no se hereda del padre. para este caso este atributo
        # sere encapsulado, por tanto es aconsejable añadir sus metodo Get y Set para ppoderlo manipular afuera de esta clase Empleado
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    

    def mostrar_detalles(self):
        # Tambien podemos llamar metodos de la clase padre, para esto tambien usamos super.Nombre_Del_Metodo(parametros)
        # Tener en cuenta que este etodo llamado SOLO tiene en cuenta los atributos heredados a esta clase de la clase padre de donde viene el metodo
        # por tanto tene en cuenta que este metodo SOLO trabaja con los atributos de la clase del cual viene.
        super().mostrar_detalles()
        # ademas hagamos que nos muestra el detalle del sueldo, pues este atributo no es de la clase padre si de esta clase original
        print(f'Sueldo: {self._sueldo}')
    
    # Notar que cuando quitamos este metodo de object, al finalizar la ejecucion nos imprime: El Objeto fue Eliminado: Pedro Juarez. esto pasa
    # porque estamos modificando este metodo en nuestra clase padre, por tanto cuando se termine de ejecutar este codigo, python por
    # defecto va eliminado cada variable, objeto, etc es decir, aplica el metodo __del__ y como esta clase usada es hereda de una clase
    # padre que tiene modificada este metodo (notar que en la clase padre esta modifica para que imprima ese texto cuando se elimine el objeto)
    # por tanto se ejecuta el codigo del metodo de la clase padre. Pero si ahora redescribimos esa metodo aca en esta clase hija, podemos modificar
    # para que no imprima eso (o bien agregarle cosas, o usarla a netro favor). esto se le llama rescribicion d los metodos.
    def __del__(self):
        return None

    # Por ejemplo en este caso reescribimos el metodo __str__. estamos usando a nuestro favor el metdo __str__ de nuestra clase padre para concatenarla con otros valores
    # (el sueldo), ahora en esta clase el metodo str trabaja como le indiquemos aca y no en como en nuestra clase padre
    # El metodo __str__ es el que no sirve para imprimir con el print(), le podemos decir como queremos que el print imprima este objeto. 
    def __str__(self) -> str:
        return f'{super().__str__()} {self._sueldo}'


empleado1 = Empleado('Pedro', 'Juarez', 29, 8000000)
print(empleado1.nombre)
print(empleado1.apellido)
print(empleado1.edad)
# Pedro
# Juarez
# 29
print(empleado1.sueldo)
# 8000000

empleado1.mostrar_detalles()
# Nombre: Pedro, Apellido: Juarez, Edad: 29.
# Sueldo: 8000000

print(empleado1)
# Pedro Juarez 29 8000000