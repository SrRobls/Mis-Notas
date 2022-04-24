//Ejercicio #4: Un profesor prepara tres cusetionarios para una evaluacion final. A, B y C. se sabe que se tarda 5 minutos en revisar el cuestionario A, 8 en revisar el cuestionario B y 6 en el C. la cantidad de examenes de cada tipo se entran por teclado. cuantas horas y cuentos minutos se tard en revisar todas las evaluaciones.
Proceso inicio
	Definir A,B,C, Tiempo_A,Tiempo_B,Tiempo_C, Tiempo_Total Como Enteros;
	Definir horas,minutos Como Reales;
	
	Escribir "¿Cual es la cantidad de examenes tipo A?";
	Leer A;
	Escribir "¿Cual es la cantidad de examenes tipo B?";
	Leer B;
	Escribir "¿Cual es la cantidad de examenes tipo C?";
	Leer C;
	Tiempo_A <- A*5;
	Tiempo_B <- B*8;
	Tiempo_C <- C*6;
	
	//Calculamos las horas y los minutos:
	Tiempo_Total <- Tiempo_A + Tiempo_B + Tiempo_C;
	horas <- trunc(Tiempo_Total / 60);
	minutos <- Tiempo_Total mod 60;
	
	Escribir "La cantidad de horas que tarda en revisar es: ",horas, " horas con ", minutos, " minutos";
FinProceso
