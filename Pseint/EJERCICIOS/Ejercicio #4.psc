//Elaborara un flujograma que muestre la suma y la serie de los numeros pares comprendidos entre (20,10) en orden ascendente
Proceso incico
	Definir num, suma Como Entero;
	num <- 12;
	suma <- 0;
	Repetir
		suma <- suma + num;
		Escribir num;
		num <- num + 2;
	Hasta Que num = 20;
	Escribir "La suma es: ",suma;
FinProceso
