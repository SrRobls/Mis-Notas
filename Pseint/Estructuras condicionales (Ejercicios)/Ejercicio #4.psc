//Ejercicio #4: Leer 2 numeros; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.
Proceso Inicio
	Definir numero1, numero2, resultado como Enteros;
	
	Escribir "Dame un numero: ";
	leer numero1;
	Escribir "Dame otro numero: ";
	leer numero2;
	
	Si(numero1 = numero2) Entonces
		resultado <- numero1 * numero2;
		Escribir "Son iguales asi que la multiplicacion es: ",resultado;
	SiNo
		Si(numero1 > numero2) Entonces
			resultado <- numero1 - numero2;
			Escribir "El primero es mayor que el segundo, asi que la resta es: ",resultado;
		SiNo
			Si(numero1 < numero2) Entonces
				resultado <- numero1 + numero2;
				Escribir "El segundo es mayor que el primero, asi que la suma es: ",resultado;
			FinSi
		FinSi
	FinSi
	
FinProceso
