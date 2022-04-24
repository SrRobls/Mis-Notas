//Ejercicio #32: diseña el programa que dado el precio de venta de un articulo calcule
//su precion antes de impuestos (IVA 21%).
Proceso Inicio
	Definir impuesto, precioInicial, precioFinal, caja Como Real;
	impuesto <- 21;
	Escribir "Hola se calculara el valor del producto antes del impuesto";
	Escribir "Asi que dame el valor del producto a comprar: ";
	Leer precioInicial;
	Escribir "el valor con IVA es: ",precioInicial,"$";
	caja <-  (precioInicial * impuesto) / 100;
	precioFinal <- precioInicial - caja;
	Escribir "El costo de ese producto sin Iva es: ",precioFinal,"$";
	
FinProceso
