//Ejercicio #61: escribe por pantalla las tabla de multiplicar del 1 al 10.
Proceso Inicio
	Definir num, tabla Como Entero;
	num <- 1;
	tabla <- 1;
	Mientras num < 11 Hacer
		Escribir "Tabla Del ",num,":";
		Mientras tabla < 11 Hacer
			Escribir num," x ",tabla," = ",num * tabla;
			tabla <- tabla + 1;
		FinMientras
		num <- num + 1;
		tabla <- 1;
		Escribir "";
	FinMientras
FinProceso
