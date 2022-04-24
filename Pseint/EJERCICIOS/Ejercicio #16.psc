//Ejercicio #16: Ingresar un numero positivo par y calcular el facotrial de ese numero
Proceso Inicio
	Definir Num, i, contenedor, resultado, caja Como Real;
	Escribir "Dame un numero par positivo al que quieras hallarle su fctorial";
	Leer Num;
	contenedor <- Num;
	caja <- Num;
	i <- 1;
	
	Si Num Mod 2 = 0 y Num >= 0 Entonces
		Repetir
			contenedor <- contenedor - 1;
			Num <- Num * (contenedor);
			i <- i + 1;
		Hasta Que i = caja
		Escribir "El factorial es: ",Num;
	SiNo
		Escribir "Debe ser un numero par positivo";
	FinSi
FinProceso
