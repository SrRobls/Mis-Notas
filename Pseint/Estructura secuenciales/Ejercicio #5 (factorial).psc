// Ejercicio #4. Calcular el factorial de un numero mayor o igual a 0.
Proceso Inicio
	Definir num Como Entero;
	Definir i,factorial Como Entero;
	Repetir
		Escribir 'Dame un numero mayor o igual a cero';
		Leer num;
	Hasta Que num>=0
	i <- 1;
	factorial <- 1;
	Mientras i<=num Hacer
		factorial <- factorial*i;
		i <- i+1;
	FinMientras
	Escribir 'El factorial es: ',factorial;
FinProceso
