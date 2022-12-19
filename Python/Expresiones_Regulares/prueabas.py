import re
prueba_numeros = """Habia una 23 que leia 42 veces mas que el promedio que era 23 y dijo, amigo 1 tengo un iq 200 mayor que  el promedio 100"""
print(re.findall(r'\d+', prueba_numeros))