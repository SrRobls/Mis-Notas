//Ejercicio #76: cuantas las vocales y las consonates que tiene una palabra dada por el usuario, y pedir una letra a ususario y buscar cuantas veces se repite esa letra
Proceso Inicio
	Definir palabra, letra, letraRepetida Como Caracter;
	Definir i, lonPalabra, contadorVocales, contadorConsonantes, contadorLetra Como Entero;
	Escribir "Dame una palabra o frase:";
	letra <- " ";
	Leer palabra;
	i <- 0;
	contadorLetra <- 0;
	letraRepetida <- " ";
	contadorConsonantes <- 0;
	contadorVocales <- 0;
	lonPalabra <- Longitud(palabra);
	Escribir "que letra o vocal quieres saber cuanto se repite en la palabra o frase: ";
	Leer letraRepetida;
	//codigo para contas la consonates o vocales y cuantas veces se repite una letra dada por el usuario:
	Para i <- 0 hasta lonPalabra - 1 Con Paso 1 Hacer
		letra <- subcadena(palabra,i,i); //porque recordemos que i empieza desde 0
		//codigo para contar letras:
		Si letra == "a" O letra == "e" O letra == "i" O letra == "o" O letra == "u" Entonces
			contadorVocales <- contadorVocales + 1;
		SiNo
			Si letra <> " " Entonces
				contadorConsonantes <- contadorConsonantes + 1;
			FinSi
		FinSi
		//codigo para letra del usuario:
		Si letraRepetida == letra Entonces
			contadorLetra <- contadorLetra + 1;
		FinSi
	FinPara
	Escribir "Hay ",contadorVocales," Vocales Y ",contadorConsonantes," Consonantes";
	Escribir "La letra [",letraRepetida,"] se repite ",contadorLetra," veces";
FinProceso
