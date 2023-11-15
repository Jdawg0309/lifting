from flask import Blueprint, render_template

blogs = Blueprint('blogs', __name__)

@blogs.route('/coaching')
def home():
    return render_template("coaching.html")