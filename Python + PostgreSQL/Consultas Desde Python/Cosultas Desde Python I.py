# Primero tenemos que importar la libreria para conectar con PostgreSQL
from shutil import ExecError
import psycopg2

# Ahora guardamos en una variable la conexion con postgres, que seria

conexion = psycopg2.connect(
    # Ahora debemos llenar una informacion para conectarse. destacar que se recibe es un diccionario, asi que usar la sintaxis correcta de estos
    user = 'postgres',
    password = 'PDUxst52',
    # vendrian el host y el puesrto, y como desde un servido local seria por defecto los siguientes
    host = '127.0.0.1',
    port = '5432',
    # Ahora le decimo a que base de datos conectarse
    database = 'Conectando Con Python'    
)
# printeamos para corroborar de que nos conectamos
print(conexion)

# Ahora creemos un cursor para hacer sentencias/consultas desde python
cursor = conexion.cursor()
# Guardemos en una variable la sentencia (esto es opcional)
consulta = "SELECT * FROM personas;"
# La ejecutamos
cursor.execute(consulta)
# Y ahora recuperamos los registros, esto lo hacemos con el metodo fecthall en una variable
resultado = cursor.fetchall()
print(resultado)
# Notar que nos trajo la consulta que hicimos desde aca en postgres.

# Por utimo, cerramos tanto el cursos como la conexion
cursor.close()
conexion.close()

conexion = psycopg2.connect(user = 'postgres', password = 'PDUxst52', host = '127.0.0.1', port = '5432', database = 'Conectando Con Python')
# Podemos usar esto con with, pero debemos hacerlo dentro la estructura try
try:
    with conexion:
        with conexion.cursor() as cursor:
            # Podemos, mediante un formato hacer que el usuario interactue con la consulta
            consulta = "SELECT * FROM personas WHERE id = %s;"
            id_persona = input('Dime el id de la persona a mostrar: ')
            # entonce al ejecutar, debemos pasar el string de la consulta y un tupla con los valores de los %
            cursor.execute(consulta, tuple(id_persona))
            # Por ultimo, usamos fectchone, que a diferencia del fectchall, retorna un valor (la tupla) y no una lista 
            resultado = cursor.fetchone()
            print(resultado)
except Exception as e:
    print(f'Ocurrio: {e}')
# finalmente, debemos cerrar conexion, pues este esta afura de la clausula try
finally:
    conexion.close()