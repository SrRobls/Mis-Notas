var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");


var lineas = 30;
var l = 0;
var p = 0;
var yi, xf;
var xi, yf;

for(l = 0; l < lineas; l++){
	yi = 10 * l;
	xf = 10 * (l + 1);
	dibujarLinea("black", 0, yi, xf, 300);
	console.log("linea l " + l);
}

for(p = 0; p < lineas; p++){
	xi = 10 * p;
	yf = 10 * (p + 1);
	dibujarLinea("blue", xi, 0, 300, yf);
	console.log("linea p " + p);
}

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal){
	lienzo.beginPath();
	lienzo.strokeStyle = color;
	lienzo.moveTo(xinicial, yinicial);
	lienzo.lineTo(xfinal, yfinal);
	lienzo.stroke();
	lienzo.closePath();
}

dibujarLinea("black",1,1,1,299);
dibujarLinea("black",0,299,299,299);
dibujarLinea("black",299,299,299,1);
dibujarLinea("black",1,1,299,1);