// "lamamos" al documento html y el elemento canvas
var CuadroDeDibujo = document.getElementById("cuadron");
var lienzo = CuadroDeDibujo.getContext("2d")

//creamos los evento que cuando demos mausedomn o click inicie el dibujo:
CuadroDeDibujo.addEventListener("mousedown", DibujarInicio);
CuadroDeDibujo.addEventListener("mousemove", DibujarMover);
CuadroDeDibujo.addEventListener("mouseup", DibujarDetener);
var colorcito = "black";
//coordenadas:
var xi;
var yi;
var xf;
var yf; 
var ComenzarDibujo = false;
//funcion para dibujar:
function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal){
	lienzo.beginPath();
	lienzo.strokeStyle = color;
	lienzo.lineWidth = 5;
	lienzo.moveTo(xinicial, yinicial);
	lienzo.lineTo(xfinal, yfinal);
	lienzo.stroke();
	lienzo.closePath();
}
function DibujarInicio(mouse){
	console.log(mouse);
	xi = mouse.layerX; //layerX, layerY Y offsetX/Y son el atributo que vemos en el console.log(evento) la cual muestra las corrdenas de un click o un mausedown dentro de canvas.
    yi = mouse.layerY;
    dibujarLinea(colorcito, xi -1 , yi - 1, xi + 1, yi + 1);
    ComenzarDibujo = true;
}  
function DibujarDetener(mause){
	ComenzarDibujo = false;
}
function DibujarMover(mouse){
	   if (ComenzarDibujo == true) {
   	   xi = mouse.layerX;
   	   yi = mouse.layerY;
       dibujarLinea(colorcito, xi - 1, yi - 1, xi + 1, yi + 1);
   }
}
 + 1