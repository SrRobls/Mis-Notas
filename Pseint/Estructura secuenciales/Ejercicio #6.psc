// Ejercicio #6: Calcular la siguiente sumatoria de los "N" elementos (1+4+9+....+n a la 2)
Proceso Inicio
	Definir elementos Como Entero;
	Definir i,suma Como Entero;
	Escribir 'Digite la cantidad de elementos a sumarse: ';
	Leer elementos;
	i <- 1;
	suma <- 0;
	Mientras i<=elementos Hacer
		suma <- suma+i^2;
		i <- i+1;
	FinMientras
	Escribir 'La suma es: ',suma;
FinProceso
