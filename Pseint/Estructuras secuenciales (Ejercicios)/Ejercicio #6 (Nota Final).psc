//Ejercicio #6: Un alumno desea saber cual sera su calificacion final en la materia de algoritmos. dicha califiacion se compone de los siguientes porcentajes
Proceso Inicio
	Definir parcial_1, parcial_2, parcial_3, promedio, ValorParciales Como Real;
	Definir  Nota_ExamenFinal, Valor_ExamenFinal, Nota_TrabajoFinal, Valor_TrabajoFinal, NotaFinal Como Real;
	
	Escribir "¿Cual fue tu nota en el parcial 1?: ";
	Leer parcial_1;
	Escribir "¿Cual fue tu nota en el parcial 2?: ";
	leer parcial_2;
	Escribir "¿Cual fue tu nota en el parcial 3?: ";
	leer parcial_3;
	promedio <- (parcial_1 + parcial_2 + parcial_3) / 3;
	ValorParciales <- promedio * 0.55;
	
	Escribir "¿Cual fue tu nota en el examen final?: ";
	Leer Nota_ExamenFinal;
	Valor_ExamenFinal <- Nota_ExamenFinal * 0.30;
	
	Escribir "¿Cual fue tu nota en tu trabajo final: ";
	Leer Nota_TrabajoFinal;
	Valor_TrabajoFinal <- Nota_TrabajoFinal * 0.15;
	
	NotaFinal <- ValorParciales + Valor_ExamenFinal + Valor_TrabajoFinal;
	
	Escribir "Tu promedio en los parciales es de: ", promedio;
	Escribir "Tu calificacion de los tres parciales que equivalen un 55% respecto a la nota final es: ", ValorParciales;
	Escribir "Tu calificacion del examen final que equivale a un 30% respecto a la nota final es: ", Valor_ExamenFinal;
	Escribir "Tu calificacion del trabajo final que equivale a un 15% respecto a la nota final es: ", Valor_TrabajoFinal;
	Escribir "Tu nota final es de: ", NotaFinal;
FinProceso
