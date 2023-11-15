from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response
from .model import Workout, User, Physique
from flask_sqlalchemy import SQLAlchemy
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_user, login_required, logout_user, current_user

form = Blueprint('form', __name__)

@form.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve the form data
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Login Successful!', category='success')
                login_user(user, remember=True)
                return redirect(request.args.get('next') or url_for('form.add_workout'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('User does not exist', category='error')

    # Render the login template for GET requests
    return render_template('login.html')

@form.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('form.login'))

@form.route('/signUp', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        # Retrieve the form data
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')
        passwordVerification = request.form.get('passwordVerification')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username is taken.', category='error')
        elif len(username) < 4:
            flash('Username must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif password != passwordVerification:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(firstName=firstName, lastName=lastName, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('structure.home'))

    # Render the signup template for GET requests
    return render_template('signUp.html')


@form.route('/add_workout', methods=['GET', 'POST'])
@login_required
def add_workout():
    if request.method == 'POST':
        name = request.form.get('name')
        date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        weight = float(request.form.get('weight'))
        reps = int(request.form.get('reps'))
        sets = int(request.form.get('sets'))
        rpe = float(request.form.get('rpe'))

        workout_session = Workout(date=date, name=name, weight=weight, reps=reps, sets=sets, rpe=rpe, username=current_user.username)
        db.session.add(workout_session)
        db.session.commit()
        flash('Lifting Data has been sent!', category='success')

    return render_template('liftInput.html', user=current_user)


@form.route('/physique', methods=['GET', 'POST'])
@login_required
def add_physique():
    if request.method == 'POST':
        date = datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
        comments = request.form.get('comments')
        weight = float(request.form.get('weight'))

        #File Upload

        pic = request.files['physique_pic']
        filename = secure_filename(pic.filename)
        mimeType = pic.mimetype

        new_physique = Physique(date=date, comments=comments, weight=weight, username=current_user.username, img=pic.read(), mimeType=mimeType, imgName=filename)
        db.session.add(new_physique)
        db.session.commit()

        flash('Physique data has been added!', category='success')

    return render_template('physique.html', user=current_user)

@form.route('/physique/<int:id>', methods=['GET'])
def getPhysiquePic(id):
    physique = Physique.query.get(id)
    if physique:
        return Response(physique.img, mimetype=physique.mimeType)
    else:
        return "Physique not found", 404