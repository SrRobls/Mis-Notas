-- INNER JOIN 

/*
Con inner join podemos concatenar informacion de un registro que tenga relacion en las dos tablas, y por tanto,
mostramos la inoformacion de las dos tablas. ejemplo: si queremos mostras informas de los registros que se relacionan
en llave foranea de la tabla personas con la llave primaria de la tabla empresasa
*/

select * from personas;
select * from empresas;

select * from personas inner join empresas on personas.id_empresa_donde_trabajan = empresas.id_empresa;
/*
traduciendolo seria como; muestrame todas las columnas de la tabla personas uniendolas con la tabla empresas donde
los valores de id_empresa... sea igual a id_persona
*/

-- LEFT Y RIGHT JOIN 
/*
basicamente nos muestra la tabla izquierda (todos lo valores) y nos muestra en la derecha los que cumplen con la
relacion
*/

select * from personas
Left Join empresas
on personas.id_empresa_donde_trabajan = '5' and empresas.id_empresa = '5';

/*
Notar que mostramos la informacion de todas las columnas de la tabla izquierda (personas) pero solamente la informacio
que cumple el on de la tabla derecha (empresas), vemos que el resto de valores estan en null

on es como si fuese el where
*/

-- Ahora con right join hacemos lo mismo pero alrevez

select * from personas right join empresas on empresas.id_empresa = 1 and personas.id_empresa_donde_trabajan = '1';

/*
Notar que en la tabla de izquierda me muestra solo el registro que cumple la cndiciones y los que no, me los muestra como null
y me muestra todos los valores de la tabla de la derecha empresas
*/

-- FULL JOIN

/*
Ahora este es una funcion de left y right, muestra informacion de la tabla izquierda y derecha y los relaciona
segun las condiciones
*/

select * from personas;
select * from empresas;

select * from personas 
full outer join empresas 
on personas.id_empresa_donde_trabajan = empresas.id_empresa;

/*
Aqui no se ve tan claro, pues cada persona tiene una valor de llave forane representando la empresa donde trabjan.
si hubiese registro que no se relaciones, los registros corresponidentes serian null
*/

-- CROS JOIN
/*
Por ultimo esta cross join, que te muestra todas las combinaciones posibles al relacionar dos tablas, por tanto
no usamos el on
*/

select * from personas cross join empresas;
-- Notar que hay 45 registros, pues estams hablando de todas las combinaciones posibles