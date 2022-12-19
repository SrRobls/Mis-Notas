"""
Las transacciones son los cambis (alteraciones) que hacemos desde python a una base de datos. asi, existe el concepto de commit, y rollback.
El primero verifica si todo esta bien (los valores, la consulta/sentencia desde python, ect) y si es asi, efectua y cambia la base de datos,
el segundo, en caso de que haya un error, entonces no ejecuta (y da marcha atras a la sentencia efectuadas en el instante) y por tanto, no 
cambia la base de datos.
"""
import psycopg2 as bd

conexion = bd.connect(
    user = 'postgres',
    password = 'PDUxst52',
    host = '127.0.0.1',
    port = '5432',
    database = 'Conectando Con Python'
)

try:
    # Con esta valor definid si el commit se hace automatico o no, la buena pratica es dejarllo como False (de hecho, ya viene asi por defecto)
    # ya que tenemos mas contro y pdremos evistar error en la base de datos. 
    conexion.autocommit = False # Aca inician las transaccines

    cursor = conexion.cursor()
    sentencia = "INSERT INTO personas(nombre, edad) VALUES (%s, %s)"
    valores = ('Ernesto', '78')
    cursor.execute(sentencia, valores)

    sentencia = "UPDATE personas SET edad = %s WHERE id = %s"
    valores = (
        ("20", "1"),
        ("35", "5"),
        ("21", "8")
    )
    cursor.executemany(sentencia, valores)

    # y como el autocommit esta desactivado, entonces debemos ordernarle que haga commit
    conexion.commit() # Aca terminan las transacciones 
    print("Se efectuo la consulta.")
except Exception as error:
    # En caso de que haya un error, ordenarle un rollback
    conexion.rollback()
    print(f"Se hace un rollback: {error}")


conexion.close()