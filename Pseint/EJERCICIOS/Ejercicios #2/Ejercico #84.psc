//Ejercicio #84: crea un subprceso que devuelva el mayor numero de una lista.
Funcion numMayor(x,z)
	Definir i, caja, posicion Como Entero;
	caja <- 0;
	posicion <- 0;
	Para i <- 0 hasta z-1 con paso 1 Hacer
		Escribir "[",x[i],"]"Sin Saltar;
		Si x[i] > caja Entonces
			caja <- x[i];
			posicion <- i+1;
		FinSi
	FinPara
	Escribir "";
	Escribir "El numero mayor es ",caja," y su posicion es ",posicion;
FinFuncion
Proceso inicio
	Definir lista, i, cantidad Como Entero;
	i <- 0;
	cantidad <- 0;
	Escribir "Dame la cantidad de numeros:";
	Leer cantidad;
	Dimension lista[cantidad];
	Para i <- 0 hasta cantidad-1 Con Paso 1 Hacer
		Escribir "Dame el valor del #",i+1;
		Leer lista[i];
	FinPara
	numMayor(lista,cantidad);
FinProceso
