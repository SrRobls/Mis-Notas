//Ejercicio #44: Calcula cuantos digitos tiene un numero
Proceso inicio
	Definir num, digitos Como Entero;
	Escribir "Dame un numero para calcular cuantos digitos tiene";
	Leer num;
	digitos <- 0;
	Si num = 0 Entonces
		Escribir "0 digitos";
	SiNo
		Mientras num <> 0 Hacer
			num <- trunc(num/10);
			digitos <- digitos + 1;
		FinMientras
	FinSi
	Escribir ,digitos," digitos";
	
	
FinProceso
