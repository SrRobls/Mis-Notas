//Ejercicio #71: Crea una matriz 3x3 con numeros aleatorios y despues transcribe su transpuesta. debe aparecer en formato de filas y columnas
Proceso Inicio
	Definir matriz, filas, columnas Como Entero;
	filas <- 0;
	columnas <- 0;
	Dimension matriz[3,3];
	Escribir "La matriz 3x3 a sacar la transpuesta es: ";
	//creacion de la matriz 3x3. la matriz tendra numeros aleatorios y no introducidos por le usuario:
	Para filas <- 0 hasta 2 Con Paso 1 Hacer
		Para columnas <- 0 hasta 2 Con Paso 1 Hacer
			matriz[filas,columnas] <- azar(10);
			Escribir matriz[filas,columnas]," " Sin Saltar;
		FinPara
		Escribir " ";
	FinPara
	Escribir "La transpuesta de esta matriz 3x3 es: ";
	//proceso para la transpuesta de la matriz anterior:
	Para columnas <- 0 hasta 2 Con Paso 1 Hacer
		Para  filas <- 0 hasta 2 Con Paso 1 Hacer
			Escribir matriz[filas,columnas]," "Sin Saltar;
		FinPara
		Escribir " ";
	FinPara
FinProceso
