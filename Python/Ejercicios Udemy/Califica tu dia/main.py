#Etapas de vida segun edad:
edad = int(input('Por favor dime tu edad: '))
frase = None #Usamos a None para referirnos a que una variable no tiene "nada"

if edad >= 0 and edad <= 10:
    frase = 'La infacia es increible!.'
elif edad > 10 and edad <= 20:
    frase = 'Muchos cambios y mucho estudio!'
elif edad > 20 and edad <= 30:
    frase = 'Amor y comienza el trabajo!'
else:
    frase = 'Eres una gran persona!'
print(f'Tenes {edad} años. asi que {frase}')
