
from shutil import ExecError
import psycopg2

conexion = psycopg2.connect(
    user = 'postgres',
    password = 'PDUxst52',
    host = '127.0.0.1',
    port = '5432',
    database = 'Conectando Con Python'
)

try:
    with conexion:
        with conexion.cursor() as cursor:
            conusulta = "INSERT INTO personas (nombre, edad) VALUES (%s, %s)"
            valores = ('Catalina', '20')
            cursor.execute(conusulta, valores)
            # Como estamos alterando la tabla en la bases de datos, deberiamos usar .commit() para guardar los cambios en la base de datos
            # conexion.commit() pero como estamos en la estructira with no es necesario ya que ete lo hace por si solo
            registros_insertados = cursor.rowcount
            print(f"Total insertados: {registros_insertados}")
except Exception as e:
    print(f'Ocurrio: {e}')
finally: 
    conexion.close()

# Ahora si vamos a nuestra base de datos, notaremos que se insertaron nuevas filas.


conexion = psycopg2.connect(
    user = 'postgres',
    password = 'PDUxst52',
    host = '127.0.0.1',
    port = '5432',
    database = 'Conectando Con Python'
)

# Podemos insertar vario elementos a la vez
try:
    with conexion:
        with conexion.cursor() as cursor:
            conusulta = "INSERT INTO personas (nombre, edad) VALUES (%s, %s)"
            valores = (
                ('Natalia', '12'),
                ('Marcos', '32'),
                ('Laura', '88')
                )
            # usamos executemany con la consulta y la tuplade valores si la consulta esta formateada, ademas se insertaran todos los registros
            # segun la catidad de tuplas de valores
            cursor.executemany(conusulta, valores)
            registros_insertados = cursor.rowcount
            print(f'Se han registrado: {registros_insertados}')
except Exception as e:
    print(f'Ocurrio {e}')
# Notar que se hicieron los registros en la base de datos.