var imagenes = [];
imagenes["50"] = "billete50.png";
imagenes["20"] = "billete20.png";
imagenes["10"] = "billete10.png";

class Billete {
	constructor(v, c){
		this.valor = v;
		this.cantidad = c;
		this.imagen = new Image();
		this.imagen.src = imagenes[this.valor];
	}
}


function EntregarDinero(){
	var t = document.getElementById("dinero");
	dinero = parseInt(t.value);
	for (var bi of caja){
		if (dinero > 0){
			div = Math.floor(dinero / bi.valor);
			if(div > bi.cantidad){
				papeles = bi.cantidad
			}
			else{
				papeles = div;
			}

			entregado.push( new Billete (bi.valor, papeles));
			dinero = dinero - (bi.valor * papeles);
		}
	}

	if (dinero > 0){
		resultado.innerHTML = "no hay money o el valor es invalido, asegurate de no pedir un valor invalido";
		}
		else {
			for(var e of entregado){
				if(e.cantidad > 0){
					resultado.innerHTML += "<img src=" + e.imagen.src + " />";
				}
			}
			resultado.innerHTML += "<hr />";
		}
}

var caja = [];
var entregado = [];
caja.push( new Billete(50, 3));
caja.push( new Billete(20, 2));
caja.push( new Billete(10, 2));

var dinero = 0;
var div = 0;
var papeles = 0;

var resultado = document.getElementById("resultado");
var p = document.getElementById("extraer");
p.addEventListener("click", EntregarDinero);