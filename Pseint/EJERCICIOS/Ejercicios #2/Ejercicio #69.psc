//Ejercicio #69: Guarda 5 numeros en un arreglo y posteriormente muestralos ordenados de mayor a menor
Proceso Inicio
	Definir arreglo, indice1, indice2, caja Como Entero;
	caja <- 0;
	indice1 <- 0;
	indice2 <- 1;
	Dimension arreglo[5];
	Para  indice1 <- 0 Hasta 5 - 1 Con Paso  1 Hacer
		Escribir "Dame el numero #",indice1 + 1;
		Leer arreglo[indice1];
	FinPara
	indice1 <- 0;
	Repetir
		Si indice1 > 3 Y indice2 > 4 Entonces
			indice1 <- 0;
			indice2 <- 1;
		SiNo
			Si arreglo[indice1] <= arreglo[indice2] Entonces
				caja <- arreglo[indice1];
				arreglo[indice1] <- arreglo[indice2];
				arreglo[indice2] <- caja;
			FinSi
			indice1 <- indice1 + 1;
			indice2 <- indice2 + 1;
		FinSi
	Hasta Que arreglo[0] >= arreglo[1] Y arreglo[1] >= arreglo[2] Y arreglo[2] >= arreglo[3] Y arreglo[3] >= arreglo[4]
	Escribir "El orden de los numeros es: ",arreglo[0],",",arreglo[1],",",arreglo[2],",",arreglo[3],",",arreglo[4],".";
FinProceso
