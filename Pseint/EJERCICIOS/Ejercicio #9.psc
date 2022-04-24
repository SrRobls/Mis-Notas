//Ejercicio #9: Suma una serie de numero que finizaliza al introducir el 999.
//El 999 no debe se tenido en cuenta para la suma (Estructura Repetir)
Proceso Inicio
	Definir Num, contenedor Como Entero;
	Num <- 0;
	contenedor <- 0;
	Repetir
		contenedor <- contenedor + Num;
		Escribir "Dame un numero";
		leer Num;
	Hasta Que Num = 999;
	Escribir "La suma es: ",contenedor;
FinProceso
