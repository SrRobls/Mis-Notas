// Ejercicio #6: una fruteria ofrece las manzanas con descuentos segun los siguientes parametros; de 0-2 kg el descuenyo es de 0 MOD , de 2.01-5 kg el descuento es de 10 MOD , de 5.01-10 kg el descuento es de 15 MOD , de 10 en adelante el descuento es de 20 MOD .
// determinar  cuanto pagara una persona que compre manzanas en la fruteria
Proceso Inicio
	Definir compra,Kgcomprado,pagar Como Real;
	Escribir '¿Cuantos kilos de manzanas compraras?: ';
	Leer Kgcomprado;
	Escribir '¿Cuanto vas a pagar por las manzanas?: ';
	Leer compra;
	Si Kgcomprado>=0 Y Kgcomprado<=2 Entonces
		pagar <- compra;
		Escribir 'El valor a pagar es: ',pagar;
	SiNo
		Si Kgcomprado>2 Y Kgcomprado<=5 Entonces
			pagar <- compra-(compra*0.1);
			Escribir 'El valor a pagar es de: ',pagar;
		SiNo
			Si Kgcomprado>5 Y Kgcomprado<=10 Entonces
				pagar <- compra-(compra*0.15);
				Escribir 'El valor a pagar es de: ',pagar;
			SiNo
				Si Kgcomprado>10 Entonces
					pagar <- compra-(compra*0.2);
					Escribir 'El valor a pagar: ',pagar;
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
