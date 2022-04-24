//Ejercicio 25: Mostrar si un numero es capicua o no.
Proceso Inicio
	Definir Num, Text_Num Como Entero;
	Escribir "VEREMOS SI EL NUMERO QUE INGRESARAS ES UN NUMERO CAPICUA";
	Escribir "Asi que dame un numero: ";
	Leer Num;
	Text_Num <- ConvertirATexto(Num);
	
	Si Num >= 0 Y Num < 10 Entonces
		Escribir Num," No es Capicua";
	FinSi
	
FinProceso
