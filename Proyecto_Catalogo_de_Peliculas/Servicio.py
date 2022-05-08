# creamos nuestra clase administrador de catalogo de peliculas, n el cual estara en un archivos txt ('catalogo.txt') que depende de los 
# objetos peliculas
import os
from Pelicula import Pelicula

class Catalogo():
    ruta_archivo = 'catalogo.txt'
    
    @classmethod
    def agregar_pelicula(cls, nueva_pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(str(nueva_pelicula)+'\n')
        return str(nueva_pelicula)

    @classmethod
    def listar_Peliculas(cls):
        string = ''
        with open(cls.ruta_archivo, 'r', encoding='utf8') as s:
            string += s.read()
        return string
    
    @classmethod
    def eliminar_Catalogo(cls):
        os.remove('catalogo.txt')

if __name__ == '__main__':
    pelicula1 = Pelicula('Batman')
    pelicula2 = Pelicula('Tom y Jerry')
    pelicula3 = Pelicula('Guerra Mundial Z')

    catalogo1 = Catalogo()

    catalogo1.agregar_pelicula(pelicula1)
    catalogo1.agregar_pelicula(pelicula2)
    catalogo1.agregar_pelicula(pelicula3)
    print(catalogo1.listar_Peliculas())
    # Esta peliculas es: Batman
    # Esta peliculas es: Tom y Jerry
    # Esta peliculas es: Guerra Mundial Z

    catalogo1.eliminar_Catalogo()
    print(catalogo1.listar_Peliculas())
    # FileNotFoundError: [Errno 2] No such file or directory: 'catalogo.txt'