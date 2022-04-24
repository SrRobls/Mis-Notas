//Ejercicio #1: Ingrese un numer entero y reportar si es par o impar.
Proceso Inicio
	Definir num Como Entero;
	
	Escribir "Dame un numero: ";
	leer num;
	
	si(num mod 2 = 0) Entonces
		Escribir "Este numero es par";
	SiNo
		Escribir "Este numero es impar";
	FinSi
	
FinProceso
