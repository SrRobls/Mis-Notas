// ejercicio #9: hacer un programa que tenga un menu with the siguientes opciones:
// opcion 1: elevar un numero a una potencia X.
// opcion 2: sacar la raiz cuadrada de un numero.
// opcion 3: salir
Proceso main
	Definir opcion, resultado, base, potencia Como reales;
	Escribir "A continuacion elige; 1 para elevar un numero a un potencia X, 2 para sacer la raiz cuadrada de un numero o 3 para salor: " ;
	Leer opcion;
	Segun opcion Hacer
		3:
			Escribir "Bye ;)";
		2:
			Escribir "Dame el numero a sacar raiz: ";
			Leer base;
			resultado <- rc(base);
			Escribir "La raiz cuadrada es: ",resultado;
		1:
			Escribir "Dame la base de la potencia: ";
			Leer base;
			Escribir "Dame la potencia (X): ";
			Leer potencia;
			resultado <- base^potencia;
			Escribir "El resultado de la potencia es: ",resultado;
		De Otro Modo:
			Escribir "Un numero del 1 a 3, pedaso de uribe";
	FinSegun
FinProceso
