"""
Este archivo tendrá la función de crear nuestra aplicación,
que iniciará la base de datos y registrará nuestros modelos.
En este momento, esto no hará mucho, pero será necesario
para el resto de nuestra aplicación. Debemos iniciar 
SQLAlchemy, establecer algunos valores de configuración y 
registrar nuestros modelos aquí.
"""
# importamos para las rutas de auteticacion
from auth import auth as auth_blueprint
from main import main as main_blueprint

import os
from flask import Flask
from models import User
from flask_login import LoginManager

app = Flask(__name__)
pwd = os.path.abspath(os.curdir)
app.config['SECRET_KEY'] = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{0}/Users.sqlite'.format(pwd)
#deshabilito que se envíe una señal cada vez que se modifica un objeto
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# iniciamos SQLAlchemy para utilizarlo despues en nuestros modelos

from db import create_models,get_user_by_id

# blueprint para las rutas de autenticacion de la app
app.register_blueprint(auth_blueprint)

# blueprint para las partes de la aplicacion que no son de autenticacion  
app.register_blueprint(main_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # ya que el user_id es solo la clave principal de nuestra tabla de usuarios, úselo en la consulta para el usuario
    #return DB.session.query(User).get(int(user_id))
    return get_user_by_id(User,user_id)

if __name__=='__main__':
    create_models()
    app.run(debug=True)