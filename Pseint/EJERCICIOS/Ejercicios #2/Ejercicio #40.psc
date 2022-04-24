//Ejercicio #40: Pide al susuario que te de el valor  de dos numeros. posteriormente el usuario tendra que elegir
// que operacion quiere que se ralice entre ellos segun menu que muestre las opciones:
//-1, suma. -2, resta. -3, multiplicacion. -4, division. Si intenta dividir entre cero (0) habra que indicarlo con un mensaje.
Proceso Inicio
	Definir Opcion, num1, num2 Como Entero;
	Definir operacion Como Real;
	
	Escribir "Damen el valor del numero 1 y numero 2: ";
	Leer num1, num2;
	operacion <- 0;
	Escribir "Ahora dame una opcion: ";
	Escribir "[1] para sumar";
	Escribir "[2] para restar";
	Escribir "[3] para multiplicar";
	Escribir "[4] para dividir";
	Leer Opcion;
	
	Segun Opcion Hacer
		1:
			operacion <- num1 + num2;
		2:
			operacion <- num1 - num2;
		3:
			operacion <- num1 * num2;
		4: 
			Si num2 = 0 Entonces
				Escribir "ERROR, NO SE PUEDE DIVIDIR ENTRE CERO (0)";
			SiNo
				operacion <- num1 / num2;
			FinSi
	FinSegun
	Escribir "El resultado de la operacion es: ",operacion;
FinProceso
