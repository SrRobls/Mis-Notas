select * from personas;
select * from empresas;

-- CREAR FUNCIONES
/*
Para crear funciones en postreSLQ es caso ta identico con en otro lenguaje de programacio, el cual seria asi
*/

create or replace function suma(num1 int, num2 int) returns integer
as
$$
select num1 + num2
$$
language SQL;

/*
primero creamo o remplazamos una funcion donde le ponemos el nombre y le pasamos los parametros con sus respectivos
tipos, tambien le especificamos que se va a retornar un valor de tipo integer. Ahora dentro de las $$ definimos
el porceso que se hace usando los parametros y al funalizar especificamos el lenguage el cual es el SQL.
*/

select suma(200, 300);
-- Notar que nos muestra 500


create or replace function BuscarSalarioPorNombreYPais(varchar, varchar) returns integer
as
$$
select salario from personas where nombre = $1 and nacion = $2
$$
language SQL;

/*
Notar que podemms pasar paramentros sin un nombre, solo basta con el tipo. y cuando queremos acceder a ellas
lo hacemos con os $n segun el orden de los parametros.
*/

select BuscarSalarioPorNombreYPais('Johan', 'Colombia');
-- Nos muestra el salario correspondiente al nombre johan y a la nacion colombia de la tabla personas


-- añado que si queremos que la funcion no retorne nada (pues puede haber casos) o no se usen paraemtros
-- pues se define la funcion sin parametros y en returns ponemos void indicando que la funcion no retornara nada


-- TRIGGER
/*
con los metodos trigger pordemos hacer "acciones" antes durante y despues de hacer una accion (update, delete, select)
a una tabla.

en este ejemplo haremos un trigger ara que antes de hacer un update a la tabla personas, en otra tabla creada llamada
resguardos_trg guardaremos los datos antes que se actualizen 
*/

create table resguardos_trg (
	id_persona int,
	nombre varchar(20),
	nacion varchar(20),
	salario int,
	id_empresa_donde_trabajan int
);

-- para describir que acciona hace el trigger debemos primero escribirla en una funcion
create function resguardar() returns trigger
as
$$
-- como especificamos que el lenguaje es el de postgreSQL entonces por eso van los begin y end
BEGIN
insert into resguardos_trg values (old.id_persona, old.nombre, old.nacion, old.salario, old.id_empresa_donde_trabajan);
-- usamos el old.olumna para indicar que se añadan los valores que estaban antes de realizar una accion dada a la tabla
return new;
-- debemos colocar return new para que se haga la accion trigger
END

$$
language plpgsql;

--Ahora tenemos que definir cuando se hace la accion trigger o cuando se aplica la funcion y sobre que tabla se activa
-- el metodo trigguer cuabdo se hace una accion dada

create trigger trg_guardar before update on personas 
for each row execute procedure resguardar();

/* 
lo que estamos diceiendo es que crear un metodo trigger con el nombre trg_guardar que se active antes de actualizar
datos en la tabla personas, por tanto, para cada una de las filas que sera actualizadas aplicar la funcion
resguardar()
*/


select * from resguardos_trg;
-- Notar que no hay nada

select * from personas;
update personas set nombre = 'Camilo' where nombre = 'Johan' and salario = 1000000;
select * from personas;

select * from resguardos_trg;
-- Notar que sale los datos de la fila que se actualizo antes de actualizarse

update personas set id_empresa_donde_trabajan = '5' where salario < 3000000;

select * from resguardos_trg;
-- Notar que se almacenaron los valores a actualizarse en la tabla


/*
Hagamos otro ejemplo, crearremos una tabla donde guarde cada una de las insersiones que le hacemos a la tabla persona
en la cual los datos a guardar sea el nombre del registro que insertamos en personas, el usuario, la fecha y a que hora
*/

create table insersiones_en_personas (
	nombre_de_registro varchar(200),
	usuario_que_lo_inserto varchar(250),
	fecha varchar(200),
	hora varchar(200)
);

select * from insersiones_en_personas;


create function guardar_insercion() returns trigger
as
$$
-- para declarar variables usamos declare, el cual debemos colocar los nombres de las variables el tipo de variable
-- y con un := le damos el valor
declare 
usuario varchar(250) := User; -- User hace relacion al usuario que esta accediendo a la tabla
fecha date := current_date; -- Con los current_date/time podemos obtener la hora exacta de una insersion o accion
hora time := current_time;

-- Ahora pasamos al proceso
begin
insert into insersiones_en_personas values(new.nombre, usuario, fecha, hora);

return new;
end
$$
language plpgsql

create trigger accion_insertar after insert on personas for each row execute procedure guardar_insercion();

select * from insersiones_en_personas;
select * from personas;

insert into personas (nombre, nacion, salario, id_empresa_donde_trabajan) values('Marcela', 'Cuba', '2000000', 2); 
select * from insersiones_en_personas;
-- Notar que se agrego informacion sobre el ultimo/s registros insertado en la tabla personas

-- Vista
/*
Podemos mostrar informacion que solo nosostros queremos mostrar de una tabla creando una view
*/
select * from personas;

create View mostrar_nombre_salario 
as select nombre, nacion from personas;
-- tambien se puede con otras funciones de select como group by, where, limit, etc.
select * from mostrar_nombre_salario;
-- Notar que solo nos muestra el nombre y la nacion de los datos.


-- CONSULATAS DE DOS O MAS TABLAS CON JOIN 
/*
Con join podemos hacer consultas de dos o mas tablas, es como si pudieramos conatenar informacion de dos tablas,
es importante que los tipo de registros de vamos a consultar de las dos tablas sean la mismas, es decir que si yo quero
consultar valores de ds columnas, nombre con los valores de esas mismos columnas pero de otra tabla entonces los tipo
de datos de cada una de las columnas de cada tabla debe ser la misma.
*/

select * from personas;
select * from empresas;

select id_persona, nombre from personas union all select id_empresa, nombre from empresas;
-- notar que mostras la informacion de las tablas ids y de nombres de cada una de las tablas.
-- con union hacemos esta concatenacion y con all estamos diciendo que nos muetre todos sin importar que haya un caso/s
-- que se repitan. tambine, podemos usar los metodos where, goup by, order, etc.

select id_persona, nombre from personas where id_persona > '5' 
union all
select id_empresa, nombre from empresas where id_empresa > '3';
-- Notar que nos muestra informacion de cada caso de cada tabla.