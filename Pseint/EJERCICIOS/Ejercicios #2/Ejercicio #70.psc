//Ejercicio #70: hacer el ejecicio 69 con el metodo denominado de seleccion consistente en buscar el nuero menor y moverlo a la derecha del todo. ddespues se repite este procedimiento hasta tener todo el arrglo colocado.
Proceso Inicio
	Definir j, i, lista, caja, p Como Entero;
	caja <- 0;
	j <- 0;
	i <- 0;
	p <- 0;
	Dimension lista[5];
	//recoleccion de los numeros:
	Para j <- 0 hasta 4 Con Paso 1 Hacer
		Escribir "Dame el numero #",j + 1;
		Leer lista[j];
	FinPara
	//bucle ordenar los numeros:
	Para j <- 4 hasta 1 Con Paso -1 Hacer 
		para p <- 0 hasta 4 con paso 1 Hacer
			Escribir lista[p]," "Sin Saltar;
		FinPara
		Escribir " ";
		Para i <- 0 hasta j Con Paso 1 Hacer
			Si lista[i] < lista[j] Entonces
				caja <- lista[i];
				lista[i] <- lista[j];
				lista[j] <- caja;
			FinSi
		FinPara
	FinPara
FinProceso
