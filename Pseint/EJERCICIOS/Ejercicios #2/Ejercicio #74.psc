//Ejercicio #74: crea una matriz 3x3 con valores aleatorios y despues indique el numero menor de cada columna
Proceso Inicio
	Definir matriz, filas, columnas, menor Como Entero;
	filas <- 0;
	columnas <- 0;
	menor <- 9999;
	Dimension matriz[3,3];
	Escribir "La matriz 3x3 es: ";
	//creacion de la matriz 3x3. la matriz tendra numeros aleatorios y no introducidos por le usuario:
	Para filas <- 0 hasta 2 Con Paso 1 Hacer
		Para columnas <- 0 hasta 2 Con Paso 1 Hacer
			matriz[filas,columnas] <- azar(10);
			Escribir matriz[filas,columnas]," " Sin Saltar;
		FinPara
		Escribir " ";
	FinPara
	//buscador del numero menor de cada  columnas:
	Para filas <- 0 hasta 2 Con Paso 1 Hacer
		Para columnas <- 0 hasta 2 Con Paso 1 Hacer
			Si matriz[filas,columnas] <= menor Entonces
				menor <- matriz[filas,columnas];
			FinSi
		FinPara
		Escribir "El numero menor de la columna #",filas + 1," es: ",menor;
		menor <- 999;
	FinPara
FinProceso
