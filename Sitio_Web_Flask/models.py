#from run_app import db
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
import db
class User(UserMixin,db.Base):
    __tablename__='Users'
    id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))
    type_user = Column(String(20))

    