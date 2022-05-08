# Ahora creamos nuestro manejador de archivos usando los metodos __enter__ y __exit__,  estos metodos son de la clase object
class ManejorDeRecursos():
    def __init__(self, archivo):
        self.archivo = archivo
    
    def __enter__(self):
        print('Entramos en el Archivo'.center(50, '-'))
        self.archivo = open(self.archivo, 'r', encoding='utf8')
        return self.archivo
    

    # La firma de este metodo es tener si o si trs parametros; tipo_de_excepcion, valor_excepcion y traza_error, pues esto lo pide para poder
    # trabajar con with y dado ocurre un error de excepcion
    def __exit__(self, tipo_de_excepcion, valor_excepcion, traza_error):
        print('Salimos del archivo'.center(50, '-'))
        # preguntamos si el atributo archivo esta apuntando a un objetos y si es asi lo cerramos
        if self.archivo:
            self.archivo.close()

if __name__ == '__main__':
    # RECORDEMOS: with aplica automaticamente los metodos __enter__ y __exit__, cuando entramos podemos hacer cosar con el archivos abierto y 
    # cuando salimos del with llo cerramos
    with ManejorDeRecursos('nuevo_archivo.txt') as archivo:
        # --------------Entramos en el Archivo--------------
        print(archivo.read())
        # Este es otro archivo que esta remplazando al anterior
        # jejejjejejje
        # estamos agregando otra lineaXd
    # ---------------Salimos del archivo----------------
