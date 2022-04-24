//Ejercicio #33: Indica si un numero dado es mayor, menor o igual a cero.
Proceso Inicio
	Definir Num Como Entero;
	Escribir "Dame un numero";
	Leer Num;
	
	Si Num = 0 Entonces
		Escribir "El numero es igual a cero: ",Num," = 0";
	SiNo
		Si Num > 0 Entonces
			Escribir "El numero es mayor a cero: ",Num," > 0";
		SiNo 
			Si Num < 0 Entonces
				Escribir "El numero es menor a cero: ",Num," < 0"; 
			FinSi
		FinSi
	FinSi
FinProceso
