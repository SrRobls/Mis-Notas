Proceso inicio
	definir oracion, letra, fraseSecretar Como Caracter;
	Definir a Como Entero;
	oracion <- "Estoy Seguro Te Urge Devolver Interes Ahora";
	a <- 0;
	letra <- " ";
	fraseSecretar <- Subcadena(oracion,a,a); //para emepzar de una vez con la primera letra de la oracion";
	Para  a <- 0 hasta Longitud(oracion) con paso 1 Hacer
		letra <- Subcadena(oracion,a,a);
		Si letra == " " Entonces
			letra <- Subcadena(oracion,a+1,a+1);
			fraseSecretar <- Concatenar(fraseSecretar,letra);
		FinSi
	FinPara
	Escribir fraseSecretar;
FinProceso
