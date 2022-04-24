//crea un subproceso que sume dos numeros, otro que los reste, otro que los multiplique y otro que los divida. posteriormente pide 
//dos numeros al usuario y que eliga la operacion que quiera realizar con ellos. muestra el resultado en pantalla.
//al menos  un subproceso tendra que ser sin retorno y otra con retorno

//funciones sin retorno:
Funcion suma(num1,num2)
	Escribir "la suma es: ",num1 + num2;
FinFuncion
Funcion resta(num1,num2)
	Escribir "la resta es: ", num1 - num2;
FinFuncion
//funciones con retorno:
Funcion multiplicacion <- mult(num1,num2)
	Escribir "la multiplicacion es: ",num1 *  num2;
FinFuncion
Funcion division <- div(num1,num2)
	Escribir "la division es:", num1 / num2;
FinFuncion
Proceso inicio
	Definir  a, b, decision, solucion Como Real;
	a <- 0;
	b <- 0;
	solucion <- 0;
	decision <- 0;
	Escribir "dame dos numeros: ";
	Leer a,b;
	Escribir "Escoge entre las siguientes operaciones:";
	Escribir "SUMA(1),RESTA(2),MULTIPLICACION(3) o DIVISION(4).";
	Escribir "Nota: esoge la operacion que quieres a escribien en pantalla el numero asignado de esa operacion";
	Leer decision;
	Segun decision Hacer
		1:
			suma(a,b);
		2:
			resta(a,b);
		3:
			Escribir mult(a,b);
		4:
			Escribir div(a,b);
		De Otro Modo:
			Escribir "ERROR: esa operacion no existe";
	FinSegun
FinProceso
