//Ejercicio #17: Escribir un flujograma que calcule la suma de los cuadros de los n
// primeros numeros naturales: 1^2+2^2+3^2+n^2
Proceso Inicio
	Definir num, i, contenedor, procedimiento Como Entero;
	Escribir "Dame un numero (el valor limite)";
	leer num;
	i <- 0;
	contenedor <- 0;
	procedimiento <- 0;
	Repetir
		i <- i + 1;
		procedimiento <- i^2;
		Escribir i,"^2"," = ",procedimiento;
		contenedor <- contenedor + procedimiento;
	Hasta Que i = num
	Escribir "El resultado de la suma es: ",contenedor;
FinProceso
