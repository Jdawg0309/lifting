from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user

structure = Blueprint('structure', __name__)

@structure.route('/')
def home():
    return render_template("index.html")