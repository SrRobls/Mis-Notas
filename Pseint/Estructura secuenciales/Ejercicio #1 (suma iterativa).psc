//Ejercicio #1: Calcular la suma de los N primeros numeros (S=1+2+3+4+5+...+N)
Proceso Inicio
	Definir N, suma, i Como Entero;
	
	Escribir "Dame la catidad de numeroa a sumar: ";
	Leer N;
	suma <- 0;
	Para i <- 1 Hasta N Con Paso 1 Hacer
		suma <- suma + i;
	FinPara
	Escribir "La suma es: ",suma;
FinProceso
