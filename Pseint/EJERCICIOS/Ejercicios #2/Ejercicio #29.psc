//Ejercicio 29: Pide al susuario dos numeros. luego muestra por la pantalla el resultados de 
//sumarlos, restarlos, multiplicarlos, dividirlos. hacer la potencia del primero elevado al segundo
//y el resto que resulte al dividir el primero entre el segundo.
Proceso Inicio
	Definir  num1, num2, suma, resta, multiplicacion Como Entero;
	Definir division, potencia, resto Como Real;
	num1 <- 0;
	num2 <- 0;
	suma <- 0;
	resta <- 0;
	multiplicacion <- 0;
	division <- 0;
	resto <- 0;
	
	Escribir "Dame el primer numero: ";
	Leer num1;
	Escribir "Ahra dame el segundo numero: ";
	Leer num2;
	
	suma <- num1 + num2;
	resta <- num1 - num2;
	multiplicacion <- num1 * num2;
	division <- num1 / num2;
	resto <- num1 mod num2;
	
	Escribir "La suma de esos dos numero es: ",suma;
	Escribir "La resta de esos dos numero es: ",resta;
	Escribir "La multiplicacion de esos dos numero es: ",multiplicacion;
	Escribir "La division de esos dos numero es: ",division;
	Escribir "el resto de esos dos numero es: ",resto;
	
FinProceso
