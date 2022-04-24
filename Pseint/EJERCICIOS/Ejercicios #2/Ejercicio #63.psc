//Ejercicio #63: dibujar una estructura cuadrada pidiendo al ususario cuantos asteriscos se tendra de alto y ancho,
Proceso Inicio
	Definir alto, ancho, asteriscosAlto, asteriscosAncho  Como Entero;
	Escribir "Dame el alto y el ancho que quieres para la estructura cuadrada:";
	Leer alto, ancho;
	asteriscosAlto <- 1;
	asteriscosAncho <- 1;
	Mientras asteriscosAlto <= alto Hacer //bucle del alto
		Mientras asteriscosAncho <= ancho Hacer //reinicio ancho
			Escribir "*" Sin Saltar;
			asteriscosAncho <- asteriscosAncho + 1;
		FinMientras
		Escribir ""; //salo de lienea
		asteriscosAncho <- 1;
		asteriscosAlto <- asteriscosAlto + 1;
	FinMientras
FinProceso
