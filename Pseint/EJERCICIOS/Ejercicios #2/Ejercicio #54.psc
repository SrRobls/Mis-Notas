//Ejercicio #54:averigua si un numero es primo o no.
Proceso inicio
	Definir num, i, contador Como Entero;
	Escribir "Dame un numero y te dire si ese numero es primo o no: ";
	Leer num;
	i <- 0;
	contador <- 0;
	Repetir
		i <- i + 1;
		Si num mod i = 0 Entonces
			contador <- contador + 1;
		FinSi
	Hasta Que i = num
	Si contador = 2 Entonces
		Escribir num," Si es primo";
	SiNo
		Escribir num," No es primo";
	FinSi
	
FinProceso
