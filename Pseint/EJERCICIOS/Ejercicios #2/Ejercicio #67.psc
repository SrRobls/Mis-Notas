//ejercicio #67: Guarda en un arreglo las 5 notas de un estudiante que has de pedir al usuario. posteriormente indica la media y cual es el mayor y la menor de ellas
Proceso inicio
	Definir promedio, notaAlta, notaBaja, arreglo, nota Como Real;
	promedio <- 0;
	nota <- 0;
	notaAlta <- -999999999999999999999999999999999999999999999999999;
	notaBaja <- 9999999999999999999999999999999999999999999999999999;
	Dimension arreglo[5];
	para nota <- 0 Hasta 4 con paso 1 Hacer
		Escribir "Dame el valor de la nota #",nota + 1;
		Leer arreglo[nota];
		Si arreglo[nota] > notaAlta Entonces
			notaAlta <- arreglo[nota];
		SiNo
			Si arreglo[nota] < notaBaja Entonces
				notaBaja <- arreglo[nota];
			FinSi
		FinSi
	FinPara
	promedio <- (arreglo[0] + arreglo[1] + arreglo[2] + arreglo[3] + arreglo[4]) / 5;
	Escribir "El promedio es: ",promedio,". La nota mas alta es: ",notaAlta,", y la nota mas baja es: ",notaBaja;
FinProceso
