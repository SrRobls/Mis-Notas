//ejercicio #36: Determinar cual es el menor de los tres numeros dados
Proceso Inicio
	Definir num1, num2, num3, caja Como Entero;
	Escribir "Dame el valor del primer, segundo y tercer numero: ";
	Leer num1,num2,num3;
	caja <- num1;
	
	Si num2 < caja Entonces
		caja <- num2;
	FinSi
	Si num3 < caja Entonces
		caja <- num3;
	FinSi
	Escribir "El numero menor es: ",caja;
	
	
FinProceso
