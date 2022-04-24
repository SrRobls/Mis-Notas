//Ejercicio #46: Suma todos los numeros comprendidos entre los dos numeros enteros que indique el usuario.
//SIN INCLUIRLOS.
Proceso Inicio
	Definir limiteUno, limiteDos, suma, caja, i Como Entero;
	Escribir "Dame dos numeros para sumar todos los numeros comprendidos entre esos dos numeros ";
	Leer limiteUno, limiteDos;
	limiteUno <- limiteUno + 1;
	limiteDos <- limiteDos - 1;
	suma <- limiteUno;
	i <- 1;
	caja <- limiteDos - limiteUno;
	Mientras i <= caja Hacer
		suma <- suma + (limiteUno + i);
		i <- i + 1;
	FinMientras
	Escribir "La suma es: ",suma;
FinProceso
