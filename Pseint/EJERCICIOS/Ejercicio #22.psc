//Ejericio #22, 23 y 24: con menu de opciones.
Proceso Inicio
	Definir Opcion, num, i Como Entero; 
	Escribir "Escoge una Opcion:";
	Escribir "(22) Para hacer el ejercicio 22"; 
	Escribir "(23) Para hacer el ejercicio 23"; 
	Escribir "(24) Para hacer el ejercicio 24"; 
	Leer Opcion;
//22. Escriba un algoritmo que lea del teclado un número entero y que compruebe si es menor que 5. 
//Si no lo es, debe volver a leer un número, repitiendo la operación hasta que el usuario escriba un valor correcto.
//Finalmente debe escribir por pantalla el valor leído.	
	Si Opcion = 22 Entonces
		Repetir
			Escribir "Dame un numero MENOR a 5: ";
			Leer num;
		Hasta Que num < 5
		Escribir "El numero Menor a 5 escogido es: ",num;
	FinSi
	
//23. Modifique el algoritmo del problema 22 para que, en vez de comprobar que el número es menor que 5, 
//compruebe que se encuentre en el rango (5 - 15).
	Si Opcion = 23 Entonces
		Repetir
			Escribir "Dame un numero Entre 5 y 15: ";
			i <- i + 1;
			Leer num;
		Hasta Que num >= 5 Y num <= 15
		Escribir "El numero entre 5 y 15 escogido es: ",num;
	FinSi
	
//24. Modifique el algoritmo del problema 23 para que cuente las veces que 
//ha leído un número del teclado y escriba el resultado por pantalla.
	i <- 0;
	Si Opcion = 24 Entonces
		Repetir
			Escribir "Dame un numero Entre 5 y 15: ";
			i <- i + 1;
			Leer num;
		Hasta Que num >= 5 Y num <= 15
		Escribir "El numero entre 5 y 15 escogido es: ",num;
		Escribir "La cantidad de que se ha leido un numero es: ",i;
	FinSi
	
//Aqui va el codigo si el usuario no escoge un numero de las opciones
	Si Opcion < 22 O Opcion > 24 Entonces
		Escribir "Esta opcion no existe";
	FinSi
	
FinProceso
