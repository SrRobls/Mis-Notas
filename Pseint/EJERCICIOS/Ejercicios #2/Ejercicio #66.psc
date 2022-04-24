//Ejercicio #66: pide al ususario que introduzca el valor de las componentes x,y,z de  de un vector de tres dimensiones y guardalas en un arreglo. despues calcula 
//y muestra por pantalla su modulo (raiz cuadrada de las sumas de los cuadrados de todos los componentes)
Proceso inicio
	Definir componentes, val, modulo Como real;
	Escribir "Me daras el valor de las tres componentes del vector: ";
	Dimension componentes[3]; //el arreglo tiene 3 dimension, pero cada Dimension  comienza des de 0: 0,1,2....
	modulo <- 0;
	val <- 0;
	Para val <- 0 hasta 2 Con Paso 1 Hacer
		Escribir "Dame el valor del componentes #",val + 1; //por que val comienza en 0
		Leer componentes[val]; //val hace como controlador de espacios
	FinPara
	modulo <- raiz((componentes[0])^2 + (componentes[1])^2 + (componentes[2])^2);
	Escribir "El modulo es: ",modulo;
FinProceso