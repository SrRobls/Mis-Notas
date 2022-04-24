//Ejercicio #52: pide al usuario que introduzca 100 numeros enteros. des calcula y muestra su media
Proceso Inicio
	Definir num, i, suma, media Como Real;
	Escribir "Dame 100 numeros: ";
	num <- 0;
	i <- 1;
	suma <- 0;
	media <- 0;
	
	Mientras i <= 100 Hacer
		Escribir "Dame el valor del numero #",i;
		Leer num;
		i <- i + 1;
		suma <- suma + num;
	FinMientras
	Escribir "La suma de esos 100 numeros es: ",suma;
	media <- suma / 100;
	Escribir "La media es: ",media;
FinProceso
