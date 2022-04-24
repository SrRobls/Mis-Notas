//Ejercicio #39: Determinar si una letra dada es vocal o no. (en minusculas y sin tildes).
Proceso Inicio
	Definir vocal Como Caracter;
	vocal <- "";
	Escribir "Dame una vocal";
	Leer vocal;
	
	Si vocal = "a" O vocal = "e" O vocal = "i" O vocal = "o" O vocal = "u" Entonces
		Escribir vocal," Si es una vocal";
	SiNo
		Escribir vocal," No es una vocal";
	FinSi
	
	
FinProceso
