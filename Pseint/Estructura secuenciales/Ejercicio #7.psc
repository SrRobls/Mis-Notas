//Ejercicio #7: Ingresar N numeros enteros, visualzar la suma de los numeros pares de la lista, cuntos numeros pares existen y cual es el promedio de los numeros impares
Proceso inicio
	Definir elementos, i, num como enteros;
	Definir sumapares, conteodepares Como Entero;
	Definir sumaImpares, conteoDeImpares como entero;
	Definir promedio Como Real;
	
	Escribir "Digite la cantidad de elementos a ingresar: ";
	Leer elementos;
	i <- 1;
	sumapares <- 0;
	conteodepares <- 0;
	
	sumaImpares <- 0;
	conteoDeImpares <- 0;
	
	Mientras i <= elementos Hacer
		Escribir i,". Digite un numero: ";
		Leer num;
		Si num mod 2 = 0 Entonces
			sumapares <- sumapares + num;
			conteodepares <- conteodepares + 1;
		SiNo
			sumaImpares <- sumaImpares + num;
			conteoDeImpares <- conteoDeImpares + 1;
		FinSi
		i <- i + 1;
	FinMientras
	
	Si conteodepares = 0 Entonces
		Escribir "No se han digitado numeros pares";
	SiNo
		Escribir "La suma de los numeros pares es: ",sumapares;
		Escribir "El  conteo de los numeros pares es: ",conteodepares;
	FinSi
	
	Si conteoDeImpares = 0 Entonces
		Escribir "No se han digitado numeros impares";
	SiNo
		promedio <- sumaImpares/conteoDeImpares;
		Escribir "El promedio de los impares es de: ", promedio;
	FinSi
FinProceso
