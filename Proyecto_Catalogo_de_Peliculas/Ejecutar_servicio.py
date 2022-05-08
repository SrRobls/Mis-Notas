from Pelicula import Pelicula
from Servicio import Catalogo

def catalogo(catalogo):
    menu = '¿Que quieres hacer?\n\t1. Agregar Pelicula\n\t2. Listar Peliculas\n\t3. Eliminar Archivo de Catalogo\n\t4. Salir\n'
    while True:
        try:
            decicision = int(input(menu + 'Opcion: '))
            if decicision == 1:
                pelicula = Pelicula(input('Nombre de la Pelicula: '))
                catalogo.agregar_pelicula(pelicula.nombre)
            elif decicision == 2:
                print(catalogo.listar_Peliculas())
            elif decicision == 3:
                catalogo.eliminar_Catalogo()
                print('Catalogo Eliminado')
            elif decicision == 4:
                break
            else:
                print('Error: Esa Opcion es Invalida')
        except ValueError:
            print('Error: Esa Opcion es Invalida')
        except FileNotFoundError:
            print('No hay Peliculas En El Catalogo')
    print('Salimos'.center(50,'-'))

catalogo1 = Catalogo()
catalogo(catalogo1)