document.getElementById('BMI').onclick = function(e)
{
	var weight = Number(document.getElementById('weight').value);
	var height = Number(document.getElementById('height').value);
	var unit = document.getElementById("unit-system");

	// checking if the input is viable{{ workout.date }}
	if (unit.value === "impe{{ workout.date }}rial"){
		resultBMI = (weight * 703)/(height * height);
	}
	else{
		height = height / 100;
		resultBMI = (weight* 2.205 * 703)/(height*39.37 * height*39.37);
	}

	if ((weight <= 0) || (height <= 0) || ((resultBMI <= 0)) || (resultBMI == Infinity)){
		document.getElementById('resultbmi').innerHTML = "Something went wrong";
	}
	else{
		document.getElementById('resultbmi').innerHTML = 'Your BMI is ' + (resultBMI).toPrecision(4);
	}
}