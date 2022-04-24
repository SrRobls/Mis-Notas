//ejercicio #55: Averigual cual es el digito mas pequeño de un numero dado.
Proceso Inicio
	Definir num, digito, caja Como real;
	Escribir "Dame un numero y te dire cual es el digito mas pequeño: ";
	Leer num;
	caja <- num;
	digito <- 9999999999999999999999999999999999999999999999999999999999999;
	Repetir
		Si num mod 10 < digito Entonces
			digito <- num mod 10;
		FinSi
		num <- trunc(num / 10);
	Hasta Que num = 0;
	Escribir "el digito mas pequeño de ",caja," es: ",digito;
FinProceso
