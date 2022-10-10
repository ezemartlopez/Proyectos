from dataclasses import dataclass
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
#from models import User
pwd = os.path.abspath(os.curdir)
database = 'sqlite:///{0}/Users.sqlite'.format(pwd)
engine = create_engine(database,connect_args={'check_same_thread': False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

def create_Administrator(admin):
    session.add(admin)
    session.commit()

def Create_User(user):
    session.add(user)
    session.commit()

def get_user_by_email(clase,mail):
    user = session.query(clase).filter_by(email=mail).first()
    return user

def get_user_by_id(clase,id):
    user = session.query(clase).get(int(id))
    return user

def create_models():
    Base.metadata.create_all(engine)