//Ejercicio #5: Elaborar un flijograma que muestre la suma y la serie de numeros pares comprendidios
//entre 20 y 10 (orden descendente) (estructura mientras)
Proceso Inicio
	Definir num, contenedor como enteros;
	
	num <- 20;
	contenedor <- 0;
	
	mientras num > 12 Hacer
		num <- num - 2;
		Escribir num;
		contenedor <- contenedor + num;
	FinMientras
	Escribir "La suma es: ",contenedor;
FinProceso
