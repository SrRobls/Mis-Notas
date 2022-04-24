//Ejercicio #8: Dadas las horas trabajadas de 5 personas y la tarifa de pago calcular el salario,
// y la sumatoria de todos los salarios.
Proceso Main
	Definir horas, i, tarifa, salario, salario_Total Como Real;
	Escribir "De cuanto es la tarifa de horas trabajadas (cuanto se paga por cada hora trabajada)?";
	Leer tarifa;
	i <- 1;
	salario_Total <- 0;
	Repetir
		Escribir "Cuantas horas trabajo el ",i," trabajador?";
		Leer horas;
		salario <- horas * tarifa;
		Escribir "salario del ",i," trabajador es: ",salario," dolares";
		i <- i + 1;
		salario_Total <- salario_Total + salario;
	Hasta Que i >= 6
	Escribir "El salario total a pagar a todos los trabajadores es: ",salario_Total," dolares";
FinProceso
