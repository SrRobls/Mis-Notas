//ejercicio #60: Calcular el MCD de dos numeros:
Proceso Inicio
	Definir num1, num2, divisor, mcd Como Real;
	Definir i Como Logico;
	Escribir "Dame el valor de dos numeros para sacar su MCD (Maximo Comun Divisor)";
	Leer num1, num2;
	i <- Falso;
	divisor <- 2;
	mcd <- 1;
	Repetir
		Si num1 mod divisor = 0 Y num2 mod divisor = 0 Entonces
			num1 <- num1 / divisor;
			num2 <- num2 / divisor;
			mcd <- mcd * divisor;
		SiNo 
			Si num1 mod divisor = 0 Y num2 mod divisor <> 0 O num1 mod divisor <> 0 Y num2 mod divisor = 0 O num1 mod divisor <> 0 Y num2 mod divisor <> 0 Y num1 >= divisor Y num1 >= divisor Entonces
				divisor <- divisor + 1;
			SiNo
				i <- Verdadero;
			FinSi
		FinSi
	Hasta Que i = Verdadero
	Escribir "El Maximo Comun divisor es ",mcd;
FinProceso
