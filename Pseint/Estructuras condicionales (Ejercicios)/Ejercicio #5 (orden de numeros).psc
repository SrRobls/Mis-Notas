// Ejercicio #5: Leer tres numeros diferentes e imprimir el numero mayor de los tres.
Proceso Inicio
	Definir num1, num2, num3 como reales;
	Escribir "Dame tres numeros aleatorios: ";
	Leer num1,num2,num3;
	Si num1 > num2 Y num1 > num3 Y num2 > num3 Entonces
		Escribir "El orden de mayor a menor es: ", num1, " ", num2, " ", num3;
	SiNo
		Si num1 > num2 Y num1 > num3 Y num3 > num2 Entonces
			Escribir "El orden de mayor a menor es: ",num1," ", num3," ",num2 ;
		SiNo
			Si num2 > num1 Y num2 > num3 Y num1 > num3 Entonces
				Escribir "El orden de mayor a menor es: ",num2, " ",num1," ",num3;
			SiNo
				Si num2 > num1 y num2 > num3 Y num3 > num1 Entonces
					Escribir "El orden de mayor a menor es: ",num2," ",num3," ",num1;
				SiNo
					Si num3 > num1 Y num3 > num2 Y num1 > num2 Entonces
						Escribir "El orden de mayor a menor es: ",num3," ",num1," ",num2;
					SiNo
						Si num3 > num1 Y num3 > num2 Y num2 > num1 Entonces
							Escribir "El orden de mayor a menor es: ",num3," ",num2," ",num1;
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinProceso
