//Ejercicio #11: Realizar la division de dos numeros mediante restas sucesivas
Proceso Inicio
	Definir Numerador, Denominador, resta  Como Real;
	Definir i, contador Como Real;
	
	Escribir "Dame el numerador";
	leer Numerador;
	Escribir "Dame el denominador";
	Leer Denominador;
	
	i <- 0;
	contador <- 0;
	resta <- 1;
	
	Repetir
		Si resta = 0 Entonces
			i <- contador;
		SiNo
			resta <- Numerador - Denominador;
			Escribir Numerador, " - ", Denominador, " = ", resta;
			Numerador <- resta;
			contador <- contador + 1;
		FinSi
	Hasta Que i = contador
	Escribir "La division es: ",contador;
	
FinProceso
