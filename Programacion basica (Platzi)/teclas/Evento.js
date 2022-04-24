var teclas = {UP: 38, DOWN: 40, LEFT: 37, RIGTH: 39};

console.log(teclas);

document.addEventListener("keydown", DibujarTeclado);

var cua = document.getElementById("cuadron");
var papel = cua.getContext("2d");
var x = 150;
var y = 150;

dibujarLinea("red", 149, 149, 151, 151, papel);

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal, lienzo){
	lienzo.beginPath();
	lienzo.strokeStyle = color;
	lienzo.lineWidth = 2;
	lienzo.moveTo(xinicial, yinicial);
	lienzo.lineTo(xfinal, yfinal);
	lienzo.stroke();
	lienzo.closePath();
}
function DibujarTeclado(evento){

    var mover = 2;
    var colorcito = "red";

    switch(evento.keyCode){
    	case teclas.UP:
    	   dibujarLinea(colorcito, x, y, x, y - mover, papel);
    	   y = y - mover;
    	   console.log("ARRIBA");
    	break;
    	case teclas.DOWN:
    	   dibujarLinea(colorcito, x, y, x, y + mover, papel);
    	   y = y + mover;
    	   console.log("ABAJO");
    	break;
    	case teclas.LEFT:
    	   dibujarLinea(colorcito, x, y, x - mover, y, papel);
    	   x = x - mover;
    	   console.log("IZQUIERDA");
    	break;
    	case teclas.RIGTH:
    	   dibujarLinea(colorcito, x, y, x + mover, y, papel);
    	   x = x + mover;
    	   console.log("DERECHA");
    	break;   
    	default:
    	   console.log("Otra Tecla");

    }
}

declarar(); console.log(variable);