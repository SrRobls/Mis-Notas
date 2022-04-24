//Ejercicio #85: Crea un subproceso que calcule el mcm (minimo comun multiplo) de varios numeros proporcionados en un arreglo. prueba su funcionamiento en el algoritmo normal

Proceso Inicio
	Definir nums, i, cantidad Como Entero;
	i <- 0;
	cantidad <- 0;
	Escribir "Dame la cantidad de los numeros a hallar su mcm";
	Leer cantidad;
	Dimension nums[cantidad];
	//recoleccion de numeros:
	Escribir "Dame los valores:";
	para i <- 0 hasta cantidad-1 Con Paso 1 Hacer
		Leer nums[i];
	FinPara
	
FinProceso
