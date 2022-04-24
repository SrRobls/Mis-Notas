//Ejercicio 27: Convertir un dato de temperatura en Celcius a Kelvin (K = C + 273)
Proceso inicio 
	Definir celcius, kelvin Como Real;
	celcius <- 0;
	kelvin <- 0;
	Escribir "¿Cual es la temperatura en celcius que quieres convertir a kelvin?: ";
	Leer celcius;
	kelvin <- celcius + 273;
	Escribir "La teperatura en celcius (",celcius,"C",") convertida a kelvin es:" Sin Saltar;
	Escribir kelvin;
FinProceso