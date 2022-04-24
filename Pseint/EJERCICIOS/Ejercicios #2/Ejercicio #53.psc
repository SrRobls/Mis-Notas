//Ejercicio #53: calcula el factorial de un numero dado.
Proceso Inicio
	Definir num, i, factorial Como Entero;
	Escribir "Dame un numero para calcular su factorial: ";
	Leer num;
	i <- 0;
	factorial <- num;
	
	Para  i <- 1 hasta num - 1 Con Paso 1 Hacer
		factorial <- (factorial * (num - 1));
		Escribir num," x " Sin Saltar; 
		num <- num - 1;
	FinPara
	Escribir 1, " = " Sin Saltar;
	Escribir factorial;
FinProceso
