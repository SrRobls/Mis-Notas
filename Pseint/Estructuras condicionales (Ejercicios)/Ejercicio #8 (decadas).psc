// Ejercicio #8: Elaborar un programa que me muestre el significado de aniversario de cada decada hastla los 60. 
// Bodas de ojalata: 10 a�os. Bodas de porcelana :  20 a�os, bodas de perlas: 30 a�os, bodas de rubi: 40 a�os, bodas de oro: 50 a�os, bodas de diamante: 60 a�os
Proceso Incio
	Definir decada Como Entero;
	Escribir "Dame un una decada desde 10 a 60 (de 10 en 10): ";
	Leer decada;
	Segun decada Hacer
		10:
			Escribir "Boda de ojalata";
		20:
			Escribir "Boda de porcelana";
		30:
			Escribir "Boda de perlas";
		40:
			Escribir "Boda de rubi";
		50:
			Escribir "Boda de oro";
		60:
			Escribir "Boda de diamante";
		De Otro Modo:
			Escribir "Las decadas van de 10 en 10 paraco HP" ;
	FinSegun
FinProceso
