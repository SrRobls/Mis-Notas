//ejrcicio #1: Calcular la cantidad de segundo que estan incluidos en el numero de horas, minutos y segundos ingresados por el ususario
Proceso inicio
	definir horas, minutos, seg Como Entero;
	
	Escribir "Dame la cantidad de hora/s: ";
	Leer horas;
	Escribir "Dame la cantidad de minuto/s: ";
	Leer minutos;
	Escribir "Dame la cantidad de segundo/s: ";
	Leer seg;
	
	Escribir "La cantidad de hora/s, minuto/s y segundo/s respectivamente es: ", horas, ": ", minutos, ": ", seg; 
	Escribir "-------Todo esto pasado a segundos---------";
	//pasando horas y minutos a segundos:
	horas <- horas * 3600;
	minutos <- minutos * 60;
	Escribir horas + minutos + seg, " segundos"; 
	
	
	
	
FinProceso
