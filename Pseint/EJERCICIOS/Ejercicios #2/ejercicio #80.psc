//crea dos  subproceso que incrementen el valor de un numero, pero no devuelven ningun valor. a una de ellas se le ha de pasar el argumentes por valor y a la otra por referencia. despues en el algoritmo principal
//llama a las dos funciones y crea un programa en el que se observen la diferencia de ambos metodos.

//por valor:
Funcion funcionConValor(var) //cuando es por valor significa que el valor de la variable asignada al parametro "var" no cambia y devuelve el valor sin cambios
	var <- var + 1; //es decir que esto afecta a "var" pero no a la variable asignada (aqui parametro <> variable asignada)
FinFuncion
//por referencia
Funcion funcionPorReferencia (var Por Referencia)// en este el valor de la variable asignada al parametro si puede cambiar y devuelve el valor con cambios dependiendo de el codigo dentro de esta 
	var <- var + 1; // esto afceta a var y tambie a la variable asignada al parametro var (aqui parametro = variable asignada)
FinFuncion
Proceso inicio
	Definir alazar Como Entero;
	alazar <- azar(20);
	Escribir "El valor antes de la funcion por valor y por referencia es: ",alazar;
	funcionConValor(alazar);
	Escribir "en la funcion por valor es: ",alazar;
	funcionPorReferencia(alazar);
	Escribir "en la funcion por valor es: ",alazar;
FinProceso
