'''
Dada una lista de personajes de la saga de Star Wars de las que se conoce su nombre, resolver 
la siguientes tareas:

a. listar los personajes ordenados alfabéticamente de manera ascendente;
b. determinar si el personaje Darth Maul está cargado y en qué posición se encuentra;
c. mostrar la información de los personajes que se encuentran antes y después de Hera Syndulla;
d. listar todos los personajes que comienzan con la letra L;
e. utilizar los métodos de ordenamiento y búsqueda más eficiente de acuerdo al tipo de dato
'''



lista = ['Luke Skywalker', 'Leia Organa', 'Han Solo', 'Darth Vader', 'Obi-Wan Kenobi', 'Doe Dameron', 
        'Kylo Ren', 'Rey', 'Finn','Anakin Skywalker', 'Padmé', 'Obi-Wan Kenobi', 'Qui-Gon Jinn', 'Jar Jar Binks',
        'Shmi Skywalker', 'Watto', 'Mace Windu', 'Lord Sidious', 'Darth Maul', 'Hera Syndulla', 'Nute Gunray', 'Conde Dooku', 'Jango Fett',
         'Senador Palpatine', 'General Grievous', 'Qira', 'Tobias  Beckett', 'Enfys Nest', 'Galen Erso']


class Star_Wars():
    def __init__(self, personajes) -> None:
        self.personajes = personajes

    # metodos:
    # Para ordenar
    def ordenar(self):
        personajes = self.personajes
        def shell(lista):
            intervalo = len(lista) // 2
            while intervalo != 0:
                for i in range(intervalo, len(lista)):
                    valor = lista[i]
                    indice = i
                    while indice >= intervalo and valor < lista[indice - intervalo]:
                        lista[indice] = lista[indice - intervalo]
                        indice -= intervalo
                    
                    lista[indice] = valor
                
                intervalo //= 2
            return lista
        personajes =  shell(personajes)
        personajes = self.personajes
        result = ''
        numeral = 0
        for personaje in  personajes:
                numeral += 1
                result += str(numeral) + '. ' + personaje +'\n'
        return result
    # Para Buscar
    def buscar(self, valor):
        personajes = self.personajes
        def Busquedad_secuencial(lista, valor_a_encontrar):
                for i in range(len(lista)):
                    if lista[i].lower() == valor_a_encontrar.lower():
                        return 'El valor ' + str(valor_a_encontrar) + ' se ecuentra en el indice ' + str(i+1)
                return 'El valor ' + str(valor_a_encontrar)+ ' No se encuentra'
        return Busquedad_secuencial(personajes, valor)
    # para mostrar los nombre antes y despues de uno dado
    def Mostrar_personajes_sin_uno_dado(self, personaje_no_mostrar):
        personajes = self.personajes
        def busquedad_secuencial(lista, valor_a_encontrar):
            for i in range(len(lista)):
                if lista[i] == valor_a_encontrar:
                    return i
            return 'El valor ' + str(valor_a_encontrar)+ ' No se encuentra'
        
        medio = busquedad_secuencial(personajes, personaje_no_mostrar)

        return personajes[:medio], personajes[medio+1:]
    # para mostrar los nombres que inicien con L
    def comienzan_con_l(self):
        personajes = self.personajes
        result = ''
        numeral = 0
        for personaje in  personajes:
            if personaje[0].upper() == 'L':
                numeral += 1
                result += str(numeral) + '. ' + personaje +'\n'
        return result
                

personasjes_star_wars = Star_Wars(lista)

#a. listar los personajes ordenados alfabéticamente de manera ascendente;
print(personasjes_star_wars.ordenar()) 
# 1. Anakin Skywalker
# 2. Conde Dooku
# 3. Darth Maul
# 4. Darth Vader
# 5. Doe Dameron
# 6. Enfys Nest
# 7. Finn
# 8. Galen Erso
# 9. General Grievous
# 10. Han Solo
# 11. Hera Syndulla
# 12. Jango Fett
# 13. Jar Jar Binks
# 14. Kylo Ren
# 15. Leia Organa
# 16. Lord Sidious
# 17. Luke Skywalker
# 18. Mace Windu
# 19. Nute Gunray
# 20. Obi-Wan Kenobi
# 21. Obi-Wan Kenobi
# 22. Padmé
# 23. Qira
# 24. Qui-Gon Jinn
# 25. Rey
# 26. Senador Palpatine
# 27. Shmi Skywalker
# 28. Tobias  Beckett
# 29. Watto

# b. determinar si el personaje Darth Maul está cargado y en qué posición se encuentra;
print(personasjes_star_wars.buscar('Darth Maul')) 
# El valor Darth Maul se ecuentra en el indice 2

# c. mostrar la información de los personajes que se encuentran antes y después de Hera Syndulla;
print(personasjes_star_wars.Mostrar_personajes_sin_uno_dado('Hera Syndulla')) 
# Antes: ['Anakin Skywalker', 'Conde Dooku', 'Darth Maul', 'Darth Vader', 'Doe Dameron', 'Enfys Nest', 'Finn', 'Galen Erso', 'General Grievous', 'Han Solo']
# despues: ['Jango Fett', 'Jar Jar Binks', 'Kylo Ren', 'Leia Organa', 'Lord Sidious', 'Luke Skywalker', 'Mace Windu', 'Nute Gunray', 'Obi-Wan Kenobi', 'Obi-Wan Kenobi', 'Padmé', 'Qira', 'Qui-Gon Jinn', 'Rey', 'Senador Palpatine', 'Shmi Skywalker', 'Tobias  Beckett', 'Watto']

# d. listar todos los personajes que comienzan con la letra L;
print(personasjes_star_wars.comienzan_con_l())
# 1. Leia Organa
# 2. Lord Sidious
# 3. Luke Skywalker

# e. utilizar los métodos de ordenamiento y búsqueda más eficiente de acuerdo al tipo de dato
'''
usamos shell sort para ordenar y busquedad secuencia para buscar, para hallar el indice de 'Hera Syndulla' y mostrar las que estan antes y de
despues de ese nombre y buscar los nombre que comienzan en  L. 
'''
print('--------------------------------------------------------------------------------')
'''
Se dispone de las lista de superhéroes y villanos de la saga de Marvel Cinematic Universe 
(MCU) de los que contamos con la información de nombre del personaje y año de la primera 
película en la que apareció; a partir de estos resolver las siguientes actividades:

a. realizar un listado ascendente de los personajes ordenados por su nombre;
b. indicar quien fue el primer y el último personaje en aparecer en una película sin realizar 
un recorrido de la lista (podrían ser más de uno tanto el primero como el último);
c. realizar un listado de los personajes ordenados de manera descendente por año de aparición;
d. calcular el rango de años entre el primer personaje en aparecer y el último;
e. determinar si los personajes Capitan America y Rocket Raccoon están en la lista y en qué 
año aparecieron
'''

MCU = [['Batman', 1964], ['Hombre Araña', 1980], ['Gatubela', 2000], ['Jocker', 1964], ['Loki', 1999], ['Ultron', 2007], ['Venom', 1985],
        ['Galactus', 1970], ['Super Man', 1966], ['Thanos', 2019], ['Mujer Maravilla', 1982], ['Aqua Man', 1970], ['Hulk', 1967], ['D.Otopus', 1980],
        ['El Duende', 1981], ['Black Panther', 2014], ['Thor', 1992], ['lagarto', 1989], ['Craneo Rojo', 2001], ['Captain America', 1966]]

class SuperHeroes_Villanos():
    def __init__(self, mcu) -> None:
        self.lista = mcu

    # metodos:
    # ordenar
    def Ordenar(self, segun_que):
        lista = self.lista
        def merge_sort(lista):
            if len(lista) < 2:
                return lista
            else:
                ind_medio = len(lista) // 2

                sublista_izq = [lista[i] for i in range(0, ind_medio)]
                sublista_der = [lista[i] for i in range(ind_medio, len(lista))]

                sublista_izq = merge_sort(sublista_izq)
                sublista_der = merge_sort(sublista_der)

                if sublista_izq[ind_medio-1][segun_que] <= sublista_der[0][segun_que]:
                    return sublista_izq + sublista_der
                else:
                    result = mezcla(sublista_izq, sublista_der)
                    return result

        def mezcla(parte_izq, parte_der):
            mezclados = []
            while len(parte_izq) > 0 and len(parte_der) > 0:
                if parte_izq[0][segun_que] < parte_der[0][segun_que]:
                    mezclados.append(parte_izq.pop(0))
                else:
                    mezclados.append(parte_der.pop(0))

            if len(parte_izq) > 0:
                mezclados += parte_izq
            else:
                mezclados += parte_der

            return mezclados
        
        return merge_sort(lista)

    # Busqueda
    def Buscar(self, valor):
        lista = self.lista
        def buscar(lista):
            for i in range(len(lista)):
                if lista[i][0] == valor:
                    return valor + ' esta en la lista. Con año de aparicion: ' + str(lista[i][1])
            return 'Ese Super Heroe o Villano no esta en la lista'
        return buscar(lista)

superheores_y_Villanos = SuperHeroes_Villanos(MCU)


def listar(lista_a_listar):
    result = ''
    i = 1
    for heroe in lista_a_listar:
        result += str(i) + '. ' + heroe[0] + ', Año: ' + str(heroe[1]) +'\n'
        i += 1
    return result

'''
Para esto impementamos que el usuario pueda escoger en ordenar si ppor el nombre (0) o el año de aparicion en pelicula(1), y tambien
creamos una funcion para lista. 
Esto nos ayudara para hacer los ejercicios.
'''
# a. realizar un listado ascendente de los personajes ordenados por su nombre;
# ordenamos segun el nombre y lo listamos
print(listar(superheores_y_Villanos.Ordenar(0)))
'''
1. Aqua Man, Año: 1970
2. Batman, Año: 1964
3. Black Panther, Año: 2014
4. Captain America, Año: 1966
5. Craneo Rojo, Año: 2001
6. D.Otopus, Año: 1980
7. El Duende, Año: 1981
8. Galactus, Año: 1970
9. Gatubela, Año: 2000
10. Hombre Araña, Año: 1980
11. Hulk, Año: 1967
12. Jocker, Año: 1964
13. Loki, Año: 1999
14. Mujer Maravilla, Año: 1982
15. Super Man, Año: 1966
16. Thanos, Año: 2019
17. Thor, Año: 1992
18. Ultron, Año: 2007
19. Venom, Año: 1985
20. lagarto, Año: 1989
'''
# b. indicar quien fue el primer y el último personaje en aparecer en una película sin realizar

valores = superheores_y_Villanos.Ordenar(1)
print(f'Primer personaje: {valores[0][0]}, año: {valores[0][1]}')
print(f'Ultimo personaje: {valores[len(valores)-1][0]}, año: {valores[len(valores)-1][1]}')

'''
Basicamente ordenamos pero segun el año y una vez esto, imprimir el elemento del indice 0 y del largo-1
Primer personaje: Jocker, año: 1964
Ultimo personaje: Thanos, año: 2019
'''

# c. realizar un listado de los personajes ordenados de manera descendente por año de aparición;
def listar(lista_a_listar):
    result = ''
    i = 1
    lista_a_listar = list(reversed(lista_a_listar))
    for heroe in lista_a_listar:
        result += str(i) + '. ' + heroe[0] + ', Año: ' + str(heroe[1]) +'\n'
        i += 1
    return result
print(listar(superheores_y_Villanos.Ordenar(1)))

'''
# Modificamos la funcion para listar anteriormente, invertimos la lista con reverse y listamos
1. Thanos, Año: 2019
2. Black Panther, Año: 2014
3. Ultron, Año: 2007
4. Craneo Rojo, Año: 2001
5. Gatubela, Año: 2000
6. Loki, Año: 1999
7. Thor, Año: 1992
8. lagarto, Año: 1989
9. Venom, Año: 1985
10. Mujer Maravilla, Año: 1982
11. El Duende, Año: 1981
12. Hombre Araña, Año: 1980
13. D.Otopus, Año: 1980
14. Galactus, Año: 1970
15. Aqua Man, Año: 1970
16. Hulk, Año: 1967
17. Super Man, Año: 1966
18. Captain America, Año: 1966
19. Batman, Año: 1964
20. Jocker, Año: 1964
'''
# d. calcular el rango de años entre el primer personaje en aparecer y el último;
valores = superheores_y_Villanos.Ordenar(1)
print(f'Nombres: {valores[0][0]} Y {valores[len(valores)-1][0]}. Diferencia de años: {valores[len(valores)-1][1] - valores[0][1]}')
# Nombres: Jocker Y Thanos. Diferencia de años: 55

# e. determinar si los personajes Capitan America y Rocket Raccoon están en la lista y en qué año aparecieron
valores = superheores_y_Villanos.Ordenar(0)
print(superheores_y_Villanos.Buscar('Captain America'))
# Captain America esta en la lista. Con año de aparicion: 1966
print(superheores_y_Villanos.Buscar('Rocket Raccoon'))
# Ese Super Heroe o Villano no esta en la lista


'''
Se cuenta con una lista de Pokémons, de cada uno de estos se sabe su nombre, número y tipo 
(solo considerar uno el principal), con los cuales deberá resolver las siguientes tareas:

a. mostrar un listado de los Pokémons ordenados por números usando el método de ordenamiento por conteo;
b. realizar un listado ordenado por nombre utilizando el método de ordenamiento rápido;
c. mostrar toda la información de pokémon número 640;
d. listar todos los Pokémons que comienzan con la letra T;
e. determinar si existe el Pokémon Cobalion y mostrar toda su información;
f. realizar un listado de todos los Pokémon de tipo eléctrico y calcular cuántos son
'''

animalitosDePelea = [['Charmander', 2, 'Fuego'], ['Raticate', 20, 'Normal'], ['Jolteon', 135, 'Electrico'], ['Wartortle', 8, 'Agua'], ['Gengar', 94,'Fantasma/Veneno'], 
['Cobalion', 638, 'Acero/Lucha'], ['Onix', 95, 'Roca/Tierra'], ['Luxio', 245, 'Electrico'],['Pikachu',  25, 'Electrico'], ['Magneton', 82, 'Electrico/Acero']]

class Pokemons():
    def __init__(self, pokemons) -> None:
        self.lista = pokemons

    def count_sort(self):
        lista = self.lista

        numeros_poke = [poke[1] for poke in lista]

        def counting_sort(lista, maximo):
            lista_conteo = [0] * (maximo + 1)
            lista_ordenada = [None] * len(lista)

            for i in lista:
                lista_conteo[i] += 1

            total = 0
            for i in range(len(lista_conteo)):
                lista_conteo[i], total, = total,  total + lista_conteo[i]

            for indice in lista:
                lista_ordenada[lista_conteo[indice]] = indice
                lista_conteo[indice] += 1
            
            return lista_ordenada
        
        def busqueda_bi(lista, nummero_poke):
            for i in range(len(lista)):
                if lista[i][1] == nummero_poke:
                    return i
        
        numeros = counting_sort(numeros_poke, max(numeros_poke))

        for i in range(len(numeros)):
            ind_cambiar = busqueda_bi(lista, numeros[i])
            lista[i], lista[ind_cambiar] = lista[ind_cambiar], lista[i] 


        string = ''
        for i in range(len(lista)):
            string += str(i+1) + '. ' + lista[i][0] + ', ' + str(lista[i][1]) + ', ' + ', ' + lista[i][2] + '\n'
        return string
            

    def Quick_sort(self):
        lista = self.lista
        def ordenamiento_rapido(lista, menor, mayor):
            if menor < mayor:
                pivote = particionado(lista, menor, mayor)

                ordenamiento_rapido(lista, menor, pivote-1)
                ordenamiento_rapido(lista, pivote+1, mayor)

        def particionado(lista, menor, mayor):
            pivote = lista[menor][0]
            izquierda = menor+1
            derecha = mayor

            while True:
                
                while izquierda <= derecha and lista[izquierda][0] <= pivote:
                    izquierda += 1
                
                while derecha >= izquierda and lista[derecha][0] >= pivote:
                    derecha -= 1
                
                if izquierda > derecha:
                    break
                else:
                    lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]

            lista[menor], lista[derecha] = lista[derecha], lista[menor]

            return derecha
        ordenamiento_rapido(lista, 0, len(lista)-1)
        string = ''
        for i in range(len(lista)):
            string += str(i+1) + '. ' + lista[i][0] + ', ' + str(lista[i][1]) + ', ' + ', ' + lista[i][2] + '\n'
        return string

    
    def Buscar(self, tipo_valor, valor):
        if tipo_valor == 'nombre':
            ind = 0
        else:
            ind = 1
        pokemons = self.lista
        def busqueda_bi(lista, valor):
            mayor = len(lista)-1
            menor = 0
            while menor < mayor:
                medio = (mayor + menor) // 2

                if lista[medio][ind] == valor:
                    return lista[medio]
                else:
                    if lista[medio][ind] > valor:
                        mayor = medio-1
                    else:
                        menor = medio + 1
            return 'Ese Pokemon no se encuentra en la lista'

        return busqueda_bi(pokemons, valor)
    
    def listar_por_letra(self, letra):
        pokemons = self.lista
        string = ''
        for poke in pokemons:
            if poke[0][0].lower() == 'l':
                string += str(poke) + '\n'
        
        return string

    def listar_por_tipo(self, tipo):
        pokemons = self.lista
        string = ''
        cont = 0
        for poke in pokemons:
            if poke[2].lower() == tipo.lower():
                string += str(poke) + '\n'
                cont += 1

        string += str(cont)
        return string


# a. mostrar un listado de los Pokémons ordenados por números usando el método de ordenamiento por conteo;
pokeomns = Pokemons(animalitosDePelea)
print(pokeomns.count_sort())
'''
1. Charmander, 2, , Fuego
2. Wartortle, 8, , Agua
3. Raticate, 20, , Normal
4. Pikachu, 25, , Electrico
5. Magneton, 82, , Electrico/Acero
6. Gengar, 94, , Fantasma/Veneno
7. Onix, 95, , Roca/Tierra
8. Jolteon, 135, , Electrico
9. Luxio, 245, , Electrico
10. Cobalion, 638, , Acero/Lucha
'''
# b. realizar un listado ordenado por nombre utilizando el método de ordenamiento rápido;
print(pokeomns.Quick_sort())

'''
1. Charmander, 2, , Fuego
2. Cobalion, 638, , Acero/Lucha
3. Gengar, 94, , Fantasma/Veneno
4. Jolteon, 135, , Electrico
5. Luxio, 245, , Electrico
6. Magneton, 82, , Electrico/Acero
7. Onix, 95, , Roca/Tierra
8. Pikachu, 25, , Electrico
9. Raticate, 20, , Normal
10. Wartortle, 8, , Agua
'''
# c. mostrar toda la información de pokémon número 640;
print(pokeomns.Buscar('numero', 640))
'''
Ese Pokemon no se encuentra en la lista
'''

# d. listar todos los Pokémons que comienzan con la letra T;
print(pokeomns.listar_por_letra('l'))
'''
['Luxio', 245, 'Electrico']
'''

# e. determinar si existe el Pokémon Cobalion y mostrar toda su información;
print(pokeomns.Buscar('nombre', 'Cobalion'))
'''
['Cobalion', 638, 'Acero/Lucha']
'''
# f. realizar un listado de todos los Pokémon de tipo eléctrico y calcular cuántos son
print(pokeomns.listar_por_tipo('Electrico'))
'''
['Jolteon', 135, 'Electrico']
['Luxio', 245, 'Electrico']
['Pikachu', 25, 'Electrico']
3
'''

'''
La empresa Netflix nos pone a nuestra disposición los datos de todas las series cargadas en esta 
plataforma con los siguientes datos: nombre, cantidad de temporadas y cantidad de capítulos 
totales de la serie. Los cuales debemos procesar desarrollando las funciones necesarias para 
dar solución a las siguientes ítems:

a. listar las series ordenadas a cuerdo a los siguientes criterios: por nombre, por cantidad de 
temporadas, por cantidad de capítulos;
b. mostrar toda la información de la serie “Los 100“;
c. determinar cuál es la serie con mayor cantidad de temporadas y mayor cantidad de capítulos;
d. calcular cuantas series dispone la plataforma y el promedio de temporadas;
e. determinar el promedio de capítulos por temporada de la serie “Star Wars: Rebels”;
f. listar el TOP 5 de series con mayor cantidad de capítulos y el top 10 de las series con mayor 
cantidad de temporadas;
g. mostrar todas las series con tres o menos temporadas
'''

vamos_a_ver_Netflix = [['The Walkind Dead', 11, 177], ['Star Wars: Rebels', 4, 75], ['Game of Thrones', 8, 73], ['Vikings', 6, 89], ['Los 100', 2, 16],
['Gambito de Dama', 11, 100], ['Jojos', 4, 152], ['Hunter X Hunter', 1, 380], ['Lupin Negro', 2, 10], ['Naruto', 9, 220]]

class Netflix():
    def __init__(self, lista):
        self.lista = lista
        self.size = len(lista)
    
    def ordenar_segun_que(self, segun_que):
        catalogos = self.lista
        ind = segun_que
        def merge_sort(lista):
            if len(lista) < 2:
                return lista
            medio = len(lista) // 2

            parte_izquierda = [lista[i] for i in range(0, medio)]
            parte_derecha = [lista[i] for i in range(medio, len(lista))]

            parte_izquierda = merge_sort(parte_izquierda)
            parte_derecha = merge_sort(parte_derecha)

            if parte_izquierda[medio-1][ind] <= parte_derecha[0][ind]:
                return parte_izquierda + parte_derecha
            else:
                result = merge(parte_izquierda, parte_derecha)
                return result
            
    
        def merge(parte_izq, parte_der):
            mezcla = []
            while len(parte_izq) > 0 and len(parte_der) > 0:
                if parte_izq[0][ind] < parte_der[0][ind]:
                    mezcla.append(parte_izq.pop(0))
                else:
                    mezcla.append(parte_der.pop(0))
            
            if len(parte_izq) > 0:
                mezcla += parte_izq
            else:
                mezcla += parte_der
            

            return mezcla
        
        return merge_sort(catalogos)

    def mostrar_catalogo(self, valor):
        catalogos = self.ordenar_segun_que(0)
        def busqueda_binaria(lista, valor):
            menor = 0
            mayor = len(lista)-1

            while menor <= mayor:
                medio = (mayor + menor) // 2
                if lista[medio][0].lower() == valor.lower():
                    return lista[medio]
                else:
                    if lista[medio][0].lower() > valor.lower():
                        mayor = medio - 1
                    else:
                        menor = medio + 1
            return None

        serie = busqueda_binaria(catalogos, valor)
        return serie
    
    def ordenar_por_capitulos_y_temporadas(self):
        catalogo = self.lista
        def insertion_sort(lista):
            for i in range(2, len(lista)+1):
                k = i-1
                while k > 0 and ((lista[k][1], lista[k][2]) > (lista[k-1][1], lista[k-1][2])):
                    lista[k], lista[k-1] = lista[k-1], lista[k]
                    k -= 1
            return lista
        return insertion_sort(catalogo)
    def total(self, ind):
        catalogo = self.lista
        temporadas = 0
        for serie in catalogo:
            temporadas += serie[ind]
        return temporadas

    def serie_y_promedioTemporadas(self):
        totalSeries = self.size
        total_capitulos = self.total(2)
        totalTemporadas = self.total(1)
        string = ''
        try:
            promedio = total_capitulos // totalTemporadas
        except ZeroDivisionError:
            string = 'No hay Series en Netflix'
        else:
            string =  'El Total de series es: ' + str(totalSeries) + '\n' + 'El promedio de de capitulos / temporadas es: ' + str(promedio)
        return string


    def promedio_capitulos_temporada(self, serie):
        serie = self.mostrar_catalogo(serie)
        try:
            promedio = serie[2] // serie[1]
        except ZeroDivisionError:
            return 'Esa serie No se ecnuentra en Netflix'
        else:
            return 'El promedio de Temporadas es: ' + str(promedio)

    def top(self, total, capitulos_o_temporadas):
        lista_top = (self.listar(capitulos_o_temporadas, total)).split('\n')
        return list(reversed(lista_top[-(total+1)::]))

    def listar(self, segunQue = None, total = None):
        series = self.ordenar_segun_que(segunQue)
        if series != None:
            largo = len(series)
        else:
            largo = total

        string = ''
        for i in range(largo):
        
            string += str(i+1) + '. ' + series[i][0] + ', Temporadas: ' + str(series[i][1]) + ', Capitulos: ' + str(series[i][2]) + '\n'
        return string

    def mostrar_solo_por_temporadas(self, numero_de_temporadas):
        series = self.lista
        string = ''
        for i in range(len(series)):
            if series[i][1] <= numero_de_temporadas:
                string += series[i][0] + ', ' + str(series[i][1]) + ', ' + str(series[i][2]) + '\n'
        return string
    
catalogos = Netflix(vamos_a_ver_Netflix)
# a. listar las series ordenadas a cuerdo a los siguientes criterios: por nombre, por cantidad de 
# temporadas, por cantidad de capítulos;
# 0 por nombre, 1 por temporadas y 2 por capitulos
# por nombre:
print(catalogos.listar(0))
''''
1. Gambito de Dama, Temporadas: 11, Capitulos: 100
2. Game of Thrones, Temporadas: 8, Capitulos: 73
3. Hunter X Hunter, Temporadas: 1, Capitulos: 380
4. Jojos, Temporadas: 4, Capitulos: 152
5. Los 100, Temporadas: 2, Capitulos: 16
6. Lupin Negro, Temporadas: 2, Capitulos: 10
7. Naruto, Temporadas: 9, Capitulos: 220
8. Star Wars: Rebels, Temporadas: 4, Capitulos: 75
9. The Walkind Dead, Temporadas: 11, Capitulos: 177
10. Vikings, Temporadas: 6, Capitulos: 89
'''
# por Temporadas:
print(catalogos.listar(1))
'''
1. Hunter X Hunter, Temporadas: 1, Capitulos: 380
2. Lupin Negro, Temporadas: 2, Capitulos: 10
3. Los 100, Temporadas: 2, Capitulos: 16
4. Jojos, Temporadas: 4, Capitulos: 152
5. Star Wars: Rebels, Temporadas: 4, Capitulos: 75
6. Vikings, Temporadas: 6, Capitulos: 89
7. Game of Thrones, Temporadas: 8, Capitulos: 73
8. Naruto, Temporadas: 9, Capitulos: 220
9. Gambito de Dama, Temporadas: 11, Capitulos: 100
10. The Walkind Dead, Temporadas: 11, Capitulos: 177
'''

# por capitulos
print(catalogos.listar(2))

'''
1. Lupin Negro, Temporadas: 2, Capitulos: 10
2. Los 100, Temporadas: 2, Capitulos: 16
3. Game of Thrones, Temporadas: 8, Capitulos: 73
4. Star Wars: Rebels, Temporadas: 4, Capitulos: 75
5. Vikings, Temporadas: 6, Capitulos: 89
6. Gambito de Dama, Temporadas: 11, Capitulos: 100
7. Jojos, Temporadas: 4, Capitulos: 152
8. The Walkind Dead, Temporadas: 11, Capitulos: 177
9. Naruto, Temporadas: 9, Capitulos: 220
10. Hunter X Hunter, Temporadas: 1, Capitulos: 380
'''

# b. mostrar toda la información de la serie “Los 100“;
print(catalogos.mostrar_catalogo('Los 100'))
# ['Los 100', 2, 16]

# c. determinar cuál es la serie con mayor cantidad de temporadas y mayor cantidad de capítulos;
print(catalogos.ordenar_por_capitulos_y_temporadas())
'''
[['The Walkind Dead', 11, 177], ['Gambito de Dama', 11, 100], ['Naruto', 9, 220], ['Game of Thrones', 8, 73], ['Vikings', 6, 89], ['Jojos', 4, 152], 
['Star Wars: Rebels', 4, 75], ['Los 100', 2, 16], ['Lupin Negro', 2, 10], ['Hunter X Hunter', 1, 380]]

rta: ['The Walkind Dead', 11, 177]
'''

# d. calcular cuantas series dispone la plataforma y el promedio de temporadas;
print(catalogos.serie_y_promedioTemporadas())
'''
El Total de series es: 10
El promedio de de capitulos / temporadas es: 22
'''

# e. determinar el promedio de capítulos por temporada de la serie “Star Wars: Rebels”
print(catalogos.listar(0))
print(catalogos.promedio_capitulos_temporada('Star Wars: Rebels'))
'''
El promedio de Temporadas es: 18
'''
# f. listar el TOP 5 de series con mayor cantidad de capítulos y el top 10 de las series con mayor 
# cantidad de temporadas;
print(catalogos.top(5, 2))
'''
['10. Hunter X Hunter, Temporadas: 1, Capitulos: 380', '9. Naruto, Temporadas: 9, Capitulos: 220', '8. The Walkind Dead, Temporadas: 11, Capitulos: 177', '7. Jojos, Temporadas: 4, Capitulos: 152', '6. Gambito de Dama, Temporadas: 11, Capitulos: 100']
'''

print(catalogos.top(10, 1))
'''
['10. Gambito de Dama, Temporadas: 11, Capitulos: 100', '9. The Walkind Dead, Temporadas: 11, Capitulos: 177', '8. Naruto, Temporadas: 9, Capitulos: 220', '7. 
Game of Thrones, Temporadas: 8, Capitulos: 73', '6. Vikings, Temporadas: 6, Capitulos: 89', '5. Star Wars: Rebels, Temporadas: 4, Capitulos: 75', '4. Jojos, Temporadas: 4, Capitulos: 152', '3. Los 100, Temporadas: 2, Capitulos: 16', '2. Lupin Negro, Temporadas: 2, Capitulos: 10', '1. Hunter X Hunter, Temporadas: 1, Capitulos: 380']
'''
# g. mostrar todas las series con tres o menos temporadas
print(catalogos.mostrar_solo_por_temporadas(3))

'''
Los 100, 2, 16
Lupin Negro, 2, 10
Hunter X Hunter, 1, 380
'''