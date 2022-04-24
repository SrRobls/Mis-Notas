//Calcula el MCM de dos numeros
Proceso Inicio
	Definir num1, num2, divisor, mcm Como Real;
	Definir i Como Logico;
	Escribir "Dame el valor de dos numeros para sacar su MCM (Minimo Comun Multiplo)";
	Leer num1, num2;
	i <- Falso;
	divisor <- 2;
	mcm <- 1;
	Repetir
		Si num1 mod divisor = 0 O num2 mod divisor = 0 Entonces
			Si num1 mod divisor = 0 Entonces
				num1 <- num1 / divisor;
			FinSi
			Si num2 mod divisor = 0 Entonces
				num2 <- num2 / divisor;
			FinSi
			mcm <- mcm * divisor;
		SiNo
			Si num1 = 1 Y num2 = 1 Entonces
				i <- Verdadero;
			SiNo
				divisor <- divisor + 1;
			FinSi
		FinSi
	Hasta Que i = Verdadero
	Escribir "El Minimo Comun Multiplo es ",mcm;
FinProceso
