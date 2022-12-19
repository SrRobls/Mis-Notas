--CREAR TABLAS

-- Una vez ya creada esta base de datos (que se puede hacer mediante la interfaz o con codigo) comenzemos
-- a ver sobre tablas

create table persona(
	--Una vez creada la tabla, definamos sus columnas
	id integer not null,
	-- a las columnas debemos definirles  su tipo (int -> integer, float -> float, string -> varchar(tamaño))
	
	-- y notemos que al id le decimo que nunca sea nulo, es decir, que id siempre va a tener un valor en cada fila
	-- esto es asi ya que id sera nuestra llave primaria (primary key)
	
	nombre varchar(20),
	cedula integer
);

-- Ahora en la interfaz notemos que en esta base de datos en la pestaña shemas en tables se creo una pestaña
-- persona que contiene informacion de esta tabla

-- tambien podemos crear tablas mediante la interfaz

-- INSERTAR DATOS EN UNA TABLA

-- para esto usamos
insert into persona values ('5','Johan','1006455725');
--esta forma nos permite insertar datos a todas las columnas de la tabla persona, notar que el orden de los
-- datos tiene que ser igual al orden de las columnas. Pero si queremos insertar datos en solo algunas columnas hacemos

insert into persona (id, nombre) values ('100','Sebastian');
-- notar que antes de values decimos en que columnas queremos colocar los datos y notar que el orden en que definimos
-- los datos tiene que ser igual cuando definimos en que columnas queremos colocar datos

-- insert into persona (nombre, cedula) values ('Robles','1013311');
-- recordemos que el valor de id nunca va a ser nulo, entonces nsi no le damos un valor cuando creamos una fila
-- nos manda error

insert into persona (id, nombre, cedula) values ('500','Robles','1013311');

-- si queremos visualilzar la tabla y su valores usamos
select * from persona;
-- usamos * para hacer referencia que me muestre TODOS los datos de la columnas

-- si queremos solo los valores de la columna nombre
select nombre from persona;

-- o si queremos solo los valres de la columna id y cedula
select id, cedula from persona;

-- Notar que cuando una columna que puede ser nula (es decir, no se le definio en not nul) y no se le dio
-- un valor, esta queda representada como [null]

-- ACTUALIZAR DATOS/REGISTROS EN UNA TABLA

select * from persona;
-- para esto uamos update (tabla) set actualizacion/es
update persona set cedula = '24234525'
where cedula is null;
-- ya con esto estamos actualizando el campo de cedlula PERO hay un gran problema, y es que estamo actualizando
-- el valor de cedula en TODAS  las filas y eso no lo quremos (al menos en este caso), asi que debemos usar where

--Ahora notemos que la cedula de sebastian fue actualizada

-- si quremos cambiar dos valores entonces seria
insert into persona (id, cedula) values ('1','112314');
insert into persona (id, cedula) values ('2','3114563');
select * from persona

update persona set nombre = 'pedro', cedula = '121414343'
where nombre is null;

-- y listo, notemos que de hecho, se crearon dos pderos con la misma cedula debido a que anteriormente
-- esas filas tenian null en nombre

-- TIPOS DE DATOS BASICOS EN POSGRESQL

-- bolean = true/false
-- character(n) = cadena de caracteres con un tamaño fijo n
-- date = fecha
-- Float = flotante
-- int, integer = numero entero
-- decimal = numero decimal exacto
-- time = tiempo en horas, minutos y segundos
-- varchar(n) = cadena de caracteres con un tamaño variable n

-- CONSULTAS/QUERYS SELECT

-- ya vimos anteriomente como podemos usar esta consulta, pero vermemos otras forma de usarla
select * from persona

select (nombre, cedula) as informacion from persona
-- esta esta forma en la cual podemos agrupar en una sola columna () los datos que queremos y le podemos
-- adiccionar que la columna se llame informacion

-- si queremos el select de un solo valor pues entonces usamos where
select (id, nombre) as dato from persona
where id = '100'
-- notemos que solo nos aparecio los datos que queriamos en una columna con un apodo

-- WHERE, CONDICIONALES (=, !=, >, <, >=, <=) Y OPERADORES LOGICOS (and, or)

select * from persona;
-- Cambiemos los valores
update persona set nombre = 'manuel', cedula = '4232552'
where id = 2;
-- Actualizamos para que el segundo pedro sea manuel con una nueva cedula

select * from persona
where id >= 100;
-- notar que solo nos muestra los valores que cumplen

select * from persona
where id = 100 and nombre = 'Sebastian';
-- Solo nos muestra los datos que cumplen esta condicion

select * from persona
where id = 100 or id = 500
-- Solo nos muestra los datos que cumplen esta condicion

-- DELETE EN SQL
-- con delete podemos eliminar filas en una tabla, esto se usa con where para especificar que fila eliminar

delete from persona;
-- si solo lo dejamos asi estariamos eliminando TODAS las filas de a columna, lo cual en la mayoria de los
-- casos no lo hacemos. asi que usamos where para especificar que fila/s

delete from persona
where id = 1;

select * from persona;
-- notar que eliminamos la fila con el id = 1

-- Por supuesto tambien podemos usarlo con los diferentes condiciones y operadores de where para especificar
-- aun mejor

delete from persona
where cedula <= 10000000 or id = 100;

select * from persona;
-- notar que se eliminaron las filas que cumplian las condiciones del where

-- MODIFICAR UNA TABLA
-- Podemos modificar una tabla usando alter table + nombre de la tabla y luego los comando de modificacion

-- para agregar una columna, usamos add column (nombre de la columna y especificar el tipo de dato que sera la columna)
alter table persona
add column test varchar(100);
-- OJO que si colocamos que esa nueva columna en una tabla con datos almacenados si le ponemos not null (es decir, que es
-- obligatorio que tenga valores) nos marcarac erro ya que los filas ya almacenadas desde un principo no se le definio el valor
-- logicamente de la nueva columna.

select * from persona;

-- para cambiar el nombre de una columna ussamos rename
alter table persona
rename test to otro_test;

select * from persona;
-- notar que se cambio el nombre de la columna

-- para eliminar una columna usamo drop
alter table persona
drop column otro_test;

select * from persona;
-- notar que se elimino la columna

-- MODIFICAR UNA COLUMNA
-- usmos tambien alter para hacer esto

-- voy a agregar mas elementos y una columna a la tabla

insert into persona values ('1', 'Sebastian', '	21342343');
insert into persona values ('2', 'Robles', '	36356724');
select * from persona;

alter table persona
add column test varchar(10);
-- creamos una nueva columna la cual su valor en las filas ya definidas es null

--demosle valores a test
update persona set test = '3';
-- aca no quiero usar where ya que quiero aplicar esto a otas la filas de la tabla

-- si queremos hacer que una columna se No nula hacemos
alter table persona
alter column test set not null;

--Ahora si añadimos una nueva fila pero no le damos valor a test nos marcara error
insert into persona (id, nombre, cedula) values ('3', 'ElPepe', '123456789');
/*ERROR:  el valor nulo en la columna «test» de la relación «persona» viola la restricción de no nulo
DETAIL:  La fila que falla contiene (3, ElPepe, 123456789, null).
SQL state: 23502*/

insert into persona values ('3', 'ElPepe', '123456789', '4');
select * from persona;

-- si queremos cambiar el tipo de dato de la columna lo hacemos con type
alter table persona
alter column test type varchar(5);

--eliminemos la columna test

alter table persona
drop test;