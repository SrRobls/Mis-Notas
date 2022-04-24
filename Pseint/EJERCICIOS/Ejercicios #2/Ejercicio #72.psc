//ejercicio #72: crea una matriz con numeros aleatorios y despues cuenta le numero de veces que aparece un numero que haya sido indicado por el usuario
Proceso Inicio
	Definir matriz, filas, columnas, num, repeticiones Como Entero;
	filas <- 0;
	columnas <- 0;
	num <- 0;
	repeticiones <- 0;
	Dimension matriz[3,3];
	Escribir "La matriz 3x3 es: ";
	//creacion de la matriz 3x3. la matriz tendra numeros aleatorios y no introducidos por le usuario:
	Para filas <- 0 hasta 2 Con Paso 1 Hacer
		Para columnas <- 0 hasta 2 Con Paso 1 Hacer
			matriz[filas,columnas] <- azar(10);
			Escribir matriz[filas,columnas]," " Sin Saltar;
		FinPara
		Escribir " ";
	FinPara
	//el numero que sera buscado:
	Escribir "Dame el numero al quieres saber cuantas veces se repite: ";
	Leer num;
	//buscador de cuantas veces se repite el numero:
	Para filas <- 0 hasta 2 Con Paso 1 Hacer
		Para columnas <- 0 hasta 2 Con Paso 1 Hacer
			Si num == matriz[filas,columnas] Entonces
				repeticiones <- repeticiones + 1;
			FinSi
		FinPara
	FinPara
	Escribir "El numero ",num," se repite ",repeticiones," vece/s";;
FinProceso
