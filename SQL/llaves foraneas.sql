-- LLAVES FORANEAS
/*
las llaves foraneas en una tabla son aquellos valores (en una columna) que hacen referencia a datos de otra tabla
asi, si yo quiero relacionar dos tablas, entonces uso una llave foranea.

por ejemplo, si yo quiero relacionar los datos de las personas con datos de otra tabla, por ejemplo empresas, para saber
en que empresas trabajan, usaria llaves foraneas para (en este caso) relacionar el id (primary key) de cada empresa
con cada una de las personas segun donde trabajen.

esto nos ayuda a asegurarnos de que el datos que estoy usando como llave foranea si o si exista en la tabla que quiero
relacionar. asi evitamos que relacionemos datos con otros datos que posiblemente no existan en la otra tabla
*/

select * from personas;

-- creemos una tabla empresas
create table empresas (
	id_empresa serial not null,
	nombre varchar(50),
	primary key (id_empresa)
);
select * from empresas;
insert into empresas (nombre) values ('Ecopetrol')
insert into empresas (nombre) values ('Electro Muebles')
insert into empresas (nombre) values ('Comfiar')
insert into empresas (nombre) values ('Mercado Libre')
insert into empresas (nombre) values ('Globant');

-- creemos una columna en persona donde iran las llaves foraneas
alter table personas add column id_empresa_donde_trabajan integer;


-- Ahora creemos o hagamos que en la columna que cremos vayan las llaves foraneas que representa el id de las
-- empresas donde trabaja cada persona
alter table personas --Alteramos la tabla donde iran las llaves foraneas
add constraint llave_foranea -- añadimos una restriccion para la configuracion dpara el momento de agregar llaves foraneas
foreign key (id_empresa_donde_trabajan) -- le decimos que columna es donde iran las llaves foraneas
references  empresas (id_empresa) -- y por ultimo, le decimos de que tabal y columna pueden ser llamadas las ll.foraneas


/*
Ahora en el momento en que le demos valor a la column de las llaaves foraneas de personas, estas si o si deben estar
o existir el la columna id_empresa de la tabla empresas, de lo contrario n nos deja y nos manda error
*/

update personas set id_empresa_donde_trabajan = 7 where nombre = 'Johan';
/*
Nos marca error, pues en empresas no existe una empresa con id = 7
ERROR:  inserción o actualización en la tabla «personas» viola la llave foránea «llave_foranea»
DETAIL:  La llave (id_empresa_donde_trabajan)=(7) no está presente en la tabla «empresas».
SQL state: 23503
*/

update personas set id_empresa_donde_trabajan = 5 where nombre = 'Johan';
-- Vemos que con un id que si exite en empresas si nos deja

select * from personas;
update personas set id_empresa_donde_trabajan = 2 where salario = 2000000;
update personas set id_empresa_donde_trabajan = 1 where salario = 1800000;
update personas set id_empresa_donde_trabajan = 3 where salario = 3000000;
update personas set id_empresa_donde_trabajan = 4 where salario = 50000000;
update personas set id_empresa_donde_trabajan = 1 where salario = 5000000;

-- asi es como se crea una llave forane, una herramienta muy util si queremos relacionar datos entre tablas