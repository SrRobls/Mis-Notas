//ejercicio #10: realiza la multiplicacion de 2 numeros mediante sumas sucesivas
Proceso inicio
	Definir Num1, Num2, I, suma, contador Como Entero;
	
	Escribir "Dame un numero";
	Leer Num1;
	Escribir "Dame el otro numero";
	Leer Num2;
	
	I <- 0;
	suma <- 0;
	contador <- 0;
	
	Repetir
		suma <- I + Num1;
		Escribir I, " + ", Num1, " = ", suma;
		I <- suma;
		contador <- contador + 1;
	Hasta Que contador = Num2
	Escribir "La multiplicacion es: ",suma;
FinProceso
