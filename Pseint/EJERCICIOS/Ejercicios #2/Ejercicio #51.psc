//Ejercicio #51: pide al usuario que introduzca 100 numeros enteros. despues indica cuantos de eso numeros
//son pares, cuantos impares, cuantos negativos y cuantos positivos.
Proceso Inicio
	Definir num, i, pares, impares, negativos, positivos Como Entero;
	Escribir "dame 100 numeros: ";
	num <- 0;
	i <- 1;
	pares <- 0;
	impares <- 0;
	negativos <- 0;
	positivos <- 0;
	Repetir
		Escribir "Dame el valor del numero #",i;
		Leer num;
		//codigo para pares o impares:
		Si num mod 2 = 0 Entonces
			pares <- pares + 1;
		SiNo
			Si num mod 2 <> 0 Entonces
				impares <- impares + 1;
			FinSi
		FinSi
		//codigo para positivos y negativos:
		Si num >= 0 Entonces
			positivos <- positivos + 1;
		SiNo
			Si num < 0 Entonces
				negativos <- negativos + 1;
			FinSi
		FinSi
		i <- i + 1;
	Hasta Que i > 100;
	Escribir "Hay ",pares," numeros pares";
	Escribir "Hay ",impares," numeros impares";
	Escribir "Hay ",positivos," numeros postivos";
	Escribir "Hay ",negativos," numeros negativos";
FinProceso
