//Ejercicio #30: Hacer un programa que calcule el area y el perimetro de un triangulo rectangulo
//dados los dos catetos
Proceso Inicio
	Definir catetoOp, catetoAd, area Como Entero;
	Definir hipotenusa, perimetro Como Real;
	Escribir "Dame el valor del catetoOp: ";
	Leer catetoOp;
	Escribir "Ahora dame el valor del catetoAd: ";
	Leer catetoAd;
	
	hipotenusa <- rc((catetoOp)^2 + (catetoAd)^2);
	Escribir "Usando teorema de pitagoras, la hipotenusa es: ",hipotenusa;
	perimetro <- hipotenusa + catetoAd + catetoOp;
	area <- (catetoOp * catetoAd) / 2;
	Escribir "El perimetro es: ",perimetro," y el area es: ",area;
	
FinProceso
