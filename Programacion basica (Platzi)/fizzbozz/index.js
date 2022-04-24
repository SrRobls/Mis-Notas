var numero = 100;
for (i = 1; i <=100; i++){
	if (EsDivisible(i,3)){
		document.write("fizz");
	}
	if (EsDivisible(i,5)) {
		document.write("bozz");
	}
	if (!EsDivisible(i,3) && !EsDivisible(i,5)){
        document.write(i);
	}

	document.write("<br />");
}

function EsDivisible(num, divisor){
	if (num % divisor == 0) {
        return true;
	}
	else{
		return false;
	}

}