//Ejercicio #18: Escribir un flujograma que calcule el cuadrado de un numero haciendo solo sumas.
//Ejemplo: el cuadrado de un numero n  es la suma de los n primeros numeros impares 
// 3^2 = 1+3+5 = 9
Proceso inicio
	Definir Num,i,Contenedor, Contenedor2 Como Reales;
	Escribir "Dame el numero a sacar su potencia a la 2 (El valor de n):";
	leer Num;
	Contenedor <- 1;
	Contenedor2 <- 1;
	Escribir Num,"^2 = ";
	Para i <- 2 Hasta Num Con paso 1 Hacer
		Contenedor2 <- Contenedor2 + 2;
		Escribir Contenedor," + ",(Contenedor2)," = ";
		Contenedor <- Contenedor + (Contenedor2);
		Escribir Contenedor;
	FinPara
FinProceso
