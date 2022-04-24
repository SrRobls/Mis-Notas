//Ejercicio #5: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debera pagar finalmente por su compra
Proceso inicio
	Definir Compra, Descuento Como Reales;
	
	Escribir "¿Cual es el valor de la compra?";
	Leer Compra;
	
	Descuento <- (compra * 15) / 100;
	Compra <- Compra - Descuento;
	
	Escribir "Se descuenta el 15% que es la cantidad de: ",Descuento;
	Escribir "El valor a pagar con un descuento del 15% es: ",Compra;
FinProceso
