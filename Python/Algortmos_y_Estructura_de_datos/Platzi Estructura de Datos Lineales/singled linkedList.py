# ahora crearemos nuestra clase linked list (singly linked list)
# Pero necesitamos llamar a nuestra clase de nodos para crear nodos

from nodos import Nodo

class SinglyLinkedList(object):
    # Creamos nuestro constructor y creamos dos atributos a tail (que hace referencia a la serie de nodos de la linked list) y size es la
    # longitud de la lista
    def __init__(self) -> None:
        self.tail = None
        self.size = 0

    # Creacion de metodos:

    # metodo para agregar nodos/elementos, pasamos el parametro del valor del nodo.
    def append(self, value):
        # creamos el nodo con la clase nodo, este nodo no apunta a un nodo siguiente, es decir, su parametro siguiente es None.
        nuevoNodo = Nodo(value)

        # Si la linked list no tiene elementos entonces la linked list sera el nodo que creamos
        if self.size == 0:
            self.tail = nuevoNodo
        
        # Si ya tiene, procedemos a interar hasta el ultimo nodo que no apunta a un nodo siguiente y al atributo siguiente de ese nodo le
        # hacemos que apunte al uevo nodo creado (nuevoNodo). asi se agregaria a la linkd list. 
        else:
            current = self.tail
            while current.siguiente != None:
                current = current.siguiente
            current.siguiente = nuevoNodo
        # Aumentamos el tamaño porque agregamos elmentos
        self.size += 1

    # Agregar elemento en inicio, solo para linked list que ya tengan valores/nodos:
    def agregarInicio(self, valor_a_agregar):
        nuevoNodo = Nodo(valor_a_agregar, self.tail)
        self.tail = nuevoNodo
        self.size += 1

    # para insertar o mas bien agregar un nuevo nodo en un indice dado (Ojo no estamos eliminando, estamos agregando en una posicion de la lista)
    # Vamos iterando por los nodos con el valor de la longitud de la lista (0 hasta self.size) hasta llegar al nodo correspondiente al la indecima
    # iteracion, creamos el nodo con el valor a insertar y que apunte al nodo correspondiente del indice y tambien con ayuda de otra variable
    # que guarda el nodo anterior al nodo corresponidente del indice y hacemos que apunte al nuevo nodo.
    def insertar(self, valor_a_insertar, indice):
        current = self.tail
        previus = self.tail
        for i in range(self.size):
            if i == indice:
                nuevoNodo = Nodo(valor_a_insertar, current)
                previus.siguiente = nuevoNodo
                self.size += 1
                return current.valor
            else:
                previus = current
                current = current.siguiente


    # Para mostra la longitud de la lista
    def __len__(self):
        return str(self.size)

    # Para eliminar un nodo de la linked list (Realmente no lo estamos eliminando, estamos hanciendo que el nodo anterior del nodo que queremos
    # eliminar apunte al nodo siguiente del nodo que queremos eliminar. asi la cadena o serie de nodos de la linked list nunca tendra un nodo
    # que lo referencie y por tanto sale de la serie.)
    def eliminar(self, valor_eliminar):

        # Current para iterar por cada nodo y previus para guardar el nodo anterior al nodo que queremos eliminar.
        current = self.tail
        previus = self.tail
        while current:
            # caso #1: si el nodo a eliminar es el primero de la linked list, entonces hacemos que nuestras serie de nodos (tail) sea
            # el 2do nodo de la serie y asi ya no se tendria en cuenta nunca mas el primer elemento.
            if current.valor == valor_eliminar:
                if current == self.tail:
                    self.tail = current.siguiente

                #  Caso #2: cuando el current de con el nodo a eliminar hacemos que el nodo anterior (previus) 
                #  apunte al nodo siguiente de current y asi sacamos de la la serie de nodos el nodo a eliminar
                else:
                    previus.siguiente = current.siguiente
                    self.size -= 1
                    return current.valor
            else:
                previus = current
                current = current.siguiente
    
    # Para eliminar el ultimo elemnto
    def elimnarUltimoElemento(self):
        current =  self.tail
        # Para el caso de que haya un solo elemnto en la linked list
        if current.siguiente == None:
            current = None
        # para el caso de que la linked list tenga mas de un elemento. la idea aca es ir iterante por cada nodo  hasta llegar al penultimo nodo
        # de la linked list (o mas bien al nodo anterior del nodo que apunta hacia None) y luego hacer que ese penultimo nodo apunte hacia None
        # asi se 'saca' al ultimo nodo de la serie y queda el penultimo nodo como ultimo. 
        else:
            while current.siguiente.siguiente != None:
                current = current.siguiente
            current.siguiente = None

        self.size -= 1
        return current
    
    # Para la buscar un elemento de la lista, retorna true si esta o false si no
    def busquedad(self, valor_a_buscar):
        current = self.tail
        while current:
            if current.valor == valor_a_buscar:
                return True
            current = current.siguiente
        return False

    # para insertar/cambiar el valor de un nodo de la linked list.
    def cambiar(self, valor_a_insertar, en_donde_insertar):
        current = self.tail
        while current:
            if current.valor == en_donde_insertar:
                current.valor = valor_a_insertar
                return valor_a_insertar
            current = current.siguiente
        return False
    
    # Para saber la cantidad de veces que aparece un elemento dado
    def contador(self, valor):
        current = self.tail
        cont = 0
        while current:
            if current.valor == valor:
                cont += 1
            current = current.siguiente
        return cont
    
    # La forma en la que se imprimara la linke list. cuando nosostro llamamos a print para imprimir la linked list, se llama este metodo.
    def __str__(self) -> str:
        current = self.tail
        string = "|"
        for i in range(self.size):
            if i != self.size-1:
                string += str(current.valor) + ', '
            else:
                string += str(current.valor)
            current = current.siguiente
        string += '|'
        return string
        # |1, 2, 3, 'Mango', True|

    # Limpiamos la linked list, es decir, volvemos a sus valores iniciales 
    def limpiar(self):
        self.tail = None
        self.size = 0

# Creemos nuestra singly linked list
linkedlist = SinglyLinkedList()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
linkedlist.append(4)
linkedlist.append(5)
linkedlist.append(5)
print(linkedlist)
# |1, 2, 3, 4, 5, 5|
linkedlist.eliminar(2)
print(linkedlist)
# |1, 3, 4, 5, 5|
print(linkedlist.__len__())
# 5
print(linkedlist.busquedad(4))
# True
print(linkedlist.busquedad(9))
# False
linkedlist.cambiar(5,4)
print(linkedlist)
# |1, 3, 5, 5, 5|
print(linkedlist.contador(5))
# 3
linkedlist.elimnarUltimoElemento()
print(linkedlist)
# |1, 3, 5, 5|
linkedlist.agregarInicio(0)
print(linkedlist)
# |0, 1, 3, 5, 5|
linkedlist.insertar(100, 2)
print(linkedlist)
# |0, 1, 100, 3, 5, 5|
linkedlist.limpiar()
print(linkedlist)
# ||

# Basicamente una linked list es una serie de nodos.