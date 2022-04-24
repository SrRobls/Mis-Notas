//Ejercicio #4: Suponga que tiene un conjunto de calificaciones de un grupo de 10 estudiantes.
//Realizar un algoritmo para calcular lla calificacion promedio y la califiacacion mas baja de todo el grupo.
Proceso Inicio
	Definir calificacion, suma, promedio, C_Baja Como Real;
	Definir i Como Entero;
	suma <- 0;
	C_Baja <- 99999;
	
	para i <- 1 hasta 10 con paso 1 Hacer
		Escribir i,".Digite una calificacion: ";
		Leer calificacion;
		
		suma <- suma + calificacion;
		
		Si calificacion < C_Baja Entonces
			C_Baja <- calificacion;
		FinSi
	FinPara
	
	promedio <- suma / 10;
	Escribir "El promedio es de: ",promedio;
	Escribir "La nota mas baja es: ", C_Baja;
FinProceso
