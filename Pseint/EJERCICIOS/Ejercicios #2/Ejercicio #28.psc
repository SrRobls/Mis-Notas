//Ejecicio #28: Calcular el precio final de un articulo, conociendo el precio inicial y el porcentaje del desciento.
Proceso Inicio
	Definir precioFinal, descuento, valorDescuento ,precioInicial Como Real;
	valorDescuento <- 19;
	precioFinal <- 0;
	precioInicial <- 0;
	descuento <- 0;
	Escribir "Hola estas en una tienda en la cual hoy todos sus productos" Sin Saltar;
	Escribir " tiene un descuento del 19%.";
	Escribir "Ahora ¿de cuentos es el valor del producto que compraras (sin el descuento)?";
	Leer precioInicial;
	descuento <- (precioInicial * valorDescuento) / 100;
	precioFinal <- precioInicial - descuento;
	Escribir "El valor a pagar (con descuento) es ",precioFinal,"$";
	
FinProceso
