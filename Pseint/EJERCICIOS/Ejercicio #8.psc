//Ejercicio #8: Calcular los multiplos de un numero ingresado por teclado, comprendidio entre 0 y N
//(Estructura Mientras)
Proceso Inicio
	Definir I, N, Contenedor Como Entero;
	Escribir "¿Cual es el numero al que desea obtener los multiplos?";
	Leer I;
	Escribir "¿Hasta cual numero?";
	leer N;
	Contenedor <- I;
	
	Mientras I <= N Hacer
		Escribir I;
		I <- I + Contenedor;
	FinMientras
FinProceso
