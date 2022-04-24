//Ejercicio #65: dibuja un cuadrado con asteriscos, en la que aparezca solamente el borde. el numero de asteriscos de ancho y alto seran los mismos y lo indicara el usuario.
Proceso inicio
	Definir Dim, caja, asteriscos Como Entero;
	Escribir "Dame las dimensiones de la estructura cuadrada ";
	Leer Dim;
	caja <- Dim;
	asteriscos <- 0;
	Mientras Dim >= 1 Hacer
		asteriscos <- 1;
		Si Dim = 1 O Dim = caja Entonces
			Mientras Dim = 1 O Dim = caja Hacer //Comienzo del bucle para el techo y la base
				Mientras asteriscos <= caja  Hacer
					Escribir "*"Sin Saltar;
					asteriscos <- asteriscos + 1;
				FinMientras
				Escribir "";
				Dim <- Dim - 1;
			FinMientras //Final del bucle para el techo y la base
		SiNo
			Mientras asteriscos <= caja Hacer //Comienzo bucle bordes
				Si asteriscos = 1 O asteriscos = caja Entonces
					Escribir "*" Sin Saltar;
					asteriscos <- asteriscos + 1;
				SiNo
					Escribir " " Sin Saltar;
					asteriscos <- asteriscos + 1;
				FinSi
			FinMientras //Final bucle bordes
			Dim <- Dim - 1;
			Escribir " ";
		FinSi
	FinMientras
FinProceso
