# Creamos nuestra clase pelicula
class Pelicula():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self) -> str:
        return f'Esta peliculas es: {self.nombre}'

if __name__ == '__main__':
    pelicula1 = Pelicula('Batman')
    pelicula2 = Pelicula('Tom y Jerry')
    pelicula3 = Pelicula('Guerra Mundial Z')

    print(pelicula1,  pelicula2, pelicula3, sep='\n')
    # Esta peliculas es: Batman
    # Esta peliculas es: Tom y Jerry
    # Esta peliculas es: Guerra Mundial Z