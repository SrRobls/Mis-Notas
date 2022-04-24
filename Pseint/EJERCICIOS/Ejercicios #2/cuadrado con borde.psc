Proceso Inicio
	Definir ancho, alto, i, j Como Entero;
	ancho <- 0;
	alto <- 0;
	i <- 0;
	j <- 0;
	Escribir "¿Cuantos asteriscos quieres de ancho?: ";
	Leer ancho;
	Escribir "Ahora ¿Cuantos asteriscos quieres de alto?: ";
	Leer alto;
	Para  i <- 1 hasta alto con paso 1 Hacer 
		Para  j <- 1 hasta ancho con paso 1 Hacer
			Si i = 1 O j = 1 O i = alto O j = ancho Entonces
				Escribir "*"Sin Saltar;
			SiNo
				Escribir " "Sin Saltar;
			FinSi
		FinPara
		Escribir " ";
	FinPara
FinProceso
