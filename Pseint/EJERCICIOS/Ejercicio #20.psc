//Ejercicio #20: Ingresar la nota de N alumnos y determinar cual es la nota baja.
Proceso Inicio
	Definir i, nota, N_Alumnos, contenedor1, contenedor2 Como Real;
	Escribir "Dame la cantidad de alumnos: ";
	Leer N_Alumnos;
	contenedor1 <- 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999;
	contenedor2 <- 0;
	Para i <- 1 Hasta N_Alumnos Con Paso 1 Hacer
		Escribir "Dame la nota del #",i," alumno:";
		Leer nota;
		Si nota < contenedor1 Entonces
			contenedor1 <- nota;
			contenedor2 <- i;
		FinSi
	FinPara
	Escribir "La nota mas baja es: ",contenedor1," y es del estudiante #",contenedor2;
FinProceso
