// Ejercicio #3: Leer 10 numeros e imprimir cuantos son positivos, y cuantos son negativos t cuantos neutros
Proceso Inicio
	Definir Num, i como entero;
	Definir Cp, Cn, Cne Como entero;
	Cp <- 0;
	Cn <- 0;
	Cne <- 0;
	Para i<-1 Hasta 10 Hacer
		Escribir i,". Digite un numero: ";
		Leer Num;
		Si Num = 0 Entonces
			Cne <- Cne + 1;
		SiNo
			Si Num > 0 Entonces
				Cp <- Cp + 1;
			SiNo
				Cn <- Cn + 1;
			FinSi
		FinSi
	FinPara
	Escribir "La cantidad de positivos es: ",Cp;
	Escribir "La cantidad de Negativos es: ",Cn;
	Escribir "La cantidad de Neutros es: ",Cne;
FinProceso
