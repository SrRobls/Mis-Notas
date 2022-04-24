Proceso main
	//Ejercicio #3
	Definir a,b, contenedor Como Reales;
	
	Escribir "dame el valor de a: ";
	Leer a;
	Escribir "dame el valor de b: ";
	Leer b;
	
	Escribir "El valor a actualamente es: ",a;
	Escribir "El valor b actualamente es: ",b;
	
	contenedor <- a;
	a <- b;
	b <- contenedor;
	
	Escribir "-----------Intercambiamos a y b-----------------";
	
	Escribir "Ahora el valor a es: ",a;
	Escribir "Ahora el valor b es: ",b;
	
FinProceso
