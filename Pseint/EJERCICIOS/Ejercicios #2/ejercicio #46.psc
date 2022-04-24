//Suma todos los numeros que indique el usuario hasta que introduzca un cero.
Proceso Inicio
	Definir num, suma Como Entero;
	suma <- 0;
	num <- 0;
	
	Repetir
		Escribir "Dame numero para sumar:";
		Leer num;
		suma <- suma + num;
		Escribir "La suma va en: ",suma;
	Hasta Que num = 0
	Escribir "La suma es: ",suma;
FinProceso
