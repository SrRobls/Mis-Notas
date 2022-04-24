Proceso Inicio
	Definir suma, num1, num2 Como Entero;
	Escribir "Dame el valor de dos numeros. el primero menor que el segundo";
	Leer num1, num2;
	suma <- 0;
	Mientras num1 < num2 - 1 Hacer
		num1 <- num1 + 1;
		suma <- suma + num1;
	FinMientras
	Escribir "La suma es: ",suma;
FinProceso
