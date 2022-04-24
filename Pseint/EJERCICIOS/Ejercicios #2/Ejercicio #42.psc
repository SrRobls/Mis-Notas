//ejercicio #42: Para determinar la tarifa de un gimnasio se tiene en cuenta la siguiente tabla (ver tabla)
//Indica cuanto tendra que pagar el usuario segun su preferncia.
Proceso Inicio
	Definir  horas, costo, periodo Como Entero;
	periodo <- 0;
	costo <- 0;
	Escribir "¿Cual es el periodo que quieres?. (1) MAÑANA o (2) TARDE";
	Leer periodo;
	Escribir "¿Cuantas horas quieres?. (1, 2 o 3 horas)";
	Leer horas;
	
	Segun periodo Hacer
		1:
			Segun horas hacer
				1:
					costo <- 20;
				2:
					costo <- 30;
				3:
					costo <- 40;					
			FinSegun
		2:
			Segun horas hacer
				1:
					costo <- 30;
				2:
					costo <- 40;
				3:
					costo <- 50;					
			FinSegun	
	FinSegun
	Escribir "El valor a pagar es: ",costo;
	
FinProceso
