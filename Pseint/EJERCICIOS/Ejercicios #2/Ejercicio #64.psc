//Ejercicio #64: dibuja una estructura triangular. preguntando al usuario cuatas filas tendra.
Proceso Inicio
	Definir asteriscos, filas, linea Como Entero;
	Escribir "¿Cuantas filas quieres que tanga la estructura triangular?: ";
	Leer filas;
	asteriscos <- 1;
	linea <- 1;
	Mientras asteriscos <= filas Hacer
		Mientras linea <= asteriscos Hacer
			Escribir "*" Sin Saltar; //dibujar asteriscos
			linea <- linea + 1; //aumento para terminar el segundo bucle
		FinMientras
		Escribir ""; //salto de linea, (para pasar al siguiente renglon)
		linea <- 1; //contro de lineas-bases para que se dibujen los asteriscos (reinicio de linea)
		asteriscos <- asteriscos + 1; //aumento para terminar el primer bucle
	FinMientras
FinProceso
