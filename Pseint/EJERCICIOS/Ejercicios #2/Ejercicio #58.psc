//ejercicio #58: averigua si un numero es perfecto. (numero positivo que es igual a la suma de sus divisores positivos)
//nota: no se cuenta a el mismo como divisor.
Proceso Inicio
	Definir num, divisor, contador como entero;
	Escribir "Dame un numero y te dire si ese es perfecto o no:";
	Leer num;
	contador <- 0;
	divisor <- 0;
	Para divisor <- 1 hasta num Con Paso 1 Hacer
		Si num Mod divisor = 0 Y divisor <> num Entonces
			contador <- contador + divisor;
		FinSi
	FinPara
	Si contador = num Entonces
		Escribir num," Es un numero perfecto";
	SiNo
		Escribir num," No es un numero perfecto";
	FinSi
FinProceso
