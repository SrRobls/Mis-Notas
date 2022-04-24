//Ejercicio #19: Ingresar la nota de N alumnos y calcular la suma y el promedio
Proceso Inicio
	Definir Alumnos,Suma,Promedio, i, Nota Como Reales;
	Escribir "¿Cuantos alumnos hay?";
	Leer Alumnos;
	i <- 1;
	suma <- 0;
	Mientras i <= Alumnos Hacer
		Escribir "¿Cual es la nota del estudiante #",i;
		Leer Nota;
		suma <- suma + Nota;
		i <- i + 1;
	FinMientras
	Escribir "La suma de las notas de los ",Alumnos," estudiantes es: ",suma;
	Promedio <- suma / Alumnos;
	Escribir "Y el promedio es: ",Promedio;
FinProceso
