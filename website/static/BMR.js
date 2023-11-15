document.getElementById('BMR').onclick = function() {
    const units = document.getElementById('unit-system').value;
    const weight = Number(document.getElementById('weight').value);
    const height = Number(document.getElementById('height').value);
    const age = Number(document.getElementById('age').value);
    const ismale = document.getElementById('male').checked;
    const activityLevel = document.getElementById('activityLevel').value;
    let bmr = 0;
    if (units === 'imperial') {
        bmr = (4.536 * weight + 15.88 * height - 5 * age + (ismale ? 5 : -161))*activityLevel;
    } 
    else if (units === 'metric') {
        bmr = (4.536 * (weight * 2.205) + 15.88 * (height / 2.54) - 5 * age + (ismale ? 5 : -161))*activityLevel;
    }
    
    if (isNaN(bmr) || bmr < 0) {
        document.getElementById('resultbmr').innerHTML = "You're missing a field";
    } else {
        document.getElementById('resultbmr').innerHTML = "You burn " + bmr.toPrecision(4) + " calories a day";
    }
}