//Numeros primos
Proceso main
	Definir Num, Contador, i Como Entero;
	Escribir "Dame un numero: ";
	leer Num;
	Contador <- 0;
	
	Para i <- 1 Hasta Num Con Paso 1 Hacer 
		Si Num Mod i = 0 Entonces
			Contador <- Contador + 1;
		FinSi
	FinPara
	
	Si Contador = 2 Entonces
		Escribir Num," SI es un numero primo";
	SiNo
		Escribir Num," NO es un numero primo";
	FinSi
	
	
FinProceso
