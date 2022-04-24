//Elaborar un flujograma que muestre la suma y la serie de los numeros pares correspondientes entre [10,20]
Proceso incio
	Definir num, suma Como Entero;
	
	num <- 10;
	suma <- 0;
	
	Repetir
		num <- num + 2;
		Escribir num;
		suma <- suma + num;
	Hasta Que num  >= 18;
	Escribir "La suma es: ",suma;
FinProceso
