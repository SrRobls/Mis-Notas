//Ejercicio #14: Ingresar un numero posistivo <20 y determinar si es primo o no.
Proceso Inicio
	Definir Num, Contador, i Como Entero;
	Contador <- 0;
	
	Escribir "Dame un numero (menor a 20 por favor)";
	
	Repetir
		leer Num;
		Si Num < 20 Y Num >= 0 Entonces
			Para i <- 1 Hasta Num Con Paso 1 Hacer
				Si Num Mod i = 0 Entonces
					Contador <- Contador + 1;
				FinSi
			FinPara
		SiNo
			Escribir "Debe ser un numero POSITIVO MENOR a 20";
		FinSi
	Hasta Que Num < 20 Y Num >= 0
	Si Contador = 2 Entonces
		Escribir Num," ES NUMERO PRIMO";
	SiNo
		Escribir Num," NO ES NUMERO PRIMO";
	FinSi
FinProceso
