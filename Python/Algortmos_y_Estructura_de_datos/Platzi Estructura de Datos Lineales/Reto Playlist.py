# Crear una clase para hacer una playlist con las siguientes restricciones, usar queues, crear metodos para añadir canciones y reproducirlas,
# es decir, sacarlas, estas se deben reproducir en el orden añadido FIFO.

# Generamos nustra clase nodo:

class Nodo(object):
    def __init__(self, valor, siguiente = None, anterior = None) -> None:
        self.valor = valor
        self.siguiente = siguiente
        self.anterior = anterior


# Ahoracreemos nuestra classe playlist.
class Playlist(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.TotalCanciones = 0
        self.indentificador = 0
    
    # Creacion de metodos:
    def añadir(self, cancion):
        nueva_cancion = Nodo(cancion)
        if self.TotalCanciones == 0:
            self.head = nueva_cancion
            self.tail = self.head
        else:
            current = self.head
            while current.siguiente != None:
                current =  current.siguiente
            current.siguiente = nueva_cancion
            nueva_cancion.anterior = current
            self.tail = nueva_cancion
        
        self.TotalCanciones += 1
    
    # Reproducir la cancion correspondiente de la playlist
    def reproducir(self):
        if self.TotalCanciones == 0 or self.indentificador >= self.TotalCanciones:
            print('No hay canciones para reproducir.')
        else:
            current = self.head
            for _ in range(self.indentificador):
                current = current.siguiente
            print(current.valor)
            self.indentificador += 1
        
        # Esta parte sirve para que cuando se reproducza la ultima cancion se seleccione la primera para ser reproducida.
        if self.indentificador == self.TotalCanciones:
            self.indentificador = 0
    
    # Para selccionar una musica anterior y posteriormente reproducirla
    def SeleccionarAnterior(self):
        if self.indentificador != 0:
            self.indentificador -= 1

    # la forma de mostrar playlist.
    def __str__(self) -> str:
        current = self.head
        string = ''
        for i in range(self.TotalCanciones):
            if i == self.indentificador:
                string += '*'
            if i == self.TotalCanciones-1:
                string += str(i+1) + '. ' + current.valor
                current = current.siguiente
                continue
            string += str(i+1) + '. ' + current.valor + '\n'
            current = current.siguiente
        return string

print('El * indica la cancion que se va a reporducir.')

canciones = Playlist()
canciones.añadir('It Was a Good Day')
canciones.añadir('After Dark')

print(canciones)
# *1. It Was a Good Day
# 2. After Dark

canciones.reproducir()
# It Was a Good Day
canciones.reproducir()
# After Dark
print(canciones)
# *1. It Was a Good Day
# 2. After Dark

canciones.reproducir()
# It Was a Good Day

canciones.añadir('Mary Jean')
canciones.añadir('Stan Lee')

print(canciones)
# 1. It Was a Good Day
# *2. After Dark
# 3. Mary Jean
# 4. Stan Lee
canciones.reproducir()
# After Dark
canciones.reproducir()
# Mary Jean
canciones.reproducir()
# Stan Lee

print(canciones)
# *1. It Was a Good Day
# 2. After Dark
# 3. Mary Jean
# 4. Stan Lee
canciones.reproducir()
# It Was a Good Day

print(canciones)
# 1. It Was a Good Day
# *2. After Dark
# 3. Mary Jean
# 4. Stan Lee

canciones.SeleccionarAnterior()
print(canciones)
# *1. It Was a Good Day
# 2. After Dark
# 3. Mary Jean
# 4. Stan Lee

canciones.reproducir()
# It Was a Good Day

canciones.SeleccionarAnterior()
print(canciones)
# *1. It Was a Good Day
# 2. After Dark
# 3. Mary Jean
# 4. Stan Lee

canciones.reproducir()
# It Was a Good Day
canciones.reproducir()
# After Dark
canciones.reproducir()
# Mary Jean

print(canciones)
# 1. It Was a Good Day
# 2. After Dark
# 3. Mary Jean
# *4. Stan Lee

canciones.SeleccionarAnterior()
canciones.SeleccionarAnterior()

print(canciones)
# 1. It Was a Good Day
# *2. After Dark
# 3. Mary Jean
# 4. Stan Lee


# como podemos apreciar, podemos agrgar canciones y reporducirlas. tambine añadi un metodo mas que es para selccionar una musica anterior
# para luego reproducirla reporducirla, y algo particula que tambien se hizo, es que cuando se reporduce la ultima cancion automaticamente se
# seleccionar la primera cancion para reporducir, generando asi un bucle como lo son las playlist. 