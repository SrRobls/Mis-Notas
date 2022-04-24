//Ejercicio #6: calcular los numeros de un numero ingresado por teclado, 
//comprendidio entre 0 y N (estructura repetir)
Proceso Inicio
	Definir N, i Como Entero;
	Escribir "¿de cual numero desea tener los multiplos?";
	Leer N;
	
	i <- N + 1;
	
	Repetir
		Si (N MOD 2) = 0 Entonces
			Escribir "2";
		FinSi
		Si (N MOD 3) = 0 Entonces
			Escribir "3";
		FinSi
		Si (N MOD 5) = 0 Entonces
			Escribir "5";
		FinSi
		Si (N MOD 7) = 0 Entonces
			Escribir "7";
		FinSi
		Si (N MOD 9) = 0 Entonces
			Escribir "9";
		FinSi
		Si (N MOD 11) = 0 Entonces
			Escribir "11";
		FinSi
	Hasta Que i > N
FinProceso
