//ejercicio #83: crea un subproceso que reciba tres numeros por referencia y que los ordene de mayor a menor al pasarle los valores desde el algoritmo principla
//muestra los valores por pantalla.
Funcion  ordenarNum(x Por Referencia)
	Definir i, j, caja Como Entero;
	j <- 0;
	i <- 0;
	caja <- 0;
	Escribir "La funcion sin ordenar es:";
	para i <- 0 hasta 3-1 Con Paso 1 Hacer
		Escribir "[",x[i],"]"Sin Saltar;
	FinPara
	para i <- 2 hasta 0 Con Paso -1 Hacer
		para j <- 0 hasta i Con Paso 1 Hacer
			Si x[j] < x[i] Entonces
				caja <- x[j];
				x[j] <- x[i];
				x[i] <- caja;
			FinSi
		FinPara	
	FinPara
	Escribir "La funcion ordenanada es:";
	para i <- 0 hasta 2 Con Paso 1 Hacer
		Escribir "[",x[i],"]"Sin Saltar;
	FinPara
FinFuncion
Proceso inicio
	Definir lista, i Como Entero;
	i <- 0; 
	Dimension lista[3];
	//para pedir la lista de numeros al usuario
	Para i <- 0 hasta 3-1 Con Paso 1 Hacer
		Escribir "Dame el valor del #",i + 1;
		Leer lista[i];
	FinPara
	ordenarNum(lista);
	Escribir "";
FinProceso
