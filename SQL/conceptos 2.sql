-- PRIMARY KEY

/*
una primary key o llave primaria es un dato UNICO (no se puede repetir) en cada una de las filas
de la tabla, por ejemplo la cedula o targeta de identidad que nosostros poseemos es una primary key,
pues es unica y diferente al de los demas. Esto nos servia para hacer consulta entre talas mas adelante.

si quisieramos crear una tabla con una primary key de una vez definida, hariamos casi lo mismo para
crear una tabla normal, si no que tambien definir la primary key.

create table persona2(
	id integer not null,
	nombre varchar(100),
	primary key (id)
);
*/ 

-- pero si queremos definirla una vez ya creada la tabla, entonces seria
alter table persona
add primary key (id);

/*
ahora si agregamos una nueva fila con un id que ya se existe, entonces nos maracaria error, pues
el id es nuestra primary key
*/

insert into persona values ('2', 'Marcela', '4536566');
/*
ERROR:  llave duplicada viola restricción de unicidad «persona_pkey»
DETAIL:  Ya existe la llave (id)=(2).
SQL state: 23505
*/

insert into persona values ('5', 'Marcela', '342524');
select * from persona;
-- Notar que ahora si se agrego la fila, pues le dimos un id unico

-- AUTO INCREMENTAL
/*
con esta funcion, podemos hacer que sql le de valores por si solo a los datos de una fila, lo cuales
va a ir en aumento 1 por 1 (1, 2, 3, 4 ...). esto usualmente es usado con la primary key para identificar
las filas.

para crear una tabla con una columna incremental, debemos colocar serial a la tabla que queremos que tenga esta
propiedad. hacemos lo siguiente
*/

create table personas(
	id_persona serial not null,
	-- Nota: ya con dale el valor de serial a una columna esta pos i solo ira aumentando a medida que se crean filas
	nombre varchar(30),
	nacionalidad varchar(30),
	primary key (id_persona)
);

insert into personas (nombre, nacionalidad) values ('Johan', 'Colombia');
insert into personas (nombre, nacionalidad) values ('Diego', 'Brasil');
insert into personas (nombre, nacionalidad) values ('Ibai', 'España');
-- Notar que ya no nos  preocupanos de darle un valor a id pues sql lo hace por nosostros
select * from personas;
-- vemos que id toma diferentes valores a medida que creamos filas.


-- DROP Y TRUNCATE
/*
Ya vimos que con delete podemos eliminar filas de la tabla, pero si hacemos esto a una tabla 
que tenga una columna incremental, y queremos reiniciar la tabla (aplicar delete sin where) al agregar
mas filas, esas filas en la columna incremental seguira con la suncecion que tenia.

si queremos entonces reiniciarla del todo (incremental y las filas y eso), hay dos formas; con drop
que basicamente elimina la tabla y pues a nosostros nos tocaria volverla a crear, pero esta tambien 
truncate que elimina todas la filas de la tabla (no se usa where, pues a truncate no se le aplica) pero hay 
que pasarle otros parametros: restart identity para reiniciar la sucecion incremental.
*/

-- eliminemos la una tabla
drop table persona;
-- notar que se elimino la tabla

-- ahora reseteemos las filas de la tabla con el incrementa y todo
truncate table personas restart identity;
select * from personas;
-- notar que se eliminaron todas las filas,ahora si le agregamos filas notar que el incremental se reincia 
-- nueva mente


-- VALORES POR DEFAULT
/*
sabemos que cuando NO le damos valores al dato de alguna columna este por defecto se rellenara por
por un null (a exepecion de que es columna fuese no nula o incremental). Nosotros podemos 
cambiar este valore por defecto por otro, pero eso se define cuando se crea una tabla.
*/

-- eliminemos y creemos otra vez la tabla pero con un valor que tenga default
drop table personas;
create table personas (
	id_persona serial not null,
	nombre varchar(20),
	nacion  varchar(20) default 'Desconocido',
	primary key (id_persona)
);

insert into personas (nombre, nacion) values ('Johan', 'Colombia');
insert into personas (nombre, nacion) values ('Diego', 'Brasil');
insert into personas (nombre, nacion) values ('Ibai', 'España');
select * from personas;
-- ahora si no le damos valores a alguna de esta dos columnas su valor por defecto sera desconocido
insert into personas (nombre) values ('Tatiana');
-- notar que el valor de nacion de la nueva fila creada dice 'Desconocido'


-- COLUMNAS CALCULADAS
/*
Podemos crear , actualizar o hacer select a columnas con calculo de otras columnas
por ejemplo con select seria
select + columna/s que queremos mostras (esto es opcional) + (columna calculada) as apodo de la columna calculada from tabla
*/

-- primero vamos a añadirle a la tabla una columna salario para trabajar con valores numericos que no sean el id
alter table personas
add column salario integer;

update personas set salario = '2000000';
select * from personas;

-- ahora para hacer select a una columna calculada, por ejemplo el salario mas 500000
select  nombre, salario, (salario + 500000) as salario_con_bono from personas;
-- notar que ahora podemos ver todos los salario + 500000, tambien podemos usarla con where claro esta

-- ahora para actualizar seria
update personas set salario = salario + 500000
where nombre = 'Johan';
select * from personas;
-- Notar que ahora Johan se le aumento su salario

update personas set salario = salario - 200000
where id_persona = 2;
select * from personas;
-- Notar ahora que el salario del id = 2 disminuyo 200000

-- y tambien notar que el orden de las filas fue alterado

-- ORDER BY
/*
Con order by podemos ordenar las filas en sql, se usa con select, 
podemos de hecho agregar mas de un parametro para ordena como tambine definir si lo ordena ascendentemente
el que viene por defecto o descendentemente
*/

select * from personas order by nombre;
-- notar que se ordeno por el nombre
select * from personas order by nombre desc;
-- ordenamos el nombre de manera descendentemente
select * from personas order by nombre, id_persona;
-- notar que se ordeno por nombre (como prioridad) y id_persona (por defecto de manera ascendente)
select * from personas order by salario asc, id_persona desc;
-- notar que se ordeno como prioria por el salario de menor a mayor y por id de la persona de menor a mayor

-- LIKE
-- con like podemos buscar valores que se parencen al algo, se usa con where

select * from personas
where nombre like '%e%';
-- notarq que solo nos sale diego ya que el tiene la letra e
/*
Entonces con los % podemos decirle a sql que nos busque aquellos nombres que tengan le letra e (aunque tambien)
puede ser una cadena) con %e% o que comience en Jo con jo% o que terminen a y cualquier otro caracter
con %a_
*/

select * from personas
where nombre like 'Jo%';
-- vemos que nos sale Johan

select * from personas
where nombre like '%a_';
-- notar que nos sale las filas donde el nombre cumpla que termina con la a y un caracter de mas