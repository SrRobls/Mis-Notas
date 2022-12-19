-- COUNT
/*
Con count podemos contar la cantidad de elemetos que nosostros le psasamos como parametro
*/

-- para que me muestre el total de todas las filas/registros
select count(*) as total_filas from personas;
-- vemos que nos dice 4, y efectivamente esos son

-- tambien podemos usar count con where o las condicionales y tal
select count(nombre) from personas
where nombre like '%e%' or nombre like '%o%';
-- vems que nos sale 2, e efectivamnete asi es.

select count(salario) from personas
where salario + 1000000 = 3000000;
-- 2

-- SUM
/*
Sum es una funcion que nos permite hacer la suma de una columna o columnas, basicamnete nos permite hacer
sumas entre registros
*/

select sum(salario) from personas;
-- nos da 8300000 y notemos que es cierto.
-- claro esta que podemos aplicar condicionales y eso

select sum(salario) from personas
where nombre like '%o%';
-- 4300000, pues hay dos nombres que tiene la letra o

-- MIN, MAX Y GROUP BY
/*
estas fucnines nos permiten buscar el valor mayor, el menor de una columna y tambien podemos agruparlas
por un paramtero
*/

select * from personas;
insert into personas (nombre, nacion, salario) values ('Diego','Alemania','5000000');
insert into personas (nombre, nacion, salario) values ('Johan','Francia','1000000');

select min(salario) as minimo_salario from personas;
-- vemos que efectivament es 1000000

select min(salario) as maximo_salario from personas;
-- vemos que efectivament es 10000000

select nombre, max(salario) from personas
group by nombre;
-- vemos que nos muestra una tabla con los salario mas altos por cada nombre, notar que en Johan y Diego
-- se muestra el salario mas alto entre los dos Johan y Diego que habian

-- traduciendo la funcio, decimos: 'muestreme los nombres con los salarios mas altos agrupados por el nombre'



-- AVG
/*
Con esta funcion podemos obtener el promedio de una funcion
*/

select avg(salario) as promedio_salario from personas;
-- 238333.3, ese es el promedio. claramente tambien lo podemos usar con gruop by

select nombre, avg(salario) from personas
group by nombre;
-- vemos que nos sale una tabla con los promedios de la salarios agrupados por los nombres, notar que vemos
-- los promedio de los Johans y los Diegos, de los otros es el mismo salario pues no tiene nombres
-- que se repitan

-- Notar tambien, que cuando queremos hacer un select con columna/s normales y funcion/es si o si, es 
-- necesaria el group by, de lo contrario nos manda error


-- HAVING
/*
having es una fucnion que nos sive como una where PERO con las columnas con la que trabaja group by
*/


select nombre, salario from personas
where nombre = 'Diego'
group by nombre, salario
having salario > 4000000;
-- notar que having trabaja solamente con las columnas con la que trabaj goup by. esta funcion tiene
-- unas reglas muy estrictas para poderse realizar

select nombre, salario from personas where salario > '1000000' having salario >= 1500000;
-- notar que nos marca error pues havi esta tomando columns del where

select nombre, salario from personas
where nombre = 'Johan'
group by nombre, salario
having salario > 2000000;

-- Notar que nos muestra el valor que su nombre sea Johan y el salario sea mayor a 2000000


-- DISTINCT
--con esta funcion podemos seleccionar los valores sin repetirse

select distinct nombre from personas;
--  nos muestra el nombre de la columna nombres isn repetir ninguna, basicamente como si fuese un set de python

select count(distinct nombre) from personas;
-- nos da 4 el total de todos los nombres diferentes 

select avg(distinct salario) from personas;
-- nos da el promedio de los salarios sin toma en cuenta aqellos que se repiten



-- BETWEEN
-- esta funcion nos sirve para parametrizar valores
select nombre, salario from personas
where salario between 2500000 and 5000000;
-- Nos muestra aquellos valores donde el salario este en este rango

-- si queremos todos los salarios qeu NO este en ese rango entonces seria
select nombre, salario from personas where salario not between 2000000 and 5000000;
-- Nos muestra aquellos valores que no esten en esos parametros.


-- RESTRICCIONES -> CONSTRAINTS Y UNIQUE
/*
podemos darle restrcicciones a nuestra tabla en el momento en que se le insertara valores o algo por el
estilo, tambien existe unique que basicamente hara que cada uno de los valores ser unico (algo asi
como si fuese una primary key). entences veamos como creamos una restricciones donde los valores no se pueden
repertir
*/

update personas set salario = 50000000 where nombre = 'Ibai';
-- hacemos esto para que los salario sean diferentes y no nos marque error al agregar la restriccion
-- unique

alter table personas
add constraint salarios_unicos
unique (salario);
-- listo, asi cremos una restriccion que cuando insertemos valores, el valor salrio no debe repetirse con los otros
-- si no, marcca error

insert into personas (nombre, nacion, salario) values ('Carla', 'Colombiana', '2000000');
/*
ERROR:  llave duplicada viola restricción de unicidad «salarios_unicos»
DETAIL:  Ya existe la llave (salario)=(2000000).
SQL state: 23505

vemos que rompio la restriccion pues el salario de 2000000 ya esta en la tabla
*/

insert into personas (nombre, nacion, salario) values ('Carla', 'Colombiana', '3000000');
-- Ahora vemos que se cumplio pues el salario de 3000000 no estaba en la tabla

select * from personas;

/*
Ahora para eliminar las restricciones debemos alterar la tabla y aplicar drop al a la restriccion especificandola con
el nombre
*/

alter table personas drop constraint salarios_unicos;
insert into personas (nombre, nacion, salario) values ('Julian', 'Peru', '2000000');
-- vemos que se agrego con un salario ya repetido, pero no paso nada ya que quitamos la restriccion


-- Funciones que me encontre en Hackerrank

-- sum() -> suma todos los valores
-- concat(valor, valr, ...) -> concatena una cadena de acaracteres, es como un print
-- los select case -> es como los condicionales if/else
-- substring(string from indice for indice) -> para acceder a un caracter o a alguna subcadea de una cadena de caracteres
-- substr(string, indice_inicial, indice_final) -> lo mismo que el anterio pero mas simplificado
-- limit n -> para mostra una cantidad n de registros de la tabla o de la consulta que queremos
-- regexp -> para trabajar con expresiones regulares
-- round(valor, n de decimales) -> para redondear un numero
-- ceiling, floor -> para redondear numeros, el primero para el siguiente valor, y floor para el anterior
-- replace -> literalmente funciona como el replace de python, inclusive este sirve con los numeros (integer)
-- power(valu, exp) -> para hacer exponensaciones
-- sign(x) -> si el parametro es un 0 nos retorna un 0, si es un numero positivo nos retorna un 1 y si es un numero negativo nos retorna un -1
-- mod(numerador, denomidaro) -> nos devuelve el medolo o resto de la division
-- Pi() -> literalmente el numero pi, por tanto no recibe parametros
-- ramdom -> un numero alearotio entre 0 y 1
-- trunc(x) o trunc(x, n decimales) -> devuelve la parte entera de un numero, tambien puedo definirle la cantida de decimales que yo quiera
-- char_length(string) -> es como el len de python, nos muestra la longitud de un string
-- Upper(string) Y Lower(string) -> para convertir los string en minusculas o mayusculas
-- Position(string in string) -> nos devuele la posicion de un string en otro string, nos devuelve 0 si no se encuentra 
-- trim -> es el strip de pythn, quita por defect caracteres de espacion en una cadena de caracteres, tambien se puede definir que tipo de 
-- caracteres quitar y si los hacemos solo en la izquierda, derecha o en general (ambos lados)


-- MANEJO DE FECHA Y HORA
/*
Podemos manajerea y trabajar con fechas y horas
*/

-- con current_date nos muestra la fecha actual
select current_date;
-- 2022-06-24

-- con current_time nos muestra la hora actual
select current_time;
-- 10:30:55.463179-05:00

-- con current_timestamp nos muestra la fecha y hora actual
select current_timestamp;
-- 2022-06-24 10:31:53.5892-05

-- con la funcion extract(dato from current_timestamp) podemos extraer datos de la decha y hora timestamp
select extract(year from current_timestamp);
-- 2022
select extract(hour from current_timestamp);
-- 10
select extract(day from current_timestamp);
-- 24
select extract(month from current_timestamp);
-- 6