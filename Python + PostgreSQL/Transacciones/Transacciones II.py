"""
Pero cuando usamos las transacciones con WITH, no es necesario los metodos commit o rollback, ya que dentro de la estructura lo hace 
automacticamnete.

Entendemos por tranasacciones aquellas consultas o Querys que altera unta tala o base de datos como; update, insert, etc.
Con los select no es necesario hacerla dentro de una transaccion, pero se puede hacer.
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
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO personas(nombre, edad) VALUES (%s, %s)"
            cursor.execute(sentencia, ("Manuel", "50"))
            print("Se hace un commit")
except Exception as e:
    print(f"Se hace rollback: {e}")
finally: conexion.close()