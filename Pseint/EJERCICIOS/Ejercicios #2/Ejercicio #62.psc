//Ejercicio #62: calcula y muestra por pantalla los factoriales de los numeros del 10 al 1
Proceso Inicio
	Definir num1, num2, factorial Como Real;
	num1 <- 0;
	num2 <- 0;
	factorial <- 0;
	Para num1 <- 10 Hasta 1 Con Paso -1 Hacer
		factorial <- num1;
		Para num2 <- num1 Hasta 2 Con Paso -1 Hacer //aca num2 debe llegar hasta para que num2 - 1, siendo num2 = 2 de como resultado 1 (2-1 = 1). en el caso de que fuese num2 = 1. daria 0 (1-1 = 0) y por ende el factorial se "daña"
			Escribir num2," x " Sin Saltar;
			factorial <- factorial * (num2 - 1);
		FinPara
		Escribir "1 = ",factorial;
	FinPara
FinProceso
