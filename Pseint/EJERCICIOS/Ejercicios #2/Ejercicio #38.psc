//Ejercicio #37: Un articulo determinado sigue la siguiente politica de descuentos:
//-15% si se compran mas de 1000 unidades
//-10% si se compran entre 500 y 999 unidades
//-5% si se compran entre 200 y 499 unidades
//Calcula el coste final de un pedido dado el precio del articulo y las unidades de compra.
Proceso Inicio
	Definir unidades, valorUnidad, precioFinal, descuento, caja Como Real;
	Escribir "¿Cuantas unidades se compra?";
	Leer unidades;
	Escribir "¿Cuanto es el costo por unidad?";
	Leer valorUnidad;
	descuento <- 0;
	caja <- unidades * valorUnidad;
	precioFinal <- caja;
	
	
	Si unidades >= 1000 Entonces
		descuento <- 15;
		caja <- (precioFinal * descuento) / 100;
		precioFinal <- precioFinal - caja;
	SiNo
		Si unidades >= 500 Y unidades < 1000 Entonces
			descuento <- 10;
			caja <- (precioFinal * descuento) / 100;
			precioFinal <- precioFinal - caja;
		SiNo
			Si unidades >= 200 Y unidades < 500 Entonces
				descuento <- 5;
				caja <- (precioFinal * descuento) / 100;
				precioFinal <- precioFinal - caja;
			SiNo 
				Si unidades < 200 Y unidades >= 0 Entonces
					caja <- 0;
				FinSi
			FinSi
		FinSi
	FinSi
	Escribir "El  descuento es de: ",caja,"$";
	Escribir "El precio a pagar con descuento (si la hay) es: ",precioFinal,"$";
	

	
FinProceso
