//Ejercicio #35: Determinar si un numero dado es multiplo de 2 y 3 o no.
Proceso Inicio
	Definir  num Como Entero;
	Escribir "Dame un  numero";
	Leer num;
	
	Si num mod 2 = 0 Y num mod 3 = 0 Entonces
		Escribir "El numero ",num," es multiplo de 2 y 3";
	SiNo
		Si num mod 2 = 0 Y num mod 3 <> 0 Entonces
			Escribir "El numero ",num," solo es multiplo de 2";
		SiNo
			Si num mod 3 = 0 Y num mod 2 <> 0 Entonces
				Escribir "El numero ",num," solo es multiplo de 3";
			SiNo 
				Escribir "El numero ",num," no es multiplo de 2 y 3";
			FinSi
		FinSi
	FinSi
FinProceso
