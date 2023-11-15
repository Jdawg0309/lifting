submit  = document.getElementById("wilks");
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
        // Calculate the Wilks score (KGs)

    if (ismale === true) {
        var a = -216.0475144;
        var b = 16.2606339;
        var c = -0.002388645;
        var d = -0.00113732;
        var e = 7.01863E-06;
        var f = -1.291E-08;
    } else {
        var a = 594.31747775582;
        var b = -27.23842536447;
        var c = 0.82112226871;
        var d = -0.00930733913;
        var e = 4.731582E-5;
        var f = -9.054E-08;
    }

    var wilks = total * 500 / (a + b * bodyweight + c * Math.pow(bodyweight, 2) + d * Math.pow(bodyweight, 3) + e * Math.pow(bodyweight, 4) + f * Math.pow(bodyweight, 5));
    
    // Display the result
    document.getElementById("resultWilks").innerHTML = "Your Wilks score is " + wilks.toFixed(2);
    }) 