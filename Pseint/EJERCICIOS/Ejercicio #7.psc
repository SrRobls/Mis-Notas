//Ejercicio #6: calcular los numeros de un numero ingresado por teclado, 
//comprendidio entre 0 y N (estructura para)
Proceso inicio
	Definir I, N, contenedor Como entero;
	Escribir "¿De que numero desea obtener los multiplos?";
	Leer I;
	contenedor <- I;
	Escribir "¿Hasta que numero desea que se implima la serie?";
	leer N;
	
	Para I<-I Hasta N Con Paso contenedor Hacer
		Escribir I;
	FinPara
FinProceso
