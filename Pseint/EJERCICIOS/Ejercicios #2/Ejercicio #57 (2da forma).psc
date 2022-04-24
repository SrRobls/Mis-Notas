//Ejercicio #57
Proceso Inicio
	Definir num, inverso, digito, caja Como Entero;
	Escribir "Dame un numero y te dare su forma inversa: ";
	Leer num;
	caja <- num;
	inverso <- 0;
	digito <- 0;
	Repetir
		digito <- num mod 10;
		num <- trunc(num / 10);
		inverso <- inverso * 10 + digito;
	Hasta Que num = 0
	Escribir "El inverso de ",caja," es: ",inverso;
FinProceso
