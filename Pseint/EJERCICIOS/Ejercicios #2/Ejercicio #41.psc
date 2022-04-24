//Ejercicio #41: Indica la calificacion de un alumno dependiendo de si calificacion.
Proceso Inicio
	Definir calificacion Como Entero;
	Escribir "Dame el valor de tu calificcion";
	Leer calificacion;
	
	segun calificacion hacer
		10:
			Escribir calificacion," Es sobresaliente";
		9:
			Escribir calificacion," Es notable";
		8: 
			Escribir calificacion," Es bien";
		7: 
			Escribir calificacion," Es aprobado";
		De Otro Modo:
			Escribir "Reprobaste ;(";
	FinSegun
FinProceso
