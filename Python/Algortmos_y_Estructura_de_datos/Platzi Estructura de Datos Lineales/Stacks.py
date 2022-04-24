# Los stacks (o pilas) son colecciones lineales basados en arrays o linked list, su principio fundamentales es LIFO (Last-In-First-Out) el primer elemento
# en llegar sera el ultimo en slair o el ultimo elemento en entrar sera el el primero en salir y tiene dirversoso metodos que podemos 
# usar si lo requeremos en inclusive pordriamos crear otros metodos.

# Creemos nuestro stack

# Necitamos otar vez los nodos
from nodos import Nodo
print('________________________________________')

class Stack(object):
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    # Creacion de metodos

    # Para agregar elementos en nuestra pila
    def push(self, valor):
        nodo = Nodo(valor)
        # Si ya hay valores en la pila, entonces hacemos que este nevo elemento este de primero en la lista (este en top). por eso, se cumple
        # el LIFO en ultimo elemento en ingesar, sera el primero en salir.
        if self.top:
            nodo.siguiente = self.top
            self.top = nodo
        # Por si no hay elementos en la pila, entonces selft top inicializa con el nuevo nodo
        else:
            self.top = nodo
        
        # Aumentamos la londitud de la pila porque estamos agregando elementos.
        self.size += 1
    
    # Para retornar si hay un elemento en la pila
    def buscar(self, valor_a_buscar):
        top = self.top
        while top:
            if top.valor == valor_a_buscar:
                return 'The value is in the stack'
            top = top.siguiente

        return 'The value is not in the stack'
    
    # Sacar elemento de la pila
    def pop(self):
        # verificamos si hay elementos en la pila y si es asi, comprobamos si el elemento a eliminar es el unico o si hay mas elemntos en la pila
        # y hacemos los respectivos procedimientos segun sea el caso.
        if self.top:
            valor_eliminado = self.top.valor
            self.size -= 1

            if self.top.siguiente:
                self.top = self.top.siguiente
            else:
                self.top = None
            
            # Retornamos el elemnto eliminado
            return valor_eliminado

        # Si el stack esta vacio, retornamos lo siguiente.
        else:
            return ('The Stack is Empty')
        
    
    # Saber que elemento esta de primero en la pila (mostrar a top)
    def peek(self):
        if self.top:
            return self.top.valor
        else:
            return 'The Stack is Empty'
    
    # Limpiar la pila
    def clear(self):
        while self.top:
            self.pop()
    
    # Para imprimir por pantalla la pila
    def __str__(self) -> str:
        top = self.top
        string = ''
        if self.size == 0:
            string = 'The Stack is Empty'

        else:
            while top:
                if top.siguiente == None:
                    string += str(top.valor)
                else: 
                    string += str(top.valor) + ' -> '
                top = top.siguiente

        return string


alimentos = Stack()
print(alimentos)
# >>> The Stack is Empty

print(alimentos.peek())
# >>> The Stack is Empty

print(alimentos.pop())
# >>> The Stack is Empty

alimentos.push('Huevos')
print(alimentos)
# >>> Huevos
alimentos.push('Tocinetas')
print(alimentos)
# >>> Tocinetas -> Huevos
alimentos.push('Jamon')
print(alimentos)
# >>> Jamon -> Tocinetas -> Huevos
alimentos.push('Pan')
print(alimentos)
# >>> Pan -> Jamon -> Tocinetas -> Huevos

print(alimentos.buscar('Jamon'))
# >>> The value is in the stack
print(alimentos.buscar('Queso'))
# >>> The value is not in the stack