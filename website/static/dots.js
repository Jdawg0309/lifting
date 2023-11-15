submit  = document.getElementById("dots");
units = document.getElementById("unit-system");
submit.addEventListener('click', function(e){
    var ismale = document.getElementById("male").checked;
    var bodyweight = parseFloat(document.getElementById("weight").value);
    var total = parseFloat(document.getElementById("total").value);

    if (units.value === "imperial"){
        // Define the Wilks coefficients
        bodyweight = bodyweight/2.20462;
        total = total/2.20462;
    }

    
    if (ismale === true) {
        var a = -0.000001093
        var b = 0.0007391293
        var c = -0.1918759221 
        var d = 24.0900756 
        var e = -307.75076
    } else {
        var a =  -0.0000010706
        var b = 0.0005158568
        var c = -0.1126655495
        var d = 13.6175032
        var e = -57.96288 
    }

    var dots = total * 500 / (e + d * bodyweight + c * Math.pow(bodyweight, 2) + b * Math.pow(bodyweight, 3) + a * Math.pow(bodyweight, 4));

    // Display the result
    document.getElementById("resultDots").innerHTML = "Your Dots score is " + dots.toFixed(2);
    }) 


