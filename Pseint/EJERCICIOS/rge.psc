//Ejercicio #13: Determinar si un numero es primo o no.
Proceso Inicio
	Definir Num Como Entero;
	Escribir "Dame un un numero";
	leer Num;
	Si Num = 2 o Num = 3 o Num = 5 o Num = 7 o Num = 11 Entonces
		Escribir Num," Es primo";
	SiNo
		Si Num mod 2 <> 0 Y Num mod 3 <> 0 Y Num Mod 5 <> 0 Y Num Mod 7 <> 0 Y Num Mod 11 <> 0  Entonces
			Escribir Num," Es primo";
		SiNo
			Escribir Num," No es primo";
		FinSi
	FinSi
FinProceso
