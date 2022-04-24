//funcions matematicas:

Proceso main
	Definir num, resultado1, resultado2, resultado3, resultado4, resultado5 Como Reales;
	
	Escribir "digite un numero: ";
	leer num;
	
	resultado1 <- abs(num); //se usa abs para hallar el valor absoluto de un numero
	Escribir "el valor absoluto del numero es: ", resultado1;
	
	resultado2 <- trunc(num); // devolver la parte entera un numero
	Escribir "la parte entera del numero digitado es: ",resultado2;
	
	resultado3 <- redon(num); //redon se utiliza para redondear al numero entero mas cercano
	Escribir "el numero redondeado seria: ", resultado3; 
	
	resultado4 <- rc(num); //rc es para hallar la raiz cuadrada
	Escribir "la raiz cuadrada del numero digitado es: ",resultado4;
	
	resultado5 <- ln(num); //ln es para hallar el logaritmo natural
	Escribir "el logaritmo natural es: ",resultado5;
	
//para usar mas funciones matematicas solo debemos desplegar la pestaña de la izquierda de Pseint y usas la que necesitemos.
FinProceso
