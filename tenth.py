from flask import Blueprint, render_template

tenth = Blueprint('tenth', __name__, static_folder='static', template_folder='templates')

@tenth.route('/home')
@tenth.route('/')
def home():
    return render_template('tenth.html')