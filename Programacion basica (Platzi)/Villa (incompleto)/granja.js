var v = document.getElementById("granja");
var papel = v.getContext("2d");

var fondo = {url: "tile.png", cargar: false};

fondo.imagen = new Image();
fondo.imagen.src = fondo.url;
fondo.imagen.addEventListener("load", cargarFondo);

//animales:
var vaca = {url: "vaca.png", cargar: false};
var duque = {url: "duque.png", cargar: false};
var pollo = {url: "pollo.png", cargar: false};

vaca.imagen = new Image();
vaca.imagen.src = vaca.url;
vaca.imagen.addEventListener("load", cargarVacas);

pollo.imagen = new Image();
pollo.imagen.src = pollo.url;
pollo.imagen.addEventListener("load", cargarPollos);

duque.imagen = new Image();
duque.imagen.src = duque.url;
duque.imagen.addEventListener("load", cargarCerdos);

//varaiables y lo necesario para que el un cerdo se mueva

var movercerdo = { url: "duque.png", cargar: false,}
movercerdo.imagen = new Image();
movercerdo.imagen.src = movercerdo.url;
movercerdo.imagen.addEventListener("load", moverAcerdo);

function moverAcerdo(){
    movercerdo.cargar = true;
    dibujar();
}

var teclas = {UP: 38, DOWN: 40, LEFT: 37, RIGTH: 39};

//funciones para que aparezcan las imagenes:
var cantidad = aleatorio(1,5)

function cargarFondo(){
    fondo.cargar = true;
    dibujar();
}

function cargarVacas(){
    vaca.cargar = true;
    dibujar();
}

function cargarCerdos(){
    duque.cargar = true;
    dibujar();
}

function cargarPollos(){
    pollo.cargar = true;
    dibujar();
}

function dibujar(){
	console.log(cantidad);
	var xi = 420;
    var yi = 420;
    var movimiento = 10;
	if (fondo.cargar == true) {
		papel.drawImage(fondo.imagen, 0, 0);
	}
	if (vaca.cargar == true) {
        for (var v = 0; v < cantidad; v++){
           var x = aleatorio(0, 5);
		   var y = aleatorio(0, 5);
		   var x = x * 80;
		   var y = y * 80;
		   papel.drawImage(vaca.imagen, x, y);
        }
	}
	if (pollo.cargar == true) {
        for (var v = 0; v < cantidad; v++){
           var x = aleatorio(0, 5);
		   var y = aleatorio(0, 5);
		   var x = x * 80;
		   var y = y * 80;
		   papel.drawImage(pollo.imagen, x, y);
        }
	}
	if (duque.cargar == true) {
        for (var v = 0; v < cantidad; v++){
           var x = aleatorio(0, 5);
		   var y = aleatorio(0, 5);
		   var x = x * 80;
		   var y = y * 80;
		   papel.drawImage(duque.imagen, x, y);
        }
	}
    document.addEventListener("keyup", mover)
    function mover(evento){
       if (movercerdo.cargar == true) {
		papel.drawImage(movercerdo.imagen, xi, yi);
		switch(evento.keyCode){
			case teclas.UP:
			yi = yi - movimiento;
			papel.drawImage(movercerdo.imagen, xi, yi); 
			break;
			case teclas.DOWN:
				yi = yi + movimiento;
			papel.drawImage(movercerdo.imagen, xi, yi); 
			break;
			case teclas.LEFT:
			xi = xi - movimiento;
			papel.drawImage(movercerdo.imagen, xi, yi); 
			break;
			case teclas.RIGTH:
			xi = xi + movimiento;
			papel.drawImage(movercerdo.imagen, xi, yi); 
		}
      } 
    }
}
function aleatorio(min, max){
	var resultado;
	resultado = Math.floor(Math.random() * (max - min + 1)) + min;
	return resultado;
}

function clear(){
	papel.drawImage(fondo.imagen, 0, 0);
	dibujar();
}

