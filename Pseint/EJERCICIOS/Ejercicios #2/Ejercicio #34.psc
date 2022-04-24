//Ejercicio #34: Calcula el sueldo de un trabajador dado su sueldo base y sabiendo que si ha trabajado mas de 4o horas combrara un 20%.
Proceso Inicio
	Definir sueldoHora, sueldo, caja, horas, descuento Como Real;
	Escribir "¿Cuanto ganas por hora de trabajo?: ";
	Leer sueldoHora;
	Escribir "¿Cuantas horas trabajaste?: ";
	Leer horas;
	descuento <- 20;
	sueldo <- 0;
	sueldo <- sueldoHora * horas;
	
	Si horas > 40 Entonces
		Escribir "Asi que hay un aumento del 20%. Entonces:";
		caja <- (sueldo * descuento) / 100;
		sueldo <- sueldo + caja;
		Escribir "El sueldo a cobrar es: ",sueldo,"$";
	SiNo
		Escribir "El sueldo es ",sueldo,"$";
	FinSi
FinProceso
