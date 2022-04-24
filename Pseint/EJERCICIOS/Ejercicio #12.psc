//Ejercicio #12: Elaborara un flujograma que calcule la suma de los numeros multiplos de 3 a paratir del 3
//y finaliza en el numero 60, no deben incluirse en la suma los numeros comprendidos entre 21 y 30
Proceso Inicio
	Definir Num, contador Como Entero;
	Num <- 0;
	contador <- 0;
	Repetir
		Num <- Num + 3;
		Si Num < 21 o Num > 30 Entonces
			contador <- contador + Num;
			Escribir Num;
	    SiNo Si Num >= 21 Y Num <= 30 Entonces
				Escribir Num, " este no se toma para la suma";
			FinSi
		FinSi
	Hasta Que Num >= 60
	Escribir "La suma es: ",contador;
FinProceso
