//Ejercicio #6: calcular los numeros de un numero ingresado por teclado, 
//comprendidio entre 0 y N (estructura repetir)
Proceso Inicio
	Definir N, I, contenedor Como Entero;
	Escribir "¿De que numero desea obtener los multiplos?";
	Leer I;
	contenedor <- I;
	Escribir "¿Hasta que numero desea que se implima la serie?";
	leer N;
	
	Repetir
		Escribir I;
		I <- I + contenedor;
	Hasta Que I > N; 
FinProceso
