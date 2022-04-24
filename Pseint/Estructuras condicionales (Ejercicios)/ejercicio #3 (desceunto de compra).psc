// Ejercicio #3: en ul almacen se hace un 20 MOD  de descuento a los clientes cuya compra supere los 100$. ¿cueal sera la cantidad que pagar la persona por su compra?
Proceso Inicio
	Definir compra, pagar como Real;
	Escribir "¿Cual es el valor de la compra?: ";
	Leer compra;
	Si compra > 100 Entonces
		pagar <- compra-(compra * 0.20);
		Escribir "El valor a pagar es: ",pagar,"$";
	SiNo
		pagar <- compra;
		Escribir "No hay descuento. El valor a pagar es de: ", pagar,"$";
	FinSi
FinProceso
