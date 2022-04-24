//Ejercicio #15: Calcular el factorial de un numero
Proceso main
	Definir Num, i, contenedor, resultado, caja Como Entero;
	i <- 1;
	resultado <- 0;
	Escribir "Dame el numero al que deseas sacar su factorial";
	Leer Num;
	contenedor <- Num;
	caja <- Num;
	Repetir
		Num <- Num * (contenedor - 1);
		contenedor <- contenedor - 1;
		i <- i + 1;
	Hasta Que i = caja
	Escribir "El factorial es: ",Num;
FinProceso
