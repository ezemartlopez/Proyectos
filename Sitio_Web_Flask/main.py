from flask import Blueprint
from flask_login import login_required, current_user
from flask import render_template

main=Blueprint('main',__name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html',name=current_user.name)

@main.route('/Admin')
@login_required
def tools_admin():
    return render_template('tools_admin.html')

