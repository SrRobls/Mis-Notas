# Crear una clase stacks pero usando arrays.

from Arrays import Array

class StackArray(object):
    def __init__(self, longitud) -> None:
        self.top = list()
        self.longitud = longitud
        for _ in range(longitud):
            self.top.append(None)
    
    def push(self, valor):
        top = self.top
        for i in range(self.longitud):
            if top[i] == None:
                top[i] = valor
                return

        return 'The stack is full'
    
    def pop(self):
        top = self.top
        veces_de_nones = 0

        for celda in top:
            if celda == None:
                veces_de_nones += 1
        
        if veces_de_nones == self.longitud:
            return 'The stack in empty'
        
        else:
            ind = self.longitud - veces_de_nones
            value = top[ind-1] 
            top[ind-1] = None
            return value
    
    def __str__(self) -> str:
        return str(self.top)
    

    def clear(self):
        top = self.top
        for i in range(self.longitud):
            if top[i] != None:
                top[i] = None

alimentos = StackArray(3)
print(alimentos)
# >>> [None, None, None]
alimentos.push('Eggs')
alimentos.push('Ham')
print(alimentos)
# >>> ['Eggs', 'Ham', None]

alimentos.pop()
print(alimentos)
# >>> ['Eggs', None, None]
alimentos.pop()
print(alimentos)
# >>> [None, None, None]

alimentos.push('Eggs')
alimentos.push('Ham')
alimentos.push('Bread')
print(alimentos)
# >>> ['Eggs', 'Ham', 'Bread']

alimentos.clear()
print(alimentos)
# >>> [None, None, None]