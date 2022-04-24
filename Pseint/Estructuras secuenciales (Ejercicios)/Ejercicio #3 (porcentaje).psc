//Ejercicio #3: Un maestro desea saber que porcentaje de hombres y mujeres  hay en un grupo de estudiantes
Proceso inicio
	Definir hombres,mujeres,total como Entero;
	Definir P_hombres, P_mujeres como reales;
	Escribir '¿Cual es la cantidad de hombre?';
	Leer hombres;
	Escribir "¿Cual es la cantidad de mujeres?";
	Leer mujeres;
	total <- hombres + mujeres;
	Escribir "El total de estudiantes es: ", total;
	P_hombres <- (hombres / total) * 100;
	P_mujeres <- (mujeres / total) * 100;
	Escribir "El porcentajes de hombres es: ", P_hombres, "%";
	Escribir "El porcentaje de mujeres es: ",P_mujeres, "%";
FinProceso
