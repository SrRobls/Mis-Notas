//Ingresar la nota de N Alumnos y determinar  cual es la nota mas alta
Proceso Inicio
	Definir N_Alumnos, i, nota, contenedor1, contenedor2 como Reales;
	Escribir "Dame la cantidad de Alumnos: ";
	Leer N_Alumnos;
	contenedor1 <- -99999999999999999999999999999999999999999999999999999999;
	Para i <- 1 Hasta N_Alumnos Con paso 1 Hacer
		Escribir "Dame el valor del estudiante #",i,":";
		Leer nota;
		Si nota > contenedor1 Entonces
			contenedor1 <- nota;
			contenedor2 <- i;
		FinSi
	FinPara
	Escribir "La nota mas alta es: ",contenedor1," del estudiante #",contenedor2;
	
FinProceso
