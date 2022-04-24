var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");
var texto = document.getElementById("texto_lineas");
var boton = document.getElementById("botoncito");
var ancho = d.width;

boton.addEventListener("click", dibujoPorClick); 

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


function dibujoPorClick(){
	var x = parseInt(texto.value);
	var lineas = x;
	var espacio = ancho/lineas;
var l = 0;
var p = 0;
var yi, xf;
var xi, yf;

for(l = 0; l < lineas; l++){
	yi = espacio * l;
	xf = espacio * (l + 1);
	dibujarLinea("black", 0, yi, xf, 300);
	console.log("linea l " + l);
}

}
