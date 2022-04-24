# Basicamente una Doubble Linked List es una linked list pero sus nodos (a excepcion del primero a no ser que sea una circular doubble linked list)
# saben o apuntan de referncia tanto al nodo siguinete de si mismo como al nodo ANTERIOR de si mismos.

# None <- Nodo1 -> <- Nodo2 -> <- Nodo3 -> <- Nodo4 -> None

# Nuestra clase de nodos
class Nodo(object):
    def __init__(self, valor, siguiente = None):
        self.valor = valor
        self.siguiente = siguiente

# creamos nuestra clase de DoubbleLinkedList y le netemos como herenecia a nuestra clase nodo (para tener de herencoa los atributos valor y siguiente) 
class DoubbleLinkedList(Nodo):
    def __init__(self, valor, previous = None, siguiente = None):
        # Aca llamamos a los atrubutos de Nodo como herencia
        Nodo.__init__(self, valor, siguiente)
        # A prevuis no lo llamamos de Nodo porque Nodo no tiene este atribito. el atributo previus es el que apuntara al nodo al nodo anterior
        self.previous = previous

# Creamos nuestra DoubbleLinkedList con un el primer nodo con valor 1, y luego lo rellenamos de valor de tal formaquer quede del 1 al 5. 
head = DoubbleLinkedList(1)
tail = head
for i in range(2, 6):
    tail.siguiente = DoubbleLinkedList(i, tail)
    tail = tail.siguiente

# Si queremos iterar de forma normal interamos desde el primer nodo hasta el ultimo usando el atributo siguiente.
while head != None:
    print(head.valor)
    head = head.siguiente

print('______')
# si queremos iterar de forma alrevez iteramos desde el utimo nodo hasta el ultimo con el atributo previous
while tail != None:
    print(tail.valor)
    tail = tail.previous

# Basicamente asi es como funciona una doubble linked list.