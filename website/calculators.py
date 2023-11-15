from flask import Blueprint, render_template

calculators = Blueprint('calculators', __name__)

@calculators.route('/BMI')
def BMI():
    return render_template('BMI.html')

@calculators.route('/BMR')
def BMR():
    return render_template('BMR.html')

@calculators.route('/RPE')
def RPE():
    return render_template('RPE.html')

@calculators.route('/Tuchscherer')
def Tuchscherer():
    return render_template('tuchscherer.html')

@calculators.route('/Wilks')
def Wilks():
    return render_template('wilks.html')

@calculators.route('/Dots')
def Dots():
    return render_template('dots.html')