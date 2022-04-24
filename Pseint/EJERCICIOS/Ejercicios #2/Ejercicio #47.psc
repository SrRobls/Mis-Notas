//Haz una juego en el que el usuario tenga que acertar un numero al azar entre el 0 y el 9.
//despues el programa indicara cuantos intentos ha intentado para acertar
//Nota azar(n) retorna un numero al azar entre 0 y n-1.
Proceso Inicio
	Definir num, intentos, acierto Como Entero;
	Escribir "Hola debes acertar un numero al zar entre el 0 y el 9. buena suerte!";
	num <- azar(10);
	intentos <- 0;
	acierto <- 0;
	
	Repetir
		Escribir "dame un numero: ";
		Leer acierto;
		intentos <- intentos + 1;
	Hasta Que acierto = num
	Escribir "Felicitaciones Acertaste!!";
	Escribir "El numero de intentos fue de: ",intentos;
	
FinProceso
