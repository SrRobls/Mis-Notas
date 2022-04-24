//Elaborar un flujograma que muestre la suma la suma y la serie de los numero impares entre (10,20)
Proceso Inicio
	Definir num, suma Como Entero;
	num <- 11;
	suma <- 0;
	
	Repetir
		Escribir num;
		suma <- suma + num;
		num <- num + 2;
	Hasta Que num >= 20
	Escribir "La suma es: ",suma;
	
FinProceso
