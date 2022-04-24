//Ejercicio #50:  cuenta cuantos numero de los comprendidos entre 500 y 1000 (incluidos), 
//cumplen que son a la vez multiplos de 2 y 3.
Proceso inicio
	Definir num, contador Como Entero;
	num <- 0;
	contador <- 0;
	Para num <- 500 hasta 1000 Con Paso 1 Hacer
		Si num mod 2 = 0 Y num mod 3 = 0 Entonces
			Escribir num," Es multiplo de 2 y de 3";
			contador <- contador + 1;
		FinSi
	FinPara
	Escribir "Hay ",contador," numeros entre 500 y 1000 que son multiplos de 2 y 3";
	
FinProceso
