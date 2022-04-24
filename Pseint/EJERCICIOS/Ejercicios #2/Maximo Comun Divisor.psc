Proceso Inicio
		Definir num1, num2, menor, i, mcd Como Real;
		Escribir "Dame el valor de dos numeros para sacar su MCD (Maximo Comun Divisor)";
		Leer num1, num2;
		i <- 0;
		menor <- 0;
		mcd <- 0;
		Si num1 < num2 Entonces
			menor <- num1;
		SiNo
			menor <- num2;
		FinSi
		Para  i <- 1 hasta menor Con Paso 1 Hacer
			Si num1 Mod i = 0 Y num2 Mod i = 0 Entonces
				mcd <- i;
			FinSi
		FinPara
		Escribir "El Maximo Comun Divisor de ",num1," y ",num2," es: ",mcd;
FinProceso
