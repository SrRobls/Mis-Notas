//Ejercicio #7: Elaborar un programa que me muestre los dias de la semana cuandro ingrese los siete primeros numeros
Proceso Inicio
	Definir Cliente Como Entero;
	
	Escribir "SOLO PUEDES INGRESAR 7 NUMEROS, CUANDO YA HAYAS COLOCADO LOS 7 NUMERO SE TERMINARA EL PROGRAMA";
	
	Escribir "Dame un numero del 1 al 7, y dependiendo del numero saldra un dia de la semana";
	Leer Cliente;
	
	Si(Cliente = 1) Entonces
		Escribir "Lunes";
	SiNo
		Si(Cliente = 2) Entonces
			Escribir "Martes";
		SiNo
			Si(Cliente = 2) Entonces
				Escribir "Miercoles";
			SiNo
				Si(Cliente = 4) Entonces
					Escribir "Jueves";
				SiNo
					Si(Cliente = 5) Entonces
						Escribir "Viernes";
					SiNo
						Si(Cliente = 6) Entonces
							Escribir "Sabado";
						SiNo
							Si(Cliente = 7) Entonces
								Escribir "Domingo";
								
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
