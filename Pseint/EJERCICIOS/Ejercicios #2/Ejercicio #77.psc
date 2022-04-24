//Ejercicio #77: averigua si una palabra dada por el usuario es la misma al Leer  al reves
Proceso inicio
	Definir palabra, palabraReves, letras Como Caracter;
	Definir longPalabra, i Como Entero;
	longPalabra <- 0;
	i <- 0;
	palabra <- "";
	letras <- "";
	palabraReves <- "";
	Escribir "Dame un palabra:";
	Leer palabra;
	longPalabra <- Longitud(palabra);
	//codigo para hallar y guardas la palabra al reves:
	Para i <- 0 hasta longPalabra - 1 Con Paso 1 Hacer
		letras <- Subcadena(palabra,i,i);
		palabraReves <- Concatenar(letras,palabraReves); //usamos concatenar para guardar en "palabraReves" la palabra dada por el usuario de forma al reves.
		//ya que esta funcon nos sirve para concatenar tanto letras como palabras.
	FinPara
	Escribir "Entonces la palabra [",palabra,"] escrita al reves es [",palabraReves,"]";
	Si palabraReves == palabra Entonces
		Escribir "La palabra SI es igual al escribirla al reves";
	SiNo
		Escribir "La palabra NO es la misma al escribirla al reves";
	FinSi
FinProceso
