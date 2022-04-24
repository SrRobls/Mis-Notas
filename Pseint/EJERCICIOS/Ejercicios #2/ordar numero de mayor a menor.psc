//ordenamiento de mayor a menor con arrays
Proceso inicio
	Definir arreglo, indice1, indice2, caja Como Entero;
	caja <- 0;
	indice1 <- 0;
	indice2 <- 0;
	Dimension arreglo[5];
	Para  indice2 <- 0 Hasta 4 Con Paso  1 Hacer
		Escribir "Dame el numero #",indice2 + 1;
		Leer arreglo[indice2];
	FinPara
	Para  indice1 <- 0 Hasta 3 Con Paso  1 Hacer //Nota como 5 numeros entonces el hasta va hasta 5 - 2
		Para indice2 <- 0 hasta 3 - indice1 Con Paso 1 Hacer
			Si arreglo[indice2] < arreglo[indice2 + 1] Entonces
				caja <- arreglo[indice2];
				arreglo[indice2 + 1] <- arreglo[indice2];
				arreglo[indice2] <- caja;
			FinSi
		FinPara
	FinPara
	Para indice2 <- 0 hasta 4 Con Paso 1 Hacer
		Escribir arreglo[indice2]," "Sin Saltar;
	FinPara
FinProceso
//NOTA: al parecer este codigo no Funciona con esta configuracion de Pseint
