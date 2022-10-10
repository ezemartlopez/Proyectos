from flask import Blueprint
from flask import render_template
from flask import redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from db import Create_User
from db import get_user_by_email


auth = Blueprint('auth', __name__)

#INICIAR SESION EN LA APLICACION
#=======================================================================
@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = get_user_by_email(User,email)

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentialss
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
#=======================================================================



#SALIR DE SESION
#=======================================================================
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
#=======================================================================




#REGISTRARSE EN LA APLICACION
#========================================================================
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    type_user = 'usuario'
    user = get_user_by_email(User,email) # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'),type_user=type_user)

    # add the new user to the database
    Create_User(new_user)

    return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return render_template('signup.html')

#=======================================================================