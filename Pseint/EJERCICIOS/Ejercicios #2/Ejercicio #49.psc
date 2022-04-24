//Calcula la suma de todos los numeros comprendidos entre 0 y el numero natural que quiera el usuario
Proceso Inicio
	Definir i, num, suma, caja Como Entero;
	Escribir "Hasta que numero quieres que vaya el conteo?:";
	Leer num;
	i <- 0;
	suma <- 0;
	caja <- suma;
	Para i <- 1 hasta num Con Paso 1 Hacer
		suma <- suma + i; 
		Escribir i," + ",caja," = ",suma;
		caja <- suma;
	FinPara
	Escribir "La suma es: ",suma;
FinProceso
