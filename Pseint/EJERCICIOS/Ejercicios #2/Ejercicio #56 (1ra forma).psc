//Ejercicio #56: indica el numero inverso a otro. ejemplo 542 -> 245
Proceso inicio
	Definir num, digito Como Entero;
	Escribir "Dame un numero y te dare su forma inversa: ";
	Leer num;
	digito <- 0;
	Repetir
		digito <- num mod 10;
		Escribir digito Sin Saltar;
		num <- trunc(num / 10);
	Hasta Que num = 0
FinProceso
