//crea un subproceso que escriba si un numero dado es primo o no. aprovecha ese subproceso para indicar si los numero naturales entre 1 y el numero dado son primos o no.
//funcion 
Funcion numPrimo(x)
	Definir i, j, caja1, caja2 Como entero;
	j <- 0;
	i <- 0;
	caja1 <- 0;
	caja2 <- 0;
	//--------------------------codigo necesario para saber si el numero dado es primo o no: --------------------------------------------
	Mientras i <> x Hacer
		i <- i + 1;
		Si x mod i = 0 Entonces
			caja1 <- caja1 + 1;
		FinSi
		//reinicio de variables:
		j <- 0;
		caja2 <- 0;
		//---------------------codigo para saber si los numeros menor a al numero dado son primos o no:-------------------
		Mientras j <> i Hacer
			j <- j + 1;
			si i mod j = 0 Entonces
				caja2 <- caja2 + 1;
			FinSi
		FinMientras
		Si caja2 == 2  Entonces
			Escribir i," Si es un numero primo";
		SiNo
			Escribir i," No es un numero primo";
		FinSi
		//------------------------------------------------------------------------------------------------------------------
	FinMientras
	//codigo para ver si el numero dado es primo o no:
	Escribir "_______________________________________________________________"; 
	Si caja1 == 2 Entonces
		Escribir x," Si es un numero primo";
	SiNo
		Escribir x," No es un numero primo";
	FinSi
	//-----------------------------------------------------------------------------------------------------------------------------------------
FinFuncion
Proceso Inicio
	Definir num Como entero;
	num <- 0;
	Escribir "Dame un numero y te dire si este es primo o no: ";
	Leer num;
	numPrimo(num);
FinProceso
