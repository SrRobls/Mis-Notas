//Ejercicio #73: crea un matriz 4x3 con valores aportados por el ususario que represente el numero de personas que viven en los pisos de un edificio de viviendas
//despues indica cual es la planta con mayor numero de vecinos, indicando tambien el numero.
Proceso inicio
	Definir edificio, filas, columnas, vecinos, contador, planta Como Entero;
	filas <- 0;
	columnas <- 0;
	vecinos <- 0;
	contador <- 0;
	planta <- 0;
	Dimension edificio[4,3];
	//creacion de la matriz (edificio) con los valores de los vecinos en cada piso:
	Para filas <- 0 hasta 3 Con Paso 1 Hacer
		para columnas <- 0 hasta 2 con paso 1 Hacer
			Escribir "dame el valor del vecino de la seccion #",columnas + 1," del piso #",4 - filas;
			Leer edificio[filas,columnas];
		FinPara
	FinPara
	//mostramos como la matriz (edificio) al usuario:
	Escribir "Entonces el edificio queda asi: ";
	Para filas <- 0 hasta 3 Con Paso 1 Hacer
		para columnas <- 0 hasta 2 con paso 1 Hacer
			Escribir edificio[filas,columnas]," "Sin Saltar;
		FinPara
		Escribir " ";
	FinPara
	//contador de vecinos de cada piso:
	Para filas <- 0 hasta 3 Con Paso 1 Hacer
		para columnas <- 0 hasta 2 con paso 1 Hacer
			contador <- contador + edificio[filas,columnas];
		FinPara
		Si contador >= vecinos Entonces
			vecinos <- contador;
			planta <- 4 - filas;
		FinSi
		contador <- 0;
	FinPara
	Escribir "El piso/planta con mas vecinos es el: ",planta," con un total de ",vecinos," vecinos";
FinProceso
