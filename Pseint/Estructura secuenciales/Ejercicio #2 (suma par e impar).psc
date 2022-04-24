// Egercicio #2: Se desea calcular indenpendientemente la suma de los dos numeros pares e impares comprendidio entre 1 - 50
Proceso Inicio
	Definir Sum_P,Sum_I,I Como Entero;
	Sum_P <- 0;
	Sum_I <- 0;
	Para I<-2 Hasta 49 Hacer
		Si I MOD 2=0 Entonces
			Sum_P <- Sum_P+I;
		SiNo
			Sum_I <- Sum_I+I;
		FinSi
	FinPara
	Escribir 'La suma en pares es de: ',Sum_P;
	Escribir 'La suma en Impares es de: ',Sum_I;
FinProceso
