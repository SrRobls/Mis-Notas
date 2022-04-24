// Ejercicio #2: Hacer un programa para ingresar el radio de un circulo y se reporte su area y longitud  de circunferencia:
Proceso inicio
	Definir Radio, Area, Long Como Real;;
	
	Escribir "dame el valor del Radio: ";
	Leer Radio;
	
	Area <-  PI * Radio^2;
	Long <- 2 * PI * Radio;
	
	Escribir "El Area de la circunferencia es: ", Area;
	Escribir "La Longitud de la circunferencia es: ", Long;
	
FinProceso
