//Ejercicio: crea un subproceso que escriba la tabla de multiplicar  del numero que se le indique. Posteriormente aprovecha ese SubProceso 
//para hcer las tablas del uno hasta el numero indicado

funcion tablas(x)
	definir mult, i, j Como Entero;
	mult <- 0;
	i <- 0;
	j <- 0;
	para i <- 1 hasta x Con Paso  1 Hacer
		Escribir "Tabla del ",i,":";
		Para j <- 1 hasta 10 Con Paso 1 Hacer
			mult <- i * j;
			Escribir i," x ",j," = ",mult;
		FinPara
		Escribir " ";
	FinPara
FinFuncion
Proceso inicio
	Definir num Como Entero;
	num <- 0;
	Escribir "Dame un numero";
	Leer num;
	tablas(num);
FinProceso
