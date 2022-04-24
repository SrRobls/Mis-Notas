//Elaborara un flujograma que muestre la suma y la serie de los numeros pares comprendidos entre (20,10) en orden descendente
Proceso Inicio
	Definir num, suma Como Entero;
	num <- 20;
	suma <- 0;
	Repetir
		num <- num - 2;
		Escribir num;
		suma <- suma + num;
	Hasta Que num = 12;
	Escribir "La suma es: ",suma;
FinProceso
