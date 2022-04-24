// Ejercicio #2: determinar si un alumno  aprueba o reprueba un curso, sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; reprueba en caso contrario.
Proceso sin_titulo
	Definir nota1,nota2,nota3,promedio Como Entero;
	Escribir 'Por favor dame las notas (de 0 a 100) de tus tres calificaciones respectivamente: ';
	Leer nota1;
	Leer nota2;
	Leer nota3;
	promedio <- redon((nota1+nota2+nota3)/3);
	Si promedio>=70 Entonces
		Escribir 'tu nota final es de: ',promedio,' aprobaste!!';
	SiNo
		Escribir 'Tu nota final es de: ',promedio,' reprobaste :(';
	FinSi
FinProceso
