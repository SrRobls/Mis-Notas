# Los queues o colas son colecciones que se basa fundamentalmente es FIFO (First-In-First-Out), que el primero en entrar es el primero en salir
# existen unas variantes de las Queues y son la Priority Queues que se basa en FIFO pero con elementos de mayor/menor prioridad.

# Queue basado en listas.




class Queue_Based_list(object):
    def __init__(self) -> None:
        self.items = []
        self.size = 0
    
    # Creacion de metodos:

    # Para agregar elementos. usamos insert para insrtar el elemento en la primera posicion de la lista (Ojo inserte es diferente que append o 
    # que remplazar), asi la lista_ Queue quedaria asi [...., elemeto3, elemeto2, elemeto1]
    def enqueue(self, valor):
        items = self.items
        items.insert(0, valor)
        self.size += 1
    
    # Para eliminar elementos. estructurando la lista como el ejemplo aterior, [...., elemeto3, elemeto2, elemeto1] al hacer pop eliminamos el ultimo
    # elemento de la lista, es decir el primer elemento ne entrar. asi se cumpliria FIFO.
    def dequeue(self):
        items = self.items
        valor = items.pop()
        self.size -= 1
        return valor
    
    # Para iterar por el Queue.
    def traverse(self):
        items = self.items
        posicion = 0
        for item in items:
            print(f'{self.size - posicion}. {item}')
            posicion += 1
            


alimento = Queue_Based_list()
alimento.enqueue('Pan')
alimento.enqueue('Arepa')
alimento.enqueue('Pizza')

alimento.traverse()
# 3. Pizza
# 2. Arepa
# 1. Pan
alimento.dequeue()
alimento.traverse()
# 2. Pizza
# 1. Arepa

# Notar que se cumple el FIFO, el primero en llegar es el primer en salir.
print('__________________________________________________________________')

# Creemos un Queue PERO basada en stack o dos listas de python.

class Queue(object):
    def __init__(self) -> None:
        self.stack_interior = []
        self.stack_exterior = []
    
    # Creacion de metodos:

    # Agregar elementos. basicamente agrgamos elementos al stack interior.
    def enqueue(self, valor):
        self.stack_interior.append(valor)

    # Eliminar elementos. si no hay elementos en el stack exterior, entonces mientras haya elemntos en el stack interior, le vamos haciendo pops
    # de tal forma que por cada elemento retornado del pop se agregue al stack exterior (cabe recalcar que basicamente estamos agregando desde el ultimo 
    # hasta el primer elemento del stack interior). luego de esto le hacemos pop al stack exterior y nos returna el primer valor que introducimos al stack interior
    # cumpliendose asi FIFO.
    def dequeue(self):
        if not self.stack_exterior:
            while self.stack_interior:
                self.stack_exterior.append(self.stack_interior.pop())
        
        print(self.stack_exterior.pop())
    
    

numeros_pares = Queue()
numeros_pares.enqueue(2)
numeros_pares.enqueue(4)
numeros_pares.enqueue(6)
numeros_pares.enqueue(8)

print(numeros_pares.stack_interior)
# [2, 4, 6, 8]
numeros_pares.dequeue()
# 2
print(numeros_pares.stack_interior)
# []
# Pues los elmentos al usar dequeue se pasan al stack_exterior
print(numeros_pares.stack_exterior)
# [8, 6, 4]

numeros_pares.dequeue()
# 4
numeros_pares.dequeue()
# 6
print(numeros_pares.stack_exterior)
# [8]
# Importante notar que se cumple el principio FIFO de los queue, los primero en llegar son los primeros en salir.

numeros_pares.enqueue(10)
numeros_pares.dequeue()
# 8
print(numeros_pares.stack_interior)
# [10]
print(numeros_pares.stack_exterior)
# []
numeros_pares.dequeue()
# 10

print(numeros_pares.stack_interior)
print(numeros_pares.stack_exterior)
# []
# []

print('____________________________________')
# mi forma:

class Queue(object):
    def __init__(self) -> None:
        self.stack_interior = []
        self.stack_exterior = []
    
    # Creacion de metodos:

    # Agregar elementos.
    def enqueue(self, valor):
        self.stack_interior.append(valor)

    # Eliminar elementos.
    def dequeue(self):
        if not self.stack_exterior:
            while self.stack_interior:
                self.stack_exterior.append(self.stack_interior.pop())
        
        print(self.stack_exterior.pop())
    
    # Para mostrar el queue.
    def __str__(self) -> str:
        stack = self.stack_interior
        while stack:
            self.stack_exterior.append(stack.pop())
        
        return str(self.stack_exterior)

deportes = Queue()
deportes.enqueue('Futbol')
deportes.enqueue('Tenis')
deportes.enqueue('Baloncesto')

print(deportes)
# 'Baloncesto', 'Tenis', 'Futbol']

deportes.dequeue()
# Futbol
print(deportes)
# ['Baloncesto', 'Tenis']

# Notar la aplicacion de FIFO, el primero que entra es el primero que sale.

# Queue basado en Nodos (Nodos dobles)
 
class NodoDoble(object):
    def __init__(self, valor, siguiente = None, anterior = None):
        self.valor = valor
        self.siguiente = siguiente
        self.anterior = anterior
    
class Queue_based_nodes:
    def __init__(self) -> None:
        # Referncia al primero nodo
        self.head = None
        # Referemncia al ultmimo nodo
        self.tail = None
        # referencia al tamaños de queue
        self.size = 0
    
    # Creacion de Nodos:
    def enqueue(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.size == 0:
            self.head = nuevo_nodo
            self.tail = self.head
        else:
            nuevo_nodo.anterior = self.tail
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo
        
        self.size += 1
    
    def dequeue(self):
        current = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
        elif self.size > 1:
            self.head = self.head.siguiente
            self.head.anterior = None
            self.size -= 1
        
        return current.valor

    def __str__(self) -> str:
        currente = self.head
        string = '| '
        while currente != None:
            string += currente.valor + ' '
            currente = currente.siguiente
        string += '|'
        return string

utiles_escolares = Queue_based_nodes()
utiles_escolares.enqueue('Lapiz')
utiles_escolares.enqueue('Borrador')
utiles_escolares.enqueue('Cuaderno')

print(utiles_escolares)
# | Lapiz Borrador Cuaderno |
utiles_escolares.dequeue()
utiles_escolares.dequeue()
print(utiles_escolares)
# | Cuaderno |
utiles_escolares.enqueue('Colores')
print(utiles_escolares)
# | Cuaderno Colores |

utiles_escolares.dequeue()
utiles_escolares.dequeue()
print(utiles_escolares)
# | |

# Notar que se cumple FIFO.