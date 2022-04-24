//Ejercicio #68: Guarda en un arreglo tantos numeros enteros como quiera el usuario. despues cuenta las veces que otro numero indicado  el usuarion arreglo
Proceso Inicio
	Definir arreglo, contador, indice, cantidad, num Como Entero;
	cantidad <- 0;
	indice <- 0;
	contador <- 0;
	num <- 0;
	Escribir "¿Cuantos numeros quieres introducir?: ";
	Leer cantidad;
	Dimension arreglo[cantidad];
	Para  indice <- 0 Hasta cantidad -1 Con Paso 1 Hacer
		Escribir "Dame el numero #",indice + 1;
		Leer arreglo[indice];
	FinPara
	Escribir "Ahora dame de cual numero quieres saber las veces que se repitio: ";
	Leer num;
	Para  indice <- 0 Hasta cantidad -1 Con Paso 1 Hacer
		Si num == arreglo[indice] Entonces
			contador <- contador + 1;
		FinSi
	FinPara
	Escribir "El numero ",num," se repite ",contador," veces";
FinProceso
